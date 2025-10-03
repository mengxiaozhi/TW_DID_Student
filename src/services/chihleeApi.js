import axios from 'axios'

const BASE_URL = 'https://api.xiaozhi.moe/chihlee'

const client = axios.create({
    baseURL: BASE_URL,
    timeout: 10000
})

const buildError = (error, fallbackMessage) => {
    const message = error?.response?.data?.error || error?.response?.data?.message || fallbackMessage || 'Chihlee API request failed'
    const wrapped = new Error(message)
    wrapped.cause = error
    return wrapped
}

const request = async (handler, fallbackMessage) => {
    try {
        const { data } = await handler()
        return data
    } catch (error) {
        throw buildError(error, fallbackMessage)
    }
}

export const createStudentCard = ({ email, sessionToken, vcId, vcCid, fields }) => {
    return request(
        () => client.post('/vc-item-data', { email, sessionToken, vcId, vcCid, fields }),
        '學生證產生失敗，請稍後再試'
    )
}

export const fetchVerificationQr = (transactionId) => {
    return request(
        () => client.get('/verify-qr', { params: { transaction_id: transactionId } }),
        '驗證 QR 產生失敗，請重新嘗試'
    )
}

export const fetchVerificationResult = (transactionId) => {
    return request(
        () => client.get('/verify-result', { params: { transaction_id: transactionId } }),
        '查詢驗證結果失敗'
    )
}

export const requestEmailVerification = (email) => {
    return request(
        () => client.post('/verify-email', { email }),
        '信箱驗證請求失敗'
    )
}

export const checkEmailVerification = (email) => {
    return request(
        () => client.get('/check-verification', { params: { email } }),
        '查詢信箱驗證狀態失敗'
    )
}
