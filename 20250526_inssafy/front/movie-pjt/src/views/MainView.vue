<!-- src/views/MainView.vue -->
<template>
  <div class="container py-4 wrap">
    <!-- Hero Match & Test 박스 (기존) -->
    <div
      class="d-flex align-items-center justify-content-between p-4 mb-4 rounded shadow-sm"
      style="background-color: #E6E6FA;"
    >
      <div class="d-flex align-items-center">
        <span class="fs-2 me-2">🎬</span>
        <h2 class="m-0" style="color: #4B0082;">Hero Match Test</h2>
      </div>
      <router-link
        class="btn"
        style="background-color: #800080; color: #fff; text-decoration:none;"
        :to="{ name: 'HeroTestView' }"
      >
        TEST 하기
      </router-link>
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

    <!-- Categories (기존 코드 그대로) -->
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

    <!-- ─────────── 여기부터 미니게임 섹션 ─────────── -->
    <section class="mt-5">
      <h3>🎮 Mini Games</h3>
      <MiniGamesHub />
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import MovieCarousel from '@/components/MovieCarousel.vue'
import { fetchTrending, GENRES } from '@/api/movie'

// ➊ 방금 만든 미니게임 허브 컴포넌트
import MiniGamesHub from '@/components/MiniGamesHub.vue'

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
.main-wrap {
  /* 화면 전체 높이에서 navbar(56px)랑 상단 여백(…)을 뺀 최소 높이 */
  min-height: calc(100vh - 56px);
  padding-bottom: 2rem;
}
</style>
