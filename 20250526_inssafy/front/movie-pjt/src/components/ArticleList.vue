<template>
  <div class="article-table">
    <div class="row header">
      <div class="cell title">Title</div>
      <div class="cell author">Author</div>
      <div class="cell date">Date</div>
      <div class="cell likes">Likes</div>
  </div>
  <div>
    <ArticleListItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
      @click="goDetail(article.id)"
    />
    </div>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router'
  import ArticleListItem from '@/components/ArticleListItem.vue'

  const router = useRouter() 
  
  defineProps({
    articles: Array
  })

  function goDetail(id) {
    router.push({ name: 'ArticleDetailView', params: { id } })
  }

</script>

<style scoped>
  .article-table {
    border: 1px solid #e5e7eb;
    border-radius: 4px;
    overflow: hidden;
  }
  .row {
    display: grid;
    grid-template-columns: 4fr 1.5fr 2fr 1fr;
    align-items: center;
    padding: 0.75rem 1rem;
    cursor: pointer;
    border-bottom: 1px solid #e5e7eb;
    transition: background 0.1s;
  }

  .row.header {
    background-color: #f3f4f6;
    font-weight: 600;
    cursor: default;
  }
</style>