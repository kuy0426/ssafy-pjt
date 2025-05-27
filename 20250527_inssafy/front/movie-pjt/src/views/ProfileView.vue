<template>
  <div v-if="user" class="profile-view">
    <h1>{{ isMine ? '내 프로필' : user.username + '님의 프로필' }}</h1>
    
    <div class="left-col">
      <ProfileInfo :user="user" :isMine="isMine" />

      <!-- 이 링크가 카드 바로 아래, 컬럼 중앙에 위치합니다 -->
      <a v-if="isMine" class="edit-btn" @click="showEdit=true">Edit Profile</a>
      <EditProfileModal 
      :show="showEdit" 
      @close="showEdit = false" 
      />
    </div>

    <!-- 3) 오른쪽: 포스트 목록 -->
    <PostFeed :key="user.id + '-' + Date.now()" :userId="user.id" />
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { ref, onMounted, watch, computed } from 'vue'
  import { useRoute, useRouter, RouterLink } from 'vue-router'
  import { useAccountStore } from '@/stores/accounts'

  import ProfileInfo from '@/components/ProfileInfo.vue'
  import PostFeed    from '@/components/PostFeed.vue'
  import EditProfileModal from '@/components/EditProfileModal.vue'

  const route = useRoute()
  const store = useAccountStore()

  const user = ref(null)
  const isMine = computed(() => {
    const paramId = route.params.id      // URL 에서 온 값
    if (paramId) {
      // paramId 가 있으면: “paramId === 내 ID” 인지 체크
      return String(paramId) === String(store.user?.id)
    }
    // paramId 없으면, 로그인 상태면 내 프로필
    return !!store.token
  })

  async function fetchUser(paramId) {
    try {
      // 1) “다른 사람 프로필” 로직
      if (paramId && String(paramId) !== String(store.user?.id)) {
        user.value = await store.getUser(paramId)
        return
      }

      // 2) “내 프로필” 로직
      if (!store.token) {
        // 로그인 안 되어 있으면 내 프로필 불가 → 로그인 페이지로
        return router.push({ name: 'LoginView' })
      }
      user.value = await store.getMyProfile()
    }
    catch (err) {
      console.error('프로필 조회 중 에러:', err)
    }
  }

  onMounted(() => fetchUser(route.params.id))

  watch(
    () => route.params.id,
    newId => {
      fetchUser(newId)
    }
  )

  const showEdit = ref(false)
</script>

<style scoped>
  .profile-view {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 2rem;
  }

  .profile-view > h1 {
    grid-column: 1 / -1;
    margin: 0 0 1rem;
  }

  .left-col {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  /* 카드 바로 아래 중앙에 살짝 여백 주기 */
  .edit-btn {
    margin-top: 1rem;
    text-decoration: none;
    font-weight: 500;
    color: white;
    align-self: flex-end;
  }
  /* hover 스타일도 필요하면 추가 */
  .edit-btn:hover {
    text-decoration: underline;
  }
</style>