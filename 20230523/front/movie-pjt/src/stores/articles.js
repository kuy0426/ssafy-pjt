import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useAccountStore } from '@/stores/accounts.js'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const accountStore = useAccountStore()

  const getArticles = function() {
  // 헤더 객체 초기화
    const config = { url: `${API_URL}/api/v1/articles/`, method: 'get' }

    // 토큰이 있을 때만 헤더 추가
    if (accountStore.token) {
      config.headers = {
        Authorization: `Token ${accountStore.token}`
      }
    }

    axios(config)
      .then(res => {
        articles.value = res.data
      })
      .catch(err => console.log('▶ API 에러:', err))
  }
  return { articles, API_URL, getArticles }  
})
