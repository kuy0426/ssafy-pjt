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

  const createArticle = async(payload) => {
    const formData = new FormData()
    formData.append('title', payload.title)
    formData.append('content', payload.content)
    
    if (payload.imageFile) {
      formData.append('image', payload.imageFile)
    }

    return axios({
      method: 'post',
      url: `${API_URL}/api/v1/articles/`,
      data: formData,
      headers: {
        'Authorization': `Token ${accountStore.token}`,
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(res => {
      // 성공 시 로컬 스토어에 즉시 추가
      articles.value.push(res.data)
      return res.data    // 컴포넌트에 결과 전달
    }) 
    .catch(err => console.error('게시글 생성 에러:',err))
  }

  return { articles, API_URL, getArticles, createArticle }  
})
