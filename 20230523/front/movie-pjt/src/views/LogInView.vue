
<template>
  <div>
    <form @submit.prevent="onLogIn">
      <label for="username">username: </label>
      <input type="text" id="username" v-model.trim="username">
      <br>
      <label for="password">password: </label>
      <input type="password" id="password" v-model.trim="password">
      <br>
      <input type="submit" value="signup">
    </form>  
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
    router.push({ name: 'ArticleView' })
  }
</script>

<style>

</style>
₩