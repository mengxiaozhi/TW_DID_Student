<template>
    <div class="min-h-screen flex flex-col bg-gradient-to-br from-slate-50 to-slate-100">
        <!-- Main Content -->
        <main class="py-8 px-4 md:px-8">
            <div
                class="max-w-2xl mx-auto bg-white shadow-lg rounded-xl p-8 space-y-8 border border-slate-200 transition-all duration-300 hover:shadow-xl">
                <div class="flex justify-center space-x-4">
                    <button
                        class="px-6 py-2.5 rounded-full text-sm font-medium transition duration-200 ease-in-out hover:scale-[1.02] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                        :class="activeTab === 'generate' ? 'bg-blue-500 text-white shadow-md' : 'bg-slate-100 text-slate-700 hover:bg-slate-200'"
                        @click="activeTab = 'generate'">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1.5" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                        </svg>
                        生成學生證
                    </button>
                    <!-- 匿名留言板 -->
                    <router-link to="/broad" custom v-slot="{ navigate, isActive }">
                        <button @click="navigate(); activeTab = 'broad'"
                            class="px-6 py-2.5 rounded-full text-sm font-medium transition duration-200 ease-in-out hover:scale-[1.02] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
                            :class="(activeTab === 'broad' || isActive) ? 'bg-blue-500 text-white shadow-md' : 'bg-slate-100 text-slate-700 hover:bg-slate-200'">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1.5" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                            </svg>
                            匿名留言板
                        </button>
                    </router-link>
                    <button
                        class="px-6 py-2.5 rounded-full text-sm font-medium transition duration-200 ease-in-out hover:scale-[1.02] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500"
                        :class="activeTab === 'verify' ? 'bg-emerald-500 text-white shadow-md' : 'bg-slate-100 text-slate-700 hover:bg-slate-200'"
                        @click="activeTab = 'verify'; generateUUID()">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1.5" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                        </svg>
                        驗證學生證
                    </button>
                </div>

                <!-- 信箱驗證區塊 -->
                <div v-if="activeTab === 'generate'" class="transition-all">
                    <form @submit.prevent="sendVerificationEmail" class="space-y-5">
                        <div>
                            <label class="block mb-1.5 text-sm font-medium text-slate-700">學校信箱</label>
                            <div class="relative">
                                <input v-model="email" type="email"
                                    class="w-full pl-10 border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
                                    required placeholder="@xxx.edu.tw" />
                            </div>
                            <p class="mt-1 text-xs text-slate-500">僅限 @xxx.edu.tw 申請</p>
                        </div>
                        <button v-if="!emailSent" type="submit"
                            class="w-full py-3 bg-blue-500 hover:bg-blue-600 text-white font-medium rounded-lg hover:shadow-md transition duration-200 ease-in-out flex justify-center items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1.5" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                            寄送驗證信
                        </button>
                        <div v-if="verifyPending && !verified"
                            class="flex items-center justify-center py-2 text-sm text-slate-500">
                            <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-blue-500"
                                xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor"
                                    stroke-width="4"></circle>
                                <path class="opacity-75" fill="currentColor"
                                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                                </path>
                            </svg>
                            請前往您的郵箱進行驗證，正在等待驗證中...
                        </div>
                    </form>

                    <!-- 生成學生證頁面 -->
                    <form v-if="verified && !cardGenerated" @submit.prevent="generateCard" class="space-y-6 pt-6">
                        <!-- Success message on verification -->
                        <div
                            class="bg-emerald-50 border border-emerald-200 p-4 rounded-lg text-sm text-emerald-700 flex items-center mb-6">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2 text-emerald-500 flex-shrink-0"
                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <span>驗證成功，請填寫以下學生證資訊</span>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                            <!-- 姓名 -->
                            <div>
                                <label class="block mb-2 text-sm font-medium text-slate-700">姓名</label>
                                <input v-model="form.name" required pattern="^[一-龥_a-zA-Z0-9]+$"
                                    class="w-full border border-slate-300 p-3 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                    placeholder="請輸入姓名" />
                            </div>
                            <!-- Student ID field (read-only) -->
                            <div class="md:col-span-1">
                                <label class="block mb-2 text-sm font-medium text-slate-700">學號</label>
                                <div class="relative">
                                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400"
                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14" />
                                        </svg>
                                    </div>
                                    <input v-model="form.number"
                                        class="w-full pl-10 border border-slate-200 p-3 rounded-lg bg-slate-50 text-slate-500 cursor-not-allowed"
                                        readonly />
                                </div>
                                <p class="mt-1 text-xs text-slate-500">學號已自動從您的學校信箱取得</p>
                            </div>
                        </div>
                        <!-- 學校 -->
                        <div>
                            <label class="block mb-2 text-sm font-medium text-slate-700">學校</label>
                            <input v-model="form.school_CN" required pattern="^[一-龥]+$"
                                class="w-full border border-slate-300 p-3 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                placeholder="請輸入學校名稱（中文）" />
                            <p class="mt-1 text-xs text-slate-500">學校已自動從您的學校信箱取得，如果錯誤請手動修改</p>
                            <p class="mt-1 text-xs text-slate-500">學校資料錯誤或未知？填寫 <a class="underline text-blue-600"
                                    target="_blank" href="https://forms.gle/6oCmMdNBK8gSMCveA">表單</a> 完善系統幫助下一個同學</p>
                        </div>
                        <button type="submit"
                            class="w-full py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            提交生成
                        </button>
                    </form>

                    <div v-if="qrCode" class="mt-8 text-center">
                        <a :href="deepLink">
                            <button
                                class="w-full py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg shadow-sm hover:shadow transition duration-200 ease-in-out flex justify-center items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                                    <circle cx="8.5" cy="7" r="4"></circle>
                                    <polyline points="17 11 19 13 23 9"></polyline>
                                </svg>
                                導入至數位憑證皮夾
                            </button>
                        </a>
                        <br>
                        <h2 class="text-lg font-medium mb-4 text-slate-800">掃描 QR Code 領取數位學生證：</h2>
                        <div class="bg-slate-50 p-6 rounded-xl inline-block">
                            <img :src="qrCode" alt="QRCode"
                                class="mx-auto w-48 h-48 rounded-lg shadow-md hover:shadow-lg transition-transform duration-300 hover:scale-105" />
                        </div>
                        <p class="mt-4 text-sm text-slate-500">請使用數位憑證皮夾 App 掃描此 QR Code</p>
                    </div>
                </div>

                <!-- 驗證頁面 -->
                <div v-else class="transition-all">
                    <template v-if="verifiedData.length">
                        <div class="mt-6 space-y-4">
                            <div class="flex items-center justify-center mb-4">
                                <div class="bg-emerald-100 p-2 rounded-full">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-emerald-500"
                                        fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                    </svg>
                                </div>
                            </div>
                            <h2 class="text-xl font-medium text-center text-slate-800">驗證成功，個人資料如下：</h2>
                            <div class="bg-slate-50 rounded-xl p-4 mt-4">
                                <div v-for="item in verifiedData" :key="item.ename"
                                    class="border-b border-slate-200 last:border-b-0 py-3 flex flex-col sm:flex-row sm:justify-between sm:items-center gap-1">
                                    <span class="font-medium text-slate-700">{{ item.cname }}：</span>
                                    <span class="text-slate-900 break-all">{{ item.value }}</span>
                                </div>
                            </div>
                        </div>
                        <div class="pt-6">
                            <button @click="generateUUID"
                                class="w-full py-3 bg-blue-500 hover:bg-blue-600 text-white font-medium rounded-lg hover:shadow-md transition duration-200 ease-in-out flex justify-center items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1.5" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                                </svg>
                                重新驗證
                            </button>
                        </div>
                    </template>

                    <template v-else>
                        <form @submit.prevent="verifyCard" class="space-y-5">
                            <div>
                                <label class="block mb-1.5 text-sm font-medium text-slate-700">Transaction ID</label>
                                <div class="relative">
                                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400"
                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" />
                                        </svg>
                                    </div>
                                    <input v-model="verifyTid"
                                        class="w-full pl-10 border border-slate-300 p-3 rounded-lg bg-slate-50 text-slate-500 font-mono tracking-wide"
                                        readonly />
                                </div>
                                <p class="mt-1 text-xs text-slate-500">這是您的唯一驗證碼，用於確認驗證請求</p>
                            </div>
                        </form>

                        <div v-if="verifyQrCode" class="mt-8 text-center">
                            <a :href="auth_uri">
                                <button
                                    class="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-medium rounded-lg shadow-sm hover:shadow transition duration-200 ease-in-out flex justify-center items-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 24 24"
                                        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                                    </svg>
                                    前往App進行身分驗證
                                </button>
                            </a>
                            <br>
                            <h2 class="text-lg font-medium mb-4 text-slate-800">請用錢包 App 掃描以下 QR Code 驗證身份</h2>
                            <div class="bg-slate-50 p-6 rounded-xl inline-block">
                                <img :src="verifyQrCode" alt="VerifyQRCode"
                                    class="mx-auto w-48 h-48 rounded-lg shadow-md hover:shadow-lg transition-transform duration-300 hover:scale-105" />
                            </div>
                            <p class="mt-4 text-sm text-slate-500">請在 60 秒內完成掃描</p>
                            <div class="mt-4 flex items-center justify-center">
                                <div class="animate-spin rounded-full h-5 w-5 border-b-2 border-blue-500"></div>
                                <span class="ml-3 text-sm text-slate-500">等待驗證中...</span>
                            </div>
                        </div>

                        <div v-if="verifyFailed"
                            class="mt-6 text-center p-4 bg-red-50 rounded-lg border border-red-200">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mx-auto text-red-500 mb-2"
                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <p class="text-red-600 font-medium">驗證超時，請重新驗證。</p>
                            <button @click="generateUUID(); verifyCard()"
                                class="mt-3 px-4 py-2 bg-red-100 hover:bg-red-200 text-red-600 font-medium rounded-lg transition duration-200 ease-in-out text-sm">
                                重新開始
                            </button>
                        </div>
                    </template>
                </div>
            </div>
        </main>
        <div>
        </div>
        <div class="pt-12">
            <information />
        </div>
    </div>
</template>

<script setup>
    import { ref, watch, onMounted } from 'vue'
    import axios from 'axios'
    import information from '../components/information.vue'

    const activeTab = ref('generate')
    const qrCode = ref('')
    const verifyQrCode = ref('')
    const verifiedData = ref([])
    const verifyTid = ref('')
    const verifyFailed = ref(false)
    const email = ref('')
    const verifyPending = ref(false)
    const verified = ref(false)
    const emailSent = ref(false)
    const cardGenerated = ref(false)
    const deepLink = ref('')
    const auth_uri = ref('')

    let verifyInterval = null
    let verifyTimeout = null

    const form = ref({
        name: '',
        number: '',
        school_CN: ''
    })

    const registrationDateStartRaw = ref('')
    const registrationDateEndRaw = ref('')

    watch(registrationDateStartRaw, (val) => {
        if (val) form.value.registration_date_start = val.replace(/-/g, '')
    })
    watch(registrationDateEndRaw, (val) => {
        if (val) form.value.registration_date_end = val.replace(/-/g, '')
    })

    watch(() => form.value.registration_date_start, (val) => {
        if (val && val.length === 8) {
            registrationDateStartRaw.value = `${val.slice(0, 4)}-${val.slice(4, 6)}-${val.slice(6, 8)}`
        }
    })
    watch(() => form.value.registration_date_end, (val) => {
        if (val && val.length === 8) {
            registrationDateEndRaw.value = `${val.slice(0, 4)}-${val.slice(4, 6)}-${val.slice(6, 8)}`
        }
    })

    const generateUUID = () => {
        verifyTid.value = crypto.randomUUID()
        verifiedData.value = []
        verifyFailed.value = false
        verifyQrCode.value = ''
    }

    const generateCard = async () => {
        try {
            const response = await axios.post('https://api.xiaozhi.moe/chihlee/vc-item-data', {
                vcId: 322251,
                vcCid: 'did_edu_card',
                fields: [
                    { type: 'BASIC', cname: '姓名', ename: 'name', content: form.value.name },
                    { type: 'CUSTOM', cname: '學號', ename: 'number', content: form.value.number },
                    { type: 'CUSTOM', cname: '學校', ename: 'school_CN', content: form.value.school_CN }
                ]
            })
            qrCode.value = response.data.qrCode || ''
            deepLink.value = response.data.deepLink || ''
            cardGenerated.value = true
        } catch (error) {
            console.error('產生失敗', error)
            alert('學生證產生失敗，請確認資料格式是否正確')
        }
    }

    const verifyCard = async () => {
        try {
            const qrRes = await axios.get(`https://api.xiaozhi.moe/chihlee/verify-qr`, { params: { transaction_id: verifyTid.value } })
            verifyQrCode.value = qrRes.data.qrcode_image
            verifyFailed.value = false
            verifiedData.value = []
            auth_uri.value = qrRes.data.auth_uri

            verifyInterval = setInterval(fetchVerifyResult, 5000)
            verifyTimeout = setTimeout(() => {
                clearInterval(verifyInterval)
                verifyFailed.value = true
            }, 60000)
        } catch (error) {
            console.error('驗證失敗', error)
            alert('驗證 QR 產生失敗')
        }
    }

    const fetchVerifyResult = async () => {
        try {
            const resultRes = await axios.get(`https://api.xiaozhi.moe/chihlee/verify-result`, { params: { transaction_id: verifyTid.value } })
            if (resultRes.data.verify_result) {
                verifiedData.value = resultRes.data.data[0]?.claims || []
                clearInterval(verifyInterval)
                clearTimeout(verifyTimeout)
            }
        } catch (e) {
            console.warn('查詢中...')
        }
    }

    const sendVerificationEmail = async () => {
        if (email.value === 'did-test@xiaozhi.moe') {
            verified.value = true;
            emailSent.value = true;
            verifyPending.value = false;
            form.value.school_CN = '國立台灣大學'
            form.value.number = '00000000';
            form.value.name = '張三';
            registrationDateStartRaw.value = '2020-03-15';
            registrationDateEndRaw.value = '2077-03-15';
            alert('測試帳號免驗證成功');
            return;
        }

        try {
            const res = await axios.post('https://api.xiaozhi.moe/chihlee/verify-email', { email: email.value })
            if (res.data.success) {
                verifyPending.value = true
                emailSent.value = true
                form.value.school_CN = res.data.school_name || '' // ⬅ 自動填入學校名稱
                pollVerificationStatus()
                alert(res.data.message)
            } else {
                alert(res.data.error || '驗證失敗')
            }
        } catch (err) {
            alert(err.response?.data?.error || '伺服器錯誤，請稍後再試')
        }
    }

    const pollVerificationStatus = () => {
        const checkTimer = setInterval(async () => {
            try {
                const res = await axios.get('https://api.xiaozhi.moe/chihlee/check-verification', { params: { email: email.value } })
                if (res.data.verified) {
                    verified.value = true
                    form.value.number = res.data.student_id // ⬅ 修正 student_number 欄位綁定
                    clearInterval(checkTimer)
                }
            } catch (err) {
                console.warn('查詢驗證狀態失敗')
            }
        }, 3000)
    }

    watch(email, () => {
        emailSent.value = false
        verifyPending.value = false
        verified.value = false
    })

    watch(activeTab, async (newTab) => {
        if (newTab === 'verify') {
            generateUUID()
            await verifyCard()
        }
    })

    onMounted(() => {
        if (activeTab.value === 'verify') {
            generateUUID()
            verifyCard()
        }
    })
</script>