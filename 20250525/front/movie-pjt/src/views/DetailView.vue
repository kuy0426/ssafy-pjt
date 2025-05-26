<!-- src/views/DetailView.vue -->
<template>
  <div class="container py-5">
    <h1 class="mb-4 text-center">Movie Detail</h1>

    <!-- 로딩 스피너 -->
    <div v-if="loading" class="text-center py-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <!-- 영화 데이터 준비되었을 때 -->
    <div v-else-if="movie" class="row">
      <!-- 포스터 -->
      <div class="col-md-5 text-center mb-4">
        <img
          v-if="movie.poster_path"
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
          alt="Poster"
          class="img-fluid rounded shadow-sm"
        />
      </div>
      <!-- 정보 -->
      <div class="col-md-7">
        <div class="mb-3">
          <label class="form-label fw-bold">TITLE</label>
          <input class="form-control" :value="movie.original_title" readonly />
        </div>
        <div class="mb-3">
          <label class="form-label fw-bold">★ Rating</label>
          <input class="form-control" :value="movie.vote_average" readonly />
        </div>
        <div class="mb-4">
          <label class="form-label fw-bold">DESCRIPTION</label>
          <textarea
            class="form-control"
            rows="4"
            :value="movie.overview"
            readonly
          />
        </div>
        <div class="mb-4">
          <label class="form-label fw-bold">ACTORS</label>
          <div class="d-flex gap-3 overflow-auto">
            <div
              v-for="(c, i) in movie.cast.slice(0,5)"
              :key="i"
              class="text-center"
              style="min-width:80px"
            >
              <img
                v-if="c.profile_path"
                :src="`https://image.tmdb.org/t/p/w185${c.profile_path}`"
                alt="Actor"
                class="img-fluid rounded shadow-sm mb-1"
              />
              <div class="small">{{ c.name }}</div>
            </div>
          </div>
        </div>
        <!-- 버튼들 -->
        <div class="d-flex gap-2">
          <button class="btn btn-secondary" @click="goHome">
            Home
          </button>
          <button class="btn btn-secondary" @click="openTrailer">
            예고편 보기
          </button>
        </div>
      </div>
    </div>

    <!-- 영화 없음 -->
    <div v-else class="text-center text-danger">
      Movie not found.
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { fetchMovieDetail } from '@/api/movie'

const route  = useRoute()
const router = useRouter()
const movieId = route.params.id

const movie   = ref(null)
const loading = ref(true)

onMounted(async () => {
  if (!movieId) {
    loading.value = false
    return
  }
  movie.value = await fetchMovieDetail(movieId)
  loading.value = false
})

function goHome() {
  router.push({ name: 'MainView' })
}

function openTrailer() {
  alert('예고편 기능은 다음 업데이트에서!')
}
</script>

<style scoped>
label.form-label {
  font-weight: 600;
}
textarea.form-control[readonly] {
  background-color: #fafafa;
}
</style>
