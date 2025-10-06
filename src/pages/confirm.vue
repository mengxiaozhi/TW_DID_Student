<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const message = ref('驗證處理中...')
const isError = ref(false)

const confirmToken = async () => {
    const token = route.query.token

    if (!token || typeof token !== 'string') {
        message.value = '缺少驗證資訊，請回到原頁面重新操作。'
        isError.value = true
        return
    }

    try {
        const response = await fetch(`https://api.xiaozhi.moe/chihlee/confirm-email?token=${token}`)
        const data = await response.json()

        if (response.ok) {
            message.value = data.message || '郵件驗證成功，請回到原頁面繼續申請。'
        } else {
            message.value = data.error || '驗證失敗，請重新申請或聯絡我們。'
            isError.value = true
        }
    } catch (error) {
        console.error('確認郵件失敗:', error)
        message.value = '伺服器連線異常，請稍後再試。'
        isError.value = true
    }
}

const goHome = () => router.push('/')

onMounted(confirmToken)
</script>

<template>
    <div class="info-page min-h-screen bg-slate-50">
        <section
            class="relative overflow-hidden bg-gradient-to-br from-white via-[#f3f8fc] to-[#e6f0f8] border-b border-slate-200/60 pb-20">
            <div class="hero-intro py-12">
                <div class="space-y-5 text-center">
                    <span class="hero-badge mx-auto">
                        郵件驗證回傳
                    </span>
                    <div class="mx-auto max-w-2xl space-y-3">
                        <h1 class="text-3xl md:text-4xl font-bold text-slate-900 leading-tight">
                            {{ message }}
                        </h1>
                        <p v-if="!isError" class="text-slate-600 text-base md:text-lg leading-relaxed">
                            系統已記錄您的驗證結果，您可以關閉本頁面或回到原本的生成流程繼續完成學生證申請。
                        </p>
                        <p v-else class="text-slate-600 text-base md:text-lg leading-relaxed">
                            若持續遇到問題，請重新發送驗證信或來信 <a href="mailto:me@xiaozhi.moe"
                                class="text-primary underline">me@xiaozhi.moe</a> 協助排查。
                        </p>
                    </div>
                    <div class="hero-actions justify-center">
                        <button class="btn btn-primary" @click="goHome">回到首頁</button>
                        <router-link to="/broad" class="btn btn-outline">探索留言板</router-link>
                    </div>
                </div>
            </div>

            <div class="pointer-events-none absolute inset-0">
                <div class="absolute -top-24 -right-14 h-64 w-64 rounded-full bg-primary/10 blur-3xl"></div>
                <div class="absolute bottom-10 left-12 h-48 w-48 rounded-full bg-secondary/10 blur-2xl"></div>
            </div>
        </section>
    </div>
</template>
