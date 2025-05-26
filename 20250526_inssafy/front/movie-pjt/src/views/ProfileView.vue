<template>
  <div v-if="user" class="profile-view">
    <h1>{{ isMine ? '내 프로필' : user.username + '님의 프로필' }}</h1>
    
    <div class="left-col">
      <ProfileInfo :user="user" :isMine="isMine" />

      <!-- 이 링크가 카드 바로 아래, 컬럼 중앙에 위치합니다 -->
      <RouterLink v-if="isMine" class="edit-btn" :to="{ name: 'EditProfile' }">Edit Profile</RouterLink>
    </div>

    <!-- 3) 오른쪽: 포스트 목록 -->
    <PostFeed :userId="user.id" />
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { ref, onMounted, watch } from 'vue'
  import { useRoute, RouterLink } from 'vue-router'
  import { useAccountStore } from '@/stores/accounts'

  import ProfileInfo from '@/components/ProfileInfo.vue'
  import PostFeed    from '@/components/PostFeed.vue'

  const route = useRoute()
  const store = useAccountStore()

  const user = ref(null)
  const isMine = ref(!route.params.id)

  async function fetchUser(id) {
    if (!id) {
      user.value = store.user
    } else {
      try {
        const res = await axios.get(
          `${store.ACCOUNT_API_URL}/profile/${id}`
        )
        user.value = res.data
      } catch (e) {
        console.error(e)
      }
    }
  }

  onMounted(() => {
    fetchUser(route.params.id)
  })

  watch(
    () => route.params.id,
    newId => {
      isMine.value = !newId
      fetchUser(newId)
    }
  )
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
    color: #333;
    align-self: flex-end;
  }
  /* hover 스타일도 필요하면 추가 */
  .edit-btn:hover {
    text-decoration: underline;
  }
</style>