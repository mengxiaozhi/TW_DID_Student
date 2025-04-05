<script setup>
  import headerVue from './components/header.vue'
  import { useRouter } from 'vue-router'

</script>
<template>
  <headerVue />
  <router-view></router-view>
</template>