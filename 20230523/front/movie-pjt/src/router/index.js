// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import { useAccountStore }               from '@/stores/accounts'

import MainView         from '@/views/MainView.vue'
import ArticleView      from '@/views/ArticleView.vue'
import SignUpView       from '@/views/SignUpView.vue'
import LogInView        from '@/views/LogInView.vue'
import CreateView       from '@/views/CreateView.vue'
import GenreView        from '@/views/GenreView.vue'
import MovieDetailView  from '@/views/MovieDetailView.vue'
import HeroMatchView    from '@/views/HeroMatchView.vue'

const routes = [
  { path: '/',            name: 'MainView',      component: MainView },
  { path: '/articles',    name: 'ArticleView',   component: ArticleView },
  { path: '/signup',      name: 'SignUpView',    component: SignUpView },
  { path: '/login',       name: 'LogInView',     component: LogInView },
  { path: '/create',      name: 'CreateView',    component: CreateView },
  { path: '/genre/:id',   name: 'GenreView',     component: GenreView,    props: true },
  { path: '/movies/:id',  name: 'MovieDetail',   component: MovieDetailView },
  { path: '/hero-match',  name: 'HeroMatchTest', component: HeroMatchView },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

router.beforeEach((to, from) => {
  const accountStore = useAccountStore()
  if (to.name === 'CreateView' && !accountStore.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
})

export default router
