<!-- src/components/HeroMatch.vue -->
<template>
  <div class="hero-match card mx-auto my-4 p-4">
    <h2>🎬 Hero Match Test</h2>
    <button class="btn btn-primary" @click="startTest">테스트 시작</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchHeroMatch } from '@/api/movie'
import { useRouter }      from 'vue-router'

const movie = ref(null)
const router = useRouter()

onMounted(async () => {
  movie.value = await fetchHeroMatch()
})

function startTest() {
  router.push({ name: 'HeroMatchTest' })
}
</script>

<style scoped>
.hero-match {
  max-width: 600px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  text-align: center;
}
</style>
