<template>
    <div class="info-page min-h-screen bg-slate-50">
        <section
            class="relative overflow-hidden bg-gradient-to-br pb-20">
            <div class="hero-intro py-10 md:py-12">
                <div class="space-y-5 text-center lg:text-left">
                    <span class="hero-badge mx-auto lg:mx-0">
                        隱私政策
                    </span>
                    <div class="space-y-3">
                        <h1 class="text-3xl md:text-4xl font-bold text-slate-900 leading-tight">
                            尊重個資的最小授權原則
                        </h1>
                        <p class="text-slate-600 text-base md:text-lg leading-relaxed max-w-3xl mx-auto lg:mx-0">
                            我們以示範 DID 校園應用為目標，僅蒐集完成體驗所需的最少資料。本政策說明資料蒐集、使用、保存、刪除與使用者權利，讓您清楚掌握資訊流向。
                        </p>
                    </div>
                    <div
                        class="flex flex-col sm:flex-row sm:items-center gap-2 sm:gap-4 text-xs md:text-sm text-slate-500 justify-center lg:justify-start">
                        <span>最後更新：2025 年 4 月 21 日</span>
                        <span>適用平台：<code class="font-mono text-primary">did-edu.xiaozhi.moe</code></span>
                    </div>
                </div>
            </div>

            <div class="pointer-events-none absolute inset-0">
                <div class="absolute -top-28 -right-20 h-72 w-72 rounded-full bg-primary/10 blur-3xl"></div>
                <div class="absolute bottom-12 left-8 h-52 w-52 rounded-full bg-secondary/10 blur-2xl"></div>
            </div>
        </section>

        <section class="px-4 md:px-6 -mt-12 md:-mt-16 pb-24">
            <div class="max-w-5xl mx-auto floating-card p-6 md:p-10 space-y-10">
                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">一、資料控管者（Data Controller）</h2>
                    <p class="text-sm md:text-base text-slate-600 leading-relaxed">本平台由個人開發者 Mengxiaozhi（以下稱「我們」）運營。</p>
                    <ul class="list-disc pl-5 space-y-1 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>聯絡信箱：<a href="mailto:me@xiaozhi.moe" class="text-primary underline">me@xiaozhi.moe</a></li>
                        <li>聯絡請以電子郵件為主，收到後將於 7 日內回覆。</li>
                    </ul>
                </article>

                <article class="space-y-4">
                    <h2 class="text-xl font-semibold text-slate-900">二、資料蒐集項目與用途</h2>
                    <section class="space-y-3">
                        <h3 class="text-lg font-semibold text-secondary flex items-center gap-2">
                            <span>📌 憑證生成功能</span>
                        </h3>
                        <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                            依《個資法施行細則》第 8 條第 1 項第 2 款規定，以下列出憑證生成所需資料與使用方式：
                        </p>
                        <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                            <li><strong>蒐集目的：</strong>學術憑證產出、系統驗證與體驗優化。</li>
                            <li><strong>蒐集類別：</strong>Email、姓名、學號、學校名稱。</li>
                            <li><strong>使用方式：</strong>僅限平台流程使用，不再利用或提供第三方。</li>
                            <li><strong>保存期限：</strong>Email 長期保留，其餘資料於流程結束即刪除。</li>
                            <li><strong>影響權益：</strong>如不願提供姓名或學校，可使用測試信箱完成流程，不影響核心功能。</li>
                        </ul>
                        <div class="overflow-x-auto rounded-xl border border-slate-200">
                            <table class="min-w-full text-sm md:text-base text-slate-600">
                                <thead class="bg-slate-100 text-slate-700">
                                    <tr>
                                        <th class="px-4 py-3 text-left">資料項目</th>
                                        <th class="px-4 py-3 text-left">蒐集方式</th>
                                        <th class="px-4 py-3 text-left">使用目的</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-200">
                                    <tr class="bg-white/80">
                                        <td class="px-4 py-3">Email 信箱</td>
                                        <td class="px-4 py-3">使用者主動輸入</td>
                                        <td class="px-4 py-3">用於身份驗證、辨識學校與後續非商業性聯絡（改版通知、問卷）。</td>
                                    </tr>
                                    <tr>
                                        <td class="px-4 py-3">學生學號</td>
                                        <td class="px-4 py-3">主動輸入或系統比對</td>
                                        <td class="px-4 py-3">協助生成 VC 卡面後回傳給使用者，不做另行儲存。</td>
                                    </tr>
                                    <tr class="bg-white/80">
                                        <td class="px-4 py-3">學生姓名</td>
                                        <td class="px-4 py-3">使用者主動輸入</td>
                                        <td class="px-4 py-3">顯示於 VC 卡面，供個人識別使用，不做另行儲存。</td>
                                    </tr>
                                    <tr>
                                        <td class="px-4 py-3">學校名稱</td>
                                        <td class="px-4 py-3">主動輸入或系統比對</td>
                                        <td class="px-4 py-3">呈現於 VC 卡面，確保憑證內容完整度，不做另行儲存。</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <p class="text-xs md:text-sm text-slate-500">
                            我們不會蒐集 Cookies、IP、裝置資訊、住址、照片、電話等敏感個資。
                        </p>
                    </section>

                    <section class="space-y-3">
                        <h3 class="text-lg font-semibold text-secondary">📌 留言板與互動紀錄</h3>
                        <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                            <li>蒐集內容：留言文字、按讚次數、匿名身份校驗結果。</li>
                            <li>使用目的：維護內容品質、防止濫用、統計互動資料。</li>
                            <li>保留時間：依營運需要保存，若違反規範則可依情況刪除。</li>
                        </ul>
                    </section>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">三、資料處理合法依據</h2>
                    <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>使用者明示同意（GDPR 第 6(1)(a) 條）。</li>
                        <li>合法利益（GDPR 第 6(1)(f) 條）：教育展示、體驗優化與平台研究。</li>
                        <li>Email 長期保留僅用於非商業性研究與通知，可隨時撤回同意。</li>
                    </ul>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">四、資料保存與刪除政策</h2>
                    <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>Email 信箱永久保存，如欲刪除或停止聯繫，可來信申請。</li>
                        <li>其他個資（姓名、學號等）於流程完成後立即銷毀。</li>
                        <li>平台不建立帳號制，不追蹤行為紀錄。</li>
                    </ul>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">五、資料揭露與第三方分享</h2>
                    <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                        我們不會向第三方出售、揭露或轉讓個人資料。僅在法律要求或您明示同意時，才會進行資料提供。
                    </p>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">六、使用者權利（GDPR 第 15~21 條）</h2>
                    <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>查閱、下載、修正或刪除個人資料。</li>
                        <li>限制或反對資料處理行為。</li>
                        <li>撤回對資料保留的同意（例如 Email）。</li>
                        <li>向資料保護主管機關提出申訴。</li>
                    </ul>
                    <p class="text-sm md:text-base text-slate-600">
                        請來信 <a href="mailto:me@xiaozhi.moe" class="text-primary underline">me@xiaozhi.moe</a>，我們將於 7 日內協助處理。
                    </p>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">七、跨境資料傳輸</h2>
                    <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                        本平台主機位於新加坡，涉及資料跨境處理。我們已評估服務供應商的資安合規標準，並遵循標準合約條款（SCC）。
                    </p>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">八、兒童資料保護</h2>
                    <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                        未滿 16 歲的使用者，請在監護人或教師協助下使用本平台。我們不主動蒐集未成年人的敏感個資，也不進行行銷聯絡。
                    </p>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">九、政策更新與通知</h2>
                    <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                        政策如有重大變更，將於首頁與本頁公告。更新後立即生效，建議定期查閱。
                    </p>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">十、聯絡我們</h2>
                    <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                        如對本政策或個資處理有任何疑問，歡迎透過以下方式聯絡：
                    </p>
                    <ul class="list-disc pl-5 space-y-1 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>Email：<a href="mailto:me@xiaozhi.moe" class="text-primary underline">me@xiaozhi.moe</a></li>
                        <li>資料控管者：Mengxiaozhi</li>
                    </ul>
                </article>

                <footer class="pt-6 border-t border-slate-200/70 text-center text-xs md:text-sm text-slate-500">
                    我們承諾以透明、可追溯的方式處理每一份資料，讓實驗性服務也能兼顧安全與信任。
                </footer>
            </div>
        </section>
    </div>
</template>
