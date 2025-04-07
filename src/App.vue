<script setup>
    import headerVue from './components/header.vue'
    import banner from './components/banner.vue';
    import { useRouter } from 'vue-router'
    import { ref } from 'vue';

    const closeDisclaimer = ref(false)
</script>

<template>
    <headerVue />
    <banner />
    <router-view></router-view>
    <!-- 隱私聲明 Modal -->
    <div v-if="!closeDisclaimer" id="disclaimer-modal"
        style="position:fixed;top:0;left:0;width:100%;height:100%;background-color:rgba(0,0,0,0.5);z-index:9999;display:flex;align-items:center;justify-content:center;padding:1rem;box-sizing:border-box;">
        <div
            style="background:#fff;padding:1.5rem;border-radius:0.5rem;width:100%;max-width:600px;max-height:90vh;box-shadow:0 4px 10px rgba(0,0,0,0.3);overflow-y:auto;">
            <h2 style="margin-top:0;">用戶須知與免責聲明</h2>
            <p>本平台「數位學生證」為學生自主開發之技術展示專案，目的在於探索分散式身份識別技術（DID）於教育領域的應用，並無任何學校或教育機構之官方授權或背書。</p>
            <ul style="padding-left: 1.2em;">
                <li>本系統所顯示之學校名稱係根據您提供之學術信箱網域自動推論，僅供技術驗證與識別用途，不具備任何法律效力。</li>
                <li>本系統未與任何學校資料庫或資訊系統連接，亦不模擬或破解任何學校登入機制。</li>
                <li>所產生之數位學生證為模擬性質，僅用於展示憑證技術格式與樣式，不得作為正式學生證使用。</li>
                <li>本平台不蒐集、處理或儲存除信箱驗證必要資訊外的個人資料，所有資料僅用於即時驗證與憑證產生，不另作他用。</li>
                <li>本平台所生成的學校名稱、憑證資訊，均為使用者自行提供，若造成任何誤解、冒用或第三方損害，本平台概不負責。</li>
            </ul>
            <p>若您為教育機構代表，有合作意願或欲提出下架通知，請聯繫本站開發者：<a href="mailto:me@xiaozhi.moe">me@xiaozhi.moe</a></p>

            <p style="font-size: 0.9em; margin-top:1.5em;">
                詳情請參閱
                <router-link class="underline blue-500" to="terms" target="_blank">使用條款</router-link>
                與
                <router-link class="underline" to="privacy" target="_blank">隱私政策</router-link>
            </p>

            <div style="text-align:right; margin-top:1.5em;">
                <button @click="closeDisclaimer = true"
                    style="padding:0.6em 1.2em;font-size:1em;background:#3182ce;color:white;border:none;border-radius:4px;cursor:pointer;">我已閱讀並同意</button>
            </div>
        </div>
    </div>

</template>