<template>
  <NavigationBar v-if="showNav"/>
  <main class="container">
    <RouterView />
  </main>
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
    max-width: 80%;
    height: auto;
    margin: 0 auto;
    padding: 2rem 1rem;
  }
</style>