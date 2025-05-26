// src/api/movie.js
import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE,  // .env 에 VITE_API_BASE=http://localhost:8000/api/v1
  withCredentials: false,
})

/**
 * 1) MainView.vue 에서 사용할 장르 목록
 */
export const GENRES = [
  { label: 'Action', id: 28 },
  { label: 'Crime',  id: 80 },
  { label: 'S/F',    id: 878 },
  { label: 'Comedy', id: 35 },
]

/**
 * 2) HeroMatch.vue 에서 사용할 예시 호출
 */
export function fetchHeroMatch() {
  return api
    .get('/movies/', { params: { genre: 'Animation', page: 1 } })
    .then(r => r.data.results[0])
}

/**
 * 3) Top-Rated (평점 상위 3편)
 */
export function fetchTopRated() {
  return api
    .get('/movies/top/', { params: { page: 1 } })
    .then(r => (r.data.results || []).slice(0, 3))
}

/**
 * 4) Top 10 Trending Movies
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
 * 5) CategoryCard.vue용: 특정 장르 썸네일 한 장
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
 * 6) MovieDetailView.vue용: 상세 + credits + videos
 */
export function fetchMovieDetail(id) {
  return api
    .get(`/movies/${id}`, { params: { append_to_response: 'credits,videos' } })
    .then(r => r.data)
}
