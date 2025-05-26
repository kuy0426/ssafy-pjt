<template>
  <div>
    <form @submit.prevent="onSignUp">
      <label for="username">username: </label>
      <input type="text" id="username" v-model.trim="username">
      <br>
      <label for="password1">password1: </label>
      <input type="password" id="password1" v-model.trim="password1">
      <br>
      <label for="password2">password2: </label>
      <input type="password" id="password2" v-model.trim="password2">
      <br>
      <input type="submit" value="signup">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts.js'
  
  const accountStore = useAccountStore()

  const username = ref('')
  const password1 = ref('')
  const password2 = ref('')

  const onSignUp = function () {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
    }
    accountStore.signUp(payload)  
  }
  
</script>

<style>

</style>
