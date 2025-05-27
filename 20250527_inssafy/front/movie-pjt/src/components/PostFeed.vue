<!-- src/components/PostFeed.vue -->
<template>
  <div class="post-feed">
    <!-- 게시글이 없을 때 -->
    <div v-if="posts.length === 0" class="empty-message">
      <h3>‼️ No Postings ... </h3>
      <RouterLink class="create-button" :to="{ name: 'CreateView'}">
        게시글 쓰러 가기 🏃‍♂️‍➡️
      </RouterLink>
    </div>
    <!-- wrapper 없는 template 사용 -->
    <template v-else>
      <div
        v-for="post in posts"
        :key="post.id"
        class="post-card"
      >
        <RouterLink
          :to="{ name: 'ArticleDetailView', params: { id: post.id } }"
        >
          <h4 class="post-title">{{ post.title }}</h4>
          <p class="post-date">{{ formatDate(post.created_at) }}</p>
          <div class="post-image" v-if="post.image">
            <img :src="`${post.image}`" alt="img" />
          </div>
          <p class="likes">❤️ {{ post.likes_count }}</p>
          <p class="content">{{ post.content }}</p>
        </RouterLink>
      </div>
    </template>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, watch } from 'vue'
import { format, parseISO, isValid } from 'date-fns'
import { useAccountStore } from '@/stores/accounts'
import { useArticleStore } from '@/stores/articles'

const props = defineProps({
  userId: { type: [String, Number], required: true }
})

const accountStore = useAccountStore()
const articleStore = useArticleStore()

const ARTICLE_API_URL = articleStore.API_URL
const posts = ref([])

async function fetchPosts(id) {
  try {
    const res = await axios.get(
      `${ARTICLE_API_URL}/api/v1/articles/?user=${id}`
    )
    posts.value = res.data
  } catch (e) {
    console.error(e)
  }
}

onMounted(() => {
  fetchPosts(props.userId)
})

watch(
  () => props.userId,
  (newId) => {
    fetchPosts(newId)
  }
)

function formatDate(dateStr) {
  if (!dateStr) return '-'
  const d = parseISO(dateStr)
  return isValid(d) ? format(d, 'yyyy-MM-dd') : '-'
}
</script>

<style scoped>
.post-feed {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.post-card {
  background: #3C3B3B;
  border-radius: 8px;
  padding: 1rem;
}
.post-card a {
  text-decoration: none;
  color: white;
}

.post-title {
  margin: 0;
  font-size: 1.4rem;
}
.post-date {
  margin: 0.25rem 0;
  color: white;
}
.post-image img {
  width: 100%;
  height: auto;
  border-radius: 4px;
  margin: 0.5rem 0;
}
.likes {
  margin: 0.5rem 0;
  font-weight: 500;
}
.content {
  margin: 0;
  color: white;
}

.empty-message {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  text-align: center;
  color: #555;
}
.empty-message h3 {
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}
.create-button {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: #3b82f6;
  color: #fff;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 500;
  transition: background-color 0.2s;
}
.create-button:hover {
  background-color: #2563eb;
}
</style>
