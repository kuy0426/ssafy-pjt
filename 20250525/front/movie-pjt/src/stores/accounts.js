import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref('')
  const router = useRouter()

  const signUp = function(payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/signup/`,

      data: {
        username, password1, password2
      }
    })
      .then(res => {
        console.log('회원가입 성공!')
      })
      .catch(err => console.log(err))
  }
  
  const logIn = function(payload) {
    const username = payload.username
    const password = payload.password

    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        console.log('로그인 응답:', res.data)
        token.value = res.data.key
      })
      .catch(err => {
        console.log(err)
      })
  }

  const isLogin = computed(() => {
    return token.value ? true : false
  })
  
  return { signUp, logIn, token, isLogin }
}, { persist: true})