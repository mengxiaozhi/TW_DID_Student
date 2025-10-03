import { createRouter, createWebHistory } from 'vue-router'
import { applySeo, defaultSeo } from '../utils/seo'

const routes = [
    {
        name: '首頁',
        path: '/',
        component: () => import('../pages/index.vue'),
        meta: {
            seo: {
                title: '數位學生證平台｜生成、驗證與導入',
                description: '以 DID 技術打造的數位學生證入口，支援信箱驗證、QR Code 導入與即時驗證流程，五分鐘內完成卡證建立。',
                keywords: '數位學生證,學生證生成,DID 驗證,QRCode 數位皮夾,校園身份'
            }
        }
    },
    {
        name: '投票',
        path: '/vote',
        component: () => import('../pages/vote.vue'),
        meta: {
            seo: {
                title: '校園投票驗證｜數位學生證 DID 投票流程',
                description: '透過雙階段 DID 驗證保障校園投票公平性，支援匿名投票、票權確認與實名查驗。',
                keywords: '校園投票,DID 驗證,匿名投票,學生自治,投票 QR Code'
            }
        }
    },
    {
        name: '留言板',
        path: '/broad/:id?',
        component: () => import('../pages/broad.vue'),
        meta: {
            seo: {
                title: '匿名留言板｜驗證後的校園交流空間',
                description: '使用數位學生證完成身份驗證後留言與互動，結合 DID 保護匿名與可靠性，同時支援貼文分享。',
                keywords: '匿名留言板,校園交流,學生驗證,DID 留言,匿名社群'
            }
        }
    },
    {
        name: '確認電子郵件',
        path: '/confirm',
        component: () => import('../pages/confirm.vue'),
        meta: {
            seo: {
                title: '信箱驗證結果｜數位學生證平台',
                description: '確認學校信箱驗證結果，完成學生身份綁定並啟用數位學生證功能。',
                keywords: '信箱驗證,學生信箱,驗證結果,數位學生證'
            }
        }
    },
    {
        name: '關於',
        path: '/about',
        component: () => import('../pages/about.vue'),
        meta: {
            seo: {
                title: '關於專案｜台灣 DID 數位學生證實驗',
                description: '了解開發背景、核心功能與技術堆疊，探索 DID 在教育場域的可能性與專案願景。',
                keywords: '關於,專案介紹,DID 教育,數位學生證'
            }
        }
    },
    {
        name: '使用條款',
        path: '/terms',
        component: () => import('../pages/terms.vue'),
        meta: {
            seo: {
                title: '使用條款｜數位學生證服務政策',
                description: '了解數位學生證服務的使用條款與責任限制，保障使用者與開發者雙方權益。',
                keywords: '使用條款,服務條款,法律聲明,數位學生證'
            }
        }
    },
    {
        name: '隱私政策',
        path: '/privacy',
        component: () => import('../pages/privacy.vue'),
        meta: {
            seo: {
                title: '隱私政策｜使用者資料與安全承諾',
                description: '詳述數位學生證平台的資料使用範圍、保存期限與安全措施，保障個人隱私。',
                keywords: '隱私政策,資料保護,個資,資訊安全'
            }
        }
    },
    {
        name: 'NotFound',
        path: '/404',
        component: () => import('../pages/404.vue'),
        meta: {
            seo: {
                title: '找不到頁面｜數位學生證平台',
                description: '您瀏覽的頁面不存在，請返回首頁或透過導覽列探索其他功能。',
                keywords: '404,找不到頁面,頁面不存在'
            }
        }
    },
    { path: '/:pathMatch(.*)*', redirect: '/404' }
]

const router = createRouter({
    scrollBehavior(to, from, savedPosition) {
        // 始终滚动到顶部
        return { top: 0 }
    },
    history: createWebHistory(),
    routes,//路由表
    mode: 'history' // history 改为 hash
})

router.afterEach((to) => {
    const seoConfig = {
        ...defaultSeo,
        ...(to.meta?.seo || {})
    }
    applySeo(seoConfig)
})

export default router
