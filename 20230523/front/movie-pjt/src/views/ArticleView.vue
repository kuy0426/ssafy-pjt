<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name:'CreateView' }">
      [CREATE]
    </RouterLink>
    <hr>
    <ArticleList :articles="articles"/>
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

<style>

</style>

