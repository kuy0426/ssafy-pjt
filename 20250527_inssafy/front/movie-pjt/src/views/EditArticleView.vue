<template>
  <div class="article-form-container">
    <form class="article-form" @submit.prevent="updateArticle">
      <h1>게시글 수정하기</h1>

      <label for="title">제목</label>
      <input type="text" id="title" v-model.trim="title" placeholder="제목을 입력하세요"/>
      
      <label for="content">내용</label>
      <textarea id="content" v-model.trim="content" placeholder="내용을 입력하세요"></textarea>

      <label for="image">사진 첨부</label>
      <input type="file" id="image" accept="image/*" @change="onFileChange"
      />

      <div class="form-actions">
        <button type="button" class="btn btn-secondary" @click="router.back()">
          취소
        </button>
        <button type="submit" class="btn btn-primary">
          등록
        </button>
      </div>
    </form>
    <div class="article-preview">
      <div class="preview-box">
        <p>Image Preview</p>
        <div class="preview-image-container">
          <img
            v-if="previewUrl"
            :src="previewUrl"
            alt="이미지 미리보기"
            class="preview-image"
          />
          <div v-else class="preview-placeholder">
            이미지가 여기에 표시됩니다
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useArticleStore } from '@/stores/articles'
  import { useRouter, useRoute } from 'vue-router'

  const store = useArticleStore()
  const route = useRoute()
  const router = useRouter()

  const articleId = route.params.id

  onMounted(async () => {  
    try{
     const article = await store.getArticle(articleId)
      console.log(article)
      title.value = article.title
      content.value = article.content
      previewUrl.value = article.image
        ? `${store.API_URL}${article.image}`
        : null
    } catch(e) {
      console.error('게시글 로드 실패:', e)
    }
  })

  const title = ref(null)
  const content = ref(null)
  const imageFile = ref(null)
  const previewUrl = ref(null)

  function onFileChange(event) {
    const file = event.target.files[0]
    if (file) {
      imageFile.value = file
      previewUrl.value = URL.createObjectURL(file)
    } else {
      imageFile.value = null
      previewUrl.value = null
    }
  }

  const updateArticle = async () => {
    const payload = {
      id:  articleId,
      title: title.value,
      content: content.value,
      imageFile: imageFile.value,
    }
    await store.updateArticle(payload)
    router.push( { name: 'CommunityView'})
  }
</script>

<style src='@/assets/css/createArticle.css' scoped></style>