<template>
    <main class="pt-3">
        <div
            class="max-w-2xl mx-auto bg-white shadow-lg rounded-xl p-8 border border-slate-200 transition-all duration-300 hover:shadow-xl\">
            <div class="flex items-center justify-center mb-6"></div>
            <h1>使用條款</h1>
            <p><strong>最後更新日期：</strong>2025 年 4 月 7 日</p>
            <p>本文件針對平台：<code>did-edu.xiaozhi.moe</code></p>

            <h2>一、服務性質聲明</h2>
            <ul>
                <li>本平台為技術展示性質之開源專案，提供非正式數位學生證憑證生成、展示與驗證功能。</li>
                <li>所有憑證資料均由使用者自行輸入與產生，平台不代表任何學校、機關或單位之授權或背書。</li>
                <li>所產生之憑證，不得用於入學註冊、社會身份認證、法律文件用途或任何正式對外主張之情境。</li>
            </ul>

            <h2>二、使用者義務</h2>
            <ul>
                <li>不得使用虛假或他人資訊進行驗證或申請數位憑證。</li>
                <li>不得利用本平台從事違反法律、公序良俗或第三方權利之行為。</li>
                <li>應妥善保管產生之憑證鏈接與資料，不得未經授權提供予他人冒用或散布。</li>
            </ul>

            <h2>三、資料隱私與安全</h2>
            <ul>
                <li>平台僅蒐集使用者輸入之信箱、姓名與憑證內容，不接觸或保存任何學號、密碼、成績或學校系統資訊。</li>
                <li>所有驗證資訊僅用於該次憑證生成過程，完成後即自動銷毀，不做永久儲存。</li>
                <li>詳情請參閱我們的 <router-link to="/privacy">隱私政策</router-link>。</li>
            </ul>

            <h2>四、智慧財產權</h2>
            <ul>
                <li>本平台介面與功能設計屬於開發者所有，若為開源專案則適用所列授權條款（如 MIT / GPL）。</li>
                <li>使用者於平台上產生之個人憑證資料，仍歸使用者本人所有。</li>
            </ul>

            <h2>五、免責聲明</h2>
            <ul>
                <li>本平台僅作為技術驗證演示用途，不提供正式身份認證或法律效力。</li>
                <li>對於因使用本平台而可能產生之資料錯誤、識別誤導或第三方誤用，開發者不負任何法律責任。</li>
                <li>平台可隨時中止或修改服務，恕不另行通知。</li>
            </ul>

            <h2>六、準據法與管轄</h2>
            <p>本條款之解釋與適用，以中華民國（台灣）法律為準據法。若發生爭議，雙方同意以台灣台北地方法院為第一審管轄法院。</p>

            <h2>七、聯絡方式</h2>
            <p>如您對使用條款有任何疑問或建議，歡迎透過以下方式與我們聯繫：</p>
            <ul>
                <li>Email：<a href="mailto:me@xiaozhi.moe">me@xiaozhi.moe</a></li>
            </ul>
        </div>
    </main>
</template>