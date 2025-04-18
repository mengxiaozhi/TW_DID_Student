<template>
    <main class="py-8 px-4 md:px-8 bg-slate-50 min-h-screen">
        <div class="max-w-3xl mx-auto bg-white shadow-lg rounded-xl p-8 border border-slate-200">
            <div class="text-center mb-6">
                <h1 class="text-2xl font-bold text-secondary">使用條款</h1>
                <p class="text-sm text-slate-500 mt-1">最後更新日期：2025 年 4 月 8 日</p>
                <p class="text-sm text-slate-500">本文件針對平台：<code
                        class="font-mono text-primary">did-edu.xiaozhi.moe</code></p>
            </div>

            <section class="space-y-6 text-slate-700 text-[15px] leading-relaxed">
                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">一、服務性質聲明</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>本平台為技術展示性質之開源專案，提供非正式數位學生證憑證生成、展示與驗證功能，並包含匿名留言板功能。</li>
                        <li>所有憑證資料與留言內容均由使用者自行輸入與產生，平台不代表任何學校、機關或單位之授權或背書。</li>
                        <li>所產生之憑證與留言，不得用於入學註冊、社會身份認證、法律文件用途或任何正式對外主張之情境。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">二、使用者義務</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>不得使用虛假或他人資訊進行驗證或申請數位憑證。</li>
                        <li>不得於留言板中散佈誹謗、中傷、違法、具攻擊性或不當內容。</li>
                        <li>不得利用本平台從事違反法律、公序良俗或第三方權利之行為。</li>
                        <li>應妥善保管產生之憑證鏈接與資料，不得未經授權提供予他人冒用或散布。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">三、功能條款區分</h2>
                    <h3 class="text-base font-semibold text-slate-800 mt-2 mb-1">1. 數位學生證（VC）生成功能</h3>
                    <ul class="list-disc list-inside space-y-1">
                        <li>使用者必須提供真實信箱與個人資料以完成憑證生成。</li>
                        <li>所有資料僅用於該次憑證生成過程，生成後資料由使用者自行持有與保存，平台不會保存學號、姓名或其他學籍相關資料。</li>
                    </ul>

                    <h3 class="text-base font-semibold text-slate-800 mt-4 mb-1">2. 留言板功能</h3>
                    <ul class="list-disc list-inside space-y-1">
                        <li>留言需先通過校名驗證，並可選擇是否附上實名。</li>
                        <li>留言與按讚行為將匿名記錄於系統，用於排序與防濫用之用途。</li>
                        <li>所有留言內容僅於平台上短期保存，並可能因內容違規而遭刪除。</li>
                        <li>平台保留刪除或隱藏不當留言的權利。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">四、資料隱私與安全</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>平台僅蒐集使用者輸入之信箱、姓名、學校名稱、留言內容與按讚紀錄，不保存密碼、不使用追蹤 Cookie。</li>
                        <li>除信箱驗證用途外，所有敏感資料皆於處理後即自動銷毀。</li>
                        <li>詳情請參閱我們的 <router-link to="/privacy"
                                class="text-primary underline hover:opacity-80">隱私政策</router-link>。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">五、智慧財產權</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>本平台介面與功能設計屬於開發者所有，適用所列授權條款（MIT）。</li>
                        <li>使用者於平台上產生之個人憑證資料與留言內容，仍歸使用者本人所有，惟平台保留刪除違規內容的權利。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">六、免責聲明</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>本平台僅作為技術驗證演示用途，不提供正式身份認證或法律效力。</li>
                        <li>對於因使用本平台而可能產生之資料錯誤、識別誤導或第三方誤用，開發者不負任何法律責任。</li>
                        <li>平台可隨時中止、暫停或修改任一功能，恕不另行通知。</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">七、準據法與管轄</h2>
                    <p>本條款之解釋與適用，以中華民國（台灣）法律為準據法。若發生爭議，雙方同意以台灣台北地方法院為第一審管轄法院。</p>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">八、聯絡方式</h2>
                    <p>如您對使用條款有任何疑問或建議，歡迎透過以下方式與我們聯繫：</p>
                    <ul class="list-disc list-inside mt-1">
                        <li>Email：<a href="mailto:me@xiaozhi.moe"
                                class="text-primary underline hover:opacity-80">me@xiaozhi.moe</a></li>
                    </ul>
                </div>
            </section>
        </div>
    </main>
</template>