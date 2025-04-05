<template>
    <main>
        <div
            class="max-w-2xl mx-auto bg-white shadow-lg rounded-xl p-8 border border-slate-200 transition-all duration-300 hover:shadow-xl">
            <div class="flex items-center justify-center mb-6">
                <h1 class="text-2xl font-semibold text-slate-700">使用說明</h1>
            </div>
            <div class="space-y-5">
                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200 hover:shadow-md transition">
                    <h2 class="font-medium text-lg text-slate-800 mb-2">校外人士測試信箱</h2>

                    <p class="text-sm text-slate-700">
                        <span class="font-medium">信箱：</span> did-test@xiaozhi.moe
                    </p>
                    <p class="mt-1 text-sm text-slate-500">
                        此信箱免校內 email 驗證，可直接使用。
                    </p>
                </div>

                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200 hover:shadow-md transition">
                    <h2 class="font-medium text-lg text-slate-800 mb-2">下載測試版 App</h2>
                    <ul class="list-disc list-inside text-sm text-blue-500 underline">
                        <li><a href="https://play.google.com/apps/testing/tw.gov.moda.diw" target="_blank">Android
                                測試版下載</a></li>
                        <li><a href="https://testflight.apple.com/join/gxr3mQFj" target="_blank">iOS 測試版下載</a></li>
                    </ul>
                </div>

                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200">
                    <h2 class="font-medium text-lg text-slate-800 mb-2">如何使用</h2>
                    <ul class="list-disc list-inside text-sm">
                        <li>下載數位皮夾測試版本</li>
                        <li>驗證校內郵箱（請勿關閉本網頁）</li>
                        <li>填寫個人資料（該個人資料本網站不會保存，僅用於生產證件）</li>
                        <li>導入至數位憑證皮夾</li>
                    </ul>
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