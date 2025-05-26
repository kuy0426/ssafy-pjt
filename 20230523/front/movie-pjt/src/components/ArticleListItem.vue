<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <div v-if="article.image">
      <img
        :src="`${store.API_URL}${article.image}`"
        alt="Article Image"
        style="max-width: 100%; height: auto;"
      />
    </div>
    <!-- <RouterLink :to="{ name: 'DetailView', params: { id: article.id } }">
      [DETAIL]
    </RouterLink> -->
    <hr>
  </div>
</template>

<script setup>
  import { useArticleStore } from '@/stores/articles'

  const store = useArticleStore()

  defineProps({
    article: Object
  })
</script>
