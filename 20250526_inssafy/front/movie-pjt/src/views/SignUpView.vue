<template>
  <div class="login-container">
    <div class="login-card">
      <RouterLink class="backHome" :to="{ name: 'MainView' }">
        <h1 class="brand">BaBoss Power</h1>
      </RouterLink>
      <p class="welcome">Welcome !</p>
      <h1 class="title">Sign Up</h1>

      <input v-model.trim="username" type="text" placeholder="Username" class="input-field"/>
      <input v-model.trim="password1" type="password" placeholder="Password" class="input-field"/>
      <input v-model.trim="password2" type="password" placeholder="Password Confirmation" class="input-field"/>
      <div class="btns">
        <button @click="onSignUp" class="btn-signup">
          SIGN UP
        </button>
        <p class="login-text">
          already have an account? 
          <RouterLink :to="{ name: 'LogInView' }">Log In</RouterLink>
        </p> 
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useAccountStore } from '@/stores/accounts.js'
  
  const accountStore = useAccountStore()
  const router = useRouter() 

  const username = ref('')
  const password1 = ref('')
  const password2 = ref('')

  const onSignUp = async () => {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
    }
    await accountStore.signUp(payload)
    router.push({ name: 'MainView' })
  }
  
</script>

<style src='@/assets/css/signup.css' scoped>

</style>
