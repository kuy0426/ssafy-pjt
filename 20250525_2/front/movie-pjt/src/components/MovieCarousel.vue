<!-- src/components/MovieCarousel.vue -->
<template>
  <div class="d-flex gap-3 overflow-auto pb-2">
    <router-link
      v-for="movie in movies"
      :key="movie.id"
      :to="`/detail/${movie.id}`"
      class="d-block"
    >
      <div class="card" style="min-width:110px;">
        <img
          v-if="movie.poster_path"
          :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`"
          :alt="movie.original_title"
          class="card-img-top"
          style="height:165px;object-fit:cover;"
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
</style>
