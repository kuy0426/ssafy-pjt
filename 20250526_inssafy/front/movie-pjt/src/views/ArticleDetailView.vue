<template>
  <div class="detail-page">
    <div class="content">
      <div class="post-header">
        <h1 class="post-title">{{ article.title }}</h1>
        <button class="like-btn" :class="{ liked: isLiked }" @click="toggleLike">
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
  import { useRoute, RouterLink } from 'vue-router'
  import { useArticleStore } from '@/stores/articles'
  import { useAccountStore } from '@/stores/accounts'
  import { format, parseISO, isValid } from 'date-fns'


  const store = useArticleStore()
  const accountStore = useAccountStore()
  const route = useRoute()
  const STATIC_BASE = `${store.API_URL}/static/images`

  onMounted(() => {
    store.getArticle(route.params.id)
  })

  const article = computed(() => store.article)
  
  const isLiked = computed(() =>
    accountStore.user && article.value.liked_users.includes(accountStore.user.id)
  )

  function toggleLike() {
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

  function formatDate(val) {
    if (!val) return '-'
    const d = parseISO(val)
    return isValid(d) ? format(d, 'yyyy-MM-dd hh:mm') : '-'
  }

  const avatarUrl = computed(() => {
    // article.value.user.profile_image 이 backend가 주는 “미디어 URL” 이라면
    const img = article.value.user?.profile_image
    return img
      ? `${store.API_URL}${img}`
      : `${STATIC_BASE}/noProfile.png`  
  })

</script>

<style src='@/assets/css/articleDetail.css' scoped />
