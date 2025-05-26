<template>
  <div class="profile-info-card">
    <div class="avatar-wrapper">
      <img :src="avatarUrl" alt="profile image" class="avatar" />
    </div>
    <h3 class="username">{{ user.username }}</h3>
    <p class="joined">Joined: {{ formatDate(user.date_joined) }}</p>
    <p class="bio" v-if="user.biography">{{ user.biography }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { format, parseISO, isValid } from 'date-fns'
import { useAccountStore } from '@/stores/accounts'
import { useRoute, RouterLink } from 'vue-router'

const props = defineProps({
  user: { type: Object, required: true },
  isMine: { type: Boolean, required: true }
})

const store = useAccountStore()
const STATIC_BASE = 'http://127.0.0.1:8000/static/images'

const avatarUrl = computed(() => {
  console.log(props.user)
  const img = props.user.profile_image
  return img ? `${store.API_URL}${img}` : `${STATIC_BASE}/noProfile.png`
})

function formatDate(dateStr) {
    if (!dateStr) return '-'
    const d = parseISO(dateStr)
    return isValid(d) ? format(d, 'yyyy-MM-dd') : '-'
  }
</script>

<style scoped>
  .profile-info-card {
    background: #f5f7fa;
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
  .joined { margin: .25rem 0; color: #555; }
  .bio { margin-top: .75rem; color: #333; }
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
