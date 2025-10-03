<template>
    <main class="py-8 px-4 md:px-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-screen fade-in">
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

                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200">
                    <h2 class="font-medium text-lg text-slate-800 mb-2">關於作者想說的話</h2>
                    <p class="text-sm text-slate-600">
                        我叫劉訊志，開發這個的當下就讀於致理科技大學資訊管理系一年級。<br>
                        Email:me@xiaozhi.moe<br>
                        <br>
                        這是我對於未來證件的想像，我們可以僅授權單一部分來證明我們擁有學生身分而不必上傳證件照片或一直重複的驗證edu信箱。健保卡和身分證同理（理工男的浪漫吧）<br>
                        我真的覺得數位憑證皮夾是個應該要大力推廣的東西，我也正在努力開發著它的其他用途。<br>
                        原本這個東西只開放我自己的學校，然後被告知這樣違反本校的商標權所以我改成了開放全部學校然後卡面及資料全部重新設計……<br>
                        我只是想做技術演示而已，致理科技大學太扯了，所以後來我決定開放全部學校<br>
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
                        <span class="font-medium">VC模板代碼/名稱：</span>did_edu_card/數位憑證皮夾學生證<br>
                        <span class="font-medium">驗證服務代碼(ref)：</span>自訂（例如：00000000_did_edu_card_full）<br>
                        <span class="font-medium">VP代碼：</span>自訂（例如：did_edu_card_full）<br>
                        <span class="font-medium">VP名稱：</span>自訂（例如：數位學生證全部資料）<br>
                        <br>
                        具體步驟請查閱數位憑證皮夾開發文檔
                    </p>
                </div>


                <div class="pt-4 border-t border-slate-200 text-center">
                    <p style="font-size: 0.9em; margin-top:1.5em;">
                        請參閱
                        <router-link class="underline blue-500" to="/terms" target="_blank">使用條款</router-link>
                        與
                        <router-link class="underline" to="/privacy" target="_blank">隱私政策</router-link>
                    </p>
                    <br>
                    <p class="text-xs text-slate-500 md:text-sm ">© 版權所有
                        <a href="https://xiaozhi.moe" target="_blank" class="underline text-primary">Mengxiaozhi</a>
                        ｜聯絡：<a class="underline text-primary" href="mailto:me@xiaozhi.moe">me@xiaozhi.moe</a>
                    </p>
                </div>
            </div>
        </div>
    </main>
</template>
