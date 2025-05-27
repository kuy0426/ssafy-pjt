<!-- src/components/MovieCarousel.vue -->
<template>
  <div
    class="d-flex gap-3 overflow-auto pb-2 carousel-scroll"
  >
    <router-link
      v-for="movie in movies"
      :key="movie.id"
      :to="{ name: 'MovieDetailView', params: { id: movie.id } }"
      class="d-block"
    >
      <div class="card" style="min-width:110px;">
        <img
          v-if="movie.poster_path"
          :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`"
          :alt="movie.original_title"
          class="card-img-top"
          style="min-width:300px; height:400px; object-fit:cover;"
        />
      </div>
    </router-link>
  </div>
</template>

<script setup>
defineProps({
  movies: {
    type: Array,
    required: true,
  },
});
</script>

<style scoped>
.d-flex { display: flex; }
.gap-3 { gap: .75rem; }
.overflow-auto { overflow-x: auto; }
.pb-2 { padding-bottom: .5rem; }

.card {
  border-radius: 6px;
  overflow: hidden;
  transition: transform .2s;
}
.card:hover { transform: scale(1.05); }
.card-img-top { width:100%; height:165px; object-fit:cover; }

/* ──────────────── 스크롤바 커스터마이징 ──────────────── */

/* Firefox */
.carousel-scroll {
  scrollbar-width: thin;
  scrollbar-color: #555 #333;  /* thumb 색, track 색 */
}

/* Webkit (Chrome, Safari) */
.carousel-scroll::-webkit-scrollbar {
  height: 6px;           /* 스크롤바 두께 */
}
.carousel-scroll::-webkit-scrollbar-track {
  background: #333;      /* 트랙 배경색 (짙은 검은색) */
}
.carousel-scroll::-webkit-scrollbar-thumb {
  background: #555;      /* thumb 색 (약간 연한 회색) */
  border-radius: 3px;    /* 둥근 모서리 */
}

/* 호버 시 색 진하게 */
.carousel-scroll::-webkit-scrollbar-thumb:hover {
  background: #777;
}
</style>
