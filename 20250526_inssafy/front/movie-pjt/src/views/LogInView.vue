<template>
  <div class="login-container">
    <div class="login-card">
      <RouterLink class="backHome" :to="{ name: 'MainView' }">
        <h1 class="brand">BaBoss Power</h1>
      </RouterLink>
      <p class="welcome">Welcome !</p>
      <h1 class="title">Login</h1>

      <input v-model.trim="username" type="text" placeholder="Username" class="input-field"/>
      <input v-model.trim="password" type="password" placeholder="Password" class="input-field"/>
      <div class="btns">
        <button @click="onLogIn" class="btn-login">
          LOGIN
        </button>
        <p class="signup-text">
          don’t have an account? 
          <RouterLink :to="{ name: 'SignUpView' }">Sign up</RouterLink>
        </p>  
      </div>
      
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useAccountStore } from '@/stores/accounts.js'

  const router = useRouter()
  const accountStore = useAccountStore()

  const username = ref('')
  const password = ref('')

  const onLogIn = async () => {
    const payload = {
      username: username.value,
      password: password.value
    }
    await accountStore.logIn(payload)
    router.push({ name: 'CommunityView' })
  }
</script>

<style src='@/assets/css/login.css' scoped></style>
