<template>
    <div class="min-h-screen flex flex-col bg-gradient-to-br from-slate-50 to-slate-100">
        <main class="py-8 px-4 md:px-8">
            <div class="max-w-2xl mx-auto bg-white shadow-lg rounded-xl p-8 space-y-8 border border-slate-200">
                <!-- 投票驗證流程 -->
                <div>
                    <div v-if="!voteVerifiedData.length">
                        <p class="text-sm text-slate-500 mb-2">驗證碼：{{ voteTid }}</p>
                        <div v-if="voteQrCode">
                            <a :href="voteAuthUri">
                                <button
                                    class="w-full py-3 bg-purple-600 text-white rounded-lg mb-4 hover:bg-purple-700">
                                    前往 App 驗證投票身分
                                </button>
                            </a>
                            <img :src="voteQrCode" alt="vote QR" class="w-48 h-48 mx-auto rounded-lg shadow" />
                            <p class="text-sm mt-4 text-slate-500">請於 60 秒內完成掃描</p>
                            <div class="flex justify-center items-center mt-2 text-sm text-slate-500">
                                <div class="animate-spin h-4 w-4 border-b-2 border-purple-500 rounded-full mr-2"></div>
                                等待驗證中...
                            </div>
                        </div>
                        <div v-if="voteFailed"
                            class="mt-4 bg-red-100 text-red-700 p-3 rounded-lg border border-red-300 text-sm text-center">
                            驗證失敗、超時或已領票，請重新驗證。
                            <button @click="generateVoteUUID(); startVoteVerification()"
                                class="mt-2 w-full py-2 bg-red-200 text-red-800 rounded-md">重新驗證</button>
                        </div>
                    </div>

                    <!-- 第一階段驗證完成 -->
                    <div v-else>
                        <p class="text-sm text-slate-500 mb-2">第二階段驗證碼：{{ secondPhaseTid }}</p>
                        <h2 class="text-xl font-semibold text-center text-purple-700">第一階段身分驗證成功</h2>
                        <div class="bg-slate-50 rounded-xl p-4 mt-4">
                            <div v-for="item in voteVerifiedData" :key="item.ename"
                                class="py-2 border-b last:border-b-0 flex justify-between">
                                <span class="font-medium text-slate-700">{{ item.cname }}</span>
                                <span class="text-slate-900">{{ item.value }}</span>
                            </div>
                        </div>

                        <button @click="startSecondPhase"
                            class="mt-6 w-full py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
                            進行第二階段匿名投票驗證
                        </button>

                        <div v-if="secondPhaseQrCode" class="mt-8 text-center">
                            <a :href="secondPhaseAuthUri">
                                <button
                                    class="w-full py-3 bg-indigo-600 text-white rounded-lg mb-4 hover:bg-indigo-700">
                                    前往 App 進行投票
                                </button>
                            </a>
                            <img :src="secondPhaseQrCode" alt="vote QR" class="w-48 h-48 mx-auto rounded-lg shadow" />
                            <p class="text-sm mt-4 text-slate-500">請於 60 秒內完成掃描</p>
                            <div class="flex justify-center items-center mt-2 text-sm text-slate-500">
                                <div class="animate-spin h-4 w-4 border-b-2 border-indigo-500 rounded-full mr-2"></div>
                                等待投票驗證中...
                            </div>
                        </div>

                        <div v-if="votedSchool && selectedOption">
                            <h3 class="text-lg font-semibold mt-6 text-center text-emerald-700">請選擇您的投票選項：</h3>
                            <div class="grid grid-cols-1 gap-4 mt-4">
                                <button v-for="option in voteOptions" :key="option" @click="selectedOption = option"
                                    :class="selectedOption === option ? 'bg-emerald-600 text-white' : 'bg-slate-100 text-slate-700'"
                                    class="py-2 rounded-lg border hover:bg-emerald-100">
                                    {{ option }}
                                </button>
                            </div>
                            <button @click="submitVote"
                                class="mt-6 w-full py-3 bg-emerald-700 text-white rounded-lg hover:bg-emerald-800">
                                送出投票
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </main>
        <div class="pt-12">
            <information />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import information from '../components/information.vue'

const voteQrCode = ref('')
const voteVerifiedData = ref([])
const voteTid = ref('')
const voteFailed = ref(false)
const voteAuthUri = ref('')

const secondPhaseQrCode = ref('')
const secondPhaseAuthUri = ref('')
const secondPhaseTid = ref('')

const selectedOption = ref('')
const voteOptions = ['贊成', '反對', '中立']
const votedSchool = ref('')

let voteInterval = null
let voteTimeout = null
let secondPhaseInterval = null
let secondPhaseTimeout = null

const generateVoteUUID = () => {
    voteTid.value = crypto.randomUUID()
    voteVerifiedData.value = []
    voteFailed.value = false
    voteQrCode.value = ''
}

const startVoteVerification = async () => {
    try {
        const qrRes = await axios.get(`https://api.xiaozhi.moe/chihlee/vote-verify`, {
            params: { transaction_id: voteTid.value }
        })
        voteQrCode.value = qrRes.data.qrcode_image
        voteAuthUri.value = qrRes.data.auth_uri

        voteInterval = setInterval(fetchVoteResult, 5000)
        voteTimeout = setTimeout(() => {
            clearInterval(voteInterval)
            voteFailed.value = true
        }, 60000)
    } catch (error) {
        console.error('第一階段驗證失敗', error)
        voteFailed.value = true
    }
}

const fetchVoteResult = async () => {
    try {
        const resultRes = await axios.get(`https://api.xiaozhi.moe/chihlee/vote-verify-result`, {
            params: { transaction_id: voteTid.value }
        })
        if (resultRes.data.verify_result) {
            voteVerifiedData.value = resultRes.data.data[0]?.claims || []
            clearInterval(voteInterval)
            clearTimeout(voteTimeout)
        }
    } catch (e) {
        console.warn('查詢中...', e)
        if (e.response?.status === 403) voteFailed.value = true
    }
}

const startSecondPhase = async () => {
    secondPhaseTid.value = crypto.randomUUID()
    try {
        const qrRes = await axios.get(`https://api.xiaozhi.moe/chihlee/vote-qr`, {
            params: { transaction_id: secondPhaseTid.value }
        })
        secondPhaseQrCode.value = qrRes.data.qrcode_image
        secondPhaseAuthUri.value = qrRes.data.auth_uri

        secondPhaseInterval = setInterval(fetchSecondPhaseResult, 5000)
        secondPhaseTimeout = setTimeout(() => {
            clearInterval(secondPhaseInterval)
        }, 60000)
    } catch (error) {
        console.error('第二階段驗證失敗', error)
        alert('投票 QR 產生失敗')
    }
}

const fetchSecondPhaseResult = async () => {
    try {
        const resultRes = await axios.get(`https://api.xiaozhi.moe/chihlee/vote-qr-result`, {
            params: { transaction_id: secondPhaseTid.value }
        })
        if (resultRes.data.verify_result) {
            clearInterval(secondPhaseInterval)
            clearTimeout(secondPhaseTimeout)

            const claims = resultRes.data.data?.[0]?.claims || []
            const schoolClaim = claims.find(claim => claim.ename === 'school_cn')
            votedSchool.value = schoolClaim?.value || '未知學校'
        }
    } catch (e) {
        console.warn('查詢投票驗證中...')
    }
}

const submitVote = async () => {
    if (!selectedOption.value || !votedSchool.value || !secondPhaseTid.value) {
        alert('請完成匿名驗證並選擇選項')
        return
    }
    try {
        await axios.post('https://api.xiaozhi.moe/chihlee/submit-vote', {
            transaction_id: secondPhaseTid.value,
            school: votedSchool.value,
            option: selectedOption.value
        })
        alert(`🎉 投票成功！您選擇了「${selectedOption.value}」`)
    } catch (err) {
        console.error('提交投票失敗', err)
        alert('提交投票失敗，請稍後重試')
    }
}

onMounted(() => {
    generateVoteUUID()
    startVoteVerification()
})
</script>
