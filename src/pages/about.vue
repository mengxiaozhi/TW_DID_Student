<template>
    <div class="about-page min-h-screen bg-slate-50">
        <section
            class="relative overflow-hidden bg-gradient-to-br pb-24">
            <div class="hero-intro py-10 md:py-14">
                <div class="space-y-6 text-center xl:text-left">
                    <span class="hero-badge mx-auto xl:mx-0">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M13 16h-1v-4h-1m1-4h.01M12 2a10 10 0 100 20 10 10 0 000-20z" />
                        </svg>
                        認識 DID 校園專案
                    </span>
                    <div class="space-y-3">
                        <h1 class="text-3xl md:text-4xl font-bold text-slate-900 leading-snug">
                            持續演進的 <span class="text-primary">數位學生證體驗</span> 與開源精神
                        </h1>
                        <p class="text-slate-600 text-base md:text-lg leading-relaxed max-w-3xl">
                            我們將政府 DID 沙盒的能力帶進校園生活，示範如何在不蒐集個資的前提下完成身份認證、留言互動與校務整合。這裡整理了專案理念、資料安全承諾，以及作者的開發心路歷程。
                        </p>
                    </div>
                    <div class="hero-actions justify-center xl:justify-start">
                        <router-link to="/" class="btn btn-primary">回到首頁體驗流程</router-link>
                        <router-link to="/broad" class="btn btn-outline">探索校園留言板</router-link>
                        <a href="mailto:me@xiaozhi.moe" class="btn btn-ghost">聯絡作者</a>
                    </div>
                </div>

                <div class="hero-grid">
                    <div class="stat-card">
                        <p class="text-sm text-slate-600">資料掌握權</p>
                        <p class="text-2xl font-semibold text-slate-900">100% 自主管理</p>
                        <p class="text-xs text-slate-500 mt-1">所有憑證內容皆由個人數位皮夾保存，不回傳伺服器。</p>
                    </div>
                    <div class="stat-card">
                        <p class="text-sm text-slate-600">串接環境</p>
                        <p class="text-2xl font-semibold text-slate-900">DID Sandbox</p>
                        <p class="text-xs text-slate-500 mt-1">建立於數位發展部的測試環境，專注於教學與示範。</p>
                    </div>
                    <div class="stat-card">
                        <p class="text-sm text-slate-600">專案精神</p>
                        <p class="text-2xl font-semibold text-slate-900">開源協作</p>
                        <p class="text-xs text-slate-500 mt-1">歡迎社群參與，持續優化身分驗證與校園應用體驗。</p>
                    </div>
                </div>
            </div>

            <div class="pointer-events-none absolute inset-0">
                <div class="absolute -top-24 -right-10 h-64 w-64 rounded-full bg-primary/10 blur-3xl"></div>
                <div class="absolute bottom-10 left-10 h-44 w-44 rounded-full bg-secondary/10 blur-2xl"></div>
            </div>
        </section>

        <section class="px-4 md:px-6 -mt-12 md:-mt-16 pb-24">
            <div class="max-w-6xl mx-auto grid gap-6 xl:grid-cols-[minmax(0,1.75fr)_minmax(0,1fr)]">
                <div class="floating-card p-6 md:p-10 space-y-10">
                    <section class="space-y-4">
                        <div class="flex items-center gap-3">
                            <span class="step-indicator">專案願景</span>
                            <span class="text-xs text-slate-500">打造可信賴的校園數位身份體驗</span>
                        </div>
                        <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                            本專案示範如何透過 DID 技術，在僅驗證 edu 信箱的前提下完成學生證申請、驗證與互動。所有資料由個人數位皮夾託管，平台不保存卡面資訊，確保隱私與自主管理。
                        </p>
                        <div class="grid gap-4 md:grid-cols-2">
                            <div class="bg-white/80 border border-slate-200 rounded-xl p-4 space-y-2">
                                <p class="text-sm font-semibold text-slate-800">核心體驗</p>
                                <ul class="text-xs md:text-sm text-slate-600 leading-relaxed space-y-1">
                                    <li>・三步驟完成學生證生成與導入</li>
                                    <li>・即時驗證與匿名留言串接校園應用</li>
                                    <li>・以 DID 為基礎，示範未來證件想像</li>
                                </ul>
                            </div>
                            <div class="bg-white/80 border border-slate-200 rounded-xl p-4 space-y-2">
                                <p class="text-sm font-semibold text-slate-800">資料安全保證</p>
                                <ul class="text-xs md:text-sm text-slate-600 leading-relaxed space-y-1">
                                    <li>・僅驗證學生信箱，其餘資料由使用者自管</li>
                                    <li>・伺服器不儲存 VC 卡面內容</li>
                                    <li>・驗證流程遵循數位憑證皮夾沙盒機制</li>
                                </ul>
                            </div>
                        </div>
                    </section>

                    <section class="space-y-3">
                        <div class="divider-label">作者的話</div>
                        <div class="space-y-3 text-sm md:text-base text-slate-600 leading-relaxed">
                            <p>
                                我是劉訊志，開發這個專案時就讀於致理科技大學資訊管理系一年級。這是我對未來證件的想像——讓我們能只授權必要資訊即可證明學生身份，不必重複上傳證件或驗證 edu 信箱。
                            </p>
                            <p>
                                我相信數位憑證皮夾值得更大力度推廣，因此持續探索更多應用場景。原本專案只服務我的學校，後來因為商標相關限制，我乾脆重新設計卡面並開放全台學校使用，只為做一場札實的技術演示。
                            </p>
                            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 text-sm text-slate-600">
                                Email：<a href="mailto:me@xiaozhi.moe" class="underline text-primary">me@xiaozhi.moe</a><br>
                                網站：<a href="https://xiaozhi.moe" target="_blank" class="underline text-primary">xiaozhi.moe</a>
                            </div>
                        </div>
                    </section>

                    <section class="space-y-4">
                        <div class="divider-label">技術與沙盒資訊</div>
                        <div class="grid gap-4 lg:grid-cols-2">
                            <div class="border border-slate-200 rounded-xl p-4 bg-white/85 space-y-2">
                                <p class="text-sm font-semibold text-slate-800">數位憑證皮夾資源</p>
                                <ul class="text-xs md:text-sm text-slate-600 leading-relaxed space-y-2">
                                    <li>
                                        <a href="https://wallet.gov.tw/" target="_blank" class="inline-flex items-center gap-1 text-primary underline">
                                            官方網站
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor">
                                                <path d="M12.293 2.293a1 1 0 011.414 0L18 6.586V7a1 1 0 11-2 0V5.414l-5.293 5.293a1 1 0 01-1.414-1.414L14.586 4H13a1 1 0 110-2h.293z" />
                                                <path d="M5 4a1 1 0 00-1 1v10a1 1 0 001 1h10a1 1 0 001-1v-3a1 1 0 112 0v3a3 3 0 01-3 3H5a3 3 0 01-3-3V5a3 3 0 013-3h3a1 1 0 110 2H5z" />
                                            </svg>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://verifier-sandbox.wallet.gov.tw/swaggerui/" target="_blank"
                                            class="inline-flex items-center gap-1 text-primary underline">驗證端 API 文件</a>
                                    </li>
                                    <li>
                                        <a href="https://issuer-sandbox.wallet.gov.tw/swaggerui/" target="_blank"
                                            class="inline-flex items-center gap-1 text-primary underline">發行端 API 文件</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="border border-slate-200 rounded-xl p-4 bg-white/85 space-y-2">
                                <p class="text-sm font-semibold text-slate-800">第三方整合提示</p>
                                <p class="text-xs md:text-sm text-slate-600 leading-relaxed">
                                    申請開發者帳號後，可在驗證端建立自訂流程，使用本專案的 VC 模板 `did_edu_card` 與 VP 代碼（例如 `did_edu_card_full`）進行測試。
                                </p>
                                <ul class="text-xs md:text-sm text-slate-600 leading-relaxed space-y-1">
                                    <li>・組織名稱：一般帳號組織</li>
                                    <li>・VC 模板代碼／名稱：did_edu_card／數位憑證皮夾學生證</li>
                                    <li>・驗證服務代碼 (ref)：自訂，例如 00000000_did_edu_card_full</li>
                                </ul>
                            </div>
                        </div>
                    </section>

                    <section class="pt-6 border-t border-slate-200/70 text-center space-y-3">
                        <p class="text-xs md:text-sm text-slate-500">
                            請留意：本專案僅供學習與示範使用，非正式證件發行服務。
                        </p>
                        <p class="text-xs md:text-sm text-slate-500">
                            <router-link to="/terms" class="underline text-primary">使用條款</router-link>
                            ｜
                            <router-link to="/privacy" class="underline text-primary">隱私政策</router-link>
                        </p>
                        <p class="text-xs text-slate-500">© 
                            <a href="https://xiaozhi.moe" target="_blank" class="underline text-primary">Mengxiaozhi</a>
                        </p>
                    </section>
                </div>

                <aside class="space-y-6">
                    <div class="floating-card p-6 space-y-4">
                        <p class="text-sm font-semibold text-slate-800">作者名片</p>
                        <div class="rounded-xl border border-slate-200 bg-white/85 p-4 space-y-2 text-sm text-slate-600">
                            <p>劉訊志｜致理科技大學資管系</p>
                            <p>專注於 DID、校園應用與 Web 技術整合。</p>
                            <a href="mailto:me@xiaozhi.moe" class="inline-flex items-center gap-1 text-primary underline">
                                聯絡我
                            </a>
                        </div>
                        <div class="grid gap-3 text-xs text-slate-600">
                            <div class="border border-primary/20 rounded-lg p-3 bg-primary/5">
                                <p class="font-semibold text-secondary">產品原則</p>
                                <p class="mt-1 leading-relaxed">尊重資料主權、降低驗證摩擦、保持開源精神。</p>
                            </div>
                            <div class="border border-secondary/20 rounded-lg p-3 bg-secondary/5">
                                <p class="font-semibold text-secondary">近期方向</p>
                                <p class="mt-1 leading-relaxed">探索更多校務流程的 DID 整合與跨組織驗證。</p>
                            </div>
                        </div>
                    </div>

                    <div class="floating-card p-6 space-y-4">
                        <p class="text-sm font-semibold text-slate-800">常用資源</p>
                        <ul class="space-y-3 text-sm text-slate-600">
                            <li class="flex items-center justify-between gap-3">
                                <span>專案 README</span>
                                <a href="https://github.com/xiaozhi-moe" target="_blank"
                                    class="text-primary underline text-xs">GitHub</a>
                            </li>
                            <li class="flex items-center justify-between gap-3">
                                <span>DID 學習筆記</span>
                                <a href="https://did.xiaozhi.moe" target="_blank"
                                    class="text-primary underline text-xs">did.xiaozhi.moe</a>
                            </li>
                            <li class="flex items-center justify-between gap-3">
                                <span>數位憑證皮夾開發者社群</span>
                                <a href="https://discord.gg/" target="_blank"
                                    class="text-primary underline text-xs">加入討論</a>
                            </li>
                        </ul>
                    </div>

                    <div class="floating-card p-6 space-y-4">
                        <p class="text-sm font-semibold text-slate-800">快速檢視</p>
                        <div class="space-y-3 text-xs text-slate-600">
                            <p>・本專案只在沙盒環境運行，不會與正式憑證混用。</p>
                            <p>・留言板使用 JWT 管理狀態，驗證一次即可跨頁互動。</p>
                            <p>・若您有合作或共創想法，歡迎直接來信。</p>
                        </div>
                    </div>
                </aside>
            </div>
        </section>
    </div>
</template>
