<!-- src/views/HeroMatchView.vue -->
<template>
  <div class="hero-match-page">
    <div class="chat-wrapper">
      <!-- 1) 메시지 리스트 -->
      <div class="chat-container">
        <div 
          v-for="(msg, idx) in messages" 
          :key="idx"
          :class="['message', msg.from]"
        >
          <p v-if="msg.from==='ai'">{{ msg.content }}</p>
          <div v-else class="bubble">{{ msg.content }}</div>
        </div>
      </div>

      <!-- 2) 입력창 + 전송 버튼 -->
      <div class="input-area">
        <input 
          v-model="input" 
          @keyup.enter="send" 
          placeholder="메시지를 입력하세요…" 
        />
        <button @click="send">➤</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const messages = ref([
  {
    from: 'ai',
    content: `Q1. 친구들과 큰 여행을 떠난다면 당신은?
A. 미리 루트를 짜두고 강행군한다
B. 함께 어울리며 당일 계획을 유동적으로 바꾼다
C. 여행지 정보를 철저히 조사한 뒤 한발짝씩 움직인다
D. 여행보다 현지 풍경·사람을 느끼며 여유로운 일정을 즐긴다`
  },
  { from: 'user', content: 'A' },
  {
    from: 'ai',
    content: `Q2. 새로운 사람들과 처음 만났을 때 당신의 태도는?
A. 적극적으로 다가가 대화를 주도한다
B. 서로 소개하며 공통점을 찾아 친해진다
C. 상대를 관찰하며 대화 포인트를 신중히 고른다
D. 느긋하게 분위기 파악 후 편한 순간에 이야기한다`
  },
  { from: 'user', content: 'D' },
  {
    from: 'ai',
    content: `추천: 도전·모험형
1. Indiana Jones (1981) – 고고학적 탐험과 스릴!
2. Mission: Impossible – 액션과 서스펜스!
3. Tomb Raider – 여성 주인공의 탐험 어드벤처!`
  }
])

const input = ref('')

function send() {
  if (!input.value.trim()) return
  messages.value.push({ from: 'user', content: input.value })
  input.value = ''
  // GPT 호출 로직을 이곳에 추가하세요.
}
</script>

<style scoped>
.hero-match-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

/* global-header 높이 만큼 아래에서 시작 */
.chat-wrapper {
  flex: 1;
  margin-top: 56px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* ── 메시지 리스트 ── */
.chat-container {
  flex: 1;
  width: 80%;
  max-width: 800px;
  background: #e0dbff;
  margin: 0;
  padding: 12px;
  overflow-y: auto;
  border-radius: 16px 16px 0 0;
}

.message {
  display: flex;
  margin-bottom: 8px;
}
.message.ai {
  justify-content: flex-start;
}
.message.ai p {
  background: #f9f9ff;
  padding: 8px;
  border-radius: 8px;
  white-space: pre-wrap;
}
.message.user {
  justify-content: flex-end;
}
.message.user .bubble {
  background: #4e70ff;
  color: #fff;
  padding: 6px 10px;
  border-radius: 16px;
  max-width: 60%;
  word-break: break-word;
}

/* ── 입력창 + 전송 버튼 ── */
.input-area {
  width: 80%;
  max-width: 800px;
  display: flex;
  align-items: center;
  background: #fff;
  margin: 0 auto 32px;       /* ← 아래 여백을 32px로 증가 */
  padding: 6px 10px;
  border-radius: 0 0 16px 16px;
  box-shadow: 0 -1px 4px rgba(0,0,0,0.05);
}

.input-area input {
  flex: 1;
  height: 36px;
  padding: 4px 8px;
  border: 1px solid #ccc;
  border-radius: 16px;
  outline: none;
}

.input-area button {
  background: #4e70ff;
  border: none;
  color: #fff;
  margin-left: 6px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 1.1rem;
  line-height: 1;
}
</style>
