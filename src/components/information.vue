<template>
    <section class="px-4 md:px-6 pb-16">
        <div class="max-w-6xl mx-auto grid gap-6 md:grid-cols-3">
            <div class="surface p-6 md:col-span-2 space-y-4">
                <div class="flex items-center gap-3">
                    <span class="chip">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M12 8c1.656 0 3-1.567 3-3.5S13.656 1 12 1 9 2.567 9 4.5 10.344 8 12 8zm0 2c-2.21 0-4-1.343-4-3s1.79-3 4-3 4 1.343 4 3-1.79 3-4 3zm0 2c4.418 0 8 1.79 8 4v2H4v-2c0-2.21 3.582-4 8-4z" />
                        </svg>
                        校外測試專用帳號
                    </span>
                    <span class="text-xs text-slate-500">Demo 用戶可直接登入體驗</span>
                </div>
                <div class="bg-white/70 border border-slate-200 rounded-xl p-6 space-y-3 shadow-sm">
                    <div class="flex items-center justify-between">
                        <p class="text-sm font-semibold text-slate-700">信箱</p>
                        <span class="text-xs text-slate-400">自動帶入所有欄位</span>
                    </div>
                    <p class="text-2xl font-mono text-primary">did-test@xiaozhi.moe</p>
                    <p class="text-xs text-slate-500">登入後可直接跳過信箱驗證步驟，方便快速演示各項功能。</p>
                </div>
                <div class="grid gap-4 md:grid-cols-2">
                    <div class="surface-muted p-4 rounded-xl space-y-2">
                        <p class="text-sm font-semibold text-secondary">開發者資源</p>
                        <ul class="text-xs text-slate-600 space-y-1">
                            <li>• DID 憑證格式與欄位說明</li>
                            <li>• 沙盒環境 Access Token 申請流程</li>
                            <li>• REST API 範例（Issuer / Verifier）</li>
                        </ul>
                    </div>
                    <div class="surface-muted p-4 rounded-xl space-y-2">
                        <p class="text-sm font-semibold text-secondary">校務應用建議</p>
                        <ul class="text-xs text-slate-600 space-y-1">
                            <li>• 新生報到 / 系所迎新快速驗證</li>
                            <li>• 校園活動票券與投票系統串接</li>
                            <li>• 合作社、宿舍門禁等實名服務</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="surface-muted p-6 rounded-2xl space-y-4">
                <h3 class="text-lg font-semibold text-slate-900">下載測試版 App</h3>
                <p class="text-xs text-slate-500">請先安裝官方沙盒 App，再進行憑證導入或驗證流程。</p>
                <div class="space-y-3">
                    <a href="https://play.google.com/apps/testing/tw.gov.moda.diw" target="_blank"
                        class="w-full inline-flex items-center justify-between px-4 py-3 rounded-xl border border-slate-200 bg-white shadow-sm hover:border-primary transition">
                        <span class="text-sm font-medium text-slate-700">Android 測試版下載</span>
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-primary" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M14 5l7 7-7 7M5 5l7 7-7 7" />
                        </svg>
                    </a>
                    <a href="https://testflight.apple.com/join/gxr3mQFj" target="_blank"
                        class="w-full inline-flex items-center justify-between px-4 py-3 rounded-xl border border-slate-200 bg-white shadow-sm hover:border-primary transition">
                        <span class="text-sm font-medium text-slate-700">iOS TestFlight 測試</span>
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-primary" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M14 5l7 7-7 7M5 5l7 7-7 7" />
                        </svg>
                    </a>
                </div>

                <div class="space-y-3 pt-4 border-t border-slate-200">
                    <h4 class="text-sm font-semibold text-slate-900">流程提醒</h4>
                    <ul class="text-xs text-slate-600 space-y-2">
                        <li>• 驗證信寄出後請保持本頁開啟，系統會自動偵測狀態。</li>
                        <li>• 憑證資料僅在生成時使用，不會儲存在伺服器。</li>
                        <li>• 若遇到信箱驗證延遲，可 30 秒後點擊重新寄送。</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="max-w-6xl mx-auto mt-10 flex flex-col md:flex-row md:items-center md:justify-between gap-4 text-xs text-slate-500">
            <p>© 版權所有 <a href="https://xiaozhi.moe" target="_blank" class="text-primary underline">Mengxiaozhi</a> ｜ 聯絡：<a class="text-primary underline" href="mailto:me@xiaozhi.moe">me@xiaozhi.moe</a></p>
            <div class="flex items-center gap-3">
                <router-link class="text-slate-500 hover:text-primary transition" to="/terms" target="_blank">使用條款</router-link>
                <span class="text-slate-300">|</span>
                <router-link class="text-slate-500 hover:text-primary transition" to="/privacy" target="_blank">隱私政策</router-link>
            </div>
        </div>
    </section>
</template>
