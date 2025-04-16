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

//環境檢查

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


//郵件功能

// 從完整子網域逐層向上尋找對應學校名稱
async function matchSchoolName(domain) {
    const parts = domain.split('.');

    const conn = await db.promise();

    while (parts.length >= 2) {
        const current = parts.join('.');

        const [rows] = await conn.query(
            'SELECT name FROM school_domains WHERE domain = ? LIMIT 1',
            [current]
        );

        if (rows.length > 0) {
            return rows[0].name;
        }

        parts.shift(); // 繼續往上層查找
    }

    return '未知學校';
}

// 驗證學生 email 並發送確認信
const eduEmailRegex = /^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.edu\.tw)$/
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
    const schoolName = await matchSchoolName(domain)
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
                <p>學校資料錯誤或未知？填寫 <a target="_blank" href="https://forms.gle/6oCmMdNBK8gSMCveA">表單</a> 完善系統幫助下一個同學</p>
                <br>
                <p>本平台「數位學生證」為學生自主開發之技術展示專案，目的在於探索分散式身份識別技術（DID）於教育領域的應用，並無任何學校或教育機構之官方授權或背書。</p>
                <ul>
                    <li>本系統所顯示之學校名稱係根據您提供之學術信箱網域自動推論，僅供技術驗證與識別用途，不具備任何法律效力。</li>
                    <li>本系統未與任何學校資料庫或資訊系統連接，亦不模擬或破解任何學校登入機制。</li>
                    <li>所產生之數位學生證為模擬性質，僅用於展示憑證技術格式與樣式，不得作為正式學生證使用。</li>
                    <li>本平台不蒐集、處理或儲存除信箱驗證必要資訊外的個人資料，所有資料僅用於即時驗證與憑證產生，不另作他用。</li>
                    <li>本平台所生成的學校名稱、憑證資訊，均為使用者自行提供，若造成任何誤解、冒用或第三方損害，本平台概不負責。</li>
                </ul>
                <p>若您為教育機構代表，有合作意願或欲提出下架通知，請聯繫本站開發者：<a href="mailto:me@xiaozhi.moe">me@xiaozhi.moe</a></p>
                <p style="font-size: 0.9em; margin-top:1.5em;">
                詳情請參閱
                <a href="https://did-edu.xiaozhi.moe/terms" target="_blank">使用條款</a>
                與
                <a href="https://did-edu.xiaozhi.moe/privacy" target="_blank">隱私政策</a>
                </p>
                <p>---</p>
                <p>此為系統自動郵件，請勿回覆。<br>
                This email is automatically sent by the system, please do not reply.
                </p>
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


//發卡及驗證功能

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


// 投票功能

// 投票：第一階段產生 QR code（身分驗證，領票）
app.get('/vote-verify', async (req, res) => {
    const { transaction_id } = req.query
    try {
        const result = await axios.get(
            'https://verifier-sandbox.wallet.gov.tw/api/oidvp/qr-code',
            {
                headers: {
                    'Access-Token': VERIFY_TOKEN
                },
                params: {
                    ref: '00000000_did_edu_card_number',
                    transaction_id
                }
            }
        )
        res.json(result.data)
    } catch (err) {
        console.error(err.response?.data || err)
        res.status(err.response?.status || 500).json(err.response?.data || { error: 'vote-qr error' })
    }
})

// 投票：查詢第一階段驗證結果（領票），並儲存避免重複領票
app.get('/vote-verify-result', async (req, res) => {
    const { transaction_id } = req.query
    try {
        const result = await axios.get(
            'https://verifier-sandbox.wallet.gov.tw/api/oidvp/result',
            {
                headers: {
                    'Access-Token': VERIFY_TOKEN
                },
                params: {
                    transaction_id
                }
            }
        )

        const claims = result.data?.data?.[0]?.claims || []
        const numberClaim = claims.find(claim => claim.ename === 'number')

        if (!numberClaim || !numberClaim.value) {
            return res.status(400).json({ error: '找不到學號資訊' })
        }

        const studentNumber = numberClaim.value

        const conn = await db.promise()
        const [rows] = await conn.query('SELECT * FROM vote_records WHERE student_number = ?', [studentNumber])

        if (rows.length > 0) {
            return res.status(403).json({ error: '此學號已領過票，無法重複領票' })
        }

        await conn.query('INSERT INTO vote_records (student_number, transaction_id, verified_at) VALUES (?, ?, NOW())', [studentNumber, transaction_id])

        res.json(result.data)
    } catch (err) {
        console.error(err.response?.data || err)
        res.status(err.response?.status || 500).json(err.response?.data || { error: 'vote-verify-result error' })
    }
})

// 投票：第二階段產生 QR code（匿名投票）
app.get('/vote-qr', async (req, res) => {
    const { transaction_id } = req.query
    try {
        const result = await axios.get(
            'https://verifier-sandbox.wallet.gov.tw/api/oidvp/qr-code',
            {
                headers: {
                    'Access-Token': VERIFY_TOKEN
                },
                params: {
                    ref: '00000000_did_edu_card_school_cn',
                    transaction_id
                }
            }
        )
        res.json(result.data)
    } catch (err) {
        console.error(err.response?.data || err)
        res.status(err.response?.status || 500).json(err.response?.data || { error: 'vote-qr error' })
    }
})

// 投票：查詢第二階段驗證結果（匿名投票）
app.get('/vote-qr-result', async (req, res) => {
    const { transaction_id } = req.query
    try {
        const result = await axios.get(
            'https://verifier-sandbox.wallet.gov.tw/api/oidvp/result',
            {
                headers: {
                    'Access-Token': VERIFY_TOKEN
                },
                params: {
                    transaction_id
                }
            }
        )
        res.json(result.data)
    } catch (err) {
        console.error(err.response?.data || err)
        res.status(err.response?.status || 500).json(err.response?.data || { error: 'vote-qr-result error' })
    }
})

// 投票：查詢第二階段，匿名投票提交
app.post('/submit-vote', async (req, res) => {
    const { transaction_id, school, option } = req.body

    if (!transaction_id || !school || !option) {
        return res.status(400).json({ error: '缺少必要欄位' })
    }

    try {
        const conn = await db.promise()
        await conn.query(
            'INSERT INTO anonymous_votes (transaction_id, school, option_selected, voted_at) VALUES (?, ?, ?, NOW())',
            [transaction_id, school, option]
        )
        res.json({ success: true, message: '投票成功' })
    } catch (error) {
        console.error('🗳️ 投票失敗：', error)
        res.status(500).json({ error: '投票記錄失敗' })
    }
})


// 匿名留言板

// 匿名留言板：匿名驗證
app.get('/broad-verify', async (req, res) => {
    const { transaction_id } = req.query
    try {
        const result = await axios.get(
            'https://verifier-sandbox.wallet.gov.tw/api/oidvp/qr-code',
            {
                headers: {
                    'Access-Token': VERIFY_TOKEN
                },
                params: {
                    ref: '00000000_did_edu_card_school_cn',
                    transaction_id
                }
            }
        )
        res.json(result.data)
    } catch (err) {
        console.error(err.response?.data || err)
        res.status(err.response?.status || 500).json(err.response?.data || { error: 'vote-qr error' })
    }
})

// 匿名留言板：匿名查詢驗證結果
app.get('/broad-qr-result', async (req, res) => {
    const { transaction_id } = req.query
    try {
        const result = await axios.get(
            'https://verifier-sandbox.wallet.gov.tw/api/oidvp/result',
            {
                headers: {
                    'Access-Token': VERIFY_TOKEN
                },
                params: {
                    transaction_id
                }
            }
        )
        res.json(result.data)
    } catch (err) {
        console.error(err.response?.data || err)
        res.status(err.response?.status || 500).json(err.response?.data || { error: 'vote-qr-result error' })
    }
})

// 匿名留言板：發佈留言
app.post('/board-message', async (req, res) => {
    const { school, content, author_name } = req.body

    if (!school || !content) {
        return res.status(400).json({ error: '缺少必要欄位' })
    }

    try {
        const conn = await db.promise()
        await conn.query(
            'INSERT INTO board_messages (school, content, author_name, created_at) VALUES (?, ?, ?, NOW())',
            [school, content, author_name || null]
        )
        res.json({ success: true, message: '留言成功' })
    } catch (err) {
        console.error('留言錯誤:', err)
        res.status(500).json({ error: '伺服器錯誤' })
    }
})

// 匿名留言板：取得留言及回覆
app.get('/board-with-replies', async (req, res) => {
    try {
        const { page = 1, pageSize = 10, search, sort } = req.query
        const pageNum = parseInt(page) || 1
        const limit = parseInt(pageSize) || 10
        const offset = (pageNum - 1) * limit

        // 組裝查詢條件
        const conditions = []
        const values = []

        // 若有 search => (school LIKE '%xxx%' OR content LIKE '%xxx%')
        // 讓 content 也比對 %search% (可搜尋 #標籤)
        if (search) {
            conditions.push("(school LIKE ? OR content LIKE ?)")
            values.push(`%${search}%`, `%${search}%`)
        }

        let whereClause = ""
        if (conditions.length > 0) {
            whereClause = "WHERE " + conditions.join(" AND ")
        }

        // 根據 sort 參數決定排序方式
        let orderBy = "created_at DESC" // 預設：時間由新到舊
        if (sort === 'time_asc') {
            orderBy = "created_at ASC"
        } else if (sort === 'time_desc') {
            orderBy = "created_at DESC"
        } else if (sort === 'likes_desc') {
            orderBy = "likes DESC"
        } else if (sort === 'likes_asc') {
            orderBy = "likes ASC"
        }

        const conn = await db.promise()

        // 1) 查詢符合條件的留言，依照 sort 決定 ORDER BY
        const [messages] = await conn.query(
            `
            SELECT id, school, content, author_name, created_at, likes
            FROM board_messages
            ${whereClause}
            ORDER BY ${orderBy}
            LIMIT ? OFFSET ?
            `,
            [...values, limit, offset]
        )

        // 2) 撈出這些留言對應的回覆
        const messageIds = messages.map(m => m.id)
        let replies = []
        if (messageIds.length > 0) {
            const [repliesRows] = await conn.query(
                `
                SELECT id, message_id, school, content, author_name, created_at
                FROM board_replies
                WHERE message_id IN (${messageIds.map(() => '?').join(',')})
                ORDER BY created_at ASC
                `,
                messageIds
            )
            replies = repliesRows
        }

        // 3) 合併：將每則留言對應的回覆整合起來
        const messagesWithReplies = messages.map(msg => ({
            ...msg,
            replies: replies.filter(r => r.message_id === msg.id)
        }))

        // 回傳
        res.json({
            success: true,
            messages: messagesWithReplies
        })
    } catch (err) {
        console.error('取得留言錯誤:', err)
        res.status(500).json({ error: '伺服器錯誤' })
    }
})

// 匿名留言板：留言按讚
app.post('/board-like', async (req, res) => {
    const { message_id } = req.body
    if (!message_id) return res.status(400).json({ error: '缺少 message_id' })

    try {
        const conn = await db.promise()
        await conn.query('UPDATE board_messages SET likes = likes + 1 WHERE id = ?', [message_id])
        res.json({ success: true })
    } catch (err) {
        console.error('按讚錯誤:', err)
        res.status(500).json({ error: '伺服器錯誤' })
    }
})

//匿名留言板：發送回覆
app.post('/board-reply', async (req, res) => {
    const { message_id, school, content, author_name } = req.body
    if (!message_id || !school || !content) {
        return res.status(400).json({ error: '缺少必要欄位' })
    }

    try {
        const conn = await db.promise()
        await conn.query(
            'INSERT INTO board_replies (message_id, school, content, author_name) VALUES (?, ?, ?, ?)',
            [message_id, school, content, author_name || null]
        )
        res.json({ success: true })
    } catch (err) {
        console.error('回覆錯誤:', err)
        res.status(500).json({ error: '伺服器錯誤' })
    }
})


app.listen(process.env.PORT, () => console.log('✅ 服務器運行在 http://localhost:' + process.env.PORT))