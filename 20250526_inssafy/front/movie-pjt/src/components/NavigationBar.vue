<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <div class="navbar-brand">BaBoss</div>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item" v-for="item in navItems" :key="item.name">
              <RouterLink class="nav-link" :to="{ name: item.name }" exact-active-class="active">
                {{ item.label }}
              </RouterLink>
            </li>
            <template v-if="!accountStore.isLogin">
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{ name: 'SignUpView' }" exact-active-class="active">
                  SignUp
                </RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{ name: 'LogInView' }" exact-active-class="active">
                  LogIn
                </RouterLink>
              </li>
            </template>
            <template v-else>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{ name: 'MyProfile' }" exact-active-class="active">
                  Profile
                </RouterLink>
              </li>
              <li class="nav-item">
                <a href="#" class="nav-link" @click.prevent="handleLogout">
                  Logout
                </a>
              </li>
            </template>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
  import { RouterLink, useRouter } from 'vue-router'
  import { useAccountStore } from '@/stores/accounts'

  const accountStore = useAccountStore()

  const navItems = [
    { name: 'MainView',    label: 'Home' },
    { name: 'CommunityView', label: 'Community' },
  ]

  const router = useRouter()

  function handleLogout() {
    accountStore
      .logOut()
      .then(() => {
        router.push({ name: 'MainView' })
      })
  }
</script>

<style scoped>

</style>