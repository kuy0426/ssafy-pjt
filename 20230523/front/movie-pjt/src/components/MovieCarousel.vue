<template>
  <div class="carousel">
    <div v-for="m in movies" :key="m.id" class="card">
      <img :src="posterUrl(m.poster_path)" />
    </div>
  </div>
</template>

<script setup>
defineProps({ movies:Array });
const posterUrl = p => `https://image.tmdb.org/t/p/w300${p}`;
</script>

<style scoped>
.carousel{display:flex;gap:.75rem;overflow-x:auto;padding-bottom:.5rem}
.card{min-width:110px;border-radius:6px;overflow:hidden;flex-shrink:0}
.card img{width:100%;height:165px;object-fit:cover}
</style>
