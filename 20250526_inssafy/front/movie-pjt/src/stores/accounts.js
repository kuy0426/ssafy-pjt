import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref('')
  const user = ref(null)

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

        return axios({
          method: 'GET',
          url: `${ACCOUNT_API_URL}/profile/`,
          headers: { Authorization: `Token ${token.value}` }
        })
      })

      .then(res => {
        console.log('내 프로필 응답: ', res.data)
        user.value = res.data
      })
      .catch(err => {
        console.log('로그인/프로필 조회 중 에러: ', err)
      })
  }

  const isLogin = computed(() => {
    return token.value ? true : false
  })

  const logOut = function() {
    return axios
      .post(
        `${ACCOUNT_API_URL}/logout/`,
        {},
        { headers: { Authorization: `Token ${token.value}` } }
      )
      .then(res => {
        token.value = ''
        user.value = null
      })
      .catch(err=> {
        console.log('failed to logout: ', err)
        alert('로그아웃에 실패했습니다. 잠시 후 다시 시도해 주세요.')
      })
  }

  const getUser = function(id) {
    return axios({
      method: 'GET',
      url: `${ACCOUNT_API_URL}/${id}`,
      headers: { Authorization: `Token ${token.value}` }
    })
    .then(res => res.data)
  }

  return { signUp, logIn, logOut, token, isLogin, getUser, user, ACCOUNT_API_URL }
}, { persist: true})