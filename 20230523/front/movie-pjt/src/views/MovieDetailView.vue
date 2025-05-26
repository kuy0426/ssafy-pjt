<!-- src/views/MovieDetailView.vue -->
<template>
  <div v-if="!movie" class="container py-5 text-center">
    <div class="spinner-border" role="status">
      <span class="visually-hidden">Loading…</span>
    </div>
  </div>

  <div v-else class="container py-4">
    <div class="row">
      <div class="col-md-4 mb-4">
        <img
          :src="posterUrl"
          class="img-fluid rounded shadow"
          alt="poster"
        />
      </div>
      <div class="col-md-8">
        <h1>{{ movie.title }}</h1>
        <div class="mb-3"><span class="h5">★ {{ movie.vote_average }}</span></div>
        <div class="mb-4">
          <h5>Description</h5>
          <p class="bg-light p-3 rounded">{{ movie.overview }}</p>
        </div>

        <div v-if="movie.credits?.cast?.length" class="mb-4">
          <h5>Actors</h5>
          <div class="d-flex overflow-auto gap-3">
            <div
              v-for="actor in movie.credits.cast.slice(0,5)"
              :key="actor.cast_id"
              class="text-center"
              style="min-width: 90px;"
            >
              <img
                :src="actor.profile_path
                  ? `https://image.tmdb.org/t/p/w200${actor.profile_path}`
                  : noImage"
                class="img-fluid rounded mb-1"
                alt="actor"
              />
              <div class="small">{{ actor.name }}</div>
            </div>
          </div>
        </div>

        <div class="d-flex gap-2">
          <button class="btn btn-primary" @click="$router.back()">Home</button>
          <button
            class="btn btn-success"
            data-bs-toggle="modal"
            data-bs-target="#trailerModal"
            @click="loadTrailer"
          >
            예고편 보기
          </button>
        </div>
      </div>
    </div>
  </div>

  <div
    v-if="movie"
    class="modal fade"
    id="trailerModal"
    tabindex="-1"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header bg-primary text-white">
          <h5 class="modal-title">{{ movie.title }} – Trailer</h5>
          <button
            type="button"
            class="btn-close btn-close-white"
            data-bs-dismiss="modal"
          ></button>
        </div>
        <div class="modal-body p-0">
          <div v-if="trailerUrl" class="ratio ratio-16x9">
            <iframe
              :src="trailerUrl"
              frameborder="0"
              allow="autoplay; encrypted-media"
              allowfullscreen
            />
          </div>
          <div v-else class="p-4 text-center">
            예고편을 불러오는 중입니다…
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute }                from 'vue-router'
import { fetchMovieDetail }        from '@/api/movie'


const route = useRoute()
const movie = ref(null)
const trailerUrl = ref('')

const posterUrl = computed(() =>
 movie.value?.poster_path
   ? `https://image.tmdb.org/t/p/w500${movie.value.poster_path}`
   : placeholder
)

onMounted(async () => {
  movie.value = await fetchMovieDetail(route.params.id)
})

function loadTrailer() {
  const vids = movie.value.videos?.results || []
  const tr = vids.find(v => v.type === 'Trailer') || vids[0]
  if (tr?.key) {
    trailerUrl.value = `https://www.youtube.com/embed/${tr.key}?autoplay=1`
  }
}
</script>

<style scoped>
.container { max-width: 960px; }
</style>
