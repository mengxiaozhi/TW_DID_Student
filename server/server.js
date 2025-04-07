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
    } else {
        console.log('✅ 成功連接到 MySQL 資料庫');
    }
});

// edu.tw 學校網域對應
const knownDomains = {
    'gm.chihlee.edu.tw': '致理科技大學',
    'mail.chihlee.edu.tw': '致理科技大學',
    'chihlee.edu.tw': '致理科技大學',
    'ntu.edu.tw': '國立臺灣大學',
    'nthu.edu.tw': '國立清華大學',
    'ncku.edu.tw': '國立成功大學',
    'nctu.edu.tw': '國立交通大學',
    'nsysu.edu.tw': '國立中山大學',
    'nchu.edu.tw': '國立中興大學',
    'nccu.edu.tw': '國立政治大學',
    'ntnu.edu.tw': '國立臺灣師範大學',
    'ncu.edu.tw': '國立中央大學',
    'ccu.edu.tw': '國立中正大學',
    'ntust.edu.tw': '國立臺灣科技大學',
    'ntut.edu.tw': '國立臺北科技大學',
    'nkust.edu.tw': '國立高雄科技大學',
    'ntua.edu.tw': '國立臺灣藝術大學',
    'tnnua.edu.tw': '國立臺南藝術大學',
    'nycu.edu.tw': '國立陽明交通大學',
    'ntou.edu.tw': '國立臺灣海洋大學',
    'niu.edu.tw': '國立宜蘭大學',
    'ntcu.edu.tw': '國立臺中教育大學',
    'ncue.edu.tw': '國立彰化師範大學',
    'yuntech.edu.tw': '國立雲林科技大學',
    'ncyu.edu.tw': '國立嘉義大學',
    'npust.edu.tw': '國立屏東科技大學',
    'nttu.edu.tw': '國立臺東大學',
    'nknu.edu.tw': '國立高雄師範大學',
    'ndhu.edu.tw': '國立東華大學',
    'ncnu.edu.tw': '國立暨南國際大學',
    'ntpu.edu.tw': '國立臺北大學',
    'ntus.edu.tw': '國立臺灣體育運動大學',
    'ntunhs.edu.tw': '國立臺北護理健康大學',
    'nfu.edu.tw': '國立虎尾科技大學',
    'nkuht.edu.tw': '國立高雄餐旅大學',
    'tcpa.edu.tw': '國立臺灣戲曲學院',
    'nou.edu.tw': '國立空中大學',
    'ncut.edu.tw': '國立勤益科技大學',
    'ntub.edu.tw': '國立臺北商業大學',
    'nutc.edu.tw': '國立臺中科技大學',
    'nkfust.edu.tw': '國立高雄第一科技大學',
    'kuas.edu.tw': '國立高雄應用科技大學',
    'ntcpe.edu.tw': '國立臺灣體育學院',
    'ntue.edu.tw': '國立臺北教育大學',
    'nptu.edu.tw': '國立屏東大學',
    'ntc.edu.tw': '國立臺東專科學校',
    'ntin.edu.tw': '國立臺南護理專科學校',
    "scu.edu.tw": "東吳大學",
    "fju.edu.tw": "輔仁大學",
    "thu.edu.tw": "東海大學",
    "tku.edu.tw": "淡江大學",
    "fcu.edu.tw": "逢甲大學",
    "cycu.edu.tw": "中原大學",
    "cmu.edu.tw": "中國醫藥大學",
    "tmu.edu.tw": "臺北醫學大學",
    "mcu.edu.tw": "銘傳大學",
    "shu.edu.tw": "世新大學",
    "usc.edu.tw": "實踐大學",
    "ttu.edu.tw": "大同大學",
    "pccu.edu.tw": "中國文化大學",
    "pu.edu.tw": "靜宜大學",
    "cgu.edu.tw": "長庚大學",
    "yzu.edu.tw": "元智大學",
    "kmu.edu.tw": "高雄醫學大學",
    "isu.edu.tw": "義守大學",
    "cju.edu.tw": "長榮大學",
    "csmu.edu.tw": "中山醫學大學",
    "huafan.edu.tw": "華梵大學",
    "chu.edu.tw": "中華大學",
    "dyu.edu.tw": "大葉大學",
    "au.edu.tw": "真理大學",
    "tcu.edu.tw": "慈濟大學",
    "nhu.edu.tw": "南華大學",
    "hcu.edu.tw": "玄奘大學",
    "fgu.edu.tw": "佛光大學",
    "ukn.edu.tw": "康寧大學",
    "asia.edu.tw": "亞洲大學",
    "knu.edu.tw": "開南大學",
    "mmc.edu.tw": "馬偕醫學院",
    "dila.edu.tw": "法鼓文理學院",
    "ctbc.edu.tw": "中信金融管理學院",
    "mcut.edu.tw": "明志科技大學",
    "csu.edu.tw": "正修科技大學",
    "hwu.edu.tw": "醒吾科技大學",
    "fy.edu.tw": "輔英科技大學",
    "tpcu.edu.tw": "臺北城市科技大學",
    "mitust.edu.tw": "敏實科技大學"
}

// 從完整子網域逐層向上尋找對應學校名稱
function matchSchoolName(domain) {
    const parts = domain.split('.')
    while (parts.length >= 2) {
        const current = parts.join('.')
        if (knownDomains[current]) return knownDomains[current]
        parts.shift()
    }
    return '未知學校'
}
const eduEmailRegex = /^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.edu\.tw)$/

// 驗證學生 email 並發送確認信
app.post('/verify-email', async (req, res) => {
    const { email } = req.body
    const match = email.match(eduEmailRegex)

    if (!match) {
        return res.status(400).json({
            success: false,
            error: '僅允許使用 .edu.tw 學生信箱'
        })
    }

    const studentId = match[1]
    const domain = match[2].toLowerCase()
    const schoolName = matchSchoolName(domain)
    const token = crypto.randomBytes(20).toString('hex')
    const tokenExpiry = Date.now() + 3 * 24 * 60 * 60 * 1000 // 三天有效

    try {
        const conn = await db.promise()
        await conn.query(
            'INSERT INTO student_verifications (email, student_id, token, token_expiry, verified) VALUES (?, ?, ?, ?, 0) ON DUPLICATE KEY UPDATE token=?, token_expiry=?, verified=0',
            [email, studentId, token, tokenExpiry, token, tokenExpiry]
        )

        const confirmUrl = `https://did-edu.xiaozhi.moe/confirm?token=${token}`

        await transporter.sendMail({
            from: '數位憑證皮夾｜學生證 <no-reply@xiaozhi.moe>',
            to: email,
            subject: '數位憑證皮夾｜學生證，申請郵件驗證',
            html: `
                <p>請點擊以下連結驗證您的學校信箱：</p>
                <a href="${confirmUrl}">${confirmUrl}</a>
                <p>系統識別您來自「<strong>${schoolName}</strong>」，如果有錯誤請至頁面主動修改。</p>
                <p>此為系統自動郵件，請勿回覆。</p>
            `
        })

        return res.json({
            success: true,
            message: `驗證信已寄出，請至信箱完成驗證`,
            school_name: schoolName
        })
    } catch (error) {
        console.error('📧 郵件發送失敗：', error)
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

        res.json({ message: '郵件驗證成功，請回到原網頁申請學生證' })
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
                    ref: '00000000_did_edu_card_full',
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

app.listen(process.env.PORT, () => console.log('✅ 服務器運行在 http://localhost:' + process.env.PORT))