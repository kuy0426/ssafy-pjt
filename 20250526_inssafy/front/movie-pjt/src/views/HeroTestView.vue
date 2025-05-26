<!-- src/views/HeroTestView.vue -->
<template>
  <div class="hero-test-page">
    <!-- 1) 로봇 + 말풍선 -->
    <div class="thinker-wrap">
      <img src="@/assets/robot.png" alt="Robot" class="robot-img" />
      <!-- 말풍선 활성화하려면 아래 주석 해제 -->
      <!-- <div class="speech-bubble">Thinking...</div> -->
    </div>

    <!-- 2) 질문 박스 -->
    <div v-if="step < questions.length" class="result-container">
      <div class="chat-box">
        <div class="avatar">🤖</div>
        <div class="bubble">
          <p class="question-text">{{ questions[step] }}</p>
          <div class="options">
            <button
              v-for="opt in options[step]"
              :key="opt.letter"
              class="btn btn-outline-primary option-btn"
              @click="select(opt.letter)"
            >
              {{ opt.letter }}. {{ opt.label }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- 3) 결과 박스 -->
    <div v-else class="result-container">
      <div class="chat-box">
        <div class="avatar">🤖</div>
        <div class="bubble">
          <h5>✨ {{ resultMap[resultLetter].label }} ✨</h5>
          <p>{{ resultMap[resultLetter].message }}</p>
          <div class="movie-list">
            <router-link
              v-for="m in recommended.slice(0,4)"
              :key="m.id"
              :to="{ name: 'MovieDetailView', params: { id: m.id } }"
              class="movie-card"
            >
              <img
                v-if="m.poster_path"
                :src="`https://image.tmdb.org/t/p/w300${m.poster_path}`"
                :alt="m.original_title"
                class="card-img"
              />
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- 4) 액션 버튼 -->
    <div class="action-buttons">
      <button
        class="btn"
        style="background-color: #800080; color: #fff;"
        @click="restart"
      >
        다시하기
      </button>
      <button
        class="btn btn-secondary"
        style="background-color: #800080; color: #fff;"
        @click="goHome"
      >
        Home
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { fetchMoviesByGenre } from '@/api/movie.js'

// 1) 질문 & 선택지
const questions = [
  '1. 문제가 생겼을 때 당신의 1차 대응 방식은?',
  '2. 새로운 사람들과 처음 만났을 때 당신의 태도는?',
  '3. 좋아하는 활동을 고른다면?',
  '4. 당신에게 동기를 부여하는 건?',
  '5.	휴식이 필요할 때 당신의 방식은?'
]
const options = [
  [
    { letter: 'A', label: '즉시 행동으로 돌파한다' },
    { letter: 'B', label: '주변의 도움을 구해 함께 해결한다' },
    { letter: 'C', label: '계획표를 짜고 단계별로 대응한다' },
    { letter: 'D', label: '잠시 감정 정리 시간을 가진 뒤 해결책을 고민한다' },
  ],
  [
    { letter: 'A', label: '대화를 주도한다' },
    { letter: 'B', label: '공통점을 찾는다' },
    { letter: 'C', label: '관찰 후 말한다' },
    { letter: 'D', label: '느긋하게 분위기 파악 후 편한 순간에 이야기한다' },
  ],
  [
    { letter: 'A', label: '번지점프·스카이다이빙 같은 액티비티' },
    { letter: 'B', label: '친구들과 함께 즐기는 레이저 태그·서바이벌' },
    { letter: 'C', label: '방탈출 게임 등 논리·퍼즐 풀기' },
    { letter: 'D', label: '야경 감상이나 명상·요가 세션' },
  ],
  [
    { letter: 'A', label: '새로운 도전' },
    { letter: 'B', label: '동료의 인정과 응원' },
    { letter: 'C', label: '논리적 성취와 문제해결' },
    { letter: 'D', label: '노력해온 과정' },
  ],
  [
    { letter: 'A', label: '운동과 액티비티로 에너지 분출' },
    { letter: 'B', label: '친구들과 수다 떨며 스트레스 해소' },
    { letter: 'C', label: '계획적인 스케줄작성으로 힐링' },
    { letter: 'D', label: '책, 음악, 영화 감상하며 감성을 충전' },
  ],
]

// 2) 결과 매핑 ← 여기에 genreId 추가!
const resultMap = {
  A: {
    label: 'S/F 추천',
    message: '공상과학 영화를 추천드립니다.',
    genreId: 878    // SF
  },
  B: {
    label: 'Action 추천',
    message: '액션 영화를 추천드립니다.',
    genreId: 28     // 액션
  },
  C: {
    label: 'Crime 추천',
    message: '범죄 스릴러를 추천드립니다.',
    genreId: 80     // 범죄
  },
  D: {
    label: 'Comedy 추천',
    message: '코미디 영화를 추천드립니다.',
    genreId: 35     // 코미디
  },
}

const step = ref(0)
const answers = ref([])

// 3) 선택 핸들러
function select(letter) {
  answers.value.push(letter)
  step.value++
  if (step.value === questions.length) {
    loadRecommended()
  }
}

// 4) 결과 알파벳 계산
const resultLetter = computed(() => {
  const counts = answers.value.reduce((acc, l) => {
    acc[l] = (acc[l] || 0) + 1
    return acc
  }, {})
  return Object.entries(counts)
    .sort(([,a],[,b]) => b - a)[0][0]
})

// 5) 추천 영화 불러오기
const recommended = ref([])
async function loadRecommended() {
  const info = resultMap[resultLetter.value]
  if (!info) return
  const all = await fetchMoviesByGenre(info.genreId, 1)
  // 랜덤으로 섞고 앞 4개만
  for (let i = all.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[all[i], all[j]] = [all[j], all[i]]
  }
  recommended.value = all.slice(0, 4)
}

// 6) 버튼
const router = useRouter()
function restart() {
  step.value = 0
  answers.value = []
  recommended.value = []
}
function goHome() {
  router.push({ name: 'MainView' })
}
</script>

<style scoped>
.hero-test-page {
  padding: 2rem;
  background: #f0efff;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

/* 1) 로봇 & 말풍선 */
.thinker-wrap {
  position: relative;
}
.robot-img {
  width: 120px;
}
/* .speech-bubble { … } */

/* 2) 질문 & 결과 박스 */
.result-container {
  width: 100%;
  max-width: 600px;
  background: #e6eafa;
  border-radius: 12px;
  padding: 1.5rem;
}
.chat-box {
  display: flex;
  gap: 1rem;
}
.avatar {
  width: 32px; height: 32px;
  background: #4b0082; color: #fff;
  display: flex; align-items: center; justify-content: center;
  border-radius: 50%;
}
.bubble {
  background: #fff;
  border-radius: 8px;
  padding: 1rem;
  flex: 1;
}
.options { display: flex; flex-direction: column; gap: .5rem; }
.option-btn { text-align: left; }

/* 3) 영화 리스트 */
.movie-list {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
  overflow-x: auto;
}
.movie-card {
  flex: 0 0 auto;
}
.card-img {
  width: 100px;
  height: 150px;
  object-fit: cover;
  border-radius: 8px;
}

/* 4) 버튼 */
.action-buttons {
  display: flex;
  gap: 1rem;
  padding-top: 1rem;
}
</style>
