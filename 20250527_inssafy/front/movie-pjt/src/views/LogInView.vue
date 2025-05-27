<template>
  <div class="login-container">
    <div class="login-card">
      <RouterLink class="backHome" :to="{ name: 'MainView' }">
        <h1 class="brand">BaBoss Power</h1>
      </RouterLink>
      <p class="welcome">👋 Welcome Back!</p>
      <h1 class="title">Login</h1>
      <form @submit.prevent="onLogIn">
        <input v-model.trim="username" type="text" placeholder="Username" class="input-field"/>
        <input v-model.trim="password" type="password" placeholder="Password" class="input-field"/>

        <p v-if="errorMessage" class="text-danger">{{ errorMessage }}</p>

        <div class="btns">
          <button type="submit" class="btn-login">
            LOGIN
          </button>
          <p class="signup-text">
            don’t have an account? 
            <RouterLink :to="{ name: 'SignUpView' }">Sign up</RouterLink>
          </p>  
        </div>
      </form>    
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
  const errorMessage = ref('') 

  const onLogIn = async () => {
    errorMessage.value = '' 

    const payload = {
      username: username.value,
      password: password.value
    }
    try {
      await accountStore.logIn(payload)
      router.push({ name: 'MainView' })
    }
    catch(err) {
      errorMessage.value = '로그인 정보를 확인하세요.'
    }
  }
</script>

<style src='@/assets/css/login.css' scoped></style>
