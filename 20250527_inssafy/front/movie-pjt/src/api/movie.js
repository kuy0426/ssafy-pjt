import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || 'http://localhost:8000/api/v1',
  withCredentials: false,
});

/**
 * Top 10 Trending Movies
 */
export const fetchTrending = () =>
  api
    .get('/movies/trending/')
    .then(r => Array.isArray(r.data) ? r.data : r.data.results || [])
    .catch(() => []);

/**
 * 영화 상세 + cast
 */
export const fetchMovieDetail = (tmdb_id) =>
  api
    .get(`/movies/${tmdb_id}/`)
    .then(r => r.data)
    .catch(() => null);

/**
 * 장르별 영화 목록 (with_genres=tmdb_id)
 */
export const fetchMoviesByGenre = (genreId, page = 1) =>
  api
    // 백엔드가 필터링하려고 기다리고 있는 param 이름이 'genreId' 여야 합니다.
    .get('/movies/', { params: { genreId, page } })
    .then(r => Array.isArray(r.data) ? r.data : r.data.results || [])
    .catch(() => []);
/**
 * 메인에서 사용할 장르 목록
 */
export const GENRES = [
  { label: 'Action', id: 28 },
  { label: 'Crime',  id: 80 },
  { label: 'S/F',    id: 878 },
  { label: 'Comedy', id: 35 },
  { label: 'Horror',     id: 27    },  // 공포
  { label: 'Thriller',   id: 53    },  // 스릴러
  { label: 'Romance',    id: 10749 }, // 로맨스
  { label: 'Animation',  id: 16    }   // 애니메이션
];

// src/api/movie.js


const TMDB_KEY = import.meta.env.VITE_TMDB_API_KEY


