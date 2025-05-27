<!-- src/views/MainView.vue -->
<template>
  <div class="container py-4 wrap">
    <!-- Hero Match & Test 박스 (기존) -->
    <div
      class="d-flex align-items-center justify-content-between p-4 mb-4 rounded shadow-sm"
      style="background-color: #9F71C3;"
    >
      <div class="d-flex align-items-center">
        <span class="fs-2 me-2">🎬</span>
        <h2 class="m-0" style="color:#fff;">Movie Match Test</h2>
      </div>
  <router-link
    class="btn"
    style="background-color: #924EBF; color: #fff; text-decoration:none;"
    :to="{ name: 'HeroTestView' }"
  >
    TEST 하기
  </router-link>
    </div>

    <!-- Top 10 Trending Movies -->
    <div
      class="section-box rounded mb-4"
    >
      <h3 class="mb-3" style="color: white;">🔥Top 10</h3>

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
      <h3 style="color: white;">📂 Categories</h3>
      <div class="row g-3">
       <div v-for="g in GENRES" :key="g.id" class="col-6 col-md-3">
         <CategoryCard
           :label="g.label"
           :id="g.id"
           :posterPath="genrePosters[g.id]"
         />
       </div>
      </div>
    </section>
    <section class="mt-5">
      <h3 style="color: white;">🎮 Mini Games</h3>
      <MiniGamesHub />
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import MovieCarousel from '@/components/MovieCarousel.vue'
import { fetchTrending, GENRES, fetchMoviesByGenre } from '@/api/movie'
import CategoryCard from '@/components/CategoryCard.vue'
import MiniGamesHub from '@/components/MiniGamesHub.vue'


const trending = ref([])
const isLoadingTrending = ref(false)
// { [genreId]: poster_path }
const genrePosters = ref({})




onMounted(async () => {
  isLoadingTrending.value = true
  trending.value = await fetchTrending()
  isLoadingTrending.value = false
   // 장르별 첫 영화 한 편만 가져와서 posterPath 세팅
  await Promise.all(
    GENRES.map(async g => {
      const movies = await fetchMoviesByGenre(g.id, 1)
      if (movies.length) {
        const pick = movies[Math.floor(Math.random() * movies.length)]
        genrePosters.value[g.id] = pick.poster_path || ''
      } else {
        genrePosters.value[g.id] = ''
      }
    })
  )
})
</script>

<style scoped>
.main-wrap {
  /* 화면 전체 높이에서 navbar(56px)랑 상단 여백(…)을 뺀 최소 높이 */
  min-height: calc(100vh - 56px);
  /* 필요하면 상단/하단 패딩 조정 */
  padding-bottom: 2rem;
}

</style>
