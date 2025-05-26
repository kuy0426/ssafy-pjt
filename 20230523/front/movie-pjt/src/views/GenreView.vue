<!-- src/views/GenreView.vue -->
<template>
  <div class="container py-4 text-center">
    <h1>{{ genreLabel }} Movies</h1>
    <div class="d-flex overflow-auto gap-3 mt-4">
      <router-link
        v-for="m in movies"
        :key="m.id"
        :to="{ name: 'MovieDetail', params: { id: m.id } }"
      >
        <img
          :src="`https://image.tmdb.org/t/p/w300${m.poster_path}`"
          class="img-fluid rounded"
          style="width: 200px;"
          alt="poster"
        />
        <p>{{ m.title }}</p>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute }       from 'vue-router'
import axios               from 'axios'

const route = useRoute()
const movies = ref([])
const genreLabel = ref('')

onMounted(async () => {
  const id = route.params.id
  // GENRES에서 label 찾기
  const { GENRES } = await import('@/api/movie')
  const g = GENRES.find(x => x.id === +id)
  genreLabel.value = g?.label || 'Genre'

  const r = await axios.get(`${import.meta.env.VITE_API_BASE}/movies/`, {
    params: { genreId: id, page: 1 }
  })
  movies.value = r.data.results || []
})
</script>

<style scoped>
.container { max-width: 960px; }
img { margin-bottom: .5rem; }
</style>
