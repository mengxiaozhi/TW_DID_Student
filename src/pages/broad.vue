<template>
    <div class="board-page min-h-screen bg-slate-50">
        <section
            class="relative overflow-hidden bg-gradient-to-br pb-24">
            <div class="hero-intro py-10 md:py-14">
                <div class="space-y-6 text-center xl:text-left">
                    <span class="hero-badge mx-auto xl:mx-0">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        校園匿名交流
                    </span>
                    <div class="space-y-3">
                        <h1 class="text-3xl md:text-4xl font-bold text-slate-900 leading-snug">
                            驗證後再發聲，打造可信賴的 <span class="text-primary">匿名留言板</span>
                        </h1>
                        <p class="text-slate-600 text-base md:text-lg leading-relaxed max-w-2xl mx-auto xl:mx-0">
                            DID 驗證與留言系統整合於同一個體驗，分享真實觀點同時保留匿名，讓每一次校園交流都更安全、更具影響力。
                        </p>
                    </div>
                    <div class="hero-actions justify-center xl:justify-start">
                        <button class="btn btn-primary"
                            @click="verifiedSchool ? scrollToCompose() : (showVerificationModal = true)">
                            {{ verifiedSchool ? '撰寫留言' : '立即完成驗證' }}
                        </button>
                        <button class="btn btn-outline" @click="openSearchPanel">
                            搜尋留言
                        </button>
                        <button class="btn btn-ghost" @click="fetchMessages">
                            重新載入
                        </button>
                    </div>
                </div>
                <!--
                <div class="hero-grid mt-8">
                    <div class="stat-card">
                        <p class="text-sm text-slate-600">已載入留言</p>
                        <p class="text-3xl font-bold text-slate-900">{{ messageCountLabel }}</p>
                        <p class="text-xs text-slate-500 mt-1">依照最新排序即時更新</p>
                    </div>
                    <div class="stat-card">
                        <p class="text-sm text-slate-600">互動累積</p>
                        <p class="text-3xl font-bold text-slate-900">{{ interactionLabel }}</p>
                        <p class="text-xs text-slate-500 mt-1">包含讚數與回覆次數</p>
                    </div>
                    <div class="stat-card">
                        <p class="text-sm text-slate-600">身分狀態</p>
                        <p class="text-3xl font-bold text-slate-900 flex items-center gap-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" :class="isVerified ? 'text-primary' : 'text-amber-500'" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path v-if="isVerified" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                                <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2v-7H3v7a2 2 0 002 2z" />
                            </svg>
                            <span>{{ verificationHeadline }}</span>
                        </p>
                        <p class="text-xs text-slate-500 mt-1">{{ verificationDetail }}</p>
                    </div>
                </div>
                            -->
            </div>
        </section>

        <section class="px-4 md:px-6 -mt-10 md:-mt-14 pb-20">
            <div class="max-w-6xl mx-auto grid gap-6 xl:grid-cols-[minmax(0,1.75fr)_minmax(0,1fr)]">
                <div class="space-y-6">
                    <section ref="composeSection" class="floating-card p-5 md:p-8 space-y-6">
                        <header class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                            <div>
                                <h2 class="text-xl font-semibold text-slate-900">分享你的觀點</h2>
                                <p class="text-sm text-slate-500">完成 DID 驗證後即可匿名或實名留言</p>
                            </div>
                            <button v-if="verifiedSchool" @click="logout"
                                class="btn btn-outline btn-sm whitespace-nowrap">
                                登出
                            </button>
                        </header>

                        <div class="flex flex-wrap items-center gap-3">
                            <span v-if="verifiedSchool"
                                class="inline-flex items-center gap-2 rounded-full bg-primary/10 text-secondary text-xs font-semibold px-3 py-1.5">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M5 13l4 4L19 7" />
                                </svg>
                                {{ verifiedSchool }}
                            </span>
                            <span v-else
                                class="inline-flex items-center gap-2 rounded-full bg-amber-100 text-amber-700 text-xs font-semibold px-3 py-1.5">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                尚未驗證
                            </span>
                            <span v-if="verifiedName"
                                class="inline-flex items-center gap-2 rounded-full bg-blue-100 text-blue-700 text-xs font-semibold px-3 py-1.5">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                </svg>
                                {{ verifiedName }}
                            </span>
                            <label v-if="verifiedName"
                                class="flex items-center gap-2 text-xs text-slate-600 bg-white/70 border border-slate-200 rounded-full px-3 py-1 cursor-pointer transition hover:border-primary/40">
                                <input type="checkbox" v-model="useRealName"
                                    class="rounded text-primary focus:ring-primary h-3.5 w-3.5" />
                                <span class="font-medium">使用實名</span>
                            </label>
                        </div>

                        <div v-if="!verifiedSchool"
                            class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 rounded-xl px-4 py-4">
                            <div class="flex items-start gap-3">
                                <div
                                    class="h-10 w-10 rounded-full bg-amber-100 flex items-center justify-center text-amber-600">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                </div>
                                <div>
                                    <p class="text-sm font-semibold text-amber-700">請先完成學校驗證</p>
                                    <p class="text-xs text-amber-600 mt-1">掃描 DID QR Code 後即可發佈留言並互動。</p>
                                </div>
                            </div>
                            <button @click="showVerificationModal = true" class="btn btn-primary btn-sm self-start">
                                立即驗證
                            </button>
                        </div>

                        <form @submit.prevent="submitMessage" class="relative space-y-4">
                            <textarea v-model="newMessage" rows="5"
                                class="w-full rounded-2xl border border-slate-200/80 bg-white/95 p-4 text-sm shadow-sm transition focus:border-primary/60 focus:ring-2 focus:ring-primary/30 focus:outline-none resize-none max-h-60"
                                placeholder="分享你的想法..." :disabled="!verifiedSchool"></textarea>

                            <div
                                class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 bg-slate-50/80 border border-slate-200 rounded-2xl px-4 py-3">
                                <div class="text-xs text-slate-600 space-y-1">
                                    <p v-if="verifiedSchool" class="font-medium text-slate-700">
                                        {{ useRealName && verifiedName ? `${verifiedName}｜${verifiedSchool}` :
                                            `${verifiedSchool}｜匿名發布` }}
                                    </p>
                                    <p v-else class="font-medium text-slate-600">完成驗證後即可留言</p>
                                    <p class="text-[11px] text-slate-500">支援貼上連結、#標籤 與圖片網址展示。</p>
                                </div>
                                <button type="submit" :disabled="submitting || !newMessage.trim() || !verifiedSchool"
                                    class="btn btn-primary min-h-[44px] px-5">
                                    <span v-if="submitting" class="flex items-center gap-2">
                                        <svg class="h-4 w-4 animate-spin text-white" xmlns="http://www.w3.org/2000/svg"
                                            fill="none" viewBox="0 0 24 24">
                                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor"
                                                stroke-width="4"></circle>
                                            <path class="opacity-75" fill="currentColor"
                                                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                                            </path>
                                        </svg>
                                        發送中...
                                    </span>
                                    <span v-else>發佈留言</span>
                                </button>
                            </div>

                            <div v-if="!verifiedSchool"
                                class="absolute inset-0 rounded-2xl bg-white/60 backdrop-blur-[1px] flex items-center justify-center cursor-not-allowed"
                                @click="showVerificationModal = true">
                                <div
                                    class="flex items-center gap-2 rounded-full bg-white/90 px-4 py-2 text-sm text-slate-700 shadow-md">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                                    </svg>
                                    點擊以驗證身份
                                </div>
                            </div>
                        </form>
                    </section>

                    <section class="surface p-0">
                        <header
                            class="flex flex-col gap-3 md:flex-row md:items-center md:justify-between border-b border-slate-200 px-6 py-5">
                            <div>
                                <h2 class="text-lg font-semibold text-slate-900">最新留言</h2>
                                <p class="text-sm text-slate-500">即時收錄校園交流</p>
                            </div>
                            <div class="flex items-center gap-2">
                                <button class="btn btn-outline btn-sm" @click="openSearchPanel">
                                    搜尋
                                </button>
                                <button class="btn btn-ghost btn-sm" @click="fetchMessages">
                                    重新載入
                                </button>
                            </div>
                        </header>
                        <div class="p-4 sm:p-6">
                            <div v-if="loading" class="flex justify-center items-center py-16">
                                <div class="h-10 w-10 border-b-2 border-primary rounded-full animate-spin"></div>
                            </div>

                            <div v-else-if="messages.length === 0"
                                class="text-center bg-slate-50 rounded-2xl p-12 border border-dashed border-slate-200">
                                <div
                                    class="bg-white rounded-full w-24 h-24 mx-auto mb-4 flex items-center justify-center shadow-inner">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-slate-300" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                            d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                                    </svg>
                                </div>
                                <h3 class="text-slate-700 font-medium text-lg mb-2">尚無留言</h3>
                                <p class="text-slate-500">成為第一個分享想法的人！</p>
                            </div>

                            <div v-else class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                                <article v-for="msg in messages" :key="msg.id" @click="(e) => onMessageCardClick(e, msg)"
                                    class="group relative flex flex-col rounded-2xl border border-slate-200/60 bg-white/95 p-6 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg cursor-pointer">
                                    <header class="flex items-start justify-between gap-3">
                                        <div class="flex items-start gap-3">
                                            <div v-if="msg.author_name"
                                                class="h-12 w-12 rounded-full bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center flex-shrink-0 shadow-sm">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary"
                                                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                                </svg>
                                            </div>
                                            <div v-else
                                                class="h-12 w-12 rounded-full bg-gradient-to-br from-slate-100 to-slate-200 flex items-center justify-center flex-shrink-0 shadow-sm">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400"
                                                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                                </svg>
                                            </div>
                                            <div class="space-y-2">
                                                <div class="flex flex-wrap items-center gap-2">
                                                    <span v-if="msg.author_name"
                                                        class="inline-flex items-center gap-1 text-sm font-medium text-secondary">
                                                        {{ msg.author_name }}
                                                        <svg xmlns="http://www.w3.org/2000/svg"
                                                            class="h-3.5 w-3.5 text-primary" fill="none"
                                                            viewBox="0 0 24 24" stroke="currentColor">
                                                            <path stroke-linecap="round" stroke-linejoin="round"
                                                                stroke-width="2"
                                                                d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                                        </svg>
                                                    </span>
                                                    <span v-else class="text-sm font-medium text-slate-600">匿名用戶</span>
                                                    <span
                                                        class="inline-flex items-center gap-1 rounded-full bg-primary/10 px-2.5 py-0.5 text-xs font-medium text-secondary">
                                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3"
                                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                            <path stroke-linecap="round" stroke-linejoin="round"
                                                                stroke-width="2"
                                                                d="M3 7l9-4 9 4-9 4-9-4zM3 7v6a9 9 0 009 9m9-9V7" />
                                                        </svg>
                                                        <span>{{ msg.school }}</span>
                                                    </span>
                                                </div>
                                                <div class="flex flex-wrap items-center gap-3 text-xs text-slate-400">
                                                    <span class="inline-flex items-center gap-1">
                                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5"
                                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                            <path stroke-linecap="round" stroke-linejoin="round"
                                                                stroke-width="2"
                                                                d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                                        </svg>
                                                        {{ formatTime(msg.created_at) }}
                                                    </span>
                                                    <span v-if="msg.replies?.length"
                                                        class="inline-flex items-center gap-1">
                                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5"
                                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                            <path stroke-linecap="round" stroke-linejoin="round"
                                                                stroke-width="2"
                                                                d="M7 8h10M7 12h4m5 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3" />
                                                        </svg>
                                                        {{ msg.replies.length }} 則回覆
                                                    </span>
                                                </div>
                                            </div>
                                        </div>
                                        <button @click.stop="shareMessage(msg.id)"
                                            class="rounded-full border border-slate-200 p-2 text-slate-400 transition hover:border-primary/40 hover:bg-primary/10 hover:text-primary">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none"
                                                viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
                                            </svg>
                                        </button>
                                    </header>

                                    <div class="mt-4 text-sm leading-relaxed text-slate-700 whitespace-pre-wrap break-words"
                                        v-html="parseContent(msg.content)" @click="onContentClick($event)"></div>

                                    <div class="mt-5 flex flex-col gap-4 text-xs text-slate-500">
                                        <div class="flex flex-wrap items-center gap-2">
                                            <button @click.stop="handleLike(msg)"
                                                class="inline-flex items-center gap-1.5 rounded-full border border-slate-200 bg-slate-50/80 px-3 py-1.5 font-medium transition hover:border-primary/40 hover:bg-primary/10 hover:text-primary">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4"
                                                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                                                </svg>
                                                <span>讚同</span>
                                                <span class="text-secondary font-semibold">({{ msg.likes || 0 }})</span>
                                            </button>
                                            <button
                                                @click.stop="verifiedSchool ? (msg.showReplyBox = !msg.showReplyBox) : showVerificationModal = true"
                                                class="inline-flex items-center gap-1.5 rounded-full border border-slate-200 bg-slate-50/80 px-3 py-1.5 font-medium transition hover:border-primary/40 hover:bg-primary/10 hover:text-primary">
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4"
                                                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="2"
                                                        d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                                                </svg>
                                                <span>回覆</span>
                                                <span class="text-secondary font-semibold">({{ msg.replies?.length || 0
                                                    }})</span>
                                            </button>
                                        </div>

                                        <div v-if="msg.showReplyBox"
                                            class="space-y-3 rounded-xl border border-slate-200 bg-slate-50/80 p-3 text-sm">
                                            <textarea v-model="msg.replyContent" rows="2"
                                                class="w-full resize-none rounded-lg border border-slate-200 bg-white p-3 text-sm text-slate-600 focus:border-primary/40 focus:ring-2 focus:ring-primary/20 transition"
                                                placeholder="輸入回覆內容..."></textarea>
                                            <div class="flex justify-end">
                                                <button @click.stop="submitReply(msg)"
                                                    class="btn btn-primary btn-sm px-4">
                                                    發佈回覆
                                                </button>
                                            </div>
                                        </div>

                                        <div v-if="msg.replies && msg.replies.length"
                                            class="space-y-3 rounded-xl border border-dashed border-slate-200 bg-white/70 p-3 text-sm">
                                            <div v-for="(r, index) in msg.replies.slice(0, 3)" :key="r.id || index"
                                                class="rounded-lg bg-slate-50/80 p-3 shadow-sm">
                                                <div class="flex items-center justify-between text-xs text-slate-400">
                                                    <span class="font-medium text-slate-600">
                                                        {{ r.author_name || ('匿名用戶｜' + r.school) }}
                                                    </span>
                                                    <span>{{ formatTime(r.created_at) }}</span>
                                                </div>
                                                <div class="mt-1 text-sm text-slate-600">{{ r.content }}</div>
                                            </div>
                                            <button v-if="msg.replies.length > 3" @click.stop="openPreview(msg)"
                                                class="inline-flex items-center gap-1 text-xs font-medium text-primary hover:underline">
                                                <span>查看全部 {{ msg.replies.length }} 則回覆</span>
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none"
                                                    viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round"
                                                        stroke-width="2" d="M9 5l7 7-7 7" />
                                                </svg>
                                            </button>
                                        </div>
                                    </div>
                                </article>
                            </div>

                            <div v-if="hasMore" class="mt-10 flex justify-center">
                                <button ref="infiniteScrollTrigger" @click="loadMoreMessages"
                                    class="flex items-center gap-2 rounded-full border border-slate-200 px-4 py-2 text-xs text-slate-500 transition hover:border-primary/40 hover:text-primary">
                                    <span v-if="loadingMore"
                                        class="h-4 w-4 animate-spin rounded-full border-b-2 border-primary/60"></span>
                                    <span>{{ loadingMore ? '載入更多留言中...' : '向下滾動將自動載入更多留言' }}</span>
                                </button>
                            </div>
                            <div v-else-if="messages.length" class="mt-10 text-center text-xs text-slate-400">
                                已經沒有更多留言
                            </div>
                        </div>
                    </section>
                </div>

                <div class="space-y-6">
                    <section ref="searchSection" class="surface p-6 space-y-6">
                        <div class="space-y-1">
                            <h3 class="text-lg font-semibold text-slate-900">快速搜尋</h3>
                            <p class="text-sm text-slate-500">輸入關鍵字或變更排序條件</p>
                        </div>
                        <div class="space-y-3">
                            <div class="relative">
                                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-400" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                                    </svg>
                                </div>
                                <input v-model="searchTerm" placeholder="搜尋關鍵字或 #標籤"
                                    class="w-full rounded-xl border border-slate-200 py-2.5 pr-3 pl-9 text-sm placeholder-slate-400 transition focus:border-primary/40 focus:ring-2 focus:ring-primary/20" />
                            </div>
                            <div class="flex flex-wrap gap-2">
                                <button @click="fetchMessages" class="btn btn-primary btn-sm">
                                    套用搜尋
                                </button>
                                <button v-if="searchTerm" @click="clearSearch"
                                    class="btn btn-ghost btn-sm text-primary">
                                    清除
                                </button>
                            </div>
                        </div>
                        <div class="space-y-2">
                            <label for="sortSelect" class="block text-sm font-medium text-slate-700">排序方式</label>
                            <div class="relative">
                                <select id="sortSelect" v-model="sortBy" @change="onSortChange"
                                    class="block w-full appearance-none border border-slate-200 rounded-xl py-2.5 px-3 pr-8 text-sm text-slate-700 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary/40">
                                    <option value="time_desc">最新優先</option>
                                    <option value="time_asc">最舊優先</option>
                                    <option value="likes_desc">讚數由高到低</option>
                                    <option value="likes_asc">讚數由低到高</option>
                                </select>
                                <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                                    <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor"
                                        viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M19 9l-7 7-7-7" />
                                    </svg>
                                </div>
                            </div>
                            <div v-if="activeFilters"
                                class="inline-flex items-center gap-2 rounded-full bg-primary/10 text-secondary text-xs font-medium px-3 py-1 mt-2">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M10 6h10M4 6h.01M6 10h10M4 10h.01M14 14h6M4 14h6M8 18h6M4 18h.01" />
                                </svg>
                                已套用篩選條件
                            </div>
                        </div>
                    </section>

                    <section class="surface p-6 space-y-4">
                        <h3 class="text-lg font-semibold text-slate-900 flex items-center gap-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            社群小提醒
                        </h3>
                        <ul class="space-y-3 text-sm text-slate-600">
                            <li class="flex items-start gap-3">
                                <span class="mt-0.5 h-2 w-2 rounded-full bg-primary"></span>
                                完成學校驗證後即可匿名或實名發言，保障討論可信度。
                            </li>
                            <li class="flex items-start gap-3">
                                <span class="mt-0.5 h-2 w-2 rounded-full bg-primary"></span>
                                支援貼上圖片網址自動預覽，亦可使用 <span class="font-mono text-secondary">#標籤</span> 聚焦話題。
                            </li>
                            <li class="flex items-start gap-3">
                                <span class="mt-0.5 h-2 w-2 rounded-full bg-primary"></span>
                                互動行為將匿名記錄於系統，用於防濫用與排序分析。
                            </li>
                        </ul>
                    </section>
                </div>
            </div>
        </section>

        <div v-if="showMobileSearch"
            class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex justify-center items-center p-4 sm:hidden">
            <div class="bg-white w-full max-w-md rounded-2xl shadow-2xl p-5 relative">
                <button @click="closeMobileSearch" class="absolute top-3 right-3 text-slate-400 hover:text-slate-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>

                <h3 class="text-lg font-semibold text-slate-900 mb-4">搜尋留言</h3>

                <div class="space-y-4">
                    <div class="relative">
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-slate-400" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                        </div>
                        <input v-model="searchTerm" placeholder="搜尋關鍵字或 #標籤"
                            class="w-full rounded-xl border border-slate-200 py-2.5 pr-3 pl-9 text-sm placeholder-slate-400 transition focus:border-primary/40 focus:ring-2 focus:ring-primary/20" />
                    </div>

                    <div class="space-y-2">
                        <label for="mobileSort" class="block text-sm font-medium text-slate-700">排序方式</label>
                        <div class="relative">
                            <select id="mobileSort" v-model="sortBy" @change="onSortChange"
                                class="block w-full appearance-none border border-slate-200 rounded-xl py-2.5 px-3 pr-8 text-sm text-slate-700 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary/40">
                                <option value="time_desc">最新優先</option>
                                <option value="time_asc">最舊優先</option>
                                <option value="likes_desc">讚數由高到低</option>
                                <option value="likes_asc">讚數由低到高</option>
                            </select>
                            <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                                <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor"
                                    viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M19 9l-7 7-7-7" />
                                </svg>
                            </div>
                        </div>
                    </div>

                    <div class="flex flex-wrap gap-2">
                        <button @click="applyMobileSearch" class="btn btn-primary btn-sm flex-1">
                            套用搜尋
                        </button>
                        <button v-if="searchTerm" @click="clearMobileSearch"
                            class="btn btn-ghost btn-sm text-primary flex-1">
                            清除
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="showPreviewModal"
            class="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 flex items-center justify-center p-4 overflow-y-auto">
            <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full p-6 relative space-y-6">
                <button @click="closePreview" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>

                <header class="space-y-2">
                    <div class="flex items-start gap-3">
                        <div
                            class="h-12 w-12 rounded-full bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center shadow-sm">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                            </svg>
                        </div>
                        <div class="flex-1">
                            <div class="flex flex-wrap items-center gap-2 justify-between">
                                <div class="flex flex-wrap items-center gap-2">
                                    <span class="text-sm font-semibold text-secondary">{{ previewMessage?.author_name ||
                                        '匿名用戶' }}</span>
                                    <span
                                        class="bg-primary/10 text-secondary text-xs px-2.5 py-0.5 rounded-full font-medium">
                                        {{ previewMessage?.school }}
                                    </span>
                                </div>
                                <span class="text-xs text-slate-400">{{ formatTime(previewMessage?.created_at) }}</span>
                            </div>
                            <p class="mt-3 text-slate-700 whitespace-pre-wrap break-words leading-relaxed"
                                v-html="parseContent(previewMessage?.content)" @click="onContentClick($event)"></p>
                        </div>
                    </div>
                </header>

                <div class="flex items-center gap-3">
                    <button @click="previewMessage && handleLike(previewMessage)"
                        class="flex items-center gap-2 text-sm text-slate-500 hover:text-primary transition">
                        <div class="p-2 rounded-full bg-slate-100 hover:bg-primary/10 transition">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                            </svg>
                        </div>
                        <span class="text-secondary font-medium">({{ previewMessage?.likes || 0 }})</span>
                    </button>
                    <button @click="previewMessage?.id && shareMessage(previewMessage.id)"
                        class="flex items-center gap-2 text-sm text-slate-500 hover:text-primary transition">
                        <div class="p-2 rounded-full bg-slate-100 hover:bg-primary/10 transition">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
                            </svg>
                        </div>
                        分享
                    </button>
                </div>

                <div>
                    <h3 class="text-slate-700 font-medium mb-4 flex items-center gap-2">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                        </svg>
                        回覆內容
                    </h3>

                    <div v-if="verifiedSchool" class="mb-6">
                        <textarea v-model="previewMessage.replyContent" rows="2"
                            class="w-full p-4 border border-slate-200 rounded-xl text-sm focus:ring-2 focus:ring-primary/30 focus:border-primary outline-none transition mb-2"
                            placeholder="輸入回覆內容..."></textarea>
                        <button @click="submitReply(previewMessage)" class="btn btn-primary btn-sm">
                            發佈回覆
                        </button>
                    </div>

                    <div v-if="previewMessage?.replies && previewMessage.replies.length"
                        class="space-y-3 text-sm max-h-[50vh] overflow-y-auto pr-2">
                        <div v-for="r in previewMessage.replies" :key="r.id"
                            class="p-3 border border-slate-100 hover:border-slate-200 rounded-xl transition hover:bg-slate-50">
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
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mx-auto mb-2 text-slate-300" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                        </svg>
                        暫無回覆，成為第一個回覆的人！
                    </div>
                </div>
            </div>
        </div>

        <div v-if="showVerificationModal"
            class="fixed inset-0 bg-black/40 backdrop-blur-sm flex items-center justify-center z-90 p-4">
            <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-6 relative space-y-4">
                <button @click="showVerificationModal = false"
                    class="absolute top-4 right-4 text-slate-400 hover:text-slate-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>

                <h2 class="text-xl font-bold text-center text-secondary">學校驗證</h2>

                <div class="flex border border-indigo-100 rounded-lg overflow-hidden">
                    <button @click="verifyMode = 'anonymous'" :class="['flex-1 py-2 text-sm font-medium transition',
                        verifyMode === 'anonymous'
                            ? 'bg-primary text-white'
                            : 'bg-white text-slate-600 hover:bg-primary/10'
                    ]">
                        匿名驗證
                    </button>
                    <button @click="verifyMode = 'realname'" :class="['flex-1 py-2 text-sm font-medium transition',
                        verifyMode === 'realname'
                            ? 'bg-primary text-white'
                            : 'bg-white text-slate-600 hover:bg-primary/10'
                    ]">
                        實名驗證
                    </button>
                </div>

                <p class="text-sm text-slate-500 text-center">
                    {{ verifyMode === 'anonymous' ? '僅驗證學校身份，保持匿名' : '驗證學校身份與真實姓名' }}
                </p>

                <div v-if="qrCode" class="flex flex-col items-center space-y-4">
                    <p class="text-sm text-slate-500 font-medium">
                        驗證碼：
                        <span class="font-mono bg-slate-100 px-2 py-0.5 rounded">{{ tid }}</span>
                    </p>
                    <img :src="qrCode" alt="QR Code" class="w-48 h-48 mx-auto rounded-xl shadow-md" />

                    <div class="w-full space-y-3">
                        <a :href="authUri">
                            <button
                                class="w-full py-3 bg-primary text-white text-sm font-medium rounded-lg hover:bg-primary/90 transition flex items-center justify-center gap-2">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                                </svg>
                                前往 App 進行驗證
                            </button>
                        </a>

                        <div class="flex items-center gap-2 justify-center pt-3">
                            <div class="inline-flex items-center px-4 py-2 bg-primary/10 rounded-full text-primary">
                                <div class="animate-pulse mr-2 h-2 w-2 bg-primary rounded-full"></div>
                                <span class="text-sm font-medium">請在 {{ verificationCountdown }} 秒內完成掃描</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div v-if="verifyFailed"
                    class="mt-2 bg-red-50 text-red-600 p-3 rounded-lg text-sm flex items-center gap-2">
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

        <button v-show="showBackToTop" @click="scrollToTop"
            class="fixed bottom-5 right-5 z-50 bg-primary text-white rounded-full p-3 shadow-lg hover:bg-primary/80 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" />
            </svg>
        </button>
    </div>
</template>




<script setup>
    import { ref, onMounted, onUnmounted, watch, computed, nextTick } from 'vue'
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

    const BOARD_TOKEN_STORAGE_KEY = 'chihlee_board_jwt'
    const boardToken = ref('')
    const boardTokenExpiry = ref(null)
    let authErrorNotified = false

    const clearBoardSession = () => {
        boardToken.value = ''
        boardTokenExpiry.value = null
        verifiedSchool.value = ''
        verifiedName.value = ''
        useRealName.value = false
        if (typeof window !== 'undefined') {
            try {
                window.localStorage.removeItem(BOARD_TOKEN_STORAGE_KEY)
            } catch (err) {
                console.warn('無法移除留言板 Token', err)
            }
        }
    }

    const decodeBoardToken = (token) => {
        if (!token) return null
        try {
            const parts = token.split('.')
            if (parts.length < 2) return null
            const base64 = parts[1].replace(/-/g, '+').replace(/_/g, '/')
            const padded = base64 + '='.repeat((4 - (base64.length % 4)) % 4)

            const toBytes = () => {
                if (typeof window !== 'undefined' && typeof window.atob === 'function') {
                    const binary = window.atob(padded)
                    const bytes = new Uint8Array(binary.length)
                    for (let i = 0; i < binary.length; i += 1) {
                        bytes[i] = binary.charCodeAt(i)
                    }
                    return bytes
                }
                if (typeof Buffer !== 'undefined') {
                    return Uint8Array.from(Buffer.from(padded, 'base64'))
                }
                throw new Error('No available base64 decoder')
            }

            const bytes = toBytes()
            let jsonText

            if (typeof TextDecoder !== 'undefined') {
                jsonText = new TextDecoder('utf-8', { fatal: false }).decode(bytes)
            } else {
                // fallback：使用 escape 轉換避免亂碼
                let binary = ''
                for (let i = 0; i < bytes.length; i += 1) {
                    binary += String.fromCharCode(bytes[i])
                }
                jsonText = decodeURIComponent(escape(binary))
            }

            return JSON.parse(jsonText)
        } catch (err) {
            console.warn('解析留言板 Token 失敗', err)
            return null
        }
    }

    const applyBoardIdentity = ({ token, identity, preserveRealNamePreference = false }) => {
        if (!token || !identity?.school) {
            clearBoardSession()
            return
        }

        boardToken.value = token
        boardTokenExpiry.value = identity.expires_at || null
        verifiedSchool.value = identity.school
        verifiedName.value = identity.name || ''

        if (!preserveRealNamePreference) {
            useRealName.value = identity.mode === 'realname' && Boolean(identity.name)
        } else if (!identity.name) {
            useRealName.value = false
        }

        if (typeof window !== 'undefined') {
            try {
                window.localStorage.setItem(BOARD_TOKEN_STORAGE_KEY, token)
            } catch (err) {
                console.warn('無法儲存留言板 Token', err)
            }
        }
    }

    const restoreBoardSession = () => {
        if (typeof window === 'undefined') return
        const stored = window.localStorage.getItem(BOARD_TOKEN_STORAGE_KEY)
        if (!stored) return

        const payload = decodeBoardToken(stored)
        if (!payload?.school) {
            window.localStorage.removeItem(BOARD_TOKEN_STORAGE_KEY)
            return
        }

        if (payload.exp && payload.exp * 1000 <= Date.now()) {
            window.localStorage.removeItem(BOARD_TOKEN_STORAGE_KEY)
            return
        }

        applyBoardIdentity({
            token: stored,
            identity: {
                school: payload.school,
                name: payload.name || '',
                mode: payload.mode || (payload.name ? 'realname' : 'anonymous'),
                expires_at: payload.exp ? payload.exp * 1000 : null
            }
        })
    }

    const handleBoardRequestError = (error) => {
        if (error?.response?.status === 401) {
            clearBoardSession()
            showVerificationModal.value = true
            verifyFailed.value = false

            if (!authErrorNotified) {
                authErrorNotified = true
                alert('身份驗證已過期，請重新驗證')
                setTimeout(() => { authErrorNotified = false }, 1500)
            }
        }
    }

    const syncIdentityFromResponse = (data) => {
        if (data?.board_identity && boardToken.value) {
            applyBoardIdentity({
                token: boardToken.value,
                identity: data.board_identity,
                preserveRealNamePreference: true
            })
        }
    }

    const boardPost = async (url, payload = {}) => {
        if (!boardToken.value) {
            showVerificationModal.value = true
            throw new Error('缺少身份驗證')
        }

        try {
            const res = await axios.post(url, payload, {
                headers: {
                    Authorization: `Bearer ${boardToken.value}`
                }
            })
            syncIdentityFromResponse(res.data)
            return res
        } catch (error) {
            handleBoardRequestError(error)
            throw error
        }
    }

    const newMessage = ref('')
    const messages = ref([])
    const submitting = ref(false)
    const loading = ref(true)
    const loadingMore = ref(false)
    const hasMore = ref(true)
    const page = ref(1)
    const pageSize = ref(10)
    const searchTerm = ref('')
    const showMobileSearch = ref(false)
    const composeSection = ref(null)
    const searchSection = ref(null)
    const infiniteScrollTrigger = ref(null)

    // 排序方式，預設最新
    const sortBy = ref('time_desc')
    const previewMessage = ref(null)
    const showPreviewModal = ref(false)

    const showBackToTop = ref(false)
    let infiniteObserver = null

    const isVerified = computed(() => Boolean(verifiedSchool.value))
    const messageCountLabel = computed(() => messages.value.length.toLocaleString('zh-TW'))
    const interactionTotal = computed(() => messages.value.reduce((total, msg) => total + (msg.likes || 0) + (msg.replies?.length || 0), 0))
    const interactionLabel = computed(() => interactionTotal.value.toLocaleString('zh-TW'))
    const verificationHeadline = computed(() => (isVerified.value ? '已完成驗證' : '尚未驗證'))
    const verificationDetail = computed(() => {
        if (!isVerified.value) {
            return '完成學校驗證後即可匿名或實名參與留言'
        }

        if (useRealName.value && verifiedName.value) {
            return `${verifiedName.value}｜${verifiedSchool.value}`
        }

        if (verifiedName.value) {
            return `${verifiedSchool.value}｜可切換匿名或實名`
        }

        return `${verifiedSchool.value}｜目前匿名發佈`
    })

    const activeFilters = computed(() => Boolean(searchTerm.value || sortBy.value !== 'time_desc'))

    const scrollToCompose = () => {
        composeSection.value?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }

    const openSearchPanel = () => {
        if (typeof window !== 'undefined' && window.innerWidth < 640) {
            showMobileSearch.value = true
            return
        }

        searchSection.value?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }

    const closeMobileSearch = () => {
        showMobileSearch.value = false
    }

    const applyMobileSearch = () => {
        fetchMessages()
        closeMobileSearch()
    }

    const clearMobileSearch = () => {
        clearSearch()
        closeMobileSearch()
    }

    function scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' })
    }

    function handleScroll() {
        showBackToTop.value = window.scrollY > 300
    }

    const observeInfiniteScroll = () => {
        if (typeof window === 'undefined') return

        if (infiniteObserver) {
            infiniteObserver.disconnect()
            infiniteObserver = null
        }

        if (!infiniteScrollTrigger.value || !hasMore.value) return

        infiniteObserver = new IntersectionObserver((entries) => {
            const entry = entries[0]
            if (entry?.isIntersecting && hasMore.value && !loading.value && !loadingMore.value) {
                loadMoreMessages()
            }
        }, {
            root: null,
            rootMargin: '0px 0px 320px 0px',
            threshold: 0
        })

        infiniteObserver.observe(infiniteScrollTrigger.value)
    }

    onMounted(() => {
        restoreBoardSession()
        fetchMessages()
        window.addEventListener('scroll', handleScroll)
        nextTick(() => observeInfiniteScroll())
    })

    onUnmounted(() => {
        window.removeEventListener('scroll', handleScroll)
        if (infiniteObserver) {
            infiniteObserver.disconnect()
            infiniteObserver = null
        }
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
        clearBoardSession()

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

                const token = result.data.board_jwt
                const identity = result.data.board_identity

                if (token && identity?.school) {
                    applyBoardIdentity({ token, identity })
                    showVerificationModal.value = false
                    fetchMessages()
                } else {
                    verifyFailed.value = true
                    const errorMessage = result.data.board_jwt_error
                        ? '無法建立留言身份，請稍後再試'
                        : '未取得驗證資訊，請重新驗證'
                    alert(errorMessage)
                }
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
            hasMore.value = newList.length === pageSize.value

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
            hasMore.value = false
        } finally {
            loading.value = false
        }
    }

    const loadMoreMessages = async () => {
        if (loadingMore.value || !hasMore.value) return
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
                hasMore.value = newList.length === pageSize.value
            } else {
                hasMore.value = false
            }
        } catch (e) {
            console.error('載入更多留言失敗', e)
        } finally {
            loadingMore.value = false
        }
    }


    const likeMessage = async (id) => {
        try {
            const res = await boardPost(`https://api.xiaozhi.moe/chihlee/board-like`, { message_id: id })

            const target = messages.value.find(m => m.id === id)
            if (target) {
                if (res.data?.likes !== undefined) {
                    target.likes = res.data.likes
                } else {
                    target.likes = (target.likes || 0) + 1
                }
            }
        } catch (e) {
            if (e?.message !== '缺少身份驗證' && e?.response?.status !== 401) {
                console.error('按讚失敗', e)
            }
        }
    }

    const handleLike = async (msg) => {
        if (!verifiedSchool.value || !boardToken.value) {
            showVerificationModal.value = true
            return
        }

        await likeMessage(msg.id)
    }

    const submitReply = async (msg) => {
        const content = msg.replyContent?.trim()
        if (!content || !verifiedSchool.value || !boardToken.value) {
            if (!verifiedSchool.value || !boardToken.value) {
                showVerificationModal.value = true
            }
            return
        }
        try {
            await boardPost(`https://api.xiaozhi.moe/chihlee/board-reply`, {
                message_id: msg.id,
                content,
                useRealName: useRealName.value && Boolean(verifiedName.value)
            })
            msg.replyContent = ''
            msg.showReplyBox = false
            fetchMessages()
        } catch (e) {
            if (e?.response?.status !== 401) {
                alert('回覆失敗')
            }
        }
    }

    const submitMessage = async () => {
        const content = newMessage.value.trim()
        if (!content || !verifiedSchool.value || !boardToken.value) {
            if (!verifiedSchool.value || !boardToken.value) {
                showVerificationModal.value = true
            }
            return
        }
        submitting.value = true
        try {
            await boardPost(`https://api.xiaozhi.moe/chihlee/board-message`, {
                content,
                useRealName: useRealName.value && Boolean(verifiedName.value)
            })
            newMessage.value = ''
            await fetchMessages()
        } catch (e) {
            if (e?.response?.status !== 401) {
                alert('留言發佈失敗，請稍後重試')
            }
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
        clearBoardSession()
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

    watch(infiniteScrollTrigger, () => {
        nextTick(() => observeInfiniteScroll())
    })

    watch(hasMore, (newVal) => {
        if (!newVal && infiniteObserver) {
            infiniteObserver.disconnect()
            infiniteObserver = null
        } else if (newVal) {
            nextTick(() => observeInfiniteScroll())
        }
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
