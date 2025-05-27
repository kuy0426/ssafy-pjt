<template>
  <div class="detail-page">
    <div class="content">
      <div class="post-header">
        <h1 class="post-title">{{ article.title }}</h1>
        <div class="post-actions" v-if="isAuthor">
          <RouterLink :to="{ name: 'EditArticleView', params: {id: article.id} }" class="btn-edit">
            <svg viewBox="-0.5 -0.5 24 24" xmlns="http://www.w3.org/2000/svg" width="24" height="24">
            <path d='M21.289.98l.59.59c.813.814.69 2.257-.277 3.223L9.435 16.96l-3.942 1.442c-.495.182-.977-.054-1.075-.525a.928.928 0 0 1 .045-.51l1.47-3.976L18.066 1.257c.967-.966 2.41-1.09 3.223-.276zM8.904 2.19a1 1 0 1 1 0 2h-4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-4a1 1 0 0 1 2 0v4a4 4 0 0 1-4 4h-12a4 4 0 0 1-4-4v-12a4 4 0 0 1 4-4h4z' 
            stroke = 'none'
            fill = 'gray'
            />
            </svg>
          </RouterLink>
          <button class="btn-delete" type="button" @click="onDelete">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
              <path d="M3 6.38597C3 5.90152 3.34538 5.50879 3.77143 5.50879L6.43567 5.50832C6.96502 5.49306 7.43202 5.11033 7.61214 4.54412C7.61688 4.52923 7.62232 4.51087 7.64185 4.44424L7.75665 4.05256C7.8269 3.81241 7.8881 3.60318 7.97375 3.41617C8.31209 2.67736 8.93808 2.16432 9.66147 2.03297C9.84457 1.99972 10.0385 1.99986 10.2611 2.00002H13.7391C13.9617 1.99986 14.1556 1.99972 14.3387 2.03297C15.0621 2.16432 15.6881 2.67736 16.0264 3.41617C16.1121 3.60318 16.1733 3.81241 16.2435 4.05256L16.3583 4.44424C16.3778 4.51087 16.3833 4.52923 16.388 4.54412C16.5682 5.11033 17.1278 5.49353 17.6571 5.50879H20.2286C20.6546 5.50879 21 5.90152 21 6.38597C21 6.87043 20.6546 7.26316 20.2286 7.26316H3.77143C3.34538 7.26316 3 6.87043 3 6.38597Z" fill="gray"/>
              <path fill-rule="evenodd" clip-rule="evenodd" d="M11.5956 22.0001H12.4044C15.1871 22.0001 16.5785 22.0001 17.4831 21.1142C18.3878 20.2283 18.4803 18.7751 18.6654 15.8686L18.9321 11.6807C19.0326 10.1037 19.0828 9.31524 18.6289 8.81558C18.1751 8.31592 17.4087 8.31592 15.876 8.31592H8.12404C6.59127 8.31592 5.82488 8.31592 5.37105 8.81558C4.91722 9.31524 4.96744 10.1037 5.06788 11.6807L5.33459 15.8686C5.5197 18.7751 5.61225 20.2283 6.51689 21.1142C7.42153 22.0001 8.81289 22.0001 11.5956 22.0001ZM10.2463 12.1886C10.2051 11.7548 9.83753 11.4382 9.42537 11.4816C9.01321 11.525 8.71251 11.9119 8.75372 12.3457L9.25372 17.6089C9.29494 18.0427 9.66247 18.3593 10.0746 18.3159C10.4868 18.2725 10.7875 17.8856 10.7463 17.4518L10.2463 12.1886ZM14.5746 11.4816C14.9868 11.525 15.2875 11.9119 15.2463 12.3457L14.7463 17.6089C14.7051 18.0427 14.3375 18.3593 13.9254 18.3159C13.5132 18.2725 13.2125 17.8856 13.2537 17.4518L13.7537 12.1886C13.7949 11.7548 14.1625 11.4382 14.5746 11.4816Z" fill="gray"/>
            </svg>
            
          </button>
        </div>
        <button v-else class="like-btn" :class="{ liked: isLiked }" @click="toggleLike">
          <!-- 좋아요 안 눌렀을 때 (outline heart) -->
          <svg v-if="!isLiked" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
            <path
              d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5
                  2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09
                  C13.09 3.81 14.76 3 16.5 3
                  19.58 3 22 5.42 22 8.5
                  c0 3.78-3.4 6.86-8.55 11.54
                  L12 21.35z"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              />
            </svg>
          <!-- 좋아요 눌렀을 때 (filled heart) -->
          <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
            <path
              d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5
                 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09
                 C13.09 3.81 14.76 3 16.5 3
                 19.58 3 22 5.42 22 8.5
                 c0 3.78-3.4 6.86-8.55 11.54
                 L12 21.35z"
              fill="currentColor"
            />
          </svg>
        </button>
      </div>
      <div class="author-info">
        <RouterLink :to="{ name: 'UserProfile', params: { id : article.author_id} }">
         <img v-if="article.user" class="avatar" :src="avatarUrl" alt="author avatar"/>
         <h4 class="username">{{ article.author }}</h4> 
        </RouterLink>
      </div>
      <p>{{ formatDate(article.created_at) }}</p>
      <hr />
      <div v-if="article.image" class="post-image">
        <img :src="`${store.API_URL}${article.image}`" alt="post image" />
      </div>

      <div class="post-body">
        <p>{{ article.content }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { onMounted, ref, computed } from 'vue'
  import { useRoute, useRouter, RouterLink } from 'vue-router'
  import { useArticleStore } from '@/stores/articles'
  import { useAccountStore } from '@/stores/accounts'
  import { format, parseISO, isValid } from 'date-fns'


  const store = useArticleStore()
  const accountStore = useAccountStore()
  const route = useRoute()
  const router = useRouter()
  const STATIC_BASE = `${store.API_URL}/static/images`
  const BASE_URL = 'http://127.0.0.1:8000'

  onMounted(() => {
    store.getArticle(route.params.id)
  })

  const article = computed(() => store.article)
  
  const isLiked = computed(() =>
    accountStore.user && article.value.liked_users.includes(accountStore.user.id)
  )

  const isAuthor = computed(() => 
    accountStore.user && article.value.author_id === accountStore.user.id
  )

  function toggleLike() {
     if (!accountStore.isLogin) {
      alert('로그인이 필요합니다.')
      return
    }

    const method = isLiked.value ? 'DELETE' : 'POST'

    axios({
      method,
      url: `${store.API_URL}/api/v1/articles/${route.params.id}/like/`,
      headers: { Authorization: `Token ${accountStore.token}` }
    })
      .then(() => {
        if (isLiked.value) {
          const idx = article.value.liked_users.indexOf(accountStore.user.id)
          if (idx > -1) article.value.liked_users.splice(idx, 1)
        } else {
          article.value.liked_users.push(accountStore.user.id)
        }
      })
  }

  async function onDelete() {
    if (!confirm('정말 이 글을 삭제하시겠습니까?')) return

    try {
      // 스토어 메서드 호출
      await store.deleteArticle(article.value.id)
      alert('삭제를 완료하였습니다.')
      router.push({name: 'MyProfile'})
    } catch (err) {
      console.error(err)
      alert('삭제에 실패했습니다.')
    }
  }

  function formatDate(val) {
    if (!val) return '-'
    const d = parseISO(val)
    return isValid(d) ? format(d, 'yyyy-MM-dd hh:mm') : '-'
  }

  const avatarUrl = computed(() => {
    // article.value.user.profile_image 이 backend가 주는 “미디어 URL” 이라면
    const img = article.value.profile_image
    return img
      ? `${BASE_URL}${img}`
      : `${STATIC_BASE}/noProfile.png`  
  })

</script>

<style src='@/assets/css/articleDetail.css' scoped />
