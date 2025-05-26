<!-- src/views/GenreView.vue -->
<template>
  <div class="container py-5">
    <!-- 장르 타이틀 -->
    <h1 class="text-center mb-4" style="color: #4B0082;">
      📂 {{ genreLabel }}
    </h1>

    <!-- 로딩 스피너 -->
    <div v-if="isLoading && !movies.length" class="text-center py-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <!-- Featured: 첫 번째 영화 -->
    <div v-else-if="movies.length" class="mb-5 text-center">
      <router-link
        :to="{ name: 'DetailView', params: { id: movies[0].id } }"
        class="d-inline-block"
      >
        <img
          :src="`https://image.tmdb.org/t/p/w500${movies[0].poster_path}`"
          class="img-fluid rounded shadow"
          style="max-height:400px;"
          alt="Featured"
        />
        <div class="mt-3">
          <h4 class="badge bg-light text-dark px-3 py-2">
            {{ movies[0].original_title }}
          </h4>
        </div>
      </router-link>
    </div>

    <!-- Grid: 나머지 영화들 -->
    <div v-if="movies.length" class="row g-4">
      <div
        v-for="(m, idx) in movies.slice(1)"
        :key="m.id + '-' + idx"
        class="col-6 col-md-3"
      >
        <router-link
          :to="{ name: 'DetailView', params: { id: m.id } }"
          class="text-decoration-none"
        >
          <div class="card h-100 shadow-sm">
            <img
              loading="lazy"
              v-if="m.poster_path"
              :src="`https://image.tmdb.org/t/p/w300${m.poster_path}`"
              class="card-img-top"
              style="height:200px; object-fit:cover;"
              alt="Poster"
            />
            <div class="card-body p-2 text-center">
              <small class="d-block text-truncate">{{ m.original_title }}</small>
            </div>
          </div>
        </router-link>
      </div>
    </div>

    <!-- 더 보기 버튼 -->
    <div v-if="movies.length" class="text-center my-4">
      <button
        class="btn btn-outline-primary"
        @click="loadMore"
        :disabled="isLoading || !hasMore"
      >
        {{ isLoading ? '불러오는 중...' : (hasMore ? '더 보기' : '모두 불러왔습니다') }}
      </button>
    </div>

    <!-- 결과 없을 때 -->
    <p v-if="!movies.length && !isLoading" class="text-center text-secondary mt-5">
      No movies found in this genre 😢
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import { useRoute } from 'vue-router';
import { fetchMoviesByGenre, GENRES } from '@/api/movie';

const route     = useRoute();
const movies    = ref([]);
const isLoading = ref(false);
const hasMore   = ref(true);
const page      = ref(1);

// params.id → 숫자로
const genreId    = computed(() => Number(route.params.id));
// id → 라벨
const genreLabel = computed(() => {
  const g = GENRES.find(x => x.id === genreId.value);
  return g ? g.label : 'Unknown';
});

// 여러 페이지를 병렬로 Prefetch (예: 1~3페이지)
async function prefetchPages(pages = [1,2,3]) {
  isLoading.value = true;
  const lists = await Promise.all(
    pages.map(p => fetchMoviesByGenre(genreId.value, p))
  );
  movies.value = lists.flat();
  page.value   = pages.length + 1;
  hasMore.value = lists[lists.length-1].length > 0;
  isLoading.value = false;
}

// “더 보기”로 다음 페이지 하나씩 로드
async function loadMore() {
  if (isLoading.value || !hasMore.value) return;
  isLoading.value = true;
  const list = await fetchMoviesByGenre(genreId.value, page.value);
  if (list.length) {
    movies.value.push(...list);
    page.value++;
  } else {
    hasMore.value = false;
  }
  isLoading.value = false;
}

// 초기화 & Prefetch
onMounted(() => prefetchPages());
// 장르 바뀌면 다시 Prefetch
watch(() => genreId.value, () => prefetchPages());
</script>

<style scoped>
.card {
  transition: transform .2s;
}
.card:hover {
  transform: translateY(-4px);
}
</style>
