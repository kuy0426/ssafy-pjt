<!-- src/views/DetailView.vue -->
<template>
  <div class="container py-5">
    <h1 class="mb-4 text-center" style="color: white;">Movie Detail</h1>

    <!-- 로딩 스피너 -->
    <div v-if="loading" class="text-center py-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <!-- 영화 데이터 준비되었을 때 -->
    <div v-else-if="movie" class="row justify-content-center align-items-start">
      <!-- 포스터 -->
      <div class="col-md-5 text-center mb-4">
        <img
          v-if="movie.poster_path"
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
          alt="Poster"
          class="img-fluid rounded shadow poster-img"
        />
      </div>

      <!-- 정보 -->
      <div class="col-md-7">
        <div class="mb-3">
          <label class="form-label fw-bold" style="color: white;">🎬 TITLE</label>
          <input class="form-control" :value="movie.original_title" readonly>
        </div>
        <div class="mb-3">
          <label class="form-label fw-bold" style="color: white;">⭐ Rating</label>
          <input class="form-control" :value="movie.vote_average" readonly>
        </div>
        <div class="mb-4">
          <label class="form-label fw-bold" style="color: white;">📝 DESCRIPTION</label>
          <textarea class="form-control" rows="5" readonly>{{ movie.overview }}</textarea>
        </div>
        <div class="mb-4">
          <label class="form-label fw-bold" style="color: white;">🧑 ACTORS</label>
          <div class="d-flex gap-3 overflow-auto actor-list">
            <div
              v-for="(c, i) in movie.cast.slice(0, 5)"
              :key="i"
              class="text-center"
              style="min-width: 100px"
            >
              <img
                v-if="c.profile_path"
                :src="`https://image.tmdb.org/t/p/w185${c.profile_path}`"
                alt="Actor"
                class="img-fluid rounded shadow-sm mb-1 actor-img"
              />
              <div class="small" style="color: white;">{{ c.name }}</div>
            </div>
          </div>
        </div>

        <!-- 버튼 -->
        <div class="text-center mt-4">
          <button class="btn btn-lg btn-primary px-5 py-2 fw-bold" @click="goHome">
            Home
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

// function openTrailer() {
//   alert('예고편 기능은 다음 업데이트에서!')
// }
</script>

<style scoped>
label.form-label {
  font-weight: 600;
}
textarea.form-control[readonly] {
  background-color: #fafafa;
}
.poster-img {
  max-height: 650px;
  object-fit: cover;
}

.actor-img {
  height: 120px;
  width: 90px;
  object-fit: cover;
  border-radius: 8px;
}

textarea.form-control[readonly] {
  background-color: #fafafa;
}

.btn-primary {
  background-color: #800080;
  border-color: #800080;
}
.btn-primary:hover {
  background-color: #5e006e;
  border-color: #5e006e;
}

.poster-img {
  max-height: 650px;
  object-fit: cover;
}
.actor-img {
  height: 120px;
  width: 90px;
  object-fit: cover;
  border-radius: 8px;
}
textarea.form-control[readonly] {
  background-color: #fafafa;
}
.btn-primary {
  background-color: #aaa7aa2f;
  border-color: #aaa7aa2f;
}
.btn-primary:hover {
  background-color: #555555;
  border-color: #555555;
}

.actor-list {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;

  scrollbar-width: thin;
  scrollbar-color: #46434b transparent;
}

.actor-list::-webkit-scrollbar {
  height: 8px;
}

.actor-list::-webkit-scrollbar-track {
  background: transparent;
}

.actor-list::-webkit-scrollbar-thumb {
  background: #a883f5;
  border-radius: 4px;
}

</style>