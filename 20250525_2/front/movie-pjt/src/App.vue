<template>
  <header>
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <div class="navbar-brand">BaBoss</div>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li
              class="nav-item"
              v-for="item in navItems"
              :key="item.name"
            >
              <RouterLink
                class="nav-link"
                :to="{ name: item.name }"
                exact-active-class="active"
              >
                {{ item.label }}
              </RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <main class="container">
    <RouterView />
  </main>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router';

const navItems = [
  { name: 'MainView',       label: 'Home'      },
  { name: 'CommunityView',  label: 'Community' },
  { name: 'SignUpView',     label: 'SignUp'    },
  { name: 'LogInView',      label: 'LogIn'     },
];
</script>

<style scoped>
.navbar {
  /* 파스텔 보라 배경 */
  background-color: #E6E6FA !important;
}
/* 텍스트와 토글 아이콘을 진한 보라로 */
.navbar-brand,
.nav-link {
  color: #4B0082 !important;
}
.navbar-toggler-icon {
  /* 햄버거 아이콘도 Indigo 계열로 교체 */
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='%234B0082' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
}
</style>
