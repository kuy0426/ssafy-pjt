<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" v-model.trim="content"></textarea><br>
      <label for="image">사진 : </label>
      <input type="file" id="image" accept="image/*" @change="onFileChange">
      <br><br>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useArticleStore } from '@/stores/articles'
  import { useRouter } from 'vue-router'

  const store = useArticleStore()
  const router = useRouter()

  const title = ref(null)
  const content = ref(null)
  const imageFile = ref(null)


  function onFileChange(event) {
    imageFile.value = event.target.files[0]  || null
  }

  const createArticle = async () => {
    const payload = {
      title: title.value,
      content: content.value,
      imageFile: imageFile.value,
    }
    await store.createArticle(payload)
    router.push( { name: 'CommunityView'})
  }
</script>

<style>

</style>
