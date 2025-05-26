<!-- src/views/MainView.vue -->
<template>
  <div class="main-view">
    <HeroMatch/>
    <TopTenCarousel/>

    <section class="categories-card">
      <h2>Categories</h2>
      <div class="categories-list">
        <CategoryCard
          v-for="g in genres"
          :key="g.id"
          :genre="g"
        />
      </div>
    </section>
  </div>
</template>

<script setup>
import HeroMatch      from '@/components/HeroMatch.vue'
import TopTenCarousel from '@/components/TopTenCarousel.vue'
import CategoryCard   from '@/components/CategoryCard.vue'
import { GENRES }     from '@/api/movie'

const genres = GENRES
</script>

<style scoped>
.main-view { padding: 2rem 0; background: #f5f5f5; }

.categories-card {
  background: #fff;
  margin: 2rem auto;
  padding: 1.5rem;
  border-radius: 8px;
  max-width: 1200px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.categories-card h2 { margin-bottom: 1rem; }
.categories-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}
</style>
