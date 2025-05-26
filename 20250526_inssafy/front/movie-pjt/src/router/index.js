import { createRouter, createWebHistory } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'
import MainView from '@/views/MainView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import CreateView from '@/views/CreateView.vue'
import GenreView from '@/views/GenreView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ProfileView from '@/views/ProfileView.vue'
import EditProfileView from '@/views/EditProfileView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import HeroTestView from '@/views/HeroTestView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView
    },
    {
      path: '/community',
      name: 'CommunityView',
      component: CommunityView
    },
    {
      path:'/article/detail/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/genre/:id',
      name: 'GenreView',
      component: GenreView,
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/profile',
      name: 'MyProfile',
      component: ProfileView,
      meta: { requiresAuth: true}
    },
    {
      path: '/profile/:id',
      name: 'UserProfile',
      component: ProfileView,
      props: true,
    },
    {
      path: '/profile/edit',
      name: 'EditProfile',
      component: EditProfileView
    },
    {
    path: '/movie/detail/:id',
    name: 'MovieDetailView',
    component: MovieDetailView,
    props: true,
    },
    {
      path: '/hero-test',
      name: 'HeroTestView',
      component: HeroTestView,
    },
  ],
})

router.beforeEach((to, from) => {
  const accountStore = useAccountStore()

  if (to.name === 'CreateView' && !accountStore.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
})

export default router
