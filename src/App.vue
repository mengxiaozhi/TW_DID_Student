<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-slate-50 to-slate-100">
    <!-- Header -->
    <header class="w-full bg-white shadow-sm py-5 px-4 md:px-8 border-b border-slate-200">
      <div class="max-w-5xl mx-auto flex flex-col md:flex-row md:justify-between items-center space-y-3 md:space-y-0">
        <a href="/" class="text-lg md:text-xl font-bold text-slate-800 text-center flex items-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2 text-blue-600" fill="none" viewBox="0 0 24 24"
            stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-3 3h6a3.001 3.001 0 00-3-3z" />
          </svg>
          <span>數位憑證皮夾｜致理科技大學數位學生證</span>
        </a>
        <nav class="flex justify-center md:justify-end space-x-6 text-sm">
          <a href="https://github.com/your-repo-url" target="_blank"
            class="text-slate-600 hover:text-blue-600 transition flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="currentColor" viewBox="0 0 24 24">
              <path
                d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
            </svg>
            GitHub
          </a>
          <a href="https://youtu.be/9Jn47KhUwtc" target="_blank"
            class="text-slate-600 hover:text-blue-600 transition flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="currentColor" viewBox="0 0 24 24">
              <path
                d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z" />
            </svg>
            演示影片
          </a>
        </nav>
      </div>
    </header>

    <!-- Main Content -->
    <main class="py-8 px-4 md:px-8">
      <div
        class="max-w-2xl mx-auto bg-white shadow-lg rounded-xl p-8 space-y-8 border border-slate-200 transition-all duration-300 hover:shadow-xl">
        <div class="flex justify-center space-x-4">
          <button
            class="px-6 py-2.5 rounded-full text-sm font-medium transition duration-200 ease-in-out hover:scale-[1.02] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            :class="activeTab === 'generate' ? 'bg-blue-500 text-white shadow-md' : 'bg-slate-100 text-slate-700 hover:bg-slate-200'"
            @click="activeTab = 'generate'">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1.5" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
            生成學生證
          </button>
          <button
            class="px-6 py-2.5 rounded-full text-sm font-medium transition duration-200 ease-in-out hover:scale-[1.02] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500"
            :class="activeTab === 'verify' ? 'bg-emerald-500 text-white shadow-md' : 'bg-slate-100 text-slate-700 hover:bg-slate-200'"
            @click="activeTab = 'verify'; generateUUID()">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1.5" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
            驗證學生證
          </button>
        </div>

        <!-- 信箱驗證區塊 -->
        <div v-if="activeTab === 'generate'" class="transition-all">
          <form @submit.prevent="sendVerificationEmail" class="space-y-5">
            <div>
              <label class="block mb-1.5 text-sm font-medium text-slate-700">學校信箱</label>
              <div class="relative">
                <input v-model="email" type="email"
                  class="w-full pl-10 border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
                  required placeholder="@gm.chihlee.edu.tw" />
              </div>
              <p class="mt-1 text-xs text-slate-500">僅限 @gm.chihlee.edu.tw 或 @mail.chihlee.edu.tw</p>
            </div>
            <button v-if="!emailSent" type="submit"
              class="w-full py-3 bg-blue-500 hover:bg-blue-600 text-white font-medium rounded-lg hover:shadow-md transition duration-200 ease-in-out flex justify-center items-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1.5" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              寄送驗證信
            </button>
            <div v-if="verifyPending && !verified" class="flex items-center justify-center py-2 text-sm text-slate-500">
              <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-blue-500" xmlns="http://www.w3.org/2000/svg" fill="none"
                viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                </path>
              </svg>
              正在等待驗證中...
            </div>
            <div v-if="verified && !cardGenerated"
              class="bg-emerald-50 border border-emerald-200 p-3 rounded-lg text-sm text-emerald-700 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1.5 text-emerald-500" fill="none"
                viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              驗證成功，您現在可以填寫表單
            </div>
          </form>

          <!-- 生成學生證頁面 -->
          <form v-if="verified && !cardGenerated" @submit.prevent="generateCard" class="space-y-5 pt-6">
            <div>
              <label class="block mb-1.5 text-sm font-medium text-slate-700">姓名</label>
              <input v-model="form.name"
                class="w-full border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
                required pattern="^[\u4e00-\u9fa5_a-zA-Z0-9]+$" />
            </div>

            <div>
              <label class="block mb-1.5 text-sm font-medium text-slate-700">科系（中文）</label>
              <input v-model="form.department_chinese"
                class="w-full border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
                required pattern="^[^~!@#$%^&*()_\-+*/]+$" />
            </div>

            <div>
              <label class="block mb-1.5 text-sm font-medium text-slate-700">Department（英文）</label>
              <input v-model="form.department_english"
                class="w-full border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
                required pattern="^[^~!@#$%^&*()_\-+*/]+$" />
            </div>

            <div>
              <label class="block mb-1.5 text-sm font-medium text-slate-700">學號</label>
              <div class="relative">
                <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14" />
                  </svg>
                </div>
                <input v-model="form.student_number"
                  class="w-full pl-10 border border-slate-300 p-3 rounded-lg bg-slate-50 text-slate-500" readonly />
              </div>
            </div>

            <div class="flex space-x-4">
              <div class="w-1/2">
                <label class="block mb-1.5 text-sm font-medium text-slate-700">註冊日期（開始）</label>
                <div class="relative">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400" fill="none"
                      viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <input v-model="form.registration_date_start" maxlength="8"
                    class="w-full pl-10 border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
                    required pattern="^\d{8}$" placeholder="YYYYMMDD" />
                </div>
              </div>
              <div class="w-1/2">
                <label class="block mb-1.5 text-sm font-medium text-slate-700">註冊日期（結束）</label>
                <div class="relative">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400" fill="none"
                      viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <input v-model="form.registration_date_end" maxlength="8"
                    class="w-full pl-10 border border-slate-300 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
                    required pattern="^\d{8}$" placeholder="YYYYMMDD" />
                </div>
              </div>
            </div>

            <button type="submit"
              class="w-full py-3 bg-blue-500 hover:bg-blue-600 text-white font-medium rounded-lg hover:shadow-md transition duration-200 ease-in-out flex justify-center items-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1.5" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              生成數位學生證
            </button>
          </form>

          <div v-if="qrCode" class="mt-8 text-center">
            <h2 class="text-lg font-medium mb-4 text-slate-800">掃描 QR Code 領取數位學生證：</h2>
            <div class="bg-slate-50 p-6 rounded-xl inline-block">
              <img :src="qrCode" alt="QRCode"
                class="mx-auto w-48 h-48 rounded-lg shadow-md hover:shadow-lg transition-transform duration-300 hover:scale-105" />
            </div>
            <p class="mt-4 text-sm text-slate-500">請使用數位憑證皮夾 App 掃描此 QR Code</p>
          </div>
        </div>

        <!-- 驗證頁面 -->
        <div v-else class="transition-all">
          <template v-if="verifiedData.length">
            <div class="mt-6 space-y-4">
              <div class="flex items-center justify-center mb-4">
                <div class="bg-emerald-100 p-2 rounded-full">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-emerald-500" fill="none"
                    viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                  </svg>
                </div>
              </div>
              <h2 class="text-xl font-medium text-center text-slate-800">驗證成功，個人資料如下：</h2>
              <div class="bg-slate-50 rounded-xl p-4 mt-4">
                <div v-for="item in verifiedData" :key="item.ename"
                  class="border-b border-slate-200 last:border-b-0 py-3 flex justify-between">
                  <span class="font-medium text-slate-700">{{ item.cname }}：</span>
                  <span class="text-slate-900">{{ item.value }}</span>
                </div>
              </div>
            </div>
            <div class="pt-6">
              <button @click="generateUUID"
                class="w-full py-3 bg-blue-500 hover:bg-blue-600 text-white font-medium rounded-lg hover:shadow-md transition duration-200 ease-in-out flex justify-center items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1.5" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                重新驗證
              </button>
            </div>
          </template>

          <template v-else>
            <form @submit.prevent="verifyCard" class="space-y-5">
              <div>
                <label class="block mb-1.5 text-sm font-medium text-slate-700">Transaction ID</label>
                <div class="relative">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-400" fill="none"
                      viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" />
                    </svg>
                  </div>
                  <input v-model="verifyTid"
                    class="w-full pl-10 border border-slate-300 p-3 rounded-lg bg-slate-50 text-slate-500 font-mono tracking-wide"
                    readonly />
                </div>
                <p class="mt-1 text-xs text-slate-500">這是您的唯一驗證碼，用於確認驗證請求</p>
              </div>
            </form>

            <div v-if="verifyQrCode" class="mt-8 text-center">
              <h2 class="text-lg font-medium mb-4 text-slate-800">請用錢包 App 掃描以下 QR Code 驗證身份</h2>
              <div class="bg-slate-50 p-6 rounded-xl inline-block">
                <img :src="verifyQrCode" alt="VerifyQRCode"
                  class="mx-auto w-48 h-48 rounded-lg shadow-md hover:shadow-lg transition-transform duration-300 hover:scale-105" />
              </div>
              <p class="mt-4 text-sm text-slate-500">請在 60 秒內完成掃描</p>
              <div class="mt-4 flex items-center justify-center">
                <div class="animate-spin rounded-full h-5 w-5 border-b-2 border-blue-500"></div>
                <span class="ml-3 text-sm text-slate-500">等待驗證中...</span>
              </div>
            </div>

            <div v-if="verifyFailed" class="mt-6 text-center p-4 bg-red-50 rounded-lg border border-red-200">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mx-auto text-red-500 mb-2" fill="none"
                viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <p class="text-red-600 font-medium">驗證超時，請重新驗證。</p>
              <button @click="generateUUID(); verifyCard()"
                class="mt-3 px-4 py-2 bg-red-100 hover:bg-red-200 text-red-600 font-medium rounded-lg transition duration-200 ease-in-out text-sm">
                重新開始
              </button>
            </div>
          </template>
        </div>
      </div>
    </main>
    <main>
      <div class="max-w-2xl mx-auto bg-white shadow-md rounded-xl p-6 border border-slate-200 text-sm text-slate-600">
        <h1 class="font-semibold text-slate-700">說明</h1>
        <p class="mt-2 text-blue-500 underline"><a
            href="https://play.google.com/apps/testing/tw.gov.moda.diw">安卓測試下載</a><br><a
            href="https://testflight.apple.com/join/gxr3mQFj">IOS測試下載</a></p>
        <p class="mt-2">本項目基於「數位發展部」所開發「數位憑證皮夾」之沙盒測試開發而來，僅供學習及參考使用，非正式用途。</p>
        <p class="mt-2">希望有一天這項技術能普及吧，「數位憑證皮夾」基於 DID 可實現去中心化存儲個人資料實現個人資料自我託管。</p>
        <p class="mt-2">© Copyright <a href="https://xiaozhi.moe" class="underline text-blue-600">Mengxiaozhi 萌小志</a>
        </p>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import axios from 'axios'

const activeTab = ref('generate')
const qrCode = ref('')
const verifyQrCode = ref('')
const verifiedData = ref([])
const verifyTid = ref('')
const verifyFailed = ref(false)
const email = ref('')
const verifyPending = ref(false)
const verified = ref(false)
const emailSent = ref(false)
const cardGenerated = ref(false)

let verifyInterval = null
let verifyTimeout = null

const form = ref({
  name: '',
  department_chinese: '',
  department_english: '',
  student_number: '',
  registration_date_start: '',
  registration_date_end: ''
})

const generateUUID = () => {
  verifyTid.value = crypto.randomUUID()
  verifiedData.value = []
  verifyFailed.value = false
  verifyQrCode.value = ''
}

const generateCard = async () => {
  try {
    const response = await axios.post('https://api.xiaozhi.moe/chihlee/vc-item-data', {
      vcId: 238720,
      vcCid: 'chihlee_student_card',
      fields: [
        { type: 'BASIC', cname: '姓名', ename: 'name', content: form.value.name },
        { type: 'CUSTOM', cname: '科系', ename: 'department_chinese', content: form.value.department_chinese },
        { type: 'CUSTOM', cname: 'Department', ename: 'department_english', content: form.value.department_english },
        { type: 'CUSTOM', cname: '學號', ename: 'student_number', content: form.value.student_number },
        { type: 'CUSTOM', cname: '註冊日期_開始', ename: 'registration_date_start', content: form.value.registration_date_start },
        { type: 'CUSTOM', cname: '註冊日期_結束', ename: 'registration_date_end', content: form.value.registration_date_end },
      ]
    })
    qrCode.value = response.data.qrCode || ''
    cardGenerated.value = true
  } catch (error) {
    console.error('產生失敗', error)
    alert('學生證產生失敗，請確認資料格式是否正確')
  }
}

const verifyCard = async () => {
  try {
    const qrRes = await axios.get(`https://api.xiaozhi.moe/chihlee/verify-qr`, { params: { transaction_id: verifyTid.value } })
    verifyQrCode.value = qrRes.data.qrcode_image
    verifyFailed.value = false
    verifiedData.value = []

    verifyInterval = setInterval(fetchVerifyResult, 5000)
    verifyTimeout = setTimeout(() => {
      clearInterval(verifyInterval)
      verifyFailed.value = true
    }, 60000)
  } catch (error) {
    console.error('驗證失敗', error)
    alert('驗證 QR 產生失敗')
  }
}

const fetchVerifyResult = async () => {
  try {
    const resultRes = await axios.get(`https://api.xiaozhi.moe/chihlee/verify-result`, { params: { transaction_id: verifyTid.value } })
    if (resultRes.data.verify_result) {
      verifiedData.value = resultRes.data.data[0]?.claims || []
      clearInterval(verifyInterval)
      clearTimeout(verifyTimeout)
    }
  } catch (e) {
    console.warn('查詢中...')
  }
}

const sendVerificationEmail = async () => {
  try {
    const res = await axios.post('https://api.xiaozhi.moe/chihlee/verify-email', { email: email.value })
    if (res.data.success) {
      verifyPending.value = true
      emailSent.value = true
      pollVerificationStatus()
      alert(res.data.message)
    } else {
      alert(res.data.error || '驗證失敗')
    }
  } catch (err) {
    alert(err.response?.data?.error || '伺服器錯誤，請稍後再試')
  }
}

const pollVerificationStatus = () => {
  const checkTimer = setInterval(async () => {
    try {
      const res = await axios.get('https://api.xiaozhi.moe/chihlee/check-verification', { params: { email: email.value } })
      if (res.data.verified) {
        verified.value = true
        form.value.student_number = res.data.student_id
        clearInterval(checkTimer)
      }
    } catch (err) {
      console.warn('查詢驗證狀態失敗')
    }
  }, 3000)
}

watch(email, () => {
  emailSent.value = false
  verifyPending.value = false
  verified.value = false
})

watch(activeTab, async (newTab) => {
  if (newTab === 'verify') {
    generateUUID()
    await verifyCard()
  }
})

onMounted(() => {
  if (activeTab.value === 'verify') {
    generateUUID()
    verifyCard()
  }
})
</script>

<style>
  body {
    font-family: 'Segoe UI', 'Noto Sans TC', 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f5f7fa;
    color: #374151;
    line-height: 1.6;
  }

  h1,
  h2 {
    font-weight: bold;
    color: #1e40af;
  }

  input[type="email"],
  input[type="text"],
  input[type="number"] {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid #d1d5db;
    border-radius: 0.75rem;
    font-size: 1rem;
    background-color: #fff;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
  }

  input:focus {
    outline: none;
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
  }

  button {
    cursor: pointer;
    font-weight: 600;
    letter-spacing: 0.5px;
    transition: all 0.2s ease-in-out;
    padding: 0.75rem 1.25rem;
    border-radius: 0.75rem;
    font-size: 1rem;
  }

  button:hover {
    transform: scale(1.03);
  }

  button:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
  }

  label {
    font-size: 0.875rem;
    font-weight: 600;
    color: #4b5563;
    display: block;
    margin-bottom: 0.35rem;
  }

  main {
    padding: 1rem;
  }

  @media (min-width: 768px) {
    main {
      padding: 2rem;
    }
  }

  .form-card {
    background-color: #ffffff;
    border-radius: 1rem;
    padding: 2rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
    transition: box-shadow 0.3s ease;
  }

  .form-card:hover {
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
  }

  .transition-card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .transition-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.1);
  }

  .section-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #111827;
    margin-bottom: 1rem;
  }

  .highlight-box {
    background-color: #f3f4f6;
    border-radius: 0.75rem;
    padding: 1rem;
    font-size: 0.95rem;
    border: 1px solid #e5e7eb;
  }

  .qr-image {
    width: 10rem;
    height: 10rem;
    border-radius: 0.75rem;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .qr-image:hover {
    transform: scale(1.08);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  }

  /* 手機響應式調整 */
  @media (max-width: 640px) {
    h1 {
      font-size: 1.125rem;
    }

    input[type="email"],
    input[type="text"],
    input[type="number"] {
      font-size: 0.9rem;
      padding: 0.65rem 0.85rem;
    }

    button {
      padding: 0.65rem 1rem;
      font-size: 0.9rem;
    }

    .form-card,
    main>div {
      padding: 1.5rem;
    }

    .qr-image {
      width: 8rem;
      height: 8rem;
    }
  }
</style>
