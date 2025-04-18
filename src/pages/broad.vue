<template>
    <div class="min-h-screen p-3 sm:p-4 md:p-6">
        <div class="max-w-4xl mx-auto">
            <!-- 頁面標題 -->
            <div class="bg-white shadow-md rounded-lg sm:rounded-xl p-3 sm:p-4 mb-4">
                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2">
                    <h2 class="text-base sm:text-lg font-bold text-secondary flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                        </svg>
                        匿名留言板
                    </h2>
                    <div class="flex items-center gap-2 flex-wrap">
                        <!--
                        <span v-if="verifiedSchool"
                            class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full flex items-center gap-1">
                            <span class="h-2 w-2 bg-green-500 rounded-full"></span>
                            已驗證 - {{ verifiedSchool }}
                        </span>
                        <span v-if="verifiedName"
                            class="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full flex items-center gap-1">
                            實名 - {{ verifiedName }}
                        </span>
                        -->
                        <button @click="showMobileSearch = true"
                            class="sm:hidden text-primary border border-primary/30 rounded-full px-3 py-1 text-sm hover:bg-indigo-50 transition flex items-center gap-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                            搜尋
                        </button>
                        <button @click="fetchMessages"
                            class="bg-white text-primary border border-primary/30 rounded-full px-3 py-1 text-sm hover:bg-indigo-50 transition flex items-center gap-1">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M4 4v6h6M20 20v-6h-6" />
                            </svg>
                            重新載入留言
                        </button>
                        <button v-if="verifiedSchool" @click="logout"
                            class="bg-primary text-white rounded-full px-3 py-1 text-sm hover:bg-primary/90 transition flex items-center gap-1">
                            登出
                        </button>
                    </div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-4">
                <!-- 發佈留言區 -->
                <div class="w-full sm:w-[60%] bg-white shadow-md rounded-lg sm:rounded-xl p-3 sm:p-4 mb-6">
                    <!-- 未驗證狀態 -->
                    <div v-if="!verifiedSchool"
                        class="flex flex-col sm:flex-row items-center justify-between gap-3 p-4 bg-slate-50 rounded-xl mb-4 border border-slate-100">
                        <div class="flex items-center gap-3">
                            <div class="bg-amber-100 p-2 rounded-full">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-amber-500" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                </svg>
                            </div>
                            <p class="text-sm text-slate-700 font-medium">請先驗證學校身份以發佈留言</p>
                        </div>
                        <button @click="showVerificationModal = true"
                            class="bg-gradient-to-r from-primary to-primary/90 text-white rounded-full px-4 py-2 text-sm hover:shadow-md hover:from-primary/90 hover:to-primary transition flex items-center gap-2 font-medium">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                            </svg>
                            立即驗證
                        </button>
                    </div>

                    <!-- 已驗證狀態 -->
                    <div v-if="verifiedSchool"
                        class="flex flex-wrap items-center gap-3 p-4 bg-gradient-to-r from-slate-50 to-indigo-50/30 rounded-xl mb-4 border border-slate-100">
                        <div class="flex items-center gap-2">
                            <span v-if="verifiedSchool"
                                class="bg-gradient-to-r from-green-100 to-green-50 text-green-700 text-xs px-3 py-1.5 rounded-full flex items-center gap-2 font-medium shadow-sm">
                                <span class="h-2 w-2 bg-green-500 rounded-full animate-pulse"></span>
                                已驗證 - {{ verifiedSchool }}
                            </span>
                            <span v-if="verifiedName"
                                class="bg-gradient-to-r from-blue-100 to-blue-50 text-blue-700 text-xs px-3 py-1.5 rounded-full flex items-center gap-2 font-medium shadow-sm">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                </svg>
                                實名 - {{ verifiedName }}
                            </span>
                        </div>
                    </div>

                    <!-- 留言表單 -->
                    <form @submit.prevent="submitMessage" class="relative">
                        <div
                            class="w-full rounded-xl border border-slate-200 shadow-sm hover:shadow transition-all overflow-hidden">
                            <textarea v-model="newMessage" rows="4"
                                class="w-full rounded-t-xl p-4 focus:outline-none text-sm resize-none max-h-60 overflow-auto"
                                placeholder="分享你的想法..." :disabled="!verifiedSchool"></textarea>

                            <div
                                class="bg-gradient-to-r from-slate-50 to-indigo-50/30 px-4 py-3 rounded-b-xl flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
                                <div class="text-xs text-slate-600">
                                    <div v-if="verifiedSchool" class="flex items-center gap-3 flex-wrap">
                                        <span v-if="!verifiedName || !useRealName" class="flex items-center gap-1.5">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-400"
                                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                            </svg>
                                            <span class="font-medium">{{ verifiedSchool }} | 匿名發布</span>
                                        </span>
                                        <span v-else class="flex items-center gap-1.5 text-primary">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                                viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                            </svg>
                                            <span class="font-medium">{{ verifiedName }}｜{{ verifiedSchool }} |
                                                實名發布</span>
                                        </span>
                                        <label v-if="verifiedName"
                                            class="flex items-center gap-1.5 cursor-pointer bg-slate-100 hover:bg-slate-200 px-2.5 py-1 rounded-full transition">
                                            <input type="checkbox" v-model="useRealName"
                                                class="rounded text-primary focus:ring-indigo-500 h-3.5 w-3.5" />
                                            <span class="text-xs text-slate-700 font-medium">使用實名</span>
                                        </label>
                                    </div>
                                    <span v-else class="flex items-center gap-1.5 text-slate-500">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                        驗證後即可發佈
                                    </span>
                                </div>

                                <button type="submit" :disabled="submitting || !newMessage.trim() || !verifiedSchool"
                                    class="bg-gradient-to-r from-primary to-primary/90 text-white rounded-full px-5 py-2 text-sm hover:shadow-md disabled:opacity-50 disabled:hover:shadow-none flex items-center gap-2 transition min-h-[44px] font-medium">
                                    <span v-if="submitting" class="flex items-center gap-2">
                                        <svg class="animate-spin h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg"
                                            fill="none" viewBox="0 0 24 24">
                                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor"
                                                stroke-width="4"></circle>
                                            <path class="opacity-75" fill="currentColor"
                                                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                                            </path>
                                        </svg>
                                        發送中...
                                    </span>
                                    <span v-else-if="!verifiedSchool"
                                        @click.prevent="showVerificationModal = true">需要驗證</span>
                                    <span v-else>發佈留言</span>
                                    <svg v-if="!submitting && verifiedSchool" xmlns="http://www.w3.org/2000/svg"
                                        class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                                    </svg>
                                </button>
                            </div>
                        </div>

                        <!-- 動畫效果：未驗證狀態下，在表單上方顯示半透明遮罩 -->
                        <div v-if="!verifiedSchool"
                            class="absolute inset-0 bg-white/60 backdrop-blur-[1px] rounded-xl flex items-center justify-center cursor-not-allowed"
                            @click="showVerificationModal = true">
                            <div
                                class="bg-white/80 backdrop-blur-sm px-4 py-3 rounded-xl shadow-lg flex items-center gap-2 text-sm text-slate-700">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                </svg>
                                點擊以驗證身份
                            </div>
                        </div>
                    </form>
                </div>

                <!-- 手機版搜尋浮層 -->
                <div v-if="showMobileSearch"
                    class="fixed inset-0  bg-black/40 backdrop-blur-sm z-50 flex justify-center items-center p-4 sm:hidden">
                    <div class="bg-white w-full max-w-md rounded-lg shadow-xl p-4 relative">
                        <button @click="showMobileSearch = false"
                            class="absolute top-2 right-2 text-slate-400 hover:text-slate-600">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>

                        <h3 class="text-base font-semibold text-secondary mb-3">搜尋</h3>

                        <div class="flex items-center gap-2 mb-2">
                            <div class="relative flex-1">
                                <input v-model="searchTerm" placeholder="搜尋" class="w-full rounded-md border border-slate-300 py-2 pr-3 pl-9
            focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50
            text-sm placeholder-slate-400 transition-all" />
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-400" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                                    </svg>
                                </div>
                            </div>

                            <button @click="fetchMessages"
                                class="bg-primary text-white px-3 py-2 rounded-md text-sm hover:bg-primary/90 flex items-center gap-1 transition">
                                搜尋
                            </button>
                        </div>

                        <button v-if="searchTerm" @click="clearSearch" class="text-sm text-primary underline">
                            清除
                        </button>

                        <div class="mb-4">
                            <label for="sortSelect" class="block text-sm font-medium text-slate-700 mb-2">
                                排序方式
                            </label>
                            <div class="relative">
                                <select id="sortSelect" v-model="sortBy" @change="onSortChange" class="block w-full appearance-none border border-slate-300 rounded-md py-2 px-3 pr-8
             text-sm focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all
             bg-white text-slate-700">
                                    <option value="time_desc">最新優先</option>
                                    <option value="time_asc">最舊優先</option>
                                    <option value="likes_desc">讚數由高到低</option>
                                    <option value="likes_asc">讚數由低到高</option>
                                </select>

                                <!-- 下拉箭頭圖示 -->
                                <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                                    <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor"
                                        viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M19 9l-7 7-7-7" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 右側搜尋區塊 (40%) -->
                <div class="hidden sm:block w-full sm:w-[40%] bg-white shadow-md rounded-lg sm:rounded-xl p-4 mb-6">
                    <h3 class="text-base font-semibold text-secondary mb-3">搜尋</h3>

                    <!-- 輸入框 + 搜尋按鈕 -->
                    <div class="flex items-center gap-2 mb-2">
                        <div class="relative flex-1">
                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-400" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                                </svg>
                            </div>
                            <input v-model="searchTerm" placeholder="搜尋" class="w-full rounded-md border border-slate-300 py-2 pr-3 pl-9
               focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50
               text-sm placeholder-slate-400 transition-all" />
                        </div>

                        <button @click="fetchMessages" class="bg-primary text-white px-3 py-2 rounded-md text-sm
             hover:bg-primary/90 flex items-center gap-1 transition">
                            搜尋
                        </button>
                    </div>
                    <!-- 清除按鈕：只有在有輸入內容時才顯示 -->
                    <button v-if="searchTerm" @click="clearSearch" class="text-sm text-primary underline mb-3">
                        清除
                    </button>
                    <br>
                    <div class="mb-4">
                        <label for="sortSelect" class="block text-sm font-medium text-slate-700 mb-2">
                            排序方式
                        </label>
                        <div class="relative">
                            <select id="sortSelect" v-model="sortBy" @change="onSortChange" class="block w-full appearance-none border border-slate-300 rounded-md py-2 px-3 pr-8
             text-sm focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50 transition-all
             bg-white text-slate-700">
                                <option value="time_desc">最新優先</option>
                                <option value="time_asc">最舊優先</option>
                                <option value="likes_desc">讚數由高到低</option>
                                <option value="likes_asc">讚數由低到高</option>
                            </select>

                            <!-- 下拉箭頭圖示 -->
                            <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                                <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M19 9l-7 7-7-7" />
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <!-- 留言瀑布流 -->
            <div class="mt-8">
                <!-- 載入中狀態 -->
                <div v-if="loading" class="flex justify-center items-center py-16">
                    <div class="animate-spin rounded-full h-10 w-10 border-b-2 border-primary"></div>
                </div>

                <!-- 無留言狀態 -->
                <div v-else-if="messages.length === 0"
                    class="text-center bg-white rounded-2xl shadow-lg p-12 transition">
                    <div class="bg-slate-50 p-6 rounded-full w-24 h-24 mx-auto mb-4 flex items-center justify-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-slate-300" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                        </svg>
                    </div>
                    <h3 class="text-slate-700 font-medium text-lg mb-2">尚無留言</h3>
                    <p class="text-slate-500">成為第一個發言的人，分享你的想法！</p>
                </div>

                <!-- 留言瀑布流 -->
                <div v-else class="columns-1 sm:columns-2 gap-6">
                    <div v-for="msg in messages" :key="msg.id" @click="(e) => onMessageCardClick(e, msg)"
                        class="bg-white rounded-xl shadow-md hover:shadow-xl p-5 transition duration-300 transform hover:translate-y-[-4px] cursor-pointer mb-6 break-inside-avoid">
                        <!-- 用戶資訊區 -->
                        <div class="flex items-start gap-3">
                            <div v-if="msg.author_name"
                                class="h-10 w-10 rounded-full bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center flex-shrink-0 shadow-sm">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                </svg>
                            </div>
                            <div v-else
                                class="h-10 w-10 rounded-full bg-gradient-to-br from-slate-100 to-slate-200 flex items-center justify-center flex-shrink-0 shadow-sm">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                </svg>
                            </div>
                            <div class="flex-1">
                                <div class="flex justify-between items-start">
                                    <div class="flex flex-wrap items-center gap-2">
                                        <span v-if="msg.author_name"
                                            class="text-sm font-medium text-secondary flex items-center gap-1">
                                            {{ msg.author_name }}
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 text-primary"
                                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                            </svg>
                                        </span>
                                        <span v-else class="text-sm font-medium text-slate-600">匿名用戶</span>
                                        <span
                                            class="bg-primary/10 text-secondary text-xs px-2.5 py-0.5 rounded-full font-medium">
                                            {{ msg.school }}
                                        </span>
                                    </div>
                                    <span class="text-xs text-slate-400">{{ formatTime(msg.created_at) }}</span>
                                </div>

                                <!-- 留言內容 -->
                                <p class="mt-3 text-slate-700 whitespace-pre-wrap break-words leading-relaxed"
                                    v-html="parseContent(msg.content)" @click="onContentClick($event)"></p>

                                <!-- 互動按鈕 -->
                                <div class="mt-4 flex justify-between">
                                    <div class="flex gap-5 text-xs text-slate-500">
                                        <button @click="handleLike(msg)"
                                            class="flex items-center gap-1.5 hover:text-primary transition group">
                                            <div
                                                class="p-1.5 rounded-full bg-slate-50 group-hover:bg-primary/10 transition">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                                    viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                                                </svg>
                                            </div>
                                            <span class="hidden md:block">讚同</span>
                                            <span class="text-secondary font-medium">({{ msg.likes || 0 }})</span>
                                        </button>
                                        <button
                                            @click="verifiedSchool ? (msg.showReplyBox = !msg.showReplyBox) : showVerificationModal = true"
                                            class="flex items-center gap-1.5 hover:text-primary transition group">
                                            <div
                                                class="p-1.5 rounded-full bg-slate-50 group-hover:bg-primary/10 transition">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                                    viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                                                </svg>
                                            </div>
                                            <span class="hidden md:block">回覆</span>
                                        </button>
                                        <button @click="shareMessage(msg.id)"
                                            class="flex items-center gap-1.5 hover:text-primary transition group">
                                            <div
                                                class="p-1.5 rounded-full bg-slate-50 group-hover:bg-primary/10 transition">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                                    viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
                                                </svg>
                                            </div>
                                            <span class="hidden md:block">分享</span>
                                        </button>
                                    </div>
                                </div>

                                <!-- 回覆輸入框 -->
                                <div v-if="msg.showReplyBox" class="mt-4 space-y-2">
                                    <textarea v-model="msg.replyContent" rows="2"
                                        class="w-full p-3 border border-slate-200 rounded-lg text-sm focus:ring-2 focus:ring-primary/30 focus:border-primary outline-none transition"
                                        placeholder="輸入回覆內容..."></textarea>
                                    <button @click="submitReply(msg)"
                                        class="text-sm bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary/90 transition shadow-sm">
                                        發佈回覆
                                    </button>
                                </div>

                                <!-- 回覆列表 -->
                                <div v-if="msg.replies && msg.replies.length"
                                    class="mt-4 pl-4 border-l-2 border-slate-200 space-y-3 text-sm">
                                    <div v-for="(r, index) in msg.replies.slice(0, 3)" :key="r.id"
                                        class="hover:bg-slate-50 rounded-lg p-2 -ml-2">
                                        <div class="text-slate-700 font-medium">
                                            {{ r.author_name || '匿名用戶｜' + r.school }}
                                        </div>
                                        <div class="text-slate-600 mt-1">{{ r.content }}</div>
                                        <div class="text-xs text-slate-400 mt-1">{{ formatTime(r.created_at) }}</div>
                                    </div>
                                    <button v-if="msg.replies.length > 3" @click.stop="openPreview(msg)"
                                        class="text-xs text-primary hover:underline flex items-center gap-1">
                                        <span>查看全部 {{ msg.replies.length }} 則回覆</span>
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M9 5l7 7-7 7" />
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 預覽留言 Modal -->
                <div v-if="showPreviewModal"
                    class="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 flex items-center justify-center p-4 overflow-y-auto">
                    <div
                        class="bg-white max-w-3xl w-full rounded-2xl shadow-xl p-6 relative animate-fadeIn max-h-[90vh] overflow-y-auto">
                        <button @click="closePreview"
                            class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 p-2 rounded-full hover:bg-slate-100 transition">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>

                        <!-- 頭像與名稱 -->
                        <div class="flex items-start gap-4 mb-6">
                            <div v-if="previewMessage?.author_name"
                                class="h-12 w-12 rounded-full bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center shadow-sm">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                </svg>
                            </div>
                            <div v-else
                                class="h-12 w-12 rounded-full bg-gradient-to-br from-slate-100 to-slate-200 flex items-center justify-center shadow-sm">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-slate-400" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                </svg>
                            </div>
                            <div>
                                <div class="flex items-center gap-2">
                                    <div class="text-base font-semibold text-slate-800">
                                        {{ previewMessage?.author_name || '匿名用戶' }}
                                    </div>
                                    <span
                                        class="bg-primary/10 text-secondary text-xs px-2.5 py-0.5 rounded-full font-medium">
                                        {{ previewMessage?.school || '' }}
                                    </span>
                                </div>
                                <div class="text-xs text-slate-400 mt-1">{{ formatTime(previewMessage?.created_at) }}
                                </div>
                            </div>
                        </div>

                        <!-- 內容 -->
                        <div class="text-slate-800 whitespace-pre-line leading-relaxed break-words text-base mb-6 bg-slate-50 p-4 rounded-xl"
                            v-html="parseContent(previewMessage?.content)" @click="onContentClick($event)">
                        </div>

                        <!-- 功能列 -->
                        <div class="flex gap-6 text-sm text-slate-500 mb-6 border-b border-slate-100 pb-6">
                            <button @click="handleLike(previewMessage)"
                                class="flex items-center gap-2 hover:text-primary transition group">
                                <div class="p-2 rounded-full bg-slate-50 group-hover:bg-primary/10 transition">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                                    </svg>
                                </div>
                                讚同
                                <span class="text-secondary font-medium">({{ previewMessage.likes || 0 }})</span>
                            </button>
                            <button @click="shareMessage(previewMessage.id)"
                                class="flex items-center gap-2 hover:text-primary transition group">
                                <div class="p-2 rounded-full bg-slate-50 group-hover:bg-primary/10 transition">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
                                    </svg>
                                </div>
                                分享
                            </button>
                        </div>

                        <!-- 回覆區標題 -->
                        <h3 class="text-slate-700 font-medium mb-4 flex items-center gap-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                            </svg>
                            回覆內容
                        </h3>

                        <!-- 回覆欄位 -->
                        <div v-if="verifiedSchool" class="mb-6">
                            <textarea v-model="previewMessage.replyContent" rows="2"
                                class="w-full p-4 border border-slate-200 rounded-xl text-sm focus:ring-2 focus:ring-primary/30 focus:border-primary outline-none transition mb-2"
                                placeholder="輸入回覆內容..."></textarea>
                            <button @click="submitReply(previewMessage)"
                                class="bg-primary text-white px-5 py-2 rounded-lg hover:bg-primary/90 transition shadow-sm font-medium">
                                發佈回覆
                            </button>
                        </div>

                        <!-- 回覆列表 -->
                        <div v-if="previewMessage?.replies && previewMessage.replies.length"
                            class="space-y-1 text-sm max-h-full overflow-y-auto pr-2">
                            <div v-for="r in previewMessage.replies" :key="r.id"
                                class="p-3 border border-slate-100 hover:border-slate-200 rounded-xl mb-3 transition hover:bg-slate-50">
                                <div class="flex justify-between items-center mb-2">
                                    <div class="font-medium text-slate-700 flex items-center gap-2">
                                        {{ r.author_name || '匿名用戶' }}
                                        <span class="bg-slate-100 text-slate-600 text-xs px-2 py-0.5 rounded-full">
                                            {{ r.school }}
                                        </span>
                                    </div>
                                    <div class="text-xs text-slate-400">{{ formatTime(r.created_at) }}</div>
                                </div>
                                <div class="text-slate-600">{{ r.content }}</div>
                            </div>
                        </div>
                        <div v-else class="text-center py-8 text-slate-400 bg-slate-50 rounded-xl">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mx-auto mb-2 text-slate-300"
                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                    d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                            </svg>
                            暫無回覆，成為第一個回覆的人！
                        </div>
                    </div>
                </div>

                <!-- 載入更多按鈕 -->
                <div v-if="messages.length >= 10" class="flex justify-center mt-8">
                    <button @click="loadMoreMessages"
                        class="bg-white text-primary border border-primary/20 rounded-full px-6 py-2.5 text-sm hover:bg-indigo-50 transition flex items-center gap-2 shadow-sm font-medium">
                        <span v-if="loadingMore"
                            class="animate-spin rounded-full h-4 w-4 border-b-2 border-primary/50"></span>
                        <span v-else>載入更多留言</span>
                    </button>
                </div>
            </div>
        </div>

        <!-- 驗證彈窗 -->
        <div v-if="showVerificationModal"
            class="fixed inset-0 bg-black/40 backdrop-blur-sm flex items-center justify-center z-90 p-4">
            <div class="bg-white rounded-xl shadow-xl max-w-md w-full p-6 relative">
                <button @click="showVerificationModal = false"
                    class="absolute top-4 right-4 text-slate-400 hover:text-slate-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>

                <h2 class="text-xl font-bold text-center text-secondary mb-4">學校驗證</h2>

                <!-- 驗證選項切換 -->
                <div class="flex border border-indigo-100 rounded-lg overflow-hidden mb-4">
                    <button @click="verifyMode = 'anonymous'" :class="[
                        'flex-1 py-2 text-sm font-medium transition',
                        verifyMode === 'anonymous'
                            ? 'bg-primary text-white'
                            : 'bg-white text-slate-600 hover:bg-primary/10'
                    ]">
                        匿名驗證
                    </button>
                    <button @click="verifyMode = 'realname'" :class="[
                        'flex-1 py-2 text-sm font-medium transition',
                        verifyMode === 'realname'
                            ? 'bg-primary text-white'
                            : 'bg-white text-slate-600 hover:bg-primary/10'
                    ]">
                        實名驗證
                    </button>
                </div>

                <p class="text-sm text-slate-500 mb-4 text-center">
                    {{ verifyMode === 'anonymous' ? '僅驗證學校身份，保持匿名' : '驗證學校身份與真實姓名' }}
                </p>

                <div v-if="qrCode" class="flex flex-col items-center">
                    <p class="text-sm text-slate-500 mb-3 font-medium">
                        驗證碼：
                        <span class="font-mono bg-slate-100 px-2 py-0.5 rounded">{{ tid }}</span>
                    </p>
                    <img :src="qrCode" alt="QR Code" class="w-48 h-48 mx-auto rounded shadow-md mb-4" />

                    <div class="w-full space-y-3">
                        <a :href="authUri">
                            <button
                                class="w-full py-3 bg-primary text-white text-sm font-medium rounded-lg hover:bg-primary/90 transition flex items-center justify-center gap-2">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                                </svg>
                                前往App進行驗證
                            </button>
                        </a>

                        <div class="flex items-center gap-2 justify-center pt-3">
                            <div class="inline-flex items-center px-4 py-2 bg-primary/10 rounded-full text-primary">
                                <div class="animate-pulse mr-2 h-2 w-2 bg-primary rounded-full"></div>
                                <span class="text-sm font-medium">請在{{ verificationCountdown }}秒內完成掃描</span>
                            </div>
                        </div>
                        <!--
                        <div class="flex items-center gap-2 justify-center pt-3">
                            <div class="h-1.5 w-1.5 bg-primary rounded-full animate-pulse"></div>
                            <p class="text-sm text-slate-500">
                                請在
                                <span class="font-semibold text-primary">{{ verificationCountdown }}</span>
                                秒內完成掃描
                            </p>
                        </div>
                        -->
                    </div>
                </div>

                <div v-if="verifyFailed"
                    class="mt-4 bg-red-50 text-red-600 p-3 rounded-lg text-sm flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    驗證失敗或超時，請重新嘗試
                    <button @click="startVerification" class="ml-auto text-red-600 hover:text-red-600/50 font-medium">
                        重試
                    </button>
                </div>
            </div>
        </div>
    </div>
    <button v-show="showBackToTop" @click="scrollToTop"
        class="fixed bottom-4 right-4 z-50 bg-primary text-white rounded-full p-3 shadow-lg hover:bg-primary/50 transition">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" />
        </svg>
    </button>
</template>

<script setup>
    import { ref, onMounted, onUnmounted, watch } from 'vue'
    import axios from 'axios'

    const tid = ref(crypto.randomUUID())
    const qrCode = ref('')
    const authUri = ref('')
    const verifyFailed = ref(false)
    const verifiedSchool = ref('')
    const verifiedName = ref('')
    const verificationCountdown = ref(60)
    const countdownInterval = ref(null)
    const showVerificationModal = ref(false)
    const verifyMode = ref('anonymous')
    const useRealName = ref(false)

    const newMessage = ref('')
    const messages = ref([])
    const submitting = ref(false)
    const loading = ref(true)
    const loadingMore = ref(false)
    const page = ref(1)
    const pageSize = ref(10)
    const searchTerm = ref('')
    const showMobileSearch = ref(false)

    // 排序方式，預設最新
    const sortBy = ref('time_desc')
    const previewMessage = ref(null)
    const showPreviewModal = ref(false)

    const showBackToTop = ref(false)

    function scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' })
    }

    function handleScroll() {
        showBackToTop.value = window.scrollY > 300
    }

    onMounted(() => {
        fetchMessages()
        window.addEventListener('scroll', handleScroll)
    })

    onUnmounted(() => {
        window.removeEventListener('scroll', handleScroll)
        if (refreshInterval) clearInterval(refreshInterval)
        if (countdownInterval.value) clearInterval(countdownInterval.value)
    })

    import { useRoute, useRouter } from 'vue-router'

    const route = useRoute()
    const router = useRouter()

    function openPreview(msg) {
        previewMessage.value = msg
        showPreviewModal.value = true
    }

    function closePreview() {
        showPreviewModal.value = false
        previewMessage.value = null
        if (route.params.id) {
            router.replace({ name: 'Broad' })
        }
    }

    // 監聽下拉選單改變
    function onSortChange() {
        // 一旦改變就重抓列表
        fetchMessages()
    }

    function onMessageCardClick(e, msg) {
        const ignoreClickInside = ['A', 'IMG', 'SPAN', 'BUTTON', 'TEXTAREA']
        if (ignoreClickInside.includes(e.target.tagName)) return
        openPreview(msg)
    }

    function shareMessage(id) {
        const url = `https://did-edu.xiaozhi.moe/broad/${id}`
        navigator.clipboard.writeText(url).then(() => {
            alert('已複製連結到剪貼簿')
        }).catch(() => {
            alert('複製失敗，請手動複製')
        })
    }

    let verifyInterval = null
    let verifyTimeout = null

    const startVerification = async () => {
        verifyFailed.value = false
        tid.value = crypto.randomUUID()
        verificationCountdown.value = 60
        verifiedSchool.value = ''
        verifiedName.value = ''
        useRealName.value = false

        try {
            const endpoint = verifyMode.value === 'anonymous'
                ? 'https://api.xiaozhi.moe/chihlee/broad-verify'
                : 'https://api.xiaozhi.moe/chihlee/verify-qr'

            const qrRes = await axios.get(endpoint, {
                params: { transaction_id: tid.value }
            })

            qrCode.value = qrRes.data.qrcode_image
            authUri.value = qrRes.data.auth_uri

            if (countdownInterval.value) clearInterval(countdownInterval.value)
            countdownInterval.value = setInterval(() => {
                verificationCountdown.value--
            }, 1000)

            // 🔁 每 5 秒輪詢驗證結果
            verifyInterval = setInterval(checkVerifyResult, 5000)

            // ⏱️ 60 秒後自動停止驗證
            verifyTimeout = setTimeout(() => {
                clearInterval(verifyInterval)
                clearInterval(countdownInterval.value)
                verifyFailed.value = true
            }, 60000)
        } catch (e) {
            verifyFailed.value = true
        }
    }

    const checkVerifyResult = async () => {
        try {
            const result = await axios.get(`https://api.xiaozhi.moe/chihlee/broad-qr-result`, {
                params: { transaction_id: tid.value }
            })

            if (result.data.verify_result) {
                clearInterval(verifyInterval)
                clearTimeout(verifyTimeout)
                clearInterval(countdownInterval.value)

                const claims = result.data.data?.[0]?.claims || []
                const schoolClaim = claims.find(c => c.ename === 'school_CN')
                const nameClaim = claims.find(c => c.ename === 'name')

                verifiedSchool.value = schoolClaim?.value || '未知學校'

                if (verifyMode.value === 'realname') {
                    verifiedName.value = nameClaim?.value || ''
                    useRealName.value = !!verifiedName.value
                }

                showVerificationModal.value = false
                fetchMessages()
            } else if (result.data.verify_result === false) {
                // 明確失敗
                clearInterval(verifyInterval)
                clearTimeout(verifyTimeout)
                clearInterval(countdownInterval.value)
                verifyFailed.value = true
            }
        } catch (err) {
            if (err.response?.status !== 400) {
                clearInterval(verifyInterval)
                clearTimeout(verifyTimeout)
                clearInterval(countdownInterval.value)
                verifyFailed.value = true
            }
        }
    }

    const fetchMessages = async () => {
        loading.value = true
        try {
            const queryParams = {
                page: 1,
                pageSize: pageSize.value
            }
            // 如果使用者輸入了搜尋
            if (searchTerm.value) {
                queryParams.search = searchTerm.value
            }

            // 帶上排序
            if (sortBy.value) {
                queryParams.sort = sortBy.value
            }

            const res = await axios.get(`https://api.xiaozhi.moe/chihlee/board-with-replies`, {
                params: queryParams
            })

            const newList = res.data.messages?.map(m => ({
                ...m,
                showReplyBox: false,
                replyContent: '',
            })) || []

            messages.value = newList
            page.value = 1

            // ✅ 改為讀取 params.id
            const idParam = parseInt(route.params.id)
            if (idParam && !isNaN(idParam)) {
                const match = newList.find(m => m.id === idParam)
                if (match) {
                    previewMessage.value = match
                    showPreviewModal.value = true
                } else {
                    router.replace({ name: 'Board' }) // 回到 /board
                }
            }
        } catch (e) {
            console.error('取得留言失敗', e)
        } finally {
            loading.value = false
        }
    }

    const loadMoreMessages = async () => {
        if (loadingMore.value) return
        loadingMore.value = true
        try {
            const nextPage = page.value + 1
            const queryParams = {
                page: nextPage,
                pageSize: pageSize.value
            }
            if (searchTerm.value) {
                queryParams.search = searchTerm.value
            }

            if (sortBy.value) {
                queryParams.sort = sortBy.value
            }

            const res = await axios.get(`https://api.xiaozhi.moe/chihlee/board-with-replies`, {
                params: queryParams
            })

            const newList = res.data.messages?.map(m => ({
                ...m,
                showReplyBox: false,
                replyContent: '',
            })) || []

            if (newList.length) {
                messages.value = [...messages.value, ...newList]
                page.value = nextPage
            }
        } catch (e) {
            console.error('載入更多留言失敗', e)
        } finally {
            loadingMore.value = false
        }
    }


    const likeMessage = async (id) => {
        try {
            const res = await axios.post(`https://api.xiaozhi.moe/chihlee/board-like`, { message_id: id })

            const target = messages.value.find(m => m.id === id)
            if (target) {
                // 優先使用後端回傳值
                if (res.data?.likes !== undefined) {
                    target.likes = res.data.likes
                } else {
                    // 或前端自行加一
                    target.likes = (target.likes || 0) + 1
                }
            }
        } catch (e) {
            console.error('按讚失敗', e)
        }
    }

    const handleLike = async (msg) => {
        if (!verifiedSchool.value) {
            showVerificationModal.value = true
            return
        }

        await likeMessage(msg.id)
    }

    const submitReply = async (msg) => {
        const content = msg.replyContent?.trim()
        if (!content || !verifiedSchool.value) return
        try {
            await axios.post(`https://api.xiaozhi.moe/chihlee/board-reply`, {
                message_id: msg.id,
                school: verifiedSchool.value,
                content,
                author_name: useRealName.value && verifiedName.value ? verifiedName.value : undefined
            })
            msg.replyContent = ''
            msg.showReplyBox = false
            fetchMessages()
        } catch (e) {
            alert('回覆失敗')
        }
    }

    const submitMessage = async () => {
        if (!newMessage.value.trim() || !verifiedSchool.value) return
        submitting.value = true
        try {
            await axios.post(`https://api.xiaozhi.moe/chihlee/board-message`, {
                school: verifiedSchool.value,
                content: newMessage.value.trim(),
                author_name: useRealName.value && verifiedName.value ? verifiedName.value : undefined
            })
            newMessage.value = ''
            await fetchMessages()
        } catch (e) {
            alert('留言發佈失敗，請稍後重試')
        } finally {
            submitting.value = false
        }
    }

    const formatTime = (time) => {
        const date = new Date(time)
        const now = new Date()
        const diff = Math.floor((now - date) / 1000)
        if (diff < 60) return '剛剛'
        if (diff < 3600) return `${Math.floor(diff / 60)}分鐘前`
        if (diff < 86400) return `${Math.floor(diff / 3600)}小時前`
        if (diff < 604800) return `${Math.floor(diff / 86400)}天前`
        return date.toLocaleDateString('zh-TW', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
    }

    const logout = () => {
        location.reload()
    }

    function onContentClick(e) {
        // 找到最近的 .hashtag-span
        const span = e.target.closest('.hashtag-span')
        if (!span) return

        // 拿到 data-hashtag
        const tag = span.getAttribute('data-hashtag')
        if (!tag) return

        // 這裡你想做什麼？例如設置 searchTerm，然後觸發搜尋
        // 假設你已經有一個 searchTerm
        searchTerm.value = `#${tag}` // 或者直接用 tag
        // 重新取得/篩選
        fetchMessages()
    }

    function parseContent(text) {
        if (!text) return ''

        let output = text

        // 1) 先把所有網址變 <a>
        const urlRegex = /(https?:\/\/[^\s]+)/gi
        output = output.replace(urlRegex, (match) => {
            return `<a href="${match}" target="_blank" rel="noopener noreferrer"
      class="text-primary underline break-all"
    >${match}</a>`
        })

        // 2) 再把 a 裡面是圖片網址的 換成 <img>
        const imgInLinkRegex = /<a[^>]*?>(https?:\/\/[^\s]+?\.(?:png|jpg|jpeg|gif|webp))<\/a>/gi
        output = output.replace(imgInLinkRegex, (match, p1) => {
            return `<img src="${p1}" alt="image" class="my-2 max-w-full h-auto rounded shadow hashtag-image"/>`
        })

        // 3) 再處理 hashtag
        const hashtagRegex = /#[^\s#]+/g
        output = output.replace(hashtagRegex, (match) => {
            const justTag = match.slice(1)
            return `<span
      class="text-primary font-medium hashtag-span"
      data-hashtag="${justTag}"
    >${match}</span>`
        })

        return output
    }



    let refreshInterval = null

    onMounted(() => {
        fetchMessages()
    })

    onUnmounted(() => {
        if (refreshInterval) clearInterval(refreshInterval)
        if (countdownInterval.value) clearInterval(countdownInterval.value)
    })

    watch(verifyMode, () => {
        if (showVerificationModal.value) startVerification()
    })

    watch(showVerificationModal, (newVal) => {
        if (newVal) startVerification()
    })

    function clearSearch() {
        searchTerm.value = ''
        fetchMessages()
    }
</script>
