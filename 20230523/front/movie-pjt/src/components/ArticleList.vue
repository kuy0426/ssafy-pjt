<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
  import { useArticleStore } from '@/stores/articles'
  import ArticleListItem from '@/components/ArticleListItem.vue'

  // const store = useArticleStore()

  defineProps({
    articles: Array
  })
</script>
