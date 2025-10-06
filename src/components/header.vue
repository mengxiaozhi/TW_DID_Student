<template>
    <header class="glass-nav">
        <div class="max-w-6xl mx-auto px-4 md:px-6">
            <div class="flex items-center justify-between gap-4 py-5">
                <router-link class="flex items-center gap-3 group" to="/">
                    <span
                        class="inline-flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br text-white shadow-md">
                        <img src="/logo.png" alt="logo" class="h-8 w-8 object-contain" />
                    </span>
                    <span class="flex flex-col">
                        <span class="text-sm text-secondary font-semibold tracking-wide">Taiwan DID</span>
                        <span
                            class="text-lg md:text-xl font-bold text-slate-900 group-hover:text-primary transition-colors">數位學生證</span>
                    </span>
                </router-link>

                <nav class="hidden md:flex items-center gap-6 text-sm font-medium text-slate-600">
                    <router-link to="/" class="hover:text-primary transition">首頁</router-link>
                    <router-link to="/broad" class="hover:text-primary transition">匿名留言板</router-link>
                    <router-link to="/vote" class="hover:text-primary transition">校園投票</router-link>
                    <router-link to="/about" class="hover:text-primary transition">關於專案</router-link>
                </nav>

                <div class="flex items-center gap-3">
                    <a href="https://github.com/mengxiaozhi/TW_DID_Student" target="_blank" rel="noopener noreferrer"
                        class="hidden md:inline-flex items-center gap-2 text-sm font-semibold text-slate-600 hover:text-primary transition">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24">
                            <path
                                d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                        </svg>
                        GitHub
                    </a>
                    <a href="https://youtu.be/9Jn47KhUwtc" target="_blank" rel="noopener noreferrer"
                        class="hidden md:inline-flex items-center gap-2 text-sm font-semibold text-slate-600 hover:text-primary transition">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24">
                            <path
                                d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z" />
                        </svg>
                        觀看影片
                    </a>
                    <router-link to="/" class="btn btn-primary hidden md:inline-flex">立即開始</router-link>
                </div>
            </div>

            <div class="md:hidden flex items-center gap-3 pb-4 overflow-x-auto text-sm font-medium text-slate-600">
                <router-link to="/"
                    class="px-3 py-1.5 rounded-full border border-slate-200 bg-white shadow-sm">首頁</router-link>
                <router-link to="/broad"
                    class="px-3 py-1.5 rounded-full border border-transparent bg-slate-100">匿名留言板</router-link>
                <router-link to="/vote"
                    class="px-3 py-1.5 rounded-full border border-transparent bg-slate-100">校園投票</router-link>
                <router-link to="/about"
                    class="px-3 py-1.5 rounded-full border border-transparent bg-slate-100">關於</router-link>
            </div>
        </div>
    </header>
</template>
