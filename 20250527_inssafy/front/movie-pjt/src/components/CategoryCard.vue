<template>
  <router-link
    class="card text-white text-center"
    :to="{ name: 'GenreView', params: { id: props.id } }"
  >
    <div
      class="card-body d-flex align-items-center justify-content-center"
      :style="{
        height: '120px',
        backgroundColor: !props.posterPath ? '#6c757d' : 'transparent',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundImage: props.posterPath
          ? `url(https://image.tmdb.org/t/p/w500${props.posterPath})`
          : 'none'
      }"
    >
      <!-- 반투명 레이어 -->
      <div class="overlay"></div>
      <!-- 글씨 -->
      <span class="label">{{ props.label }}</span>
    </div>
  </router-link>
</template>

<script setup>
const props = defineProps({
  label: String,
  id: Number,
  posterPath: {
    type: String,
    default: ''
  }
});
</script>

<style scoped>
.card {
  border-radius: 8px;
  overflow: hidden;
  text-decoration: none;
}
.card:hover {
  opacity: 0.9;
}
.card-body {
  position: relative; /* overlay 배치 기준 */
}
/* 검정 반투명 레이어 */
.overlay {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-color: rgba(0, 0, 0, 0.4); /* 40% 불투명 검정 */
}
/* 레이블은 overlay 위, 최상단에 */
.label {
  position: relative;
  z-index: 1;
  font-size: 1.25rem;
}
</style>
