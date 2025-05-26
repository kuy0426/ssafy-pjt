<template>
  <div class="community-page">
    <header class="community-header">
      <h2 class="title">BaBoss Talk</h2>
    </header>
    <RouterLink :to="{ name: 'CreateView' }" class="btn-create">
      CREATE
    </RouterLink>
    <hr />
    <ArticleList :articles="articles" />
  </div>
</template>

<script setup>
  import { onMounted, watch, computed } from 'vue'
  import { useArticleStore } from '@/stores/articles.js'
  import { useAccountStore } from '@/stores/accounts.js'
  import { RouterLink } from 'vue-router'
  import ArticleList from '@/components/ArticleList.vue'

  const store = useArticleStore()
  const accountStore = useAccountStore()

  onMounted(() => {
    store.getArticles()
  })

  watch(
    () => accountStore.token,
    token => {
      if (token) store.getArticles()
    },
    { immediate: false }
  )

  const articles = computed(() => store.articles)
</script>

<style scoped>
  .community-page {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem 1rem;
  }

  .btn-create {
    display: inline-block;
    margin: 1rem 0;
    padding: 0.35rem 0.75rem;
    background-color: #2563eb;
    color: white;
    border-radius: 4px;
    text-decoration: none;
  }

  .btn-create:hover {
    background-color: #1e40af;
  }

  hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 1rem 0;
  }
</style>
