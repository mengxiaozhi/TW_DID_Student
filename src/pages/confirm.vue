<script>
    import { onMounted, ref } from 'vue'
    import { useRoute } from 'vue-router'

    export default {
        setup() {
            const route = useRoute();
            const token = route.query.token;

            const confirm_messages = ref(" ");

            // 驗證Token
            const confirm_token = async () => {
                try {
                    const response = await fetch(`https://api.xiaozhi.moe/chihlee/confirm-email?token=${token}`)
                    const data = await response.json()
                    confirm_messages.value = data.message || data.error;
                } catch (error) {
                    console.error('確認訂閱失敗:', error)
                    confirm_messages.value = '伺服器錯誤，無法確認訂閱';
                }
            }

            onMounted(() => {
                confirm_token()
            })

            return {
                confirm_messages
            }
        }
    }
</script>
<template>
    <main class="pt-3">
        <div
            class="max-w-2xl mx-auto bg-white shadow-lg rounded-xl p-8 border border-slate-200 transition-all duration-300 hover:shadow-xl\">
            <div class="flex items-center justify-center mb-6">
                <h1 class="text-2xl font-semibold text-slate-700">{{ confirm_messages }}</h1>
            </div>
        </div>
    </main>
</template>