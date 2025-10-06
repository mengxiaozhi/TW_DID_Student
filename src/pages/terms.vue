<template>
    <div class="info-page min-h-screen bg-slate-50">
        <section
            class="relative overflow-hidden bg-gradient-to-br pb-20">
            <div class="hero-intro py-10 md:py-12">
                <div class="space-y-5 text-center lg:text-left">
                    <span class="hero-badge mx-auto lg:mx-0">
                        使用條款
                    </span>
                    <div class="space-y-3">
                        <h1 class="text-3xl md:text-4xl font-bold text-slate-900 leading-tight">
                            保障實驗性服務的使用共識
                        </h1>
                        <p class="text-slate-600 text-base md:text-lg leading-relaxed max-w-3xl mx-auto lg:mx-0">
                            DID 校園專案是一個非營利、以教學展示為目的的實驗平台。以下條款說明使用者在操作本服務時的權利、義務與責任，協助我們共同維護安全、尊重的數位應用環境。
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
                <div class="absolute -top-28 -right-16 h-72 w-72 rounded-full bg-primary/10 blur-3xl"></div>
                <div class="absolute bottom-10 left-8 h-48 w-48 rounded-full bg-secondary/10 blur-2xl"></div>
            </div>
        </section>

        <section class="px-4 md:px-6 -mt-12 md:-mt-16 pb-24">
            <div class="max-w-5xl mx-auto floating-card p-6 md:p-10 space-y-10">
                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">一、服務性質聲明</h2>
                    <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>本平台為開源、非營利之技術展示專案，提供非正式數位學生證（Verifiable Credential, VC）生成、展示與驗證，以及匿名留言板功能。</li>
                        <li>所有憑證與留言內容皆由使用者主動輸入，平台不代表任何學校、政府機關或法人之授權、背書或保證。</li>
                        <li>本平台產生之憑證不得用於正式身份驗證或法律用途，使用者應自行辨識風險。</li>
                    </ul>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">二、使用者義務</h2>
                    <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>不得使用虛假或他人資料進行憑證申請或驗證。</li>
                        <li>不得於留言板發表誹謗、仇恨、違法或其他侵害權益之言論。</li>
                        <li>不得從事違反中華民國法律或公序良俗的行為。</li>
                        <li>應妥善保管由平台產生的憑證資料或連結，避免外流或濫用。</li>
                        <li>未滿 16 歲的使用者，請於監護人或教師協助下操作本服務。</li>
                    </ul>
                </article>

                <article class="space-y-4">
                    <h2 class="text-xl font-semibold text-slate-900">三、功能條款區分</h2>
                    <div class="space-y-3">
                        <h3 class="text-lg font-semibold text-secondary">1. 數位學生證（VC）生成功能</h3>
                        <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                            <li>使用者需提供真實且可驗證之電子郵件與必要資料，以完成憑證生成流程。</li>
                            <li>憑證產生後由使用者自行保存，平台不保留學號、姓名或學籍資料，僅保留 Email 信箱（詳見資料隱私說明）。</li>
                            <li>憑證僅供個人識別展示，無法律效力，亦不得主張任何學籍或身份認證權利。</li>
                        </ul>
                    </div>
                    <div class="space-y-3">
                        <h3 class="text-lg font-semibold text-secondary">2. 留言板功能</h3>
                        <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                            <li>使用者需完成學校驗證後才可留言，並可選擇是否附上實名資訊。</li>
                            <li>留言與按讚行為以匿名方式記錄，僅用於防濫用與內容排序分析。</li>
                            <li>平台不預審留言內容，但保留審查與刪除違規留言的權利。</li>
                            <li>違反社群規範者，平台得依情節限制或封鎖相關功能。</li>
                        </ul>
                    </div>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">四、資料隱私與安全</h2>
                    <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>平台僅蒐集電子郵件、姓名、學校名稱、留言內容與按讚紀錄，不保存密碼、不使用追蹤 Cookie、亦不進行行銷推播。</li>
                        <li>Email 信箱將永久保留，以便進行產品調研、問卷或系統通知等非商業用途；如需刪除請來信。</li>
                        <li>除信箱外，其他個資於處理後即自動銷毀，不建立使用者帳號也不跨站追蹤。</li>
                        <li>詳見 <router-link to="/privacy" class="text-primary underline">隱私政策</router-link> 取得更多資料保護資訊。</li>
                    </ul>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">五、智慧財產權</h2>
                    <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>本平台介面設計、後端架構與整體功能由開發者所有，並依 MIT License 開源釋出。</li>
                        <li>使用者於平台產生的憑證與留言內容仍屬個人所有，平台僅保留違規刪除之權利。</li>
                        <li>未經授權不得重製、修改或轉售平台程式碼與功能架構。</li>
                    </ul>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">六、免責聲明</h2>
                    <ul class="list-disc pl-5 space-y-2 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>本平台為展示用途，不承擔因憑證資訊錯誤、識別誤導或第三方濫用所造成之責任。</li>
                        <li>使用者應自行評估憑證與留言之正確性、完整性與外部使用風險。</li>
                        <li>開發者得隨時調整或暫停功能，對因此造成的資料遺失或可用性影響不負責。</li>
                    </ul>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">七、準據法與管轄</h2>
                    <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                        本條款之解釋與適用，以中華民國（台灣）法律為準據法。如有爭議，雙方同意以台灣台北地方法院為第一審管轄法院。
                    </p>
                </article>

                <article class="space-y-3">
                    <h2 class="text-xl font-semibold text-slate-900">八、聯絡方式</h2>
                    <p class="text-sm md:text-base text-slate-600 leading-relaxed">
                        若對本使用條款有任何疑問、建議或欲行使資料權利，歡迎與我們聯繫：
                    </p>
                    <ul class="list-disc pl-5 space-y-1 text-sm md:text-base text-slate-600 leading-relaxed">
                        <li>Email：<a href="mailto:me@xiaozhi.moe" class="text-primary underline">me@xiaozhi.moe</a></li>
                        <li>資料控管者與開發者：Mengxiaozhi</li>
                    </ul>
                </article>

                <footer class="pt-6 border-t border-slate-200/70 text-center text-xs md:text-sm text-slate-500">
                    感謝您參與這項實驗性服務，一起推進可信賴的校園數位身份體驗。
                </footer>
            </div>
        </section>
    </div>
</template>
