<template>
  <div id="app" class="theme-dark">
    <NavigationBar v-if="showNav"/>
    <main class="container">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
  import { computed } from 'vue'
  import { RouterView, useRoute } from 'vue-router'
  import NavigationBar from '@/components/NavigationBar.vue'

  const route = useRoute()

  const showNav = computed(() => {
    return !['LogInView', 'SignUpView'].includes(route.name)
  })

</script>

<style scoped>
  main {
    height: auto;
    margin: 0 auto;
    padding: 2rem 1rem;
  } 
</style>

<style>
  .theme-dark {
    min-height: 100vh;
    /* background-color: #262726; */
    /* background-color: #000000; */
    /* background: #1e1c1c;
    color: #E0E0E0; */
     min-height: 100vh;
  background: linear-gradient(to bottom, #1a1a1a, #3C2A4D);

  }
  /* 버튼·카드 같은 공통 스타일도 여기로 옮기세요 */
  .theme-dark .btn-test {
    background-color: #E50914;
    color: #fff;
  }
  
</style>