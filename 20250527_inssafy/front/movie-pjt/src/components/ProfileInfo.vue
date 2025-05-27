<template>
  <div class="profile-info-card">
    <div class="avatar-wrapper">
      <img :src="avatarUrl" alt="profile image" class="avatar" />
    </div>
    <h3 class="username">{{ displayUser.username }}</h3>
    <p class="joined">Joined: {{ formatDate(displayUser.date_joined) }}</p>
    <p class="bio" v-if="displayUser.biography">{{ displayUser.biography }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { format, parseISO, isValid } from 'date-fns'
import { useAccountStore } from '@/stores/accounts'

const props = defineProps({
  user: { type: Object, required: true },
  isMine: { type: Boolean, required: true }
})

const store = useAccountStore()
const STATIC_BASE = 'http://127.0.0.1:8000/static/images'
const BASE_URL = 'http://127.0.0.1:8000'

const displayUser = computed(() =>
  props.isMine ? store.user : props.user
)

const avatarUrl = computed(() => {
  const img = displayUser.value.profile_image
  return img ? `${BASE_URL}${img}` : `${STATIC_BASE}/noProfile.png`
})

function formatDate(dateStr) {
    if (!dateStr) return '-'
    const d = parseISO(dateStr)
    return isValid(d) ? format(d, 'yyyy-MM-dd') : '-'
  }
</script>

<style scoped>
  .profile-info-card {
    max-width: 100%;
    width: 100%;
    background: #21201E;
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
    }
  .avatar-wrapper {
    width: 70%;
    aspect-ratio: 1 / 1; 
    margin: 0 auto 1rem;
    border-radius: 70%;
    overflow: hidden;
    background: #e2e8f0;
  }
  .avatar { width: 100%; height: 100%; object-fit: cover; }
  .username { margin: .5rem 0; font-size: 1.25rem; }
  .joined { margin: .25rem 0; color: #777; }
  .bio { margin-top: .75rem; color: white; }
  .edit-btn {
    display: inline-block;
    margin-top: 1rem;
    padding: .5rem 1rem;
    background: #3b82f6;
    color: white;
    border-radius: 4px;
    text-decoration: none;
  }
</style>
