<!-- src/components/ProfileEditModal.vue -->
<template>
  <Teleport to="body">
    <div v-if="show" class="modal-overlay" @click.self="handleClose">
      <div class="modal-window">
        <button class="modal-close" @click="handleClose">×</button>
        <div class="profile-edit">
          <h1>프로필 수정</h1>
          <form @submit.prevent="onSubmit">
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
      </div>
    </div>
  </Teleport>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useAccountStore } from '@/stores/accounts'

const props = defineProps({
  show: { type: Boolean, required: true }
})
const emit = defineEmits(['close'])

const store     = useAccountStore()
const biography = ref('')
const file      = ref(null)
const preview   = ref(null)
const BASE_URL  = 'http://127.0.0.1:8000'

// 부모가 show를 false로 바꿔서 모달을 닫도록
function handleClose() {
  emit('close')
}

async function loadProfile() {
  try {
    const data = await store.getMyProfile()
    biography.value = data.biography || ''
    preview.value   = data.profile_image
      ? `${BASE_URL}${data.profile_image}`
      : null
  } catch (err) {
    console.error('프로필 로드 실패:', err)
  }
}

function onFileChange(e) {
  const selected = e.target.files[0]
  if (selected) {
    file.value = selected
    preview.value = URL.createObjectURL(selected)
  }
}

async function onSubmit() {
  const payload = {
    biography:     biography.value,
    profile_image: file.value
  }
  try {
    await store.updateProfile(payload)
    alert('프로필이 성공적으로 업데이트되었습니다.')
    emit('close')
  } catch (err) {
    console.error('프로필 업데이트 실패:', err)
    alert('프로필 업데이트에 실패했습니다.')
  }
}

// show가 true로 바뀔 때마다 프로필 로드
watch(() => props.show, val => {
  if (val) loadProfile()
})
</script>

<style src='@/assets/css/editProfileModal.css' scoped></style>
