<template>
  <header>
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <!-- 1) 브랜드 로고를 클릭하면 MainView로 -->
        <RouterLink class="navbar-brand text-white" :to="{ name: 'MainView' } ">
          BaBoss
        </RouterLink>

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
          <!-- 빈 왼쪽 메뉴 (필요 없으니 비워두거나 완전 삭제) -->
          <ul class="navbar-nav me-auto "></ul>

          <!-- 오른쪽 메뉴: Community → (로그아웃, 프로필) or (SignUp, LogIn) -->
          <ul class="navbar-nav align-items-center ">
            <!-- Community 항상 보이기 -->
            <li class="nav-item">
              <RouterLink
                class="nav-link"
                :to="{ name: 'CommunityView' }"
                exact-active-class="active"
              >
                Community
              </RouterLink>
            </li>

            <template v-if="accountStore.isLogin">
              <!-- Logout -->
              <li class="nav-item">
                <a href="#" class="nav-link" @click.prevent="handleLogout">
                  Logout
                </a>
              </li>
              <!-- Profile Avatar -->
              <li class="nav-item">
                <RouterLink class="nav-link p-0" :to="{ name: 'MyProfile' }">
                  <img :src="avatarUrl" class="nav-avatar" alt="Profile" />
                </RouterLink>
              </li>
            </template>
            <template v-else>
              <li class="nav-item">
                <RouterLink
                  class="nav-link"
                  :to="{ name: 'SignUpView' }"
                  exact-active-class="active"
                >
                  SignUp
                </RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink
                  class="nav-link"
                  :to="{ name: 'LogInView' }"
                  exact-active-class="active"
                >
                  LogIn
                </RouterLink>
              </li>
            </template>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { computed } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

const accountStore = useAccountStore()
const router = useRouter()

// 프로필 이미지 URL
const BASE_URL = 'http://127.0.0.1:8000'
const STATIC_BASE = `${BASE_URL}/static/images`
const avatarUrl = computed(() => {
  const img = accountStore.user?.profile_image
  return img
    ? `${BASE_URL}${img}`
    : `${STATIC_BASE}/noProfile.png`
})

function handleLogout() {
  accountStore.logOut().then(() => {
    router.push({ name: 'MainView' })
  })
}
</script>

<style scoped>
.navbar {
  /* background-color: #21201E; */
  background-color: none;
}
.nav-link {
  color: white
}

.nav-link:hover, 
.navbar-brand:hover {
  color: #924EBF
}

.navbar-brand {
  color: white;
  cursor: pointer;
}

/* 오른쪽 메뉴 아이템 간 간격 */
.navbar-nav .nav-item + .nav-item {
  margin-left: 0.75rem;
}

.nav-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #ddd;
}

.navbar .nav-link.active {
  color: #924EBF !important;  /* 원하시는 포인트 컬러로 교체 */
}
</style>
