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

  /* 🟣 이거 바꿔 */
  background-color: #3C2A4D; /* NEW: 짙은 보라 계열 */
  color: #FAFAFA;
}

.hero-box h2,
.hero-box span {
  /* 텍스트도 밝은 색으로 덮어줌 */
  color: #FAFAFA;
}
</style>