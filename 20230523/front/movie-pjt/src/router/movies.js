// ─────────────────────────────────────────────
// src/api/movie.js
// ─────────────────────────────────────────────
import axios from 'axios'

// 1) Axios 인스턴스 (VITE_API_BASE 는 .env 에 설정)
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE,
  withCredentials: false,
})

/**
 * 2) MainView.vue 에서 쓰는 장르 목록
 */
export const GENRES = [
  { label: 'Action', id: 28 },
  { label: 'Crime',  id: 80 },
  { label: 'S/F',    id: 878 },
  { label: 'Comedy', id: 35 },
]

/**
 * 3) Hero Match 예시 (Animation 첫 영화)
 */
export function fetchHeroMatch() {
  return api
    .get('/movies/', { params: { genre: 'Animation', page: 1 } })
    .then(r => r.data.results[0])
}

/**
 * 4) 평점 상위 3편 (Now Trending)
 */
export function fetchTopRated() {
  return api
    .get('/movies/top/', { params: { page: 1 } })
    .then(r => (r.data.results || []).slice(0, 3))
}

/**
 * 5) Top 10 Trending Movies
 */
export function fetchTopTen() {
  return api
    .get('/movies/top/', { params: { page: 1 } })
    .then(r => {
      const arr = r.data.results || []
      return arr.slice(0, 10).map(m => ({
        id:     m.id,
        title:  m.title,
        poster: m.poster_path
          ? `https://image.tmdb.org/t/p/w300${m.poster_path}`
          : ''
      }))
    })
}

/**
 * 6) CategoryCard.vue용: 특정 장르 썸네일 한 장
 */
export function fetchGenreThumb(genreId) {
  return api
    .get('/movies/', { params: { genreId, page: 1 } })
    .then(r => {
      const arr = r.data.results || []
      if (!arr.length) return ''
      const m = arr[0]
      return m.poster_path
        ? `https://image.tmdb.org/t/p/w300${m.poster_path}`
        : ''
    })
}

/**
 * 7) MovieDetailView.vue용: 상세 + credits + videos
 */
export function fetchMovieDetail(id) {
  return api
    .get(`/movies/${id}`, { params: { append_to_response: 'credits,videos' } })
    .then(r => r.data)
}
