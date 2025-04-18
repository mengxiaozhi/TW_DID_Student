<template>
    <div class="min-h-screen flex flex-col bg-gradient-to-br from-slate-50 to-slate-100">
        <!-- Main Content -->
        <main class="py-8 px-4 md:px-8">
            <div
                class="max-w-2xl mx-auto bg-white shadow-lg rounded-xl p-8 space-y-8 border border-slate-200 transition-all duration-300 hover:shadow-xl">
                <!-- Tab Navigation -->
                <div class="flex border-b border-gray-200">
                    <button
                        class="flex-1 py-3 px-1 sm:px-6 font-medium text-center relative overflow-hidden transition-all hover:bg-gray-50 focus:outline-none group text-xs sm:text-sm"
                        :class="activeTab === 'generate' ? 'text-primary' : 'text-gray-600'"
                        @click="activeTab = 'generate'">
                        <div class="flex items-center justify-center md:text-sm">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                            </svg>
                            生成學生證
                        </div>
                        <div class="absolute bottom-0 left-0 w-full h-0.5 bg-primary transform scale-x-0 group-hover:scale-x-100 transition-transform origin-left"
                            :class="activeTab === 'generate' ? 'scale-x-100' : 'scale-x-0'"></div>
                    </button>

                    <router-link to="/broad" custom v-slot="{ navigate, isActive }">
                        <button @click="navigate(); activeTab = 'broad'"
                            class="flex-1 py-3 px-1 sm:px-6 font-medium text-center relative overflow-hidden transition-all hover:bg-gray-50 focus:outline-none group text-xs sm:text-sm"
                            :class="activeTab === 'broad' || isActive ? 'text-primary' : 'text-gray-600'">
                            <div class="flex items-center justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
                                </svg>
                                匿名留言板
                            </div>
                            <div class="absolute bottom-0 left-0 w-full h-0.5 bg-primary transform scale-x-0 group-hover:scale-x-100 transition-transform origin-left"
                                :class="activeTab === 'broad' ? 'scale-x-100' : 'scale-x-0'"></div>
                        </button>
                    </router-link>

                    <button
                        class="flex-1 py-3 px-1 sm:px-6 font-medium text-center relative overflow-hidden transition-all hover:bg-gray-50 focus:outline-none group text-xs sm:text-sm"
                        :class="activeTab === 'verify' ? 'text-primary' : 'text-gray-600'"
                        @click="activeTab = 'verify'; generateUUID()">
                        <div class="flex items-center justify-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                            </svg>
                            驗證學生證
                        </div>
                        <div class="absolute bottom-0 left-0 w-full h-0.5 bg-primary transform scale-x-0 group-hover:scale-x-100 transition-transform origin-left"
                            :class="activeTab === 'verify' ? 'scale-x-100' : 'scale-x-0'"></div>
                    </button>
                </div>

                <!-- Generate Student ID Content -->
                <div v-if="activeTab === 'generate'" class="space-y-6">
                    <template v-if="!emailSent">
                        <h3 class="text-lg font-semibold text-gray-800 mb-4">第一步：驗證您的學生身分</h3>

                        <form @submit.prevent="sendVerificationEmail" class="space-y-5">
                            <div class="bg-primary/10 rounded-lg p-4 border border-primary/20 mb-6">
                                <div class="flex">
                                    <div class="flex-shrink-0">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                    </div>
                                    <div class="ml-3">
                                        <p class="text-sm text-primary">我們將向您的學校信箱發送驗證碼，請確保您能夠訪問此信箱。</p>
                                    </div>
                                </div>
                            </div>

                            <div>
                                <label class="block mb-2 font-medium text-gray-700">學校信箱</label>
                                <div class="relative">
                                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400"
                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                        </svg>
                                    </div>
                                    <input v-model="email" type="email" required placeholder="您的學校信箱地址" class="w-full rounded-lg border border-slate-300 py-2 pr-3 pl-9
               focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all" />
                                </div>
                                <p class="mt-2 text-xs text-gray-500">僅限 edu.tw 信箱可申請數位學生證</p>
                            </div>

                            <button type="submit"
                                class="w-full py-3 bg-primary text-white font-medium rounded-lg hover:bg-primary/90 shadow-sm hover:shadow transition duration-200 flex items-center justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                </svg>
                                寄送驗證碼
                            </button>
                        </form>
                    </template>

                    <div v-if="verifyPending && !verified" class="py-8 text-center">
                        <div class="w-16 h-16 mx-auto mb-4 flex items-center justify-center">
                            <svg class="animate-spin h-10 w-10 text-primary" xmlns="http://www.w3.org/2000/svg"
                                fill="none" viewBox="0 0 24 24">
                                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor"
                                    stroke-width="4"></circle>
                                <path class="opacity-75" fill="currentColor"
                                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                                </path>
                            </svg>
                        </div>
                        <h3 class="text-lg font-medium text-gray-800 mb-2">驗證進行中</h3>
                        <p class="text-gray-600">請前往您的郵箱查收驗證郵件並點擊驗證連結</p>
                        <!--
                        <p class="text-sm text-gray-500 mt-4">沒有收到郵件？<button
                                class="text-primary hover:underline">重新發送</button></p>
                        -->
                    </div>

                    <!-- Student ID Information Form -->
                    <form v-if="verified && !cardGenerated" @submit.prevent="generateCard" class="space-y-6">
                        <div class="bg-green-50 border border-green-100 rounded-lg p-4 flex items-start">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-green-500 mt-0.5 mr-3 flex-shrink-0" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M5 13l4 4L19 7" />
                            </svg>
                            <div>
                                <h4 class="font-medium text-green-800">驗證成功</h4>
                                <p class="text-sm text-green-700 mt-1">請填寫以下信息完成學生證生成</p>
                            </div>
                        </div>

                        <h3 class="text-lg font-semibold text-gray-800 mt-4">第二步：填寫學生證資訊</h3>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block mb-2 font-medium text-gray-700">姓名</label>
                                <input v-model="form.name" required pattern="^[一-龥_a-zA-Z0-9]+$" class="w-full rounded-lg border border-slate-300 py-2 pr-3 pl-3
               focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all"
                                    placeholder="請輸入您的姓名" />
                            </div>

                            <div>
                                <label class="block mb-2 font-medium text-gray-700">學號</label>
                                <div class="relative">
                                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400"
                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14" />
                                        </svg>
                                    </div>
                                    <input v-if="email === 'did-test@xiaozhi.moe'" v-model="form.number" readonly class="w-full rounded-lg border border-slate-300 py-2 pr-3 pl-9
               focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all" />
                                    <input v-else v-model="form.number" class="w-full rounded-lg border border-slate-300 py-2 pr-3 pl-9
               focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all" />
                                </div>
                                <p class="mt-1 text-xs text-gray-500">學號已自動從您的學校信箱取得</p>
                            </div>
                        </div>

                        <div>
                            <label class="block mb-2 font-medium text-gray-700">學校</label>
                            <div class="relative">
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                                    </svg>
                                </div>
                                <input v-if="email === 'did-test@xiaozhi.moe'" v-model="form.school_CN" required
                                    pattern="^[一-龥]+$" readonly
                                    class="w-full pl-10 border border-gray-300 p-3 rounded-lg bg-gray-50 text-gray-600 cursor-not-allowed focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all"
                                    placeholder="請輸入學校名稱（中文）" />
                                <input v-else v-model="form.school_CN" required pattern="^[一-龥]+$" class="w-full rounded-lg border border-slate-300 py-2 pr-3 pl-9
               focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all"
                                    placeholder="請輸入學校名稱（中文）" />
                            </div>
                            <div class="flex items-start mt-2">
                                <svg xmlns="http://www.w3.org/2000/svg"
                                    class="h-4 w-4 text-gray-400 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <p class="ml-2 text-xs text-gray-500">學校資料錯誤或未知？<a class="text-primary hover:underline"
                                        href="https://forms.gle/6oCmMdNBK8gSMCveA" target="_blank">填寫表單</a> 完善系統幫助下一個同學
                                </p>
                            </div>
                        </div>

                        <button type="submit"
                            class="w-full py-3.5 bg-primary text-white font-medium rounded-lg hover:bg-primary/90 shadow-sm hover:shadow transition duration-200 flex items-center justify-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M5 13l4 4L19 7" />
                            </svg>
                            生成我的數位學生證
                        </button>
                    </form>

                    <!-- QR Code Display -->
                    <div v-if="qrCode" class="py-6 text-center">
                        <div class="mb-8">
                            <div
                                class="w-16 h-16 bg-green-100 rounded-full mx-auto flex items-center justify-center mb-4">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-green-500" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M5 13l4 4L19 7" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-semibold text-gray-800">學生證生成成功！</h3>
                            <p class="text-gray-600 mt-2">請使用數位憑證皮夾 App 掃描下方 QR Code</p>
                        </div>

                        <div class="bg-gray-50 p-6 rounded-xl inline-block mb-8">
                            <img :src="qrCode" alt="QRCode"
                                class="mx-auto w-52 h-52 rounded-lg shadow hover:shadow-md transition duration-300" />
                        </div>

                        <a :href="deepLink" class="block">
                            <button
                                class="w-full py-3.5 bg-primary text-white font-medium rounded-lg hover:bg-primary/90 shadow-sm hover:shadow transition duration-200 flex items-center justify-center">
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
                        <!--
                        <div class="mt-6 text-center">
                            <p class="text-sm text-gray-500">遇到問題？<a href="#"
                                    class="text-primary hover:underline">查看常見問題</a> 或 <a href="#"
                                    class="text-primary hover:underline">聯繫客服</a></p>
                        </div>
                        -->
                    </div>
                </div>

                <!-- Verify Student ID Content -->
                <div v-if="activeTab === 'verify'" class="space-y-6">
                    <template v-if="!verifiedData.length">
                        <h3 class="text-lg font-semibold text-gray-800 mb-6">驗證數位學生證</h3>

                        <div class="bg-primary/10 rounded-lg p-4 border border-primary/20 mb-6">
                            <div class="flex">
                                <div class="flex-shrink-0">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                </div>
                                <div class="ml-3">
                                    <p class="text-sm text-primary">請使用數位憑證皮夾 App 掃描以下 QR Code
                                        進行驗證。驗證過程將保護您的隱私，資料不會傷害你。</p>
                                </div>
                            </div>
                        </div>

                        <div class="mb-6">
                            <label class="block mb-2 font-medium text-gray-700">驗證碼</label>
                            <div class="relative">
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" />
                                    </svg>
                                </div>
                                <input v-model="verifyTid" readonly class="w-full border p-3 rounded-lg bg-gray-50 text-gray-700 font-mono tracking-wide border-slate-300 py-2 pr-3 pl-9
               focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all" />
                            </div>
                            <p class="mt-1 text-xs text-gray-500">這是您的唯一驗證碼，用於確認驗證請求的有效性</p>
                        </div>

                        <!-- QR Code for Verification -->
                        <div v-if="verifyQrCode && !verifyFailed" class="py-8 text-center">
                            <div
                                class="bg-gradient-to-r from-gray-50 to-gray-100 p-8 rounded-xl inline-block mb-6 border border-gray-200">
                                <img :src="verifyQrCode" alt="VerifyQRCode"
                                    class="mx-auto w-56 h-56 rounded-lg shadow-sm" />
                            </div>

                            <a :href="auth_uri" class="block mb-6">
                                <button
                                    class="w-full py-3.5 bg-primary text-white font-medium rounded-lg hover:bg-primary/90 shadow-sm hover:shadow transition duration-200 flex items-center justify-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 24 24"
                                        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                                    </svg>
                                    前往App進行驗證
                                </button>
                            </a>
                            <div class="mt-3">
                                <div class="inline-flex items-center px-4 py-2 bg-primary/10 rounded-full text-primary">
                                    <div class="animate-pulse mr-2 h-2 w-2 bg-primary rounded-full"></div>
                                    <span class="text-sm font-medium">請在{{ verificationCountdown }}秒內完成掃描</span>
                                </div>
                            </div>
                            <!--
                            <div class="flex items-center justify-center text-gray-500">
                                <div class="animate-spin rounded-full h-5 w-5 border-b-2 border-primary"></div>
                                <span class="ml-3 text-sm">等待驗證中...</span>
                            </div>
                            -->
                        </div>

                        <!-- Verification Failed Message -->
                        <div v-if="verifyFailed" class="text-center py-6">
                            <div
                                class="mx-auto w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mb-4">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-red-500" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                            </div>
                            <h3 class="text-xl font-medium text-gray-800 mb-2">驗證超時</h3>
                            <p class="text-gray-600 mb-6">驗證請求已過期，請重新開始驗證流程</p>
                            <button @click="generateUUID(); verifyCard()"
                                class="px-6 py-2.5 bg-red-100 hover:bg-red-200 text-red-700 font-medium rounded-lg transition duration-200">
                                重新開始驗證
                            </button>
                        </div>
                    </template>

                    <!-- Verification Success Result -->
                    <template v-else>
                        <div class="text-center py-6">
                            <div
                                class="mx-auto w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mb-6">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-green-500" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                </svg>
                            </div>
                            <h3 class="text-2xl font-semibold text-gray-800 mb-2">驗證成功</h3>
                            <p class="text-gray-600 mb-8">此數位學生證是有效的，以下是持證人資料</p>

                            <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden mb-6">
                                <div class="bg-gradient-to-r from-primary to-primary/50 p-4">
                                    <h4 class="text-white font-medium text-center">學生資料</h4>
                                </div>
                                <div class="divide-y divide-gray-200">
                                    <div v-for="item in verifiedData" :key="item.ename"
                                        class="px-4 py-3 flex justify-between items-center group hover:bg-gray-50">
                                        <span class="text-gray-700 font-medium">{{ item.cname }}：</span>
                                        <span class="text-gray-800">{{ item.value }}</span>
                                    </div>
                                </div>
                            </div>

                            <div class="p-4 bg-primary/10 rounded-lg border border-primary/20 mb-6">
                                <p class="text-sm text-primary">驗證通過確認該學生身份資料與數位學生證資訊一致，且證件未被篡改。</p>
                            </div>

                            <button @click="generateUUID"
                                class="px-6 py-3 bg-primary hover:bg-primary/90 text-white font-medium rounded-lg shadow-sm hover:shadow transition duration-200 flex items-center justify-center mx-auto">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1.5" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                                </svg>
                                驗證新證件
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
    const verificationCountdown = ref(60)
    const countdownInterval = ref(null)

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
        verificationCountdown.value = 60
        verifyFailed.value = false
        verifyQrCode.value = ''
        verifiedData.value = []
        auth_uri.value = ''

        try {
            const qrRes = await axios.get('https://api.xiaozhi.moe/chihlee/verify-qr', {
                params: { transaction_id: verifyTid.value }
            })

            verifyQrCode.value = qrRes.data.qrcode_image
            auth_uri.value = qrRes.data.auth_uri

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
            alert('驗證 QR 產生失敗')
        }
    }

    const fetchVerifyResult = async () => {
        try {
            const resultRes = await axios.get(`https://api.xiaozhi.moe/chihlee/verify-result`, { params: { transaction_id: verifyTid.value } })
            if (resultRes.data.verify_result) {
                verifiedData.value = resultRes.data.data[0]?.claims || []
                verified.value = true
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
            form.value.school_CN = '國立台灣没考上大學'
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