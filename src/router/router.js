import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    { name: '首頁', path: '/', meta: { title: '示例页面' }, component: () => import('../pages/index.vue') },
    { name: '確認電子郵件', path: '/confirm', component: () => import('../pages/confirm.vue') },
    { name: '關於', path: '/about', component: () => import('../pages/about.vue') },
    { name: 'NotFound', path: '/404', component: () => import('../pages/404.vue') },
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
export default router