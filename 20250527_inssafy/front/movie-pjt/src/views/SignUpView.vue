<template>
  <div class="login-container">
    <div class="login-card">
      <RouterLink class="backHome" :to="{ name: 'MainView' }">
        <h1 class="brand">BaBoss Power</h1>
      </RouterLink>
      <p class="welcome">👋 Welcome !</p>
      <h1 class="title">Sign Up</h1>
      <form ref="formRef" @submit.prevent="onSignUp">
        <input v-model.trim="username" type="text" placeholder="Username" class="input-field"/>
        <small v-if="usernameError" class="text-danger">{{ usernameError }}</small>
        <input v-model.trim="password1" type="password" placeholder="Password" class="input-field"/>
        <input v-model.trim="password2" type="password" placeholder="Password Confirmation" class="input-field"/>
        <p class="help-text">사용자 이름과 너무 비슷한 비밀번호는 사용할 수 없습니다.</p>
        <small v-if="passwordError" class="text-danger">{{ passwordError }}</small>
        <div class="btns">
          <button type="submit" class="btn-signup">
            SIGN UP
          </button>
          <p class="login-text">
            already have an account? 
            <RouterLink :to="{ name: 'LogInView' }">Log In</RouterLink>
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
  
  const accountStore = useAccountStore()
  const router = useRouter() 

  const formRef = ref(null)

  const username = ref('')
  const password1 = ref('')
  const password2 = ref('')

  const usernameError = ref('')
  const passwordError = ref('')

  const onSignUp = async () => {
    usernameError.value = ''
    passwordError.value = ''

    if (password1.value !== password2.value) {
      passwordError.value = '비밀번호가 일치하지 않습니다.'
      return  // API 호출하지 말고 종료
    }

    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
    }
    try{
      await accountStore.signUp(payload)
      router.push({ name: 'MainView' })
    } catch(e) {
      if (e.message.includes('이미 사용 중')) {
        usernameError.value = e.message

        username.value = ''
        password1.value = ''
        password2.value = ''
        return
    } else{
        passwordError.value = '비밀번호를 다시 입력하세요.'
        password1.value = ''
        password2.value = ''
        return
    }
  }
}
  
</script>

<style src='@/assets/css/signup.css' scoped>

</style>
