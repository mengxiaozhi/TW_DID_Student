<script setup>
    import headerVue from './components/header.vue'
    import { ref, onMounted } from 'vue'
    import { useRoute, RouterView } from 'vue-router'
    import Cookies from 'js-cookie'

    const route = useRoute()
    const closeDisclaimer = ref(false)

    onMounted(() => {
        // 讀取 cookie 是否已同意
        const agreed = Cookies.get('disclaimer_accepted')
        if (!agreed) {
            closeDisclaimer.value = false
        } else {
            closeDisclaimer.value = true
        }
    })

    const acceptDisclaimer = () => {
        Cookies.set('disclaimer_accepted', 'true', { expires: 365 }) // 一年內不再提醒
        closeDisclaimer.value = true
    }
</script>


<template>
    <div class="app-shell">
        <headerVue />
        <!--<banner />-->
        <RouterView v-slot="{ Component, route: viewRoute }">
            <Transition name="route-fade" mode="out-in">
                <component :is="Component" :key="viewRoute.fullPath" class="route-view" />
            </Transition>
        </RouterView>
    </div>
    <Transition name="backdrop-fade">
        <div v-if="!closeDisclaimer && route.path !== '/terms' && route.path !== '/privacy' && route.path !== '/confirm'"
            class="fixed inset-0 z-[9999] bg-black/50 flex items-center justify-center p-4">
            <div class="bg-white p-6 rounded-xl max-w-lg w-full max-h-[90vh] overflow-y-auto shadow-xl">
                <h2 class="text-xl font-semibold mb-4">用戶須知與免責聲明</h2>
                <p class="mb-3">
                    本平台「數位學生證」為學生自主開發之技術展示專案，目的在於探索分散式身份識別技術（DID）於教育領域的應用，並無任何學校或教育機構之官方授權或背書。
                </p>
                <ul class="list-disc pl-6 space-y-1 text-sm text-slate-700">
                    <li>本系統所顯示之學校名稱係根據您提供之學術信箱網域自動推論，僅供技術驗證與識別用途。</li>
                    <li>不連接任何學校資料庫或登入機制。</li>
                    <li>數位學生證為模擬用途，不具法律效力。</li>
                    <li>平台僅使用必要資訊進行即時驗證，不做其他用途。</li>
                    <li>所有內容由使用者提供，平台不負責其真實性。</li>
                </ul>
                <p class="text-sm mt-4">
                    教育機構如需合作或下架請聯繫：
                    <a href="mailto:me@xiaozhi.moe" class="text-primary underline">me@xiaozhi.moe</a>
                </p>
                <p class="text-sm mt-2">
                    詳情請參閱
                    <router-link to="/terms" class="underline text-primary" target="_blank">使用條款</router-link> 與
                    <router-link to="/privacy" class="underline text-primary" target="_blank">隱私政策</router-link>
                </p>
                <div class="text-right mt-6">
                    <button @click="acceptDisclaimer"
                        class="bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary/90 transition">
                        我已閱讀並同意
                    </button>
                </div>
            </div>
        </div>
    </Transition>

</template>
