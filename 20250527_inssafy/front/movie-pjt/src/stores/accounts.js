import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref('')
  const user = ref(null)

  const signUp = async function(payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    
    return axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/signup/`,

      data: {
        username, password1, password2
      }
    })
      .then(res => {
        console.log('회원가입 성공!')
      })
      .catch(err => {
        const resp = err.response
        console.log('▶ signUp 실패 응답 데이터:', err.response?.data)
        if(resp && resp.status === 400 && resp.data.username) {
          throw new Error('이미 사용 중인 아이디입니다.')
        }
        throw err
      })
  }
  
  const logIn = function(payload) {
    const username = payload.username
    const password = payload.password

    return axios({
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
        throw err
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

  async function getUser(id) {
    const res = await axios.get(
      `${ACCOUNT_API_URL}/profile/${id}/`
    )
    return res.data
  }

    // 내 프로필
  async function getMyProfile() {
    const res = await axios.get(
      `${ACCOUNT_API_URL}/profile/`,
      { headers: { Authorization: `Token ${token.value}` } }
    )
    user.value = res.data
    return res.data
  }

  async function updateProfile(payload) {
    const biography = payload.biography
    const profile_image = payload.profile_image
    
    const formData = new FormData()

    if(biography !== null) {
      formData.append('biography', biography)
    }
    if(profile_image !== null) {
      formData.append('profile_image', profile_image)
    }

    return axios({
      method: 'patch',
      url: `${ACCOUNT_API_URL}/profile/`,
      data: formData,
      headers: {
        'Authorization': `Token ${token.value}`,
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(res => {
      user.value = res.data
      return res.data
    })
    .catch(err => {
      console.error('회원 정보 수정 에러: ', err)
      console.log(err.response.data)
    })
  }

  return { signUp, logIn, logOut, token, isLogin, getUser, getMyProfile, updateProfile, user, ACCOUNT_API_URL }
}, { persist: true})