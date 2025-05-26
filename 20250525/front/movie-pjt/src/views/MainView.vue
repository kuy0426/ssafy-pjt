<!-- src/views/MainView.vue -->
<template>
  <div class="container py-4">
    <!-- Hero Match & Test 박스 (기존) -->
    <div
      class="d-flex align-items-center justify-content-between p-4 mb-4 rounded shadow-sm"
      style="background-color: #E6E6FA;"
    >
      <div class="d-flex align-items-center">
        <span class="fs-2 me-2">🎬</span>
        <h2 class="m-0" style="color: #4B0082;">Hero Match Test</h2>
      </div>
      <button class="btn" style="background-color: #800080; color: #fff;">
        TEST 하기
      </button>
    </div>

    <!-- Top 10 Trending Movies -->
    <div
      class="section-box p-4 rounded mb-4"
      style="background-color: #e9ecef;"
    >
      <h3 class="mb-3">🔥 Top 10 Trending Movies</h3>

      <!-- 스피너 -->
      <div v-if="isLoadingTrending" class="text-center py-5">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>

      <!-- 데이터 준비되면 캐러셀 -->
      <MovieCarousel v-else :movies="trending" />
    </div>

    <!-- Categories (생략: 기존 코드 그대로) -->
    <section>
      <h3>📂 Categories</h3>
      <div class="row g-3">
        <div
          v-for="g in GENRES"
          :key="g.id"
          class="col-6 col-md-3"
        >
          <router-link
            class="text-decoration-none"
            :to="{ name: 'GenreView', params: { id: g.id } }"
          >
            <div
              class="p-4 rounded text-center text-white h-100"
              style="background-color: #6c757d;"
            >
              {{ g.label }}
            </div>
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import MovieCarousel from '@/components/MovieCarousel.vue'
import { fetchTrending, GENRES } from '@/api/movie'

const trending = ref([])
const isLoadingTrending = ref(false)

onMounted(async () => {
  isLoadingTrending.value = true
  trending.value = await fetchTrending()
  isLoadingTrending.value = false
})
</script>

<style scoped>
.section-box { }
</style>
