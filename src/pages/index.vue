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
                                    required placeholder="@gm.chihlee.edu.tw" />
                            </div>
                            <p class="mt-1 text-xs text-slate-500">僅限 @gm.chihlee.edu.tw 或 @mail.chihlee.edu.tw</p>
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
                            正在等待驗證中...
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

                        <!-- Two-column layout for personal info -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                            <!-- Name field -->
                            <div class="md:col-span-1">
                                <label class="block mb-2 text-sm font-medium text-slate-700">姓名</label>
                                <div class="relative">
                                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400"
                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                        </svg>
                                    </div>
                                    <input v-model="form.name"
                                        class="w-full pl-10 border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-200"
                                        required pattern="^[\u4e00-\u9fa5_a-zA-Z0-9]+$" placeholder="請輸入您的姓名" />
                                </div>
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
                                    <input v-model="form.student_number"
                                        class="w-full pl-10 border border-slate-200 p-3 rounded-lg bg-slate-50 text-slate-500 cursor-not-allowed"
                                        readonly />
                                </div>
                                <p class="mt-1 text-xs text-slate-500">學號已自動從您的學校信箱取得</p>
                            </div>
                        </div>

                        <!-- Department selection with enhanced UI -->
                        <div>
                            <label class="block mb-2 text-sm font-medium text-slate-700">科系</label>
                            <div class="relative">
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path d="M12 14l9-5-9-5-9 5 9 5z" />
                                        <path
                                            d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />
                                    </svg>
                                </div>
                                <select v-model="form.department_chinese" @change="onDepartmentChange"
                                    class="w-full pl-10 border border-slate-300 p-3 pr-8 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-200 appearance-none"
                                    required>
                                    <option value="" disabled selected>請選擇科系</option>
                                    <option v-for="d in departments" :key="d.zh" :value="d.zh">
                                        {{ d.zh }} / {{ d.en }}
                                    </option>
                                </select>
                                <div
                                    class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3 text-slate-400">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M19 9l-7 7-7-7" />
                                    </svg>
                                </div>
                            </div>
                        </div>

                        <!-- Registration dates with improved calendar UI -->
                        <div class="bg-slate-50 p-5 rounded-lg border border-slate-200">
                            <h3 class="text-sm font-medium text-slate-700 mb-4 flex items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2 text-blue-500" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                </svg>
                                註冊有效期間
                            </h3>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                                <div>
                                    <label class="block mb-2 text-sm font-medium text-slate-700">開始日期</label>
                                    <div class="relative">
                                        <div
                                            class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400"
                                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                            </svg>
                                        </div>
                                        <input type="date" v-model="registrationDateStartRaw"
                                            class="w-full pl-10 border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-200"
                                            required />
                                    </div>
                                </div>
                                <div>
                                    <label class="block mb-2 text-sm font-medium text-slate-700">結束日期</label>
                                    <div class="relative">
                                        <div
                                            class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400"
                                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                            </svg>
                                        </div>
                                        <input type="date" v-model="registrationDateEndRaw"
                                            class="w-full pl-10 border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all duration-200"
                                            required />
                                    </div>
                                </div>
                            </div>
                            <p class="mt-3 text-xs text-slate-500">請選擇數位學生證的有效期限，通常為您的學期或學年期間</p>
                        </div>

                        <!-- Submit button with animation -->
                        <button type="submit"
                            class="w-full py-4 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white font-medium rounded-lg shadow-md hover:shadow-lg transition-all duration-200 flex justify-center items-center mt-6">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                            </svg>
                            生成數位學生證
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
        department_chinese: '',
        department_english: '',
        student_number: '',
        registration_date_start: '',
        registration_date_end: ''
    })

    const departments = [
        { zh: '商務智慧與創新研究所', en: 'GraduateInstituteofBusinessIntelligenceandInnovation' },
        { zh: '企業管理系企業管理系', en: 'DepartmentofBusinessAdministration' },
        { zh: '服務業經營管理碩士班', en: 'MasterProgramofServiceIndustryManagement' },
        { zh: '財務金融系', en: 'DepartmentofFinance' },
        { zh: '會計資訊系', en: 'DepartmentofAccounting Information' },
        { zh: '行銷與流通管理系', en: 'DepartmentofMarketingandDistributionManagement' },
        { zh: '休閒遊憩管理系', en: 'DepartmentofLeisureandRecreationManagement' },
        { zh: '國際貿易系', en: 'DepartmentofInternationalTrade' },
        { zh: '國際貿易系國際經營與數位貿易碩士班', en: 'MasterProgramofInternationalBusinessandDigitalTrade' },
        { zh: '應用英語系', en: 'DepartmentofAppliedEnglish' },
        { zh: '應用日語系', en: 'DepartmentofAppliedJapanese' },
        { zh: '資訊管理系', en: 'DepartmentofInformationManagement' },
        { zh: '商務科技管理系', en: 'DepartmentofBusinessTechnologyManagement' },
        { zh: '多媒體設計系', en: 'DepartmentofMultimediaDesign' }
    ]

    const onDepartmentChange = (e) => {
        const selectedZh = e.target.value
        const selected = departments.find(d => d.zh === selectedZh)
        if (selected) {
            form.value.department_chinese = selected.zh
            form.value.department_english = selected.en
        }
    }

    // 日期的原始輸入格式 YYYY-MM-DD
    const registrationDateStartRaw = ref('')
    const registrationDateEndRaw = ref('')

    // 當使用者選擇新日期時，自動轉換成 YYYYMMDD 格式儲存到表單
    watch(registrationDateStartRaw, (val) => {
        if (val) form.value.registration_date_start = val.replace(/-/g, '')
    })
    watch(registrationDateEndRaw, (val) => {
        if (val) form.value.registration_date_end = val.replace(/-/g, '')
    })

    // 若已有值，初始化 raw（表單 reset 時適用）
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
                vcId: 238720,
                vcCid: 'chihlee_student_card',
                fields: [
                    { type: 'BASIC', cname: '姓名', ename: 'name', content: form.value.name },
                    { type: 'CUSTOM', cname: '科系', ename: 'department_chinese', content: form.value.department_chinese },
                    { type: 'CUSTOM', cname: 'Department', ename: 'department_english', content: form.value.department_english },
                    { type: 'CUSTOM', cname: '學號', ename: 'student_number', content: form.value.student_number },
                    { type: 'CUSTOM', cname: '註冊日期_開始', ename: 'registration_date_start', content: form.value.registration_date_start },
                    { type: 'CUSTOM', cname: '註冊日期_結束', ename: 'registration_date_end', content: form.value.registration_date_end },
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
            // 測試帳號
            verified.value = true;
            emailSent.value = true;
            verifyPending.value = false;
            form.value.student_number = '00000000';
            form.value.name = '張三';
            form.value.registration_date_start = '20200315';
            form.value.registration_date_end = '20770315';
            form.value.department_chinese = '資訊管理系';
            form.value.department_english = 'DepartmentofInformationManagement';

            // 更新日期選擇器的顯示
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
                    form.value.student_number = res.data.student_id
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