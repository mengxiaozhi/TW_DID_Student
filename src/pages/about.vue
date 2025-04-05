<template>
    <main>
        <div
            class="max-w-2xl mx-auto bg-white shadow-lg rounded-xl p-8 border border-slate-200 transition-all duration-300 hover:shadow-xl">
            <div class="flex items-center justify-center mb-6">
                <h1 class="text-2xl font-semibold text-slate-700">關於</h1>
            </div>

            <div class="space-y-5">
                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200">
                    <h2 class="font-medium text-lg text-slate-800 mb-2">關於本專案</h2>
                    <p class="text-sm text-slate-600">
                        本專案除了驗證學生身份的email外，完全不會儲存您的任何個人資料，所有資料都有您個人的數位皮夾自行託管。
                        本專案基於「數位發展部」開發之「數位憑證皮夾」沙盒環境，僅供學習及參考使用，非正式用途。
                        希望這項技術未來能普及，「數位憑證皮夾」透過 DID 技術可實現個人資料的去中心化存儲與自主管理。
                    </p>
                </div>

                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200 hover:shadow-md transition">
                    <h2 class="font-medium text-lg text-slate-800 mb-2">數位憑證皮夾官網</h2>
                    <a href="https://wallet.gov.tw/" target="_blank"
                        class="text-sm text-blue-500 underline">wallet.gov.tw</a><br>
                    <a href="https://verifier-sandbox.wallet.gov.tw/swaggerui/" target="_blank"
                        class="text-sm text-blue-500 underline">驗證端服務API</a><br>
                    <a href="https://issuer-sandbox.wallet.gov.tw/swaggerui/" target="_blank"
                        class="text-sm text-blue-500 underline">發行端服務API</a><br>
                </div>

                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200">
                    <h2 class="font-medium text-lg text-slate-800 mb-2">第三方接入API驗證本證件</h2>
                    <p class="text-sm text-slate-600 break-all">
                        取得數位憑證皮夾開發者帳號<br>
                        登入驗證端網頁<br>
                        <br>
                        <span class="text-lg font-medium">本證件VP資料如下</span><br>
                        <br>
                        <span class="font-medium">組織名稱：</span>一般帳號組織<br>
                        <span class="font-medium">VC模板代碼/名稱：</span>chihlee_student_card/致理科技大學數位學生證<br>
                        <span class="font-medium">驗證服務代碼(ref)：</span>自訂（例如：00000000_chihlee_student_card_full）<br>
                        <span class="font-medium">VP代碼：</span>自訂（例如：chihlee_student_card_full）<br>
                        <span class="font-medium">VP名稱：</span>自訂（例如：致理科技大學學生證全部資料）<br>
                        <br>
                        具體步驟請查閱數位憑證皮夾開發文檔
                    </p>
                </div>


                <div class="pt-4 border-t border-slate-200 text-center">
                    <p class="text-xs text-slate-500 md:text-sm ">© 版權所有
                        <a href="https://xiaozhi.moe" target="_blank" class="underline text-blue-600">Mengxiaozhi</a>
                        ｜聯絡：<a class="underline text-blue-600" href="mailto:me@xiaozhi.moe">me@xiaozhi.moe</a>
                    </p>
                </div>
            </div>
        </div>
    </main>
</template>