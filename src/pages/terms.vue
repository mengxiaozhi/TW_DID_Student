<template>
    <main class="py-8 px-4 md:px-8 bg-slate-50 min-h-screen">
        <div class="max-w-3xl mx-auto bg-white shadow-lg rounded-xl p-8 border border-slate-200">
            <div class="text-center mb-6">
                <h1 class="text-2xl font-bold text-secondary">使用條款</h1>
                <p class="text-sm text-slate-500 mt-1">最後更新日期：2025 年 4 月 21 日</p>
                <p class="text-sm text-slate-500">本文件針對平台：<code
                        class="font-mono text-primary">did-edu.xiaozhi.moe</code></p>
            </div>

            <section class="space-y-6 text-slate-700 text-[15px] leading-relaxed">
                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">一、服務性質聲明</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>本平台為開源、非營利之技術展示性質專案，提供非正式數位學生證（Verifiable Credential, VC）生成、展示與驗證功能，另設有匿名留言板作為社群互動平台。</li>
                        <li>所有憑證與留言內容皆由使用者主動輸入與產生，平台不代表任何學校、政府機關或法人之授權、背書或保證。</li>
                        <li>本平台產生之憑證不得用於入學註冊、身份證明、法律用途或其他正式文件替代，使用者應自行辨識風險。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">二、使用者義務</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>不得使用虛假或他人資料進行憑證申請或驗證。</li>
                        <li>不得於留言板發表誹謗、仇恨、違法、騷擾、攻擊或不當言論。</li>
                        <li>不得從事任何違反中華民國法律、公序良俗或侵害第三方權益之行為。</li>
                        <li>使用者應妥善保管由平台產生之憑證資料或連結，避免資料外流、冒用或濫用。</li>
                        <li>若您為未滿 16 歲之未成年人，請於監護人或教師協助下使用本服務。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">三、功能條款區分</h2>
                    <h3 class="text-base font-semibold text-slate-800 mt-2 mb-1">1. 數位學生證（VC）生成功能</h3>
                    <ul class="list-disc list-inside space-y-1">
                        <li>使用者需提供真實且可驗證之電子郵件信箱與必要資料，以完成憑證生成流程。</li>
                        <li>憑證產生後由使用者自行保存，平台不永久保留學號、姓名或學籍資料，僅保留 Email 信箱（詳見第四條）。</li>
                        <li>憑證用途僅供個人識別展示，不具備法律效力，亦不得主張任何學籍或身份認證權利。</li>
                    </ul>

                    <h3 class="text-base font-semibold text-slate-800 mt-4 mb-1">2. 留言板功能</h3>
                    <ul class="list-disc list-inside space-y-1">
                        <li>使用者需先完成學校驗證，方可進行留言，並可選擇是否附上實名資訊。</li>
                        <li>留言與按讚行為將匿名記錄於系統，用於防濫用與內容排序分析。</li>
                        <li>所有留言內容由使用者自行發表，平台不預審留言內容，但保留審查與刪除權限。</li>
                        <li>違反社群規範之留言，平台可依情節刪除、隱藏或封鎖相關功能。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">四、資料隱私與安全</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>本平台僅蒐集使用者輸入之電子郵件、姓名、學校名稱、留言內容與按讚紀錄，不保存密碼、不使用追蹤 Cookie、也不進行行銷推播。</li>
                        <li>為改善產品品質與服務規劃，Email 信箱將永久保留，僅用於未來產品調研、使用者問卷聯繫或系統改版通知等非商業用途。</li>
                        <li>使用者可來信請求刪除其 Email 或拒絕後續聯繫，詳情請見 <router-link to="/privacy"
                                class="text-primary underline hover:opacity-80">隱私政策</router-link>。</li>
                        <li>除信箱外，所有個資皆於處理後即自動銷毀，不建立使用者帳號、不進行跨網站追蹤。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">五、智慧財產權</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>本平台介面設計、後端架構與整體功能皆屬開發者所有，並依據開源授權條款（MIT License）釋出。</li>
                        <li>使用者透過本平台產生之個人憑證與留言內容仍屬使用者本人所有權利財產，平台僅於必要時行使違規刪除權利。</li>
                        <li>未經授權不得重製、修改或轉售本平台之功能架構或程式碼。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">六、免責聲明</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>本平台為展示用途，不承擔任何憑證資訊錯誤、識別誤導或資料被第三方濫用所導致之責任。</li>
                        <li>使用者應自行評估憑證與留言之正確性、完整性與外部使用風險。</li>
                        <li>開發者得視情況隨時中止、暫停或調整任一功能而不另行通知，亦不對因此產生之資料遺失或可用性影響負責。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">七、準據法與管轄</h2>
                    <p>本使用條款之解釋與適用，以中華民國（台灣）法律為準據法。若發生爭議，雙方同意以台灣台北地方法院為第一審管轄法院。</p>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">八、聯絡方式</h2>
                    <p>如您對本使用條款有任何問題、建議或欲行使資料權利，歡迎透過下列方式與我們聯繫：</p>
                    <ul class="list-disc list-inside mt-1">
                        <li>Email：<a href="mailto:me@xiaozhi.moe"
                                class="text-primary underline hover:opacity-80">me@xiaozhi.moe</a></li>
                        <li>資料控管者與開發者：Mengxiaozhi</li>
                    </ul>
                </div>
            </section>
        </div>
    </main>
</template>
