import { createRouter, createWebHistory } from 'vue-router';

import MainView      from '@/views/MainView.vue';
import GenreView     from '@/views/GenreView.vue';
import CommunityView from '@/views/CommunityView.vue';
import DetailView    from '@/views/DetailView.vue';
import SignUpView    from '@/views/SignUpView.vue';
import LogInView     from '@/views/LogInView.vue';
import CreateView    from '@/views/CreateView.vue';
import HeroTestView   from '@/views/HeroTestView.vue' 

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView,
  },
  {
    path: '/genre/:id',
    name: 'GenreView',
    component: GenreView,
    props: true,
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView,
  },
  {
    path: '/detail/:id',
    name: 'DetailView',
    component: DetailView,
    props: true,
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView,
  },
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView,
  },
  {
    path: '/hero-test',
    name: 'HeroTestView',
    component: HeroTestView,
  },
];

export default createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});
