<template>
    <main class="py-8 px-4 md:px-8 bg-slate-50 min-h-screen">
        <div class="max-w-3xl mx-auto bg-white shadow-lg rounded-xl p-8 border border-slate-200">
            <div class="text-center mb-6">
                <h1 class="text-2xl font-bold text-secondary">隱私政策</h1>
                <p class="text-sm text-slate-500 mt-1">最後更新日期：2025 年 4 月 8 日</p>
                <p class="text-sm text-slate-500">本文件針對平台：<code
                        class="font-mono text-primary">did-edu.xiaozhi.moe</code></p>
            </div>

            <section class="text-slate-700 text-[15px] leading-relaxed space-y-8">
                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">一、資料控管者（Data Controller）</h2>
                    <p>本平台由個人開發者 Mengxiaozhi（以下稱「我們」）運營。</p>
                    <ul class="list-disc list-inside mt-2 space-y-1">
                        <li>Email：me@xiaozhi.moe</li>
                        <li>聯絡請以電子郵件為主</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">二、資料蒐集項目與用途</h2>

                    <h3 class="text-base font-medium mt-4 mb-2">📌 憑證生成功能</h3>
                    <div class="overflow-x-auto">
                        <table class="table-auto w-full text-sm border border-slate-300 rounded-lg overflow-hidden">
                            <thead class="bg-slate-100 text-slate-700 font-semibold">
                                <tr>
                                    <th class="border px-3 py-2">資料項目</th>
                                    <th class="border px-3 py-2">蒐集方式</th>
                                    <th class="border px-3 py-2">使用目的</th>
                                </tr>
                            </thead>
                            <tbody class="text-slate-700">
                                <tr>
                                    <td class="border px-3 py-2">Email 信箱</td>
                                    <td class="border px-3 py-2">使用者主動輸入</td>
                                    <td class="border px-3 py-2">用於驗證學術身份、自動辨識學校名稱，生成憑證後由本網站紀錄留存。</td>
                                </tr>
                                <tr>
                                    <td class="border px-3 py-2">學生學號</td>
                                    <td class="border px-3 py-2">系統自動匹配 Email 信箱取得</td>
                                    <td class="border px-3 py-2">生成憑證後由個人數位皮夾託管。</td>
                                </tr>
                                <tr>
                                    <td class="border px-3 py-2">學生姓名</td>
                                    <td class="border px-3 py-2">使用者主動輸入</td>
                                    <td class="border px-3 py-2">展示於憑證頁面，供個人識別之用。</td>
                                </tr>
                                <tr>
                                    <td class="border px-3 py-2">學生學校</td>
                                    <td class="border px-3 py-2">主動輸入或系統匹配</td>
                                    <td class="border px-3 py-2">展示於憑證頁面，供個人識別之用。</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <h3 class="text-base font-medium mt-6 mb-2">💬 留言板功能</h3>
                    <div class="overflow-x-auto">
                        <table class="table-auto w-full text-sm border border-slate-300 rounded-lg overflow-hidden">
                            <thead class="bg-slate-100 text-slate-700 font-semibold">
                                <tr>
                                    <th class="border px-3 py-2">資料項目</th>
                                    <th class="border px-3 py-2">蒐集方式</th>
                                    <th class="border px-3 py-2">使用目的</th>
                                </tr>
                            </thead>
                            <tbody class="text-slate-700">
                                <tr>
                                    <td class="border px-3 py-2">留言內容</td>
                                    <td class="border px-3 py-2">使用者主動輸入</td>
                                    <td class="border px-3 py-2">顯示於公開留言板。</td>
                                </tr>
                                <tr>
                                    <td class="border px-3 py-2">學校名稱</td>
                                    <td class="border px-3 py-2">通過 VC 驗證取得</td>
                                    <td class="border px-3 py-2">用於提升留言可信度。</td>
                                </tr>
                                <tr>
                                    <td class="border px-3 py-2">姓名（選填）</td>
                                    <td class="border px-3 py-2">通過 VC 實名驗證</td>
                                    <td class="border px-3 py-2">附於留言以表明身分（若使用）。</td>
                                </tr>
                                <tr>
                                    <td class="border px-3 py-2">按讚紀錄（非識別化）</td>
                                    <td class="border px-3 py-2">點擊按鈕送出</td>
                                    <td class="border px-3 py-2">用於統計與排序，不綁定身分。</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <p class="mt-4 text-sm text-slate-600"><strong>我們不會蒐集以下類型資訊：</strong>Cookies、IP、裝置資料、個人照片、住址等敏感個資。
                    </p>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">三、合法性依據（Legal Basis）</h2>
                    <ol class="list-decimal list-inside space-y-1">
                        <li>使用者明示同意（GDPR 第 6(1)(a) 條）</li>
                        <li>合法權益（第 6(1)(f) 條）以教育展示為目的</li>
                    </ol>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">四、資料儲存與保留期限</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>系統不會永久儲存任何個資，除驗證信箱外處理後即時銷毀</li>
                        <li>資料僅用於該次生成流程，不建立長期留存</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">五、資料接收對象</h2>
                    <p>我們不會向任何第三方揭露或出售使用者資料。</p>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">六、使用者權利（GDPR 第 15-21 條）</h2>
                    <ul class="list-disc list-inside space-y-1">
                        <li>查閱、更正、刪除、限制處理個人資料</li>
                        <li>請求資料攜出（提供 JSON 格式）</li>
                        <li>撤回同意（不影響過去處理合法性）</li>
                        <li>向資料保護主管機關提出申訴</li>
                    </ul>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">七、資料跨境傳輸</h2>
                    <p>本平台伺服器位於新加坡，涉及資料跨境處理。</p>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">八、兒童個資聲明</h2>
                    <p>若您未滿 16 歲，請在監護人或教師協助下使用本系統。</p>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">九、政策變更</h2>
                    <p>本政策如有更新，將於本頁公布最新版本，請定期查閱。</p>
                </div>

                <div>
                    <h2 class="text-lg font-semibold text-primary mb-2">十、聯絡我們</h2>
                    <p>如有任何資料相關問題，請透過以下方式聯繫：</p>
                    <ul class="list-disc list-inside mt-1">
                        <li>Email：<a href="mailto:me@xiaozhi.moe"
                                class="text-primary underline hover:opacity-80">me@xiaozhi.moe</a></li>
                    </ul>
                </div>
            </section>
        </div>
    </main>
</template>