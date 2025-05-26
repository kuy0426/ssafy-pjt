<template>
  <div class="profile-edit">
    <h1>프로필 수정</h1>
    <form @submit.prevent="updateProfile">
      <div class="form-group">
        <label for="biography">한 줄 소개</label>
        <textarea
          id="biography"
          v-model="biography"
          placeholder="한 줄 소개를 입력하세요"
          rows="3"
        ></textarea>
      </div>

      <div class="form-group">
        <label for="profile_image">프로필 사진</label>
        <input
          id="profile_image"
          type="file"
          accept="image/*"
          @change="onFileChange"
        />
        <div v-if="preview" class="preview-wrapper">
          <img :src="preview" alt="이미지 미리보기" class="preview-img" />
        </div>
      </div>

      <button type="submit">저장</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useAccountStore } from '@/stores/accounts'

const accountStore = useAccountStore()
// 백엔드 API 기준 URL
const BASE_URL = 'http://127.0.0.1:8000/accounts'

const biography = ref('')
const file = ref(null)
const preview = ref(null)

async function fetchProfile() {
  try {
    const res = await axios.get(`${BASE_URL}`, {
      headers: { Authorization: `Token ${accountStore.token}` }
    })
    biography.value = res.data.biography || ''
    if (res.data.profile_image) {
      // MEDIA_URL 설정에 따라 조정
      preview.value = `http://127.0.0.1:8000${res.data.profile_image}`
    }
  } catch (err) {
    console.error('프로필 조회 에러:', err)
  }
}

function onFileChange(e) {
  const selected = e.target.files[0]
  if (selected) {
    file.value = selected
    preview.value = URL.createObjectURL(selected)
  }
}

async function updateProfile() {
  const formData = new FormData()
  formData.append('biography', biography.value)
  if (file.value) {
    formData.append('profile_image', file.value)
  }

  try {
    const res = await axios.patch(
      `${BASE_URL}/user_info/`,
      formData,
      {
        headers: {
          Authorization: `Token ${accountStore.token}`,
          'Content-Type': 'multipart/form-data'
        }
      }
    )
    // 성공 메시지나 리다이렉트 처리 등
    console.log('프로필 업데이트 완료:', res.data)
  } catch (err) {
    console.error('프로필 업데이트 에러:', err)
  }
}

onMounted(fetchProfile)
</script>

<style scoped>
.profile-edit { max-width: 500px; margin: auto; }
.form-group { margin-bottom: 1rem; }
.preview-wrapper { margin-top: 0.5rem; }
.preview-img {
  width: 120px; height: 120px;
  object-fit: cover;
  border-radius: 50%;
}
button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
