<template>
    <!-- 臭傻逼 -->
    <div v-if="!announcementClosed">
        <div
            class="bg-gradient-to-r from-blue-500 via-indigo-500 to-purple-500 text-white py-2 overflow-hidden relative flex justify-between">
            <div class="flex items-center space-x-2 px-6">
                <svg class="h-8 w-8 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"
                    stroke-linecap="round" stroke-linejoin="round">
                    <path d="M13 16h-1v-4h-1m1-4h.01M12 20a8 8 0 100-16 8 8 0 000 16z" />
                </svg>
            </div>
            <div class="flex items-center space-x-2">
                <span>這是技術演示，不是官方證件，僅供學術交流及參考使用，也不會收集Email外的任何個人資料，謝謝！</span>
            </div>
            <button @click="announcementClosed = true" class="text-white">
                <svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"
                    stroke-linecap="round" stroke-linejoin="round">
                    <path d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    const announcementClosed = ref(false)
</script>