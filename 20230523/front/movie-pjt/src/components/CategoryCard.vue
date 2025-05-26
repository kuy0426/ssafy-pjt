<!-- src/components/CategoryCard.vue -->
<template>
  <div class="category-card">
    <router-link :to="{ name: 'GenreView', params: { id: genre.id }}">
      <img :src="thumbUrl || placeholder" class="thumb" alt="장르 썸네일" />
      <div class="label">{{ genre.label }}</div>
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchGenreThumb } from '@/api/movie'


const props = defineProps({
  genre: { type: Object, required: true }
})

const thumbUrl = ref('')

onMounted(() => {
  fetchGenreThumb(props.genre.id).then(url => {
    thumbUrl.value = url
  })
})
</script>

<style scoped>
.category-card {
  width: 160px;
  text-align: center;
  border: 1px solid #ddd;
  border-radius: 6px;
  overflow: hidden;
}
.thumb {
  width: 100%;
  height: 120px;
  object-fit: cover;
}
.label {
  padding: 0.5rem 0;
  font-weight: bold;
}
</style>
