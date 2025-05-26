<template>
  <div class="community-page">
    <header class="community-header">
      <h2 class="title">BaBoss Talk</h2>
    </header>
    <RouterLink :to="{ name: 'CreateView' }" class="btn-create">
      <svg viewBox="-0.5 -0.5 24 24" xmlns="http://www.w3.org/2000/svg" width="24" height="24">
       <path d='M21.289.98l.59.59c.813.814.69 2.257-.277 3.223L9.435 16.96l-3.942 1.442c-.495.182-.977-.054-1.075-.525a.928.928 0 0 1 .045-.51l1.47-3.976L18.066 1.257c.967-.966 2.41-1.09 3.223-.276zM8.904 2.19a1 1 0 1 1 0 2h-4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-4a1 1 0 0 1 2 0v4a4 4 0 0 1-4 4h-12a4 4 0 0 1-4-4v-12a4 4 0 0 1 4-4h4z' 
       stroke = 'none'
       fill = 'gray'
       />
      </svg>
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

<style src="@/assets/css/community.css" scoped />
