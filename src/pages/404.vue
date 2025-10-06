<template>
    <div class="info-page min-h-screen bg-slate-50">
        <section
            class="relative overflow-hidden bg-gradient-to-br from-white via-[#f3f8fc] to-[#e6f0f8] border-b border-slate-200/60 pb-20">
            <div class="hero-intro py-12">
                <div class="space-y-5 text-center">
                    <span class="hero-badge mx-auto">
                        404｜找不到頁面
                    </span>
                    <div class="space-y-3">
                        <h1 class="text-3xl md:text-4xl font-bold text-slate-900 leading-tight">
                            抱歉，我們暫時找不到這個連結
                        </h1>
                        <p class="text-slate-600 text-base md:text-lg leading-relaxed max-w-2xl mx-auto">
                            可能是網址輸入錯誤，或是資源已被移除。您可以回到首頁或探索其他功能，繼續體驗 DID 校園專案。
                        </p>
                    </div>
                    <div class="hero-actions justify-center">
                        <router-link to="/" class="btn btn-primary">回到首頁</router-link>
                        <router-link to="/broad" class="btn btn-outline">前往校園留言板</router-link>
                    </div>
                </div>
            </div>

            <div class="pointer-events-none absolute inset-0">
                <div class="absolute -top-24 -right-16 h-72 w-72 rounded-full bg-primary/10 blur-3xl"></div>
                <div class="absolute bottom-12 left-10 h-48 w-48 rounded-full bg-secondary/10 blur-2xl"></div>
            </div>
        </section>
    </div>
</template>
