<template>
    <div class="min-h-screen bg-gradient-to-r from-indigo-50 to-purple-50 p-4 md:p-6">
        <div class="max-w-4xl mx-auto">
            <!-- 頁面標題 -->
            <div class="bg-white shadow-md rounded-xl p-4 mb-4">
                <div class="flex items-center justify-between">
                    <h2 class="text-lg font-bold text-indigo-800 flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-600" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                        </svg>
                        匿名留言板
                    </h2>
                    <div class="flex items-center gap-2">
                        <span v-if="verifiedSchool"
                            class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full flex items-center gap-1">
                            <span class="h-2 w-2 bg-green-500 rounded-full"></span>
                            已驗證 - {{ verifiedSchool }}
                        </span>
                        <span v-if="verifiedName"
                            class="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full flex items-center gap-1">
                            實名 - {{ verifiedName }}
                        </span>
                        <button v-if="verifiedSchool" @click="logout"
                            class="bg-indigo-600 text-white rounded-full px-3 py-1 text-sm hover:bg-indigo-700 transition flex items-center gap-1">
                            登出
                        </button>
                    </div>
                </div>
            </div>

            <!-- 發佈留言區 -->
            <div class="bg-white shadow-md rounded-xl p-4 mb-6">
                <div v-if="!verifiedSchool" class="flex items-center justify-between p-3 bg-slate-50 rounded-lg mb-2">
                    <p class="text-sm text-slate-600">請先驗證學校身份以發佈留言</p>
                    <button @click="showVerificationModal = true"
                        class="bg-indigo-600 text-white rounded-full px-3 py-1 text-sm hover:bg-indigo-700 transition flex items-center gap-1">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                        </svg>
                        立即驗證
                    </button>
                </div>
                <form @submit.prevent="submitMessage">
                    <div
                        class="border border-slate-200 rounded-lg focus-within:ring-2 focus-within:ring-indigo-400 focus-within:border-indigo-400 transition">
                        <textarea v-model="newMessage" rows="3"
                            class="w-full rounded-t-lg p-3 focus:outline-none text-sm resize-none"
                            placeholder="分享你的想法..." :disabled="!verifiedSchool"></textarea>
                        <div class="bg-slate-50 px-3 py-2 rounded-b-lg flex justify-between items-center">
                            <div class="text-xs text-slate-500">
                                <div v-if="verifiedSchool" class="flex items-center gap-2">
                                    <span v-if="!verifiedName || !useRealName">
                                        {{ verifiedSchool }}以匿名身份發布
                                    </span>
                                    <span v-else class="text-blue-600 font-medium flex items-center gap-1">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                        </svg>
                                        以實名 {{ verifiedName }}｜{{ verifiedSchool }}發布
                                    </span>

                                    <label v-if="verifiedName" class="flex items-center gap-1 cursor-pointer">
                                        <input type="checkbox" v-model="useRealName"
                                            class="rounded text-indigo-600 focus:ring-indigo-500 h-3 w-3" />
                                        <span class="text-xs text-slate-600">使用實名</span>
                                    </label>
                                </div>
                                <span v-else>驗證後即可發佈</span>
                            </div>
                            <button type="submit" :disabled="submitting || !newMessage.trim() || !verifiedSchool"
                                class="bg-indigo-600 text-white rounded-full px-4 py-1.5 text-sm hover:bg-indigo-700 disabled:opacity-50 flex items-center gap-1 transition">
                                <span v-if="submitting">發送中...</span>
                                <span v-else-if="!verifiedSchool"
                                    @click.prevent="showVerificationModal = true">需要驗證</span>
                                <span v-else>發佈</span>
                                <svg v-if="!submitting && verifiedSchool" xmlns="http://www.w3.org/2000/svg"
                                    class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </form>
            </div>

            <!-- 留言瀑布流 -->
            <div class="mt-4">
                <div v-if="loading" class="flex justify-center items-center py-12">
                    <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-700"></div>
                </div>

                <div v-else-if="messages.length === 0" class="text-center bg-white rounded-xl shadow-md p-12">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mx-auto text-slate-300 mb-3" fill="none"
                        viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                            d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                    </svg>
                    <p class="text-slate-500">目前尚無留言。成為第一個發言的人！</p>
                </div>

                <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div v-for="msg in messages" :key="msg.id"
                        class="bg-white rounded-xl shadow-md p-4 hover:shadow-lg hover:scale-[1.01] transition cursor-pointer">
                        <div class="flex items-start gap-2">
                            <div v-if="msg.author_name"
                                class="h-8 w-8 rounded-full bg-blue-100 flex items-center justify-center flex-shrink-0">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-blue-600" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                </svg>
                            </div>
                            <div v-else
                                class="h-8 w-8 rounded-full bg-indigo-100 flex items-center justify-center flex-shrink-0">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-indigo-600" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                </svg>
                            </div>
                            <div class="flex-1">
                                <div class="flex justify-between items-start">
                                    <span class="text-sm font-medium flex items-center gap-1">
                                        <span v-if="msg.author_name" class="text-blue-700 flex items-center gap-1">
                                            {{ msg.author_name }}
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-blue-500"
                                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                            </svg>
                                        </span>
                                        <span v-else>匿名用戶</span>
                                        <span
                                            class="bg-indigo-100 text-indigo-800 text-xs px-1.5 py-0.5 rounded-full">{{
                                                msg.school }}</span>
                                    </span>
                                    <span class="text-xs text-slate-400">{{ formatTime(msg.created_at) }}</span>
                                </div>
                                <p class="mt-2 text-slate-700 whitespace-pre-wrap break-words">{{ msg.content }}</p>

                                <div class="mt-3 flex gap-4 text-xs text-slate-500">
                                    <button @click="likeMessage(msg.id)" class=" flex items-center gap-1
                                        hover:text-indigo-600 transition">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                                        </svg>
                                        讚同
                                        <span class="text-indigo-500 font-medium">({{ msg.likes || 0 }})</span>
                                    </button>
                                    <button
                                        @click="verifiedSchool ? (msg.showReplyBox = !msg.showReplyBox) : showVerificationModal = true"
                                        class="flex items-center gap-1 hover:text-indigo-600 transition">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                                        </svg>
                                        回覆
                                    </button>
                                    <!--
                                    <button class="flex items-center gap-1 hover:text-indigo-600 transition">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
                                        </svg>
                                        分享
                                    </button>
                                    -->
                                </div>
                                <div v-if="msg.showReplyBox" class="mt-2 space-y-2">
                                    <textarea v-model="msg.replyContent" rows="2"
                                        class="w-full p-2 border rounded text-sm" placeholder="輸入回覆內容..."></textarea>
                                    <button @click="submitReply(msg)"
                                        class="text-sm bg-indigo-600 text-white px-3 py-1 rounded hover:bg-indigo-700">
                                        發佈回覆
                                    </button>
                                </div>

                                <!-- 回覆列表 -->
                                <div v-if="msg.replies && msg.replies.length"
                                    class="mt-2 pl-4 border-l-2 border-slate-200 space-y-1 text-sm">
                                    <div v-for="r in msg.replies" :key="r.id">
                                        <div class="text-slate-700">{{ r.author_name || '匿名用戶｜' + r.school }}：{{
                                            r.content }}</div>
                                        <div class="text-xs text-slate-400">{{ formatTime(r.created_at) }}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 載入更多按鈕 -->
                <div v-if="messages.length >= 10" class="flex justify-center mt-6">
                    <button @click="loadMoreMessages"
                        class="bg-white text-indigo-600 border border-indigo-200 rounded-full px-4 py-2 text-sm hover:bg-indigo-50 transition flex items-center gap-2">
                        <span v-if="loadingMore"
                            class="animate-spin rounded-full h-4 w-4 border-b-2 border-indigo-700"></span>
                        <span v-else>載入更多留言</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- 驗證彈窗 -->
        <div v-if="showVerificationModal"
            class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-20 p-4">
            <div class="bg-white rounded-xl shadow-xl max-w-md w-full p-6 relative">
                <button @click="showVerificationModal = false"
                    class="absolute top-4 right-4 text-slate-400 hover:text-slate-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>

                <h2 class="text-xl font-bold text-center text-indigo-800 mb-4">學校驗證</h2>

                <!-- 驗證選項切換 -->
                <div class="flex border border-indigo-100 rounded-lg overflow-hidden mb-4">
                    <button @click="verifyMode = 'anonymous'" :class="[
                        'flex-1 py-2 text-sm font-medium transition',
                        verifyMode === 'anonymous'
                            ? 'bg-indigo-500 text-white'
                            : 'bg-white text-slate-600 hover:bg-indigo-50'
                    ]">
                        匿名驗證
                    </button>
                    <button @click="verifyMode = 'realname'" :class="[
                        'flex-1 py-2 text-sm font-medium transition',
                        verifyMode === 'realname'
                            ? 'bg-indigo-500 text-white'
                            : 'bg-white text-slate-600 hover:bg-indigo-50'
                    ]">
                        實名驗證
                    </button>
                </div>

                <p class="text-sm text-slate-500 mb-4 text-center">
                    {{ verifyMode === 'anonymous' ? '僅驗證學校身份，保持匿名' : '驗證學校身份與真實姓名' }}
                </p>

                <div v-if="qrCode" class="flex flex-col items-center">
                    <p class="text-sm text-slate-500 mb-3 font-medium">驗證碼：<span
                            class="font-mono bg-slate-100 px-2 py-0.5 rounded">{{ tid }}</span></p>
                    <img :src="qrCode" alt="QR Code" class="w-48 h-48 mx-auto rounded shadow-md mb-4" />

                    <div class="w-full space-y-3">
                        <a :href="authUri">
                            <button
                                class="w-full py-3 bg-indigo-600 text-white text-sm font-medium rounded-lg hover:bg-indigo-700 transition flex items-center justify-center gap-2">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                                </svg>
                                前往 App 進行{{ verifyMode === 'realname' ? '實名' : '' }}驗證
                            </button>
                        </a>

                        <div class="flex items-center gap-2 justify-center">
                            <div class="h-1.5 w-1.5 bg-indigo-500 rounded-full animate-pulse"></div>
                            <p class="text-sm text-slate-500">請在 <span class="font-semibold text-indigo-600">{{
                                verificationCountdown }}</span> 秒內完成掃描</p>
                        </div>
                    </div>
                </div>

                <div v-if="verifyFailed"
                    class="mt-4 bg-red-50 text-red-600 p-3 rounded-lg text-sm flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    驗證失敗或超時，請重新嘗試
                    <button @click="startVerification"
                        class="ml-auto text-indigo-600 hover:text-indigo-800 font-medium">
                        重試
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted, onUnmounted, watch } from 'vue'
    import axios from 'axios'

    const tid = ref(crypto.randomUUID())
    const qrCode = ref('')
    const authUri = ref('')
    const verifyFailed = ref(false)
    const verifiedSchool = ref('')
    const verifiedName = ref('')
    const verificationCountdown = ref(60)
    const countdownInterval = ref(null)
    const showVerificationModal = ref(false)
    const verifyMode = ref('anonymous')
    const useRealName = ref(false)

    const newMessage = ref('')
    const messages = ref([])
    const submitting = ref(false)
    const loading = ref(true)
    const loadingMore = ref(false)
    const page = ref(1)
    const pageSize = ref(10)

    const startVerification = async () => {
        verifyFailed.value = false
        tid.value = crypto.randomUUID()
        verificationCountdown.value = 60

        try {
            const endpoint = verifyMode.value === 'anonymous'
                ? 'https://api.xiaozhi.moe/chihlee/broad-verify'
                : 'https://api.xiaozhi.moe/chihlee/verify-qr'

            const qrRes = await axios.get(endpoint, {
                params: { transaction_id: tid.value }
            })
            qrCode.value = qrRes.data.qrcode_image
            authUri.value = qrRes.data.auth_uri

            if (countdownInterval.value) clearInterval(countdownInterval.value)
            countdownInterval.value = setInterval(() => {
                verificationCountdown.value--
                if (verificationCountdown.value <= 0) {
                    clearInterval(countdownInterval.value)
                    verifyFailed.value = true
                }
            }, 1000)

            const checkInterval = setInterval(async () => {
                try {
                    const result = await axios.get(`https://api.xiaozhi.moe/chihlee/broad-qr-result`, {
                        params: { transaction_id: tid.value }
                    })
                    if (result.data.verify_result) {
                        clearInterval(checkInterval)
                        clearInterval(countdownInterval.value)
                        const schoolClaim = result.data.data?.[0]?.claims?.find(c => c.ename === 'school_CN')
                        verifiedSchool.value = schoolClaim?.value || '未知學校'

                        if (verifyMode.value === 'realname') {
                            const nameClaim = result.data.data?.[0]?.claims?.find(c => c.ename === 'name')
                            verifiedName.value = nameClaim?.value || ''
                            useRealName.value = !!verifiedName.value
                        }

                        showVerificationModal.value = false
                        fetchMessages()
                    } else if (result.data.verify_result === false) {
                        clearInterval(checkInterval)
                        clearInterval(countdownInterval.value)
                        verifyFailed.value = true
                    }
                } catch (err) {
                    if (err.response?.status !== 400) {
                        clearInterval(checkInterval)
                        clearInterval(countdownInterval.value)
                        verifyFailed.value = true
                    }
                }
            }, 3000)

            setTimeout(() => {
                clearInterval(checkInterval)
                clearInterval(countdownInterval.value)
                if (!verifiedSchool.value) verifyFailed.value = true
            }, 61000)
        } catch (e) {
            verifyFailed.value = true
        }
    }

    const fetchMessages = async () => {
        loading.value = true
        try {
            const res = await axios.get(`https://api.xiaozhi.moe/chihlee/board-with-replies`, {
                params: { page: 1, pageSize: pageSize.value }
            })
            messages.value = res.data.messages?.map(m => ({ ...m, showReplyBox: false, replyContent: '' })) || []
            page.value = 1
        } catch (e) {
            console.error('取得留言失敗', e)
        } finally {
            loading.value = false
        }
    }

    const loadMoreMessages = async () => {
        if (loadingMore.value) return
        loadingMore.value = true
        try {
            const nextPage = page.value + 1
            const res = await axios.get(`https://api.xiaozhi.moe/chihlee/board-with-replies`, {
                params: { page: nextPage, pageSize: pageSize.value }
            })
            const newMessages = res.data.messages?.map(m => ({ ...m, showReplyBox: false, replyContent: '' })) || []
            if (newMessages.length) {
                messages.value = [...messages.value, ...newMessages]
                page.value = nextPage
            }
        } catch (e) {
            console.error('載入更多留言失敗', e)
        } finally {
            loadingMore.value = false
        }
    }

    const likeMessage = async (id) => {
        try {
            await axios.post(`https://api.xiaozhi.moe/chihlee/board-like`, { message_id: id })
            fetchMessages()
        } catch (e) {
            console.error('按讚失敗', e)
        }
    }

    const submitReply = async (msg) => {
        const content = msg.replyContent?.trim()
        if (!content || !verifiedSchool.value) return
        try {
            await axios.post(`https://api.xiaozhi.moe/chihlee/board-reply`, {
                message_id: msg.id,
                school: verifiedSchool.value,
                content,
                author_name: useRealName.value && verifiedName.value ? verifiedName.value : undefined
            })
            msg.replyContent = ''
            msg.showReplyBox = false
            fetchMessages()
        } catch (e) {
            alert('回覆失敗')
        }
    }

    const submitMessage = async () => {
        if (!newMessage.value.trim() || !verifiedSchool.value) return
        submitting.value = true
        try {
            await axios.post(`https://api.xiaozhi.moe/chihlee/board-message`, {
                school: verifiedSchool.value,
                content: newMessage.value.trim(),
                author_name: useRealName.value && verifiedName.value ? verifiedName.value : undefined
            })
            newMessage.value = ''
            await fetchMessages()
        } catch (e) {
            alert('留言發佈失敗，請稍後重試')
        } finally {
            submitting.value = false
        }
    }

    const formatTime = (time) => {
        const date = new Date(time)
        const now = new Date()
        const diff = Math.floor((now - date) / 1000)
        if (diff < 60) return '剛剛'
        if (diff < 3600) return `${Math.floor(diff / 60)}分鐘前`
        if (diff < 86400) return `${Math.floor(diff / 3600)}小時前`
        if (diff < 604800) return `${Math.floor(diff / 86400)}天前`
        return date.toLocaleDateString('zh-TW', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
    }

    const logout = () => {
        location.reload()
    }

    onMounted(() => {
        fetchMessages()
    })

    onUnmounted(() => {
        if (countdownInterval.value) {
            clearInterval(countdownInterval.value)
        }
    })

    watch(verifyMode, () => {
        if (showVerificationModal.value) startVerification()
    })

    watch(showVerificationModal, (newVal) => {
        if (newVal) startVerification()
    })
</script>
