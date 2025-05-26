<!-- src/components/TopTenCarousel.vue -->
<template>
  <div class="top-ten">
    <h2>🔥 Top 10 Trending Movies</h2>
    <div class="movie-list">
      <router-link
        v-for="m in movies"
        :key="m.id"
        :to="{ name: 'MovieDetail', params: { id: m.id } }"
        class="movie-item"
      >
        <img :src="m.poster" :alt="m.title" />
        <p class="title">{{ m.title }}</p>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchTopTen }   from '@/api/movie'

const movies = ref([])

onMounted(() => {
  fetchTopTen().then(list => { movies.value = list })
})
</script>

<style scoped>
.top-ten {
  background: #fff;
  padding: 1.5rem;
  margin: 2rem auto;
  border-radius: 8px;
  max-width: 1200px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.movie-list {
  display: flex;
  overflow-x: auto;
  gap: 1rem;
  padding-bottom: .5rem;
}
.movie-item {
  flex: 0 0 auto;
  width: 120px;
  text-align: center;
  color: inherit;
  text-decoration: none;
}
.movie-item img {
  width: 100%;
  border-radius: 4px;
}
.title {
  margin-top: .5rem;
  font-size: .9rem;
}
</style>
