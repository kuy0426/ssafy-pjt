<template>
  <div
    class="hero-box d-flex flex-column align-items-center justify-content-center mb-4"
  >
    <div class="d-flex align-items-center mb-3">
      <span class="me-2 fs-2">🎬</span>
      <h2 class="m-0">Movie Match</h2>
    </div>
    <button class="btn btn-outline-dark" @click="startTest">
      TEST 하기
    </button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();

function startTest() {
  router.push({ name: 'HeroTest' });
}
</script>

<style scoped>
.hero-box {
  width: 100%;
  height: 180px;
  border-radius: 0.5rem;
  /* 파스텔 보라 배경 */
  background-color: #E6E6FA;
  /* 진한 보라 텍스트 */
  color: #4B0082;
}
.hero-box h2,
.hero-box span {
  /* 타이틀과 이모티콘도 진한 보라 */
  color: #4B0082;
}
.hero-box button {
  font-weight: bold;
}
</style>
