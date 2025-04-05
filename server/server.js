const express = require('express')
const axios = require('axios')
const cors = require('cors')
const nodemailer = require('nodemailer')
const mysql = require('mysql2')
const crypto = require('crypto')
require('dotenv').config()

const app = express()
app.use(cors({
    origin: '*',
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    allowedHeaders: ['Content-Type', 'Authorization']
}));
app.use(express.json())

const ISSUE_TOKEN = process.env.ISSUE_TOKEN
const VERIFY_TOKEN = process.env.VERIFY_TOKEN

const db = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME
})

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS
    }
})

// 驗證 Gmail 應用程式
transporter.verify((error, success) => {
    if (error) {
        console.error('❌ 驗證失敗：', error)
    } else {
        console.log('✅ Gmail 登入成功')
    }
})

// 驗證  MySQL 連接
db.getConnection((err, connection) => {
    if (err) {
        console.error('❌資料庫連接失敗');
    }else{
        console.log('✅ 成功連接到 MySQL 資料庫');
    }
});

// 驗證學生 email 並發送確認信
app.post('/verify-email', async (req, res) => {
    const { email } = req.body
    const eduEmailRegex = /^([a-zA-Z0-9]+)@(gm\.chihlee\.edu\.tw|mail\.chihlee\.edu\.tw)$/
    const match = email.match(eduEmailRegex)

    if (!match) {
        return res.status(400).json({
            success: false,
            error: '僅允許使用 chihlee.edu.tw 學生信箱'
        })
    }

    const studentId = match[1]
    const token = crypto.randomBytes(20).toString('hex')
    const tokenExpiry = Date.now() + 3 * 24 * 60 * 60 * 1000

    try {
        const conn = await db.promise()
        await conn.query(
            'INSERT INTO student_verifications (email, student_id, token, token_expiry, verified) VALUES (?, ?, ?, ?, 0) ON DUPLICATE KEY UPDATE token=?, token_expiry=?, verified=0',
            [email, studentId, token, tokenExpiry, token, tokenExpiry]
        )

        const confirmUrl = `https://chihlee.xiaozhi.moe/chihlee/confirm?token=${token}`

        await transporter.sendMail({
            from: '數位憑證皮夾｜致理科技大學數位學生證 <no-reply@xiaozhi.moe>',
            to: email,
            subject: '學生證申請郵件驗證',
            html: `
            <p>請點擊以下連結驗證您的學校信箱，有效期限三天：</p>
            <a href="${confirmUrl}">${confirmUrl}</a>
            <p>此為系統自動郵件，請勿回覆。</p>
            `
        })

        return res.json({
            success: true,
            message: '驗證信已寄出，請至信箱完成驗證'
        })
    } catch (error) {
        console.error('📧 郵件發送失敗：', error.response || error.message)
        return res.status(500).json({
            success: false,
            error: '伺服器錯誤，無法發送驗證信'
        })
    }
})


// 驗證 token 並啟用資格
app.get('/confirm-email', async (req, res) => {
    const { token } = req.query
    if (!token) return res.status(400).json({ error: '缺少 token' })

    try {
        const conn = await db.promise()
        const [rows] = await conn.query('SELECT * FROM student_verifications WHERE token = ?', [token])
        if (!rows.length) return res.status(400).json({ error: '無效或過期連結' })

        const user = rows[0]
        if (Date.now() > user.token_expiry) {
            return res.status(400).json({ error: '驗證連結已過期' })
        }

        await conn.query('UPDATE student_verifications SET verified = 1, token = NULL, token_expiry = NULL WHERE id = ?', [user.id])

        res.json({ message: '郵件驗證成功，您現在可以申請學生證' })
    } catch (error) {
        console.error(error)
        res.status(500).json({ error: '伺服器錯誤，無法驗證郵件' })
    }
})

// 查詢是否已通過驗證，並取得學號
app.get('/check-verification', async (req, res) => {
    const { email } = req.query
    try {
        const conn = await db.promise()
        const [rows] = await conn.query('SELECT verified, student_id FROM student_verifications WHERE email = ?', [email])
        if (!rows.length) return res.json({ verified: false })
        res.json({ verified: !!rows[0].verified, student_id: rows[0].student_id })
    } catch (error) {
        console.error(error)
        res.status(500).json({ error: '查詢驗證狀態失敗' })
    }
})

// 發卡：建立 VC 卡片資料
app.post('/vc-item-data', async (req, res) => {
    try {
        const result = await axios.post(
            'https://issuer-sandbox.wallet.gov.tw/api/vc-item-data',
            req.body,
            {
                headers: {
                    'Access-Token': ISSUE_TOKEN,
                    'Content-Type': 'application/json'
                }
            }
        )
        res.json(result.data)
    } catch (err) {
        console.error(err.response?.data || err)
        res.status(err.response?.status || 500).json(err.response?.data || { error: 'proxy error' })
    }
})

// 驗證：產生驗證 QR code
app.get('/verify-qr', async (req, res) => {
    const { transaction_id } = req.query
    try {
        const result = await axios.get(
            `https://verifier-sandbox.wallet.gov.tw/api/oidvp/qr-code`,
            {
                headers: {
                    'Access-Token': VERIFY_TOKEN
                },
                params: {
                    ref: '00000000_chihlee_student_card_full',
                    transaction_id
                }
            }
        )
        res.json(result.data)
    } catch (err) {
        console.error(err.response?.data || err)
        res.status(err.response?.status || 500).json(err.response?.data || { error: 'verify-qr error' })
    }
})

// 驗證：查詢驗證結果
app.get('/verify-result', async (req, res) => {
    const { transaction_id } = req.query
    try {
        const result = await axios.get(
            `https://verifier-sandbox.wallet.gov.tw/api/oidvp/result`,
            {
                headers: {
                    'Access-Token': VERIFY_TOKEN
                },
                params: {
                    transaction_id,
                    response_code: ' '
                }
            }
        )
        res.json(result.data)
    } catch (err) {
        console.error(err.response?.data || err)
        res.status(err.response?.status || 500).json(err.response?.data || { error: 'verify-result error' })
    }
})

app.listen(process.env.PORT, () => console.log('✅ 服務器運行在 http://localhost:'+process.env.PORT))