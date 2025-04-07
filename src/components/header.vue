<template>
    <!-- Enhanced Header -->
    <header class="w-full bg-white shadow-sm py-7 px-4 md:px-8 border-b border-slate-200">
        <div class="max-w-5xl mx-auto flex flex-col md:flex-row md:justify-between items-center space-y-3 md:space-y-0">
            <!-- Logo and Title -->
            <router-link class="text-lg md:text-xl font-bold text-slate-800 text-center flex items-center gap-2 group" to="/">
                <img src="/logo.png" alt="logo" class="h-7 w-7 object-contain" />
                <span class="group-hover:text-blue-600 transition-colors">數位憑證皮夾｜學生證</span>
            </router-link>

            <!-- Navigation -->
            <nav class="flex flex-wrap justify-center md:justify-end gap-4 md:gap-6 text-sm">
                <a href="https://github.com/mengxiaozhi/TW_DID_Student" target="_blank" rel="noopener noreferrer"
                    class="text-slate-600 hover:text-blue-600 transition flex items-center font-medium">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="currentColor"
                        viewBox="0 0 24 24">
                        <path
                            d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
                    </svg>
                    GitHub
                </a>
                <a href="https://youtu.be/9Jn47KhUwtc" target="_blank" rel="noopener noreferrer"
                    class="text-slate-600 hover:text-blue-600 transition flex items-center font-medium">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="currentColor"
                        viewBox="0 0 24 24">
                        <path
                            d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z" />
                    </svg>
                    演示影片
                </a>
                <router-link to="/about"
                    class="text-slate-600 hover:text-blue-600 transition flex items-center font-medium">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    關於
                </router-link>
            </nav>
        </div>
    </header>
</template>