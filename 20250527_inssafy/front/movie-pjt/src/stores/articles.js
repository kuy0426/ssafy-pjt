import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useAccountStore } from '@/stores/accounts.js'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const article = ref({ liked_users: []})
  
  const API_URL = 'http://127.0.0.1:8000'
  const accountStore = useAccountStore()

  const getArticles = function() {
    const config = { url: `${API_URL}/api/v1/articles/`, method: 'get' }

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

  const getArticle = function(id) {
    const config = { url: `${API_URL}/api/v1/articles/${id}`, method: 'get' }
    
    if (accountStore.token) {
      config.headers = {
        Authorization: `Token ${accountStore.token}`
      }
    }

    return axios(config)
      .then(res => {
        article.value = res.data
        return res.data
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
    .catch(err => {
      console.error('게시글 생성 에러:',err)
      console.log(err.response.data)
    })
  }

  const updateArticle = async(payload) => {
    const id = payload.id
    const formData = new FormData()
    formData.append('title', payload.title)
    formData.append('content', payload.content)
    
    if (payload.imageFile) {
      formData.append('image', payload.imageFile)
    }

    return axios({
      method: 'put',
      url: `${API_URL}/api/v1/articles/${id}/`,
      data: formData,
      headers: {
        'Authorization': `Token ${accountStore.token}`,
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(res => {
      if(article.value.id === res.data.id){
        article.value = res.data
      }
      return res.data
    })
    .catch(err => {
      console.error('게시글 수정 에러:', err)
    })
  }

  const deleteArticle = async(id) => {
    try {
      // 서버에 DELETE 요청
      await axios.delete(
        `${API_URL}/api/v1/articles/${id}/`,
        { headers: {'Authorization': `Token ${accountStore.token}`} }
      )
      // 로컬 스토어에서 해당 글 제거
      articles.value = articles.value.filter(a => a.id !== +id)
    } catch (err) {
      console.error('▶ deleteArticle 오류:', err)
      throw err
    }
  }
  

  return { API_URL, getArticles, articles, createArticle, updateArticle, deleteArticle, getArticle, article }  
})
