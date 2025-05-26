<template>
  <div class="row">
    <div class="cell title">{{ article.title }}</div>
    <div class="cell author">{{ article.author }}</div>
    <div class="cell date">{{ formatDate(article.created_at) }}</div>
    <div class="cell like">15</div>
  </div>
</template>

<script setup>
  import { format, parseISO, isValid } from 'date-fns'

  function formatDate(val) {
    if (!val) return '-'
    const date = typeof val === 'string'
      ? parseISO(val)
      : val instanceof Date
        ? val
        : null

    return date && isValid(date)
      ? format(date, 'yyyy-MM-dd')
      : '-'
  }
  
  defineProps({
    article: Object
  })
</script>

<style scoped>
  .cell {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
</style>
