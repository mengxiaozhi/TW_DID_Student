<template>
    <div class="min-h-screen flex flex-col">
        <section class="hero-intro">
            <div class="space-y-6">
                <span class="hero-badge">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    DID 校園驗證沙盒
                </span>
                <div class="space-y-3">
                    <h1 class="text-3xl md:text-4xl font-bold text-slate-900 leading-snug">
                        三步驟完成 <span class="text-primary">數位學生證</span>，同步支援驗證、留言與校務應用
                    </h1>
                    <p class="text-slate-600 text-base md:text-lg leading-relaxed">
                        透過政府 DID 沙盒串接，學生可快速生成並導入個人憑證，校務單位也能即時驗證，確保身份資訊安全可信。
                    </p>
                </div>
                <div class="flex flex-wrap items-center gap-3">
                    <button class="btn btn-primary" @click="activeTab = 'generate'">開始生成學生證</button>
                    <button class="btn btn-outline" @click="activeTab = 'verify'">立即驗證學生證</button>
                    <router-link to="/broad" class="btn btn-ghost">探索校園留言板</router-link>
                </div>
            </div>

            <div class="hero-grid">
                <div class="stat-card">
                    <p class="text-sm text-slate-600">日常驗證流程耗時</p>
                    <p class="text-3xl font-bold text-slate-900">3 分鐘內</p>
                    <p class="text-xs text-slate-500 mt-1">支援 DID 規格與數位憑證皮夾</p>
                </div>
                <div class="stat-card">
                    <p class="text-sm text-slate-600">已發行測試憑證</p>
                    <p class="text-3xl font-bold text-slate-900">500+ 張</p>
                    <p class="text-xs text-slate-500 mt-1">跨 40 所校院 / 社群使用者參與</p>
                </div>
                <div class="stat-card">
                    <p class="text-sm text-slate-600">匿名留言安全性</p>
                    <p class="text-3xl font-bold text-slate-900">100%</p>
                    <p class="text-xs text-slate-500 mt-1">多階段驗證、全程保護真實身份</p>
                </div>
            </div>
        </section>

        <section class="px-4 md:px-6 pb-16">
            <div class="max-w-6xl mx-auto floating-card p-6 md:p-8 space-y-6">
                <div class="flex flex-wrap items-center gap-2">
                    <span class="step-indicator">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                        </svg>
                        建立或驗證數位學生證
                    </span>
                    <span class="text-xs text-slate-500">選擇左側流程，填寫資訊即可完成</span>
                </div>

                <div class="tab-panel">
                    <aside class="space-y-3">
                        <button class="tab-button" :class="{ 'is-active': activeTab === 'generate' }" @click="activeTab = 'generate'">
                            <div class="flex items-center gap-3">
                                <span class="inline-flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                                    </svg>
                                </span>
                                <div class="text-left">
                                    <p class="font-semibold text-slate-800">生成學生證</p>
                                    <p class="text-xs text-slate-500">驗證 edu 信箱後建立 DID VC</p>
                                </div>
                            </div>
                        </button>

                        <button class="tab-button" :class="{ 'is-active': activeTab === 'verify' }" @click="activeTab = 'verify'">
                            <div class="flex items-center gap-3">
                                <span class="inline-flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                    </svg>
                                </span>
                                <div class="text-left">
                                    <p class="font-semibold text-slate-800">驗證學生證</p>
                                    <p class="text-xs text-slate-500">掃碼確認憑證真實性</p>
                                </div>
                            </div>
                        </button>

                        <RouterLink to="/broad" custom v-slot="{ navigate, isActive }">
                            <button class="tab-button" :class="{ 'is-active': isActive }" @click="activeTab = 'broad'; navigate()">
                                <div class="flex items-center gap-3">
                                    <span class="inline-flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
                                        </svg>
                                    </span>
                                    <div class="text-left">
                                        <p class="font-semibold text-slate-800">匿名留言板</p>
                                        <p class="text-xs text-slate-500">瀏覽校園提案與經驗分享</p>
                                    </div>
                                </div>
                            </button>
                        </RouterLink>

                        <div class="sidebar-hint p-5 space-y-3">
                            <p class="text-sm font-semibold text-slate-800">快速提示</p>
                            <ul class="space-y-2 text-xs text-slate-600">
                                <li class="flex items-start gap-2"><span class="mt-1 inline-flex h-1.5 w-1.5 rounded-full bg-primary"></span> Edu.tw 信箱驗證約需 45 秒。</li>
                                <li class="flex items-start gap-2"><span class="mt-1 inline-flex h-1.5 w-1.5 rounded-full bg-primary"></span> 憑證結果可直接導入官方 App。</li>
                                <li class="flex items-start gap-2"><span class="mt-1 inline-flex h-1.5 w-1.5 rounded-full bg-primary"></span> 驗證流程逾時可再次產生 QR Code。</li>
                            </ul>
                        </div>
                    </aside>

                    <div class="space-y-6">
                        <div v-if="activeTab === 'generate'" class="space-y-6">
                            <template v-if="!emailSent">
                                <div class="space-y-2">
                                    <div class="divider-label">STEP 1 ｜ 驗證學校信箱</div>
                                    <h3 class="text-xl font-semibold text-slate-900">使用 edu.tw 信箱獲得授權</h3>
                                    <p class="text-sm text-slate-600">我們會寄出一封一次性驗證信，確認您具備學生資格。完成後即可自動帶入學校資訊。</p>
                                </div>

                                <form @submit.prevent="sendVerificationEmail" class="form-card space-y-5">
                                    <div>
                                        <label class="block mb-2 text-sm font-medium text-slate-700">學校信箱</label>
                                        <div class="relative">
                                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">@</div>
                                            <input v-model="email" type="email" required placeholder="name@example.edu.tw"
                                                class="w-full rounded-xl border border-slate-300 py-3 pl-9 pr-3 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all" />
                                        </div>
                                        <p class="mt-2 text-xs text-slate-500">僅支援 edu.tw 信箱，若所在校院尚未建置，歡迎使用下方表單回報。</p>
                                    </div>

                                    <button type="submit" class="btn btn-primary w-full justify-center">寄送驗證信</button>
                                </form>
                            </template>

                            <div v-if="verifyPending && !verified" class="surface-muted p-6 rounded-xl">
                                <div class="flex items-center gap-4">
                                    <div class="inline-flex h-12 w-12 items-center justify-center rounded-full bg-primary/10 text-primary">
                                        <svg class="animate-spin h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                        </svg>
                                    </div>
                                    <div>
                                        <h3 class="text-lg font-semibold text-slate-900">等待信箱驗證中...</h3>
                                        <p class="text-xs text-slate-500">請於 5 分鐘內完成信件內的認證流程，系統會自動偵測狀態。</p>
                                    </div>
                                </div>
                            </div>

                            <div v-if="verified" class="space-y-6">
                                <div class="space-y-2">
                                    <div class="divider-label">STEP 2 ｜ 補齊卡面資訊</div>
                                    <h3 class="text-xl font-semibold text-slate-900">補充個人顯示資訊</h3>
                                    <p class="text-sm text-slate-600">這些欄位會出現在您的 VC 卡片上，可隨時修改並重新生成。</p>
                                </div>

                                <div class="grid gap-6 md:grid-cols-2">
                                    <div class="form-card space-y-4">
                                        <div>
                                            <label class="block mb-2 text-sm font-semibold text-slate-700">姓名</label>
                                            <input v-model="form.name" required pattern="^[一-龥_a-zA-Z0-9]+$"
                                                class="w-full rounded-xl border border-slate-300 py-3 px-3 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all"
                                                placeholder="請輸入您的姓名" />
                                        </div>
                                        <div>
                                            <label class="block mb-2 text-sm font-semibold text-slate-700">學號</label>
                                            <input v-model="form.number" :readonly="email === 'did-test@xiaozhi.moe'"
                                                class="w-full rounded-xl border border-slate-300 py-3 px-3 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all"
                                                placeholder="自動帶入或自行填寫" />
                                        </div>
                                        <div>
                                            <label class="block mb-2 text-sm font-semibold text-slate-700">學校名稱</label>
                                            <input v-model="form.school_CN" required pattern="^[一-龥]+$" :readonly="email === 'did-test@xiaozhi.moe'"
                                                class="w-full rounded-xl border border-slate-300 py-3 px-3 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all"
                                                placeholder="請輸入中文全名" />
                                        </div>
                                    </div>

                                    <div class="form-card space-y-4">
                                        <div class="grid gap-4 md:grid-cols-2">
                                            <div>
                                                <label class="block mb-2 text-sm font-semibold text-slate-700">學籍起始日</label>
                                                <input type="date" v-model="registrationDateStartRaw"
                                                    class="w-full rounded-xl border border-slate-300 py-3 px-3 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all" />
                                            </div>
                                            <div>
                                                <label class="block mb-2 text-sm font-semibold text-slate-700">學籍到期日</label>
                                                <input type="date" v-model="registrationDateEndRaw"
                                                    class="w-full rounded-xl border border-slate-300 py-3 px-3 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all" />
                                            </div>
                                        </div>

                                        <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-3">
                                            <p class="text-sm font-semibold text-slate-800">資料使用聲明</p>
                                            <p class="text-xs text-slate-500 leading-relaxed">資訊僅用於生成可攜式 VC（Verifiable Credential）檔案，本平台不保存卡面資料。您可隨時刪除或重新生成。</p>
                                        </div>
                                        <button class="btn btn-primary w-full" @click="generateCard">生成我的數位學生證</button>
                                    </div>
                                </div>
                            </div>

                            <div v-if="qrCode" class="surface-muted p-6 rounded-xl space-y-6">
                                <div class="flex flex-wrap items-center justify-between gap-4">
                                    <div>
                                        <h3 class="text-lg font-semibold text-slate-900">學生證生成成功</h3>
                                        <p class="text-xs text-slate-500">請使用數位憑證皮夾 App 掃描下方 QR Code 完成導入。</p>
                                    </div>
                                    <a :href="deepLink" class="btn btn-primary">導入至數位皮夾</a>
                                </div>
                                <div class="grid md:grid-cols-[200px_1fr] gap-6 items-center">
                                    <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                                        <img :src="qrCode" alt="QRCode" class="mx-auto w-40 h-40" />
                                    </div>
                                    <ul class="space-y-2 text-sm text-slate-600">
                                        <li>• 導入後即可在 App 內查看完整卡面。</li>
                                        <li>• 日後若資料有更新，可再次於此處重新生成。</li>
                                        <li>• 如需申請紙本，請依校方規定補交相關文件。</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <div v-else-if="activeTab === 'verify'" class="space-y-6">
                            <div class="space-y-2">
                                <div class="divider-label">STEP 1 ｜ 取得驗證 QR</div>
                                <h3 class="text-xl font-semibold text-slate-900">掃描 QR Code 並授權資料</h3>
                                <p class="text-sm text-slate-600">發起驗證後，將於 60 秒內偵測是否授權成功，若超時可重新產生新的驗證碼。</p>
                            </div>

                            <div class="form-card space-y-5">
                                <div class="grid gap-4 md:grid-cols-[1fr_auto] md:items-center">
                                    <div>
                                        <label class="block text-xs font-medium text-slate-500 uppercase tracking-wide">驗證碼</label>
                                        <div class="mt-2 flex items-center gap-3">
                                            <span class="font-mono text-lg tracking-widest text-slate-800">{{ verifyTid }}</span>
                                            <button class="btn btn-ghost text-xs" @click="generateUUID(); verifyCard()">重新產生</button>
                                        </div>
                                    </div>
                                    <div class="flex items-center gap-3 justify-end text-sm text-slate-500">
                                        <span class="chip">剩餘 {{ verificationCountdown }} 秒</span>
                                    </div>
                                </div>

                                <div class="grid gap-6 md:grid-cols-[220px_1fr] md:items-start">
                                    <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                                        <img v-if="verifyQrCode && !verifyFailed" :src="verifyQrCode" alt="VerifyQRCode"
                                            class="w-44 h-44 mx-auto" />
                                        <div v-else class="flex items-center justify-center text-xs text-slate-500 h-44">
                                            驗證 QR 即將出現…
                                        </div>
                                    </div>
                                    <div class="space-y-3 text-sm text-slate-600">
                                        <p class="font-semibold text-slate-800">如何驗證？</p>
                                        <ol class="space-y-2 list-decimal list-inside">
                                            <li>打開數位憑證皮夾 App，選擇「掃描驗證」。</li>
                                            <li>掃描左側 QR Code，並確認授權內容後送出。</li>
                                            <li>返回此頁即可查看驗證結果與卡面資訊。</li>
                                        </ol>
                                        <a :href="auth_uri" class="btn btn-outline w-full md:w-auto">在 App 中開啟授權頁</a>
                                    </div>
                                </div>
                            </div>

                            <div v-if="verifyFailed" class="surface-muted p-6 rounded-xl flex flex-col md:flex-row md:items-center gap-4">
                                <div class="inline-flex h-12 w-12 items-center justify-center rounded-full bg-red-100 text-red-600">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                </div>
                                <div>
                                    <h3 class="text-lg font-semibold text-slate-900">驗證超時或取消</h3>
                                    <p class="text-xs text-slate-500">請重新產生驗證碼並於 60 秒內完成授權流程。</p>
                                </div>
                                <button class="btn btn-primary md:ml-auto" @click="generateUUID(); verifyCard()">重新開始</button>
                            </div>

                            <div v-if="verifiedData.length" class="surface-muted p-6 rounded-xl space-y-6">
                                <div class="flex items-center gap-3">
                                    <span class="inline-flex h-10 w-10 items-center justify-center rounded-full bg-emerald-100 text-emerald-600">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                        </svg>
                                    </span>
                                    <div>
                                        <h3 class="text-lg font-semibold text-slate-900">驗證成功</h3>
                                        <p class="text-xs text-slate-500">以下資訊由憑證持有人授權提供。</p>
                                    </div>
                                </div>
                                <div class="bg-white border border-slate-200 rounded-xl overflow-hidden divide-y divide-slate-200">
                                    <div v-for="item in verifiedData" :key="item.ename" class="px-4 py-3 flex justify-between items-center">
                                        <span class="text-slate-600 font-medium">{{ item.cname }}</span>
                                        <span class="text-slate-800">{{ item.value }}</span>
                                    </div>
                                </div>
                                <button class="btn btn-outline w-full md:w-auto" @click="generateUUID(); verifyCard()">驗證下一位學生</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <div class="pt-8">
            <information />
        </div>
    </div>
</template>

<script setup>
    import { ref, watch, onMounted } from 'vue'
    import information from '../components/information.vue'
    import {
        createStudentCard,
        fetchVerificationQr,
        fetchVerificationResult,
        requestEmailVerification,
        checkEmailVerification
    } from '../services/chihleeApi'
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
    const verificationCountdown = ref(60)
    const countdownInterval = ref(null)
    const sessionToken = ref('')

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
        if (email.value !== 'did-test@xiaozhi.moe' && !sessionToken.value) {
            alert('請先完成信箱驗證後再產生學生證')
            return
        }

        try {
            const data = await createStudentCard({
                email: email.value,
                sessionToken: email.value === 'did-test@xiaozhi.moe' ? 'TEST_BYPASS' : sessionToken.value,
                vcId: 491908,
                vcCid: 'did_edu_card_v2',
                fields: [
                    { type: 'BASIC', cname: '姓名', ename: 'name', content: form.value.name },
                    { type: 'CUSTOM', cname: '學號', ename: 'number', content: form.value.number },
                    { type: 'CUSTOM', cname: '學校', ename: 'school_CN', content: form.value.school_CN }
                ]
            })
            qrCode.value = data.qrCode || ''
            deepLink.value = data.deepLink || ''
            cardGenerated.value = true
            if (email.value !== 'did-test@xiaozhi.moe') {
                sessionToken.value = ''
            }
        } catch (error) {
            console.error('產生失敗', error)
            alert(error.message || '學生證產生失敗，請確認資料格式是否正確')
        }
    }

    const verifyCard = async () => {
        verificationCountdown.value = 60
        verifyFailed.value = false
        verifyQrCode.value = ''
        verifiedData.value = []
        auth_uri.value = ''

        try {
            const qrRes = await fetchVerificationQr(verifyTid.value)

            verifyQrCode.value = qrRes.qrcode_image
            auth_uri.value = qrRes.auth_uri

            if (countdownInterval.value) clearInterval(countdownInterval.value)
            countdownInterval.value = setInterval(() => {
                verificationCountdown.value--
            }, 1000)

            verifyInterval = setInterval(fetchVerifyResult, 5000)

            verifyTimeout = setTimeout(() => {
                clearInterval(verifyInterval)
                clearInterval(countdownInterval.value)
                verifyFailed.value = true
            }, 60000)
        } catch (error) {
            console.error('驗證失敗', error)
            verifyFailed.value = true
            alert(error.message || '驗證 QR 產生失敗')
        }
    }

    const fetchVerifyResult = async () => {
        try {
            const result = await fetchVerificationResult(verifyTid.value)
            if (result.verify_result) {
                verifiedData.value = result.data?.[0]?.claims || []
                verified.value = true
                clearInterval(verifyInterval)
                clearTimeout(verifyTimeout)
            }
        } catch (e) {
            console.warn('查詢中...')
        }
    }

    const sendVerificationEmail = async () => {
        sessionToken.value = ''

        if (email.value === 'did-test@xiaozhi.moe') {
            verified.value = true;
            emailSent.value = true;
            verifyPending.value = false;
            form.value.school_CN = '國立台灣沒有考上大學'
            form.value.number = '00000000';
            form.value.name = '張三';
            registrationDateStartRaw.value = '2020-03-15';
            registrationDateEndRaw.value = '2077-03-15';
            sessionToken.value = 'TEST_BYPASS'
            alert('測試帳號免驗證成功');
            return;
        }

        try {
            const res = await requestEmailVerification(email.value)
            if (res.success) {
                verifyPending.value = true
                emailSent.value = true
                form.value.school_CN = res.school_name || '' // ⬅ 自動填入學校名稱
                pollVerificationStatus()
                alert(res.message || '驗證信已寄出，請至信箱完成驗證')
            } else {
                alert(res.error || '驗證失敗')
            }
        } catch (err) {
            alert(err.message || '伺服器錯誤，請稍後再試')
        }
    }

    const pollVerificationStatus = () => {
        const checkTimer = setInterval(async () => {
            try {
                const res = await checkEmailVerification(email.value)
                if (res.verified) {
                    verified.value = true
                    form.value.number = res.student_id // ⬅ 修正 student_number 欄位綁定
                    sessionToken.value = res.session_token || ''
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
        sessionToken.value = ''
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
