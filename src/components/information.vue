<template>
    <main class="py-8 px-4 md:px-8">
        <div class="max-w-2xl mx-auto mt-12 bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
            <div class="bg-gray-50 p-6 border-b border-gray-200">
                <h2 class="text-xl font-semibold text-gray-800">使用說明</h2>
            </div>
            <div class="p-6 space-y-4">
                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200 hover:shadow-md transition">
                    <h2 class="font-medium text-lg text-secondary mb-2">校外人士測試信箱</h2>

                    <p class="text-sm text-primary">
                        <span class="font-medium">信箱：</span> did-test@xiaozhi.moe
                    </p>
                    <p class="mt-1 text-sm text-slate-500">
                        此信箱免校內 email 驗證，可直接使用。
                    </p>
                </div>

                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200 hover:shadow-md transition">
                    <h2 class="font-medium text-lg text-secondary mb-2">下載測試版 App</h2>
                    <ul class="list-disc list-inside text-sm text-primary underline">
                        <li><a href="https://play.google.com/apps/testing/tw.gov.moda.diw" target="_blank">Android
                                測試版下載</a></li>
                        <li><a href="https://testflight.apple.com/join/gxr3mQFj" target="_blank">iOS 測試版下載</a></li>
                    </ul>
                </div>

                <div class="p-5 bg-slate-50 rounded-lg border border-slate-200">
                    <h2 class="font-medium text-lg text-secondary mb-2">如何使用</h2>
                    <ul class="list-disc list-inside text-sm">
                        <li>下載數位皮夾測試版本</li>
                        <li>驗證校內郵箱（請勿關閉本網頁）</li>
                        <li>填寫個人資料（該個人資料本網站不會保存，僅用於生產證件）</li>
                        <li>導入至數位憑證皮夾</li>
                    </ul>
                </div>
            </div>

            <div class="bg-gray-50 p-6 border-t border-gray-200 flex justify-between items-center">
                <div class="text-gray-500">
                    <p class="text-xs text-slate-500 ">© 版權所有
                        <a href="https://xiaozhi.moe" target="_blank" class="underline text-primary">Mengxiaozhi</a>
                        ｜聯絡：<a class="underline text-primary" href="mailto:me@xiaozhi.moe">me@xiaozhi.moe</a>
                    </p>
                </div>
                <div class="flex space-x-4 text-sm">
                    <a href="#" class="text-gray-400 hover:text-gray-600">
                        <span class="sr-only">Terms</span>
                        <router-link class="underline blue-500" to="terms" target="_blank">使用條款</router-link>
                    </a>
                    <a href="#" class="text-gray-400 hover:text-gray-600">
                        <span class="sr-only">Privacy</span>
                        <router-link class="underline" to="privacy" target="_blank">隱私政策</router-link>
                    </a>
                </div>
            </div>
        </div>
    </main>
</template>