<template>
    <div class="info-page min-h-screen bg-slate-50">
        <section
            class="relative overflow-hidden bg-gradient-to-br from-white via-[#f3f8fc] to-[#e6f0f8] border-b border-slate-200/60 pb-20">
            <div class="hero-intro py-10 md:py-12">
                <div class="space-y-5 text-center lg:text-left">
                    <span class="hero-badge mx-auto lg:mx-0">校園投票示範</span>
                    <div class="space-y-3">
                        <h1 class="text-3xl md:text-4xl font-bold text-slate-900 leading-tight">
                            兩階段 DID 驗證，體驗安全的 <span class="text-primary">匿名投票流程</span>
                        </h1>
                        <p class="text-slate-600 text-base md:text-lg leading-relaxed max-w-3xl mx-auto lg:mx-0">
                            先透過 VC 驗證學生身份，再使用一次性票證完成匿名投票。整個過程僅需掃描兩次 QR Code，即可示範校園投票的安全流程設計。
                        </p>
                    </div>
                    <div class="hero-actions justify-center lg:justify-start">
                        <button class="btn btn-primary" @click="resetVoteFlow()">
                            重新產生驗證流程
                        </button>
                        <router-link to="/" class="btn btn-outline">回到首頁</router-link>
                    </div>
                </div>
            </div>

            <div class="pointer-events-none absolute inset-0">
                <div class="absolute -top-28 -right-20 h-72 w-72 rounded-full bg-primary/10 blur-3xl"></div>
                <div class="absolute bottom-12 left-8 h-52 w-52 rounded-full bg-secondary/10 blur-2xl"></div>
            </div>
        </section>

        <section class="px-4 md:px-6 -mt-12 md:-mt-16 pb-24">
            <div class="max-w-6xl mx-auto grid gap-6 xl:grid-cols-[minmax(0,1.8fr)_minmax(0,1fr)]">
                <div class="floating-card p-6 md:p-8 space-y-8">
                    <header class="space-y-2 text-center md:text-left">
                        <span class="step-indicator mx-auto md:mx-0">投票驗證流程</span>
                        <h2 class="text-2xl font-semibold text-slate-900">即時展示驗證與匿名投票串接</h2>
                        <p class="text-sm md:text-base text-slate-600 max-w-2xl mx-auto md:mx-0">
                            掃描第一階段 QR 驗證學生身份，取得匿名票證後即可進入第二階段投票。下方示例提供流程中每個步驟的狀態視覺化回饋。
                        </p>
                    </header>

                    <div class="space-y-8">
                        <div class="bg-white/80 border border-slate-200 rounded-xl p-4 space-y-2 shadow-sm">
                            <p class="text-xs font-semibold text-secondary uppercase tracking-wide">本次投票議題</p>
                            <p class="text-base font-semibold text-slate-900 leading-snug">{{ voteQuestion }}</p>
                        </div>

                        <section class="space-y-4">
                            <div class="flex flex-col gap-2">
                                <p class="text-xs font-medium text-slate-500 uppercase tracking-wide">
                                    第一階段｜身分驗證
                                </p>
                                <p class="text-sm text-slate-500">驗證碼：{{ voteTid }}</p>
                            </div>

                            <div v-if="!voteVerifiedData.length" class="space-y-5">
                                <div v-if="voteQrCode" class="space-y-4">
                                    <a :href="voteAuthUri" class="block">
                                        <button
                                            class="w-full py-3 rounded-xl bg-primary text-white font-semibold shadow-sm hover:bg-secondary transition">
                                            前往 App 驗證投票身分
                                        </button>
                                    </a>
                                    <div class="flex flex-col items-center gap-3">
                                        <img :src="voteQrCode" alt="vote QR"
                                            class="w-48 h-48 rounded-2xl border border-slate-200 shadow" />
                                        <p class="text-sm text-slate-500">請於 60 秒內完成掃描</p>
                                        <div class="flex items-center gap-3 text-sm text-slate-500">
                                            <span class="h-4 w-4 border-b-2 border-primary rounded-full animate-spin"></span>
                                            等待驗證中...
                                        </div>
                                    </div>
                                </div>

                                <div v-if="voteFailed"
                                    class="rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-center space-y-2 text-sm text-red-700">
                                    <p>{{ voteFailureMessage || '驗證失敗、超時或已領票，請重新驗證。' }}</p>
                                    <button @click="resetVoteFlow()"
                                        class="w-full rounded-lg bg-red-200 py-2 font-semibold text-red-800 hover:bg-red-300 transition">
                                        重新驗證
                                    </button>
                                </div>
                            </div>

                            <div v-else class="space-y-6">
                                <p class="text-sm text-slate-500">第二階段驗證碼：{{ secondPhaseTid }}</p>
                                <div class="rounded-xl border border-slate-200 bg-white/80 p-4 space-y-3">
                                    <h3 class="text-lg font-semibold text-secondary text-center md:text-left">
                                        第一階段身份已確認
                                    </h3>
                                    <div class="divide-y divide-slate-200 text-sm text-slate-700">
                                        <div v-for="item in voteVerifiedData" :key="item.ename"
                                            class="flex flex-col md:flex-row md:items-center md:justify-between gap-1 py-2">
                                            <span class="font-medium">{{ item.cname }}</span>
                                            <span class="text-slate-900">{{ item.value }}</span>
                                        </div>
                                    </div>
                                </div>

                                <button @click="startSecondPhase"
                                    class="w-full rounded-xl bg-secondary py-3 font-semibold text-white shadow-sm hover:bg-primary transition">
                                    進行第二階段匿名投票驗證
                                </button>

                                <div v-if="secondPhaseQrCode" class="space-y-4 text-center">
                                    <a :href="secondPhaseAuthUri" class="block">
                                        <button
                                            class="w-full rounded-xl bg-indigo-600 py-3 font-semibold text-white shadow-sm hover:bg-indigo-700 transition">
                                            前往 App 進行投票
                                        </button>
                                    </a>
                                    <div class="flex flex-col items-center gap-3">
                                        <img :src="secondPhaseQrCode" alt="vote QR"
                                            class="w-48 h-48 rounded-2xl border border-slate-200 shadow" />
                                        <p class="text-sm text-slate-500">請於 60 秒內完成掃描</p>
                                        <div class="flex items-center gap-3 text-sm text-slate-500">
                                            <span class="h-4 w-4 border-b-2 border-indigo-500 rounded-full animate-spin"></span>
                                            等待投票驗證中...
                                        </div>
                                    </div>
                                </div>

                                <div v-if="votedSchool && selectedOption" class="space-y-4">
                                    <h3 class="text-lg font-semibold text-center text-emerald-700">
                                        請選擇您的投票選項：
                                    </h3>
                                    <p class="text-sm text-slate-500 text-center">議題：{{ voteQuestion }}</p>
                                    <div class="grid gap-3 sm:grid-cols-3">
                                        <button v-for="option in voteOptionsDisplay" :key="option"
                                            @click="selectedOption = option"
                                            :class="selectedOption === option
                                                ? 'bg-emerald-600 text-white shadow'
                                                : 'bg-slate-100 text-slate-700 hover:bg-slate-200'"
                                            class="rounded-xl border border-slate-200 py-2 font-medium transition">
                                            {{ option }}
                                        </button>
                                    </div>
                                    <button @click="submitVote"
                                        class="w-full rounded-xl bg-emerald-600 py-3 font-semibold text-white shadow-sm hover:bg-emerald-700 transition">
                                        送出投票
                                    </button>
                                </div>
                            </div>
                        </section>
                    </div>
                </div>
                <aside class="space-y-6">
                    <div class="floating-card p-6 md:p-6 space-y-5">
                        <div class="space-y-1">
                            <p class="text-xs font-semibold text-secondary uppercase tracking-wide">即時投票統計</p>
                            <h3 class="text-base font-semibold text-slate-900 leading-snug">{{ voteQuestion }}</h3>
                            <p class="text-xs text-slate-500">累計 {{ totalVotes.toLocaleString('zh-TW') }} 票</p>
                        </div>
                        <div v-if="totalVotes" class="space-y-4">
                            <div v-for="option in voteOptionsDisplay" :key="`stat-` + option" class="space-y-2">
                                <div class="flex items-center justify-between text-sm font-medium text-slate-700">
                                    <span>{{ option }}</span>
                                    <span>{{ getVoteCount(option).toLocaleString('zh-TW') }} 票 · {{ getVotePercent(option) }}</span>
                                </div>
                                <div class="h-2 bg-slate-200/70 rounded-full overflow-hidden">
                                    <div class="h-full bg-primary rounded-full transition-all duration-500" :style="{ width: getVoteBarWidth(option) }"></div>
                                </div>
                            </div>
                        </div>
                        <p v-else class="text-sm text-slate-500">目前尚無投票紀錄，成為第一位投票的人吧！</p>
                        <p class="text-xs text-slate-400">統計每 15 秒更新一次</p>
                    </div>
                </aside>
            </div>
        </section>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import axios from 'axios'
import { fetchVoteStats } from '../services/chihleeApi'

const voteQrCode = ref('')
const voteVerifiedData = ref([])
const voteTid = ref('')
const voteFailed = ref(false)
const voteFailureMessage = ref('')
const voteAuthUri = ref('')

const secondPhaseQrCode = ref('')
const secondPhaseAuthUri = ref('')
const secondPhaseTid = ref('')

const selectedOption = ref('')
const DEFAULT_VOTE_OPTIONS = ['同意', '不同意', '無意見/棄權']
const voteOptions = ref([...DEFAULT_VOTE_OPTIONS])
const voteQuestion = ref('是否應該禁止在學校使用手機')
const voteStats = ref(Object.fromEntries(DEFAULT_VOTE_OPTIONS.map((option) => [option, 0])))
const voteOptionsDisplay = computed(() => (voteOptions.value && voteOptions.value.length ? voteOptions.value : DEFAULT_VOTE_OPTIONS))
const totalVotes = computed(() => voteOptionsDisplay.value.reduce((sum, option) => sum + (voteStats.value?.[option] || 0), 0))

const getVoteCount = (option) => voteStats.value?.[option] || 0
const getVotePercent = (option) => {
    if (!totalVotes.value) return '0%'
    return `${Math.round((getVoteCount(option) / totalVotes.value) * 100)}%`
}
const getVoteBarWidth = (option) => {
    if (!totalVotes.value) return '0%'
    const percent = (getVoteCount(option) / totalVotes.value) * 100
    return `${percent.toFixed(2)}%`
}
const votedSchool = ref('')
const ballotToken = ref('')

let voteInterval = null
let voteTimeout = null
let secondPhaseInterval = null
let secondPhaseTimeout = null
let voteStatsInterval = null

const clearFirstPhaseTimers = () => {
    if (voteInterval) {
        clearInterval(voteInterval)
        voteInterval = null
    }
    if (voteTimeout) {
        clearTimeout(voteTimeout)
        voteTimeout = null
    }
}

const clearSecondPhaseTimers = () => {
    if (secondPhaseInterval) {
        clearInterval(secondPhaseInterval)
        secondPhaseInterval = null
    }
    if (secondPhaseTimeout) {
        clearTimeout(secondPhaseTimeout)
        secondPhaseTimeout = null
    }
}

const resetSecondPhaseState = () => {
    clearSecondPhaseTimers()
    secondPhaseQrCode.value = ''
    secondPhaseAuthUri.value = ''
    secondPhaseTid.value = ''
    votedSchool.value = ''
    selectedOption.value = ''
}

const generateVoteUUID = () => {
    voteTid.value = crypto.randomUUID()
    voteVerifiedData.value = []
    voteFailed.value = false
    voteFailureMessage.value = ''
    voteQrCode.value = ''
    voteAuthUri.value = ''
    ballotToken.value = ''
}

const startVoteVerification = async () => {
    clearFirstPhaseTimers()
    resetSecondPhaseState()

    try {
        const qrRes = await axios.get(`https://api.xiaozhi.moe/chihlee/vote-verify`, {
            params: { transaction_id: voteTid.value }
        })

        voteQrCode.value = qrRes.data.qrcode_image
        voteAuthUri.value = qrRes.data.auth_uri
        voteFailed.value = false
        voteFailureMessage.value = ''

        voteInterval = setInterval(fetchVoteResult, 5000)
        voteTimeout = setTimeout(() => {
            clearFirstPhaseTimers()
            voteFailed.value = true
            voteFailureMessage.value = '驗證逾時，請重新產生 QR Code'
        }, 60000)
    } catch (error) {
        console.error('第一階段驗證失敗', error)
        voteFailed.value = true
        voteFailureMessage.value = 'QR 產生失敗，請稍後再試'
    }
}

const fetchVoteResult = async () => {
    try {
        const { data } = await axios.get(`https://api.xiaozhi.moe/chihlee/vote-verify-result`, {
            params: { transaction_id: voteTid.value }
        })

        if (data.verify_result) {
            voteVerifiedData.value = data.data?.[0]?.claims || []
            ballotToken.value = data.ballot_token || ''
            voteFailureMessage.value = ''
            voteFailed.value = false
            if (Array.isArray(data.vote_options) && data.vote_options.length) {
                voteOptions.value = data.vote_options
            }
            if (data.vote_question) {
                voteQuestion.value = data.vote_question
            }
            clearFirstPhaseTimers()
            return
        }

        if (data.pending === false && data.verify_result === false) {
            voteFailed.value = true
            voteFailureMessage.value = data.message || '驗證未通過，請重新領取'
            ballotToken.value = ''
            clearFirstPhaseTimers()
        }
    } catch (e) {
        console.warn('查詢中...', e)
        if (e.response?.status === 403) {
            voteFailed.value = true
            voteFailureMessage.value = e.response?.data?.error || '此學號已領過票，無法重複領票'
            ballotToken.value = ''
            clearFirstPhaseTimers()
        }
    }
}

const startSecondPhase = async () => {
    if (!ballotToken.value) {
        alert('請先完成身分驗證並領票')
        return
    }

    resetSecondPhaseState()
    secondPhaseTid.value = crypto.randomUUID()

    try {
        const qrRes = await axios.get(`https://api.xiaozhi.moe/chihlee/vote-qr`, {
            params: { transaction_id: secondPhaseTid.value }
        })

        secondPhaseQrCode.value = qrRes.data.qrcode_image
        secondPhaseAuthUri.value = qrRes.data.auth_uri

        secondPhaseInterval = setInterval(fetchSecondPhaseResult, 5000)
        secondPhaseTimeout = setTimeout(() => {
            clearSecondPhaseTimers()
        }, 60000)
    } catch (error) {
        console.error('第二階段驗證失敗', error)
        alert('投票 QR 產生失敗')
    }
}

const fetchSecondPhaseResult = async () => {
    try {
        const { data } = await axios.get(`https://api.xiaozhi.moe/chihlee/vote-qr-result`, {
            params: { transaction_id: secondPhaseTid.value }
        })

        if (data.verify_result) {
            clearSecondPhaseTimers()
            const claims = data.data?.[0]?.claims || []
            const schoolClaim = claims.find(claim => claim.ename === 'school_cn' || claim.ename === 'school_CN')
            votedSchool.value = schoolClaim?.value || '未知學校'
        }
    } catch (e) {
        console.warn('查詢投票驗證中...', e)
    }
}

const submitVote = async () => {
    if (!ballotToken.value) {
        alert('請先完成第一階段驗證取得投票資格')
        return
    }
    if (!selectedOption.value || !votedSchool.value || !secondPhaseTid.value) {
        alert('請完成匿名驗證並選擇選項')
        return
    }
    try {
        await axios.post('https://api.xiaozhi.moe/chihlee/submit-vote', {
            transaction_id: secondPhaseTid.value,
            school: votedSchool.value,
            option: selectedOption.value,
            ballot_token: ballotToken.value
        })
        alert(`🎉 投票成功！您選擇了「${selectedOption.value}」`)
        ballotToken.value = ''
        selectedOption.value = ''
        resetSecondPhaseState()
        await refreshVoteStats()
    } catch (err) {
        console.error('提交投票失敗', err)
        if (err.response?.status === 409) {
            alert('此票已完成投票，無法重複投票')
        } else if (err.response?.status === 403) {
            alert('尚未取得投票資格或驗證已過期')
        } else {
            alert('提交投票失敗，請稍後重試')
        }
    }
}

const refreshVoteStats = async () => {
    try {
        const stats = await fetchVoteStats()
        voteQuestion.value = stats?.question || voteQuestion.value
        if (Array.isArray(stats?.options) && stats.options.length) {
            voteOptions.value = stats.options
        }
        const totals = Object.fromEntries((stats?.options || DEFAULT_VOTE_OPTIONS).map((option) => [option, 0]))
        if (stats?.totals) {
            for (const [option, count] of Object.entries(stats.totals)) {
                if (option in totals) {
                    totals[option] = Number(count) || 0
                }
            }
        }
        voteStats.value = totals
    } catch (err) {
        console.warn('取得投票統計失敗', err)
    }
}

const startVoteStatsPolling = () => {
    refreshVoteStats()
    if (voteStatsInterval) clearInterval(voteStatsInterval)
    voteStatsInterval = setInterval(refreshVoteStats, 15000)
}

const stopVoteStatsPolling = () => {
    if (voteStatsInterval) {
        clearInterval(voteStatsInterval)
        voteStatsInterval = null
    }
}

const resetVoteFlow = () => {
    clearFirstPhaseTimers()
    resetSecondPhaseState()
    voteOptions.value = [...DEFAULT_VOTE_OPTIONS]
    voteQuestion.value = '是否應該禁止在學校使用手機'
    voteStats.value = Object.fromEntries(DEFAULT_VOTE_OPTIONS.map((option) => [option, 0]))
    generateVoteUUID()
    startVoteVerification()
    refreshVoteStats()
}

onMounted(() => {
    resetVoteFlow()
    startVoteStatsPolling()
})

onUnmounted(() => {
    clearFirstPhaseTimers()
    clearSecondPhaseTimers()
    stopVoteStatsPolling()
})
</script>
