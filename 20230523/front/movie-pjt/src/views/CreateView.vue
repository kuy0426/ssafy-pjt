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
import axios from 'axios'
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { useAccountStore } from '@/stores/accounts'
import { useRouter } from 'vue-router'

const store = useArticleStore()
const accountStore = useAccountStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)
const imageFile = ref(null)


function onFileChange(event) {
  imageFile.value = event.target.files[0]  || null
}

const createArticle = function () {
  const formData = new FormData()

  formData.append('title', title.value)
  formData.append('content', content.value)
  if (imageFile.value) {
    formData.append('image', imageFile.value)
  }

  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: formData,
    headers: {
      'Authorization' : `Token ${accountStore.token}`,
      'Content-Type': 'multipart/form-data'
    }
  })
    .then(() => {
      router.push({name: 'ArticleView'})
    })
    .catch(err => console.log(err))
}
</script>

<style>

</style>
