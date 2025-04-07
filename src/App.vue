<script setup>
  import headerVue from './components/header.vue'
  import banner from './components/banner.vue';
  import { useRouter } from 'vue-router'
</script>

<template>
  <headerVue />
  <banner />
  <router-view></router-view>
</template>