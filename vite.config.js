import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'
import Sitemap from 'vite-plugin-sitemap'

const dynamicRoutes = [
  '/',
  '/vote',
  '/broad',
  '/confirm',
  '/about',
  '/terms',
  '/privacy',
  '/404'
]

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), tailwindcss(), Sitemap({ hostname: 'https://did-edu.xiaozhi.moe', dynamicRoutes, }),],
})
