<!-- src/views/HeroTestView.vue -->
<template>
  <div class="hero-test-wrap">


    <div class="chat-container">
      <!-- 타이틀 -->
      <header class="chat-header">
        <h1>Hero Match</h1>
      </header>

      <!-- 메시지 리스트 -->
      <section class="chat-messages">
        <div
          v-for="(msg, idx) in messages"
          :key="idx"
          :class="['chat-msg', msg.from === 'ai' ? 'ai' : 'user']"
        >
          <div class="avatar">{{ msg.from === 'ai' ? 'AI' : 'You' }}</div>
          <div class="bubble">{{ msg.text }}</div>
        </div>
      </section>

      <!-- 입력창 + 전송 -->
      <footer class="chat-input">
        <input
          v-model="inputText"
          @keyup.enter="sendMessage"
          type="text"
          placeholder="Type your message..."
        />
        <button @click="sendMessage">▶︎</button>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 초기 AI 질문들
const messages = ref([
  {
    from: 'ai',
    text: `Q. 친구들과 큰 여행을 떠난다면 당신은?  
A. 미리 루트·일정을 정해두고 계획적으로 움직인다  
B. 함께 의견 나누며 당일 계획을 유동적으로 바꾼다  
C. 여행지 정보를 철저히 조사한 뒤 한발짝씩 움직인다  
D. 여행보다 현지 풍경·사람을 느끼며 여유로운 일정을 즐긴다`
  },
  {
    from: 'ai',
    text: `Q. 새로운 사람들과 처음 만났을 때 당신의 태도는?  
A. 적극적으로 다가가 대화를 주도한다  
B. 서로 소개하며 공통점을 찾아 친해진다  
C. 상대를 관찰하며 대화 포인트를 신중히 고른다  
D. 느긋하게 분위기 파악 후 편한 순간에 이야기한다`
  }
])

const inputText = ref('')

// 메세지 전송 핸들러
function sendMessage() {
  const text = inputText.value.trim()
  if (!text) return

  // 1) 유저 메세지 추가
  messages.value.push({ from: 'user', text })
  inputText.value = ''

  // 2) AI 답변 더미
  setTimeout(() => {
    messages.value.push({
      from: 'ai',
      text: `추천: '도전·모험형' 사용자님께 드리는 영화 리스트입니다!  
1. 인디아나 존스 (Indiana Jones: Raiders of the Lost Ark, 1981)  
2. 미션 임파서블 (Mission: Impossible – Fallout, 2018)  
3. 툼 레이더 (Tomb Raider, 2018)`
    })

    // 자동 스크롤
    scrollToBottom()
  }, 500)
}

// 메시지 영역 스크롤
function scrollToBottom() {
  requestAnimationFrame(() => {
    const el = document.querySelector('.chat-messages')
    el.scrollTop = el.scrollHeight
  })
}

// 페이지 로드 시 자동 스크롤
onMounted(scrollToBottom)
</script>

<style scoped>
.hero-test-wrap {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f5f5f5;
  overflow: hidden;
}

.navbar {
  font-weight: bold;
}

.chat-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  margin: 1rem;
  background: #e6e6fa;
  border-radius: 8px;
  overflow: hidden;
}

.chat-header {
  background: #4b0082;
  color: white;
  text-align: center;
  padding: 0.75rem;
}

.chat-messages {
  flex: 1;
  padding: 1rem;
  overflow-y: auto;
}

.chat-msg {
  display: flex;
  margin-bottom: 0.75rem;
  align-items: flex-start;
}
.chat-msg .avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #4b0082;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  margin-right: 0.5rem;
}
.chat-msg.ai .bubble {
  background: white;
  color: black;
}
.chat-msg.user {
  flex-direction: row-reverse;
}
.chat-msg.user .avatar {
  background: #6c757d;
  margin-right: 0;
  margin-left: 0.5rem;
}
.chat-msg .bubble {
  max-width: 75%;
  padding: 0.5rem 0.75rem;
  border-radius: 12px;
  background: #dcdcff;
  white-space: pre-wrap;
}

.chat-input {
  display: flex;
  border-top: 1px solid #ccc;
}
.chat-input input {
  flex: 1;
  border: none;
  padding: 0.75rem;
  font-size: 1rem;
  outline: none;
  background: white;
}
.chat-input button {
  width: 3rem;
  border: none;
  background: #4b0082;
  color: white;
  font-weight: bold;
  cursor: pointer;
}
</style>
