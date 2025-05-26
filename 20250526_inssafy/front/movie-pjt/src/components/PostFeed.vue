<template>
  <div class="post-feed">
    <div v-for="post in posts" :key="post.id" class="post-card">
      <h4 class="post-title">{{ post.title }}</h4>
      <p class="post-date">{{ formatDate(post.created_at) }}</p>
      <div class="post-image" v-if="post.image">
        <img :src="`${post.image}`" alt="img"/>
      </div>
      <p class="likes">❤️ {{ post.likes_count }}</p>
      <p class="content">{{ post.content }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { format, parseISO, isValid } from 'date-fns'
import { useAccountStore } from '@/stores/accounts'
import { useArticleStore } from '@/stores/articles'

const props = defineProps({
  userId: { type: [String, Number], required: true }
})

const accountStore = useAccountStore()
const articleStore = useArticleStore()

const ACCOUNT_API_URL = accountStore.ACCOUNT_API_URL
const ARTICLE_API_URL = articleStore.API_URL
const posts = ref([])

async function fetchPosts() {
  try {
    const res = await axios.get(`${ARTICLE_API_URL}/api/v1/articles/?user=${props.userId}`)
    console.log(res.data)
    posts.value = res.data
  } catch (e) {
    console.error(e)
  }
}

onMounted(fetchPosts)

  function formatDate(dateStr) {
    if (!dateStr) return '-'
    const d = parseISO(dateStr)
    return isValid(d) ? format(d, 'yyyy-MM-dd') : '-'
  }
</script>

<style scoped>
.post-feed { display: flex; flex-direction: column; gap: 1.5rem; }
.post-card {
  background: #f5f7fa;
  border-radius: 8px;
  padding: 1rem;
}
.post-title { margin: 0; font-size: 1.4rem; }
.post-date { margin: .25rem 0; color: #666; }
.post-image img { width: 100%; height: auto; border-radius: 4px; margin: .5rem 0;}
.likes { margin: .5rem 0; font-weight: 500; }
.content { margin: 0; color: #333; }
</style>


