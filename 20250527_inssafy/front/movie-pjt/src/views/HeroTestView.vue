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
              class="btn btn-outline-dark option-btn"
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
          <p v-html="resultMap[resultLetter].message"></p>
          <div class="movie-list">
            <router-link
              v-for="m in recommended.slice(0,6)"
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
  '1. 문제를 직면했을 때, 당신의 대처 방식은?',
  '2. 당신의 평소 성격에 가장 가까운 것은?',
  '3. 진짜 영화 같다. 라고 느껴지는 상황은?',
  '4. 다음 중 당신이 직접 겪는다면, 가장 오래 기억에 남을 장면은?',
  '5.	당신의 스트레스 해소 방식은?'
]
const options = [
  [
    { letter: 'A', label: '새로운 방식이 없을까? 논리보다 상상을 우선시함.' },
    { letter: 'B', label: '곧장 몸이 먼저 반응한다. 고민은 사치' },
    { letter: 'C', label: '상황을 분석하고, 원인을 따져서 계획부터 세운다.' },
    { letter: 'D', label: '웃음으로 불안함을 잠깐이라도 탈출하려 한다.' },
  ],
  [
    { letter: 'A', label: '호기심 많고 종종 말이 안 되는 상상도 진지하게 한다.' },
    { letter: 'B', label: '단체 활동을 즐기고, 리더 역할을 자주 맡는다.' },
    { letter: 'C', label: '조용하지만 예리하고, 사람 관찰하는 것을 좋아한다.' },
    { letter: 'D', label: '내가 없으면 안돼! 분위기 메이커 역할이다.' },
  ],
  [
    { letter: 'A', label: '갑자기 하늘이 이상하게 변하고 사람들이 그것을 못 본 척할 때' },
    { letter: 'B', label: '엘리베이터 문이 열리자마자 싸움이 터질 때' },
    { letter: 'C', label: '평소 조용한 친구가 무엇을 숨기고 있는 것을 느낄 때' },
    { letter: 'D', label: '중요한 순간 누군가 진지한 표정으로 바나나 껍질을 밟을 때' },
  ],
  [
    { letter: 'A', label: '"사실 당신은 실험체였습니다."라는 말을 듣고 어릴적 기억들이 퍼즐처럼 맞춰질 때' },
    { letter: 'B', label: '다 끝난 줄 알았지만, 갑자기 "아직 안 끝났어"하고 등장하는 장면' },
    { letter: 'C', label: '모든 퍼즐이 하나로 연결되고 범인을 알게되는 순간' },
    { letter: 'D', label: '누가봐도 망한 상황인데, 내가 너무 진지해서 상황이 웃길 때' },
  ],
  [
    { letter: 'A', label: '다른 세상을 상상하며 현실에서 잠깐 벗어난다.' },
    { letter: 'B', label: '운동과 같이 활동적인 것을 한다.' },
    { letter: 'C', label: '무언가를 정리하며 마음을 가라앉힌다.' },
    { letter: 'D', label: '웃긴 콘텐츠를 찾아 기분을 전환한다.' },
  ],
]

// 2) 결과 매핑 ← 여기에 genreId 추가!
const resultMap = {
  A: {
    label: 'S/F 영화 처방전',
    message: `당신은 현실에선 살짝 지루해하는 타입.<br>
우주든 시간 여행이든, 상상력에 엔진 달아주는 S/F 영화가 필요해요.<br>
내일보다 2347년을 생각하는 당신께,<br>
외계인과의 티타임을 추천드립니다 👽`,
    genreId: 878
  },
  B: {
    label: 'Action 영화 처방전',
    message: `멈춰 있는 건 죄! 당신은 인생에서도 영화에서도 스피드를 즐깁니다.<br>
말보단 주먹, 고민보단 폭발, 그리고 적당한 동료애.<br>
심장 박동수를 높이고 싶은 당신께 액션 영화를 처방합니다 💥🦹‍♂️`,
    genreId: 28
  },
  C: {
    label: 'Crime 영화 처방전',
    message: `당신은 세상을 관찰하는 조용한 천재.<br>
단서 하나로 모든 걸 꿰뚫는 그 촉, 아무 영화로는 만족 못 하죠.<br>
반전, 추리, 심리전… 이 모든 걸 갖춘 범죄 영화로<br>
당신의 브레인에 연료를 공급하세요 🕵️‍♂️🔪`,
    genreId: 80
  },
  D: {
    label: 'Comedy 영화 처방전',
    message: `당신은 분위기를 띄우는 인간 탄산수.<br>
진지한 건 10분 이상 못 버티고, 웃음이 있어야 인생이 굴러갑니다.<br>
재치, 뻘소리, 엉뚱한 상황 속 진심—<br>
코미디 영화가 당신의 에너지 드링크입니다 🤣🎉`,
    genreId: 35
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
  recommended.value = all.slice(0, 6)
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
  background: #363274;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  border-radius: 16px; ;
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
  max-width: 800px;
  background: #5a5697;
  border-radius: 12px;
  padding: 2rem;
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
  background: #eee8fa;
  border-radius: 12px;
  padding: 1.5rem;           /* 여백 늘림 */
  flex: 1;
  color: #222;
  font-size: 1.1rem;         /* 글자 살짝 키움 */
  line-height: 1.8;          /* 줄 간격 여유 있게 */
  max-width: 700px;          /* 전체 박스 크기 늘림 */
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

.question-text {
  color: #222 !important;
}
/* 옵션 버튼 글자·테두리색 더 진하게 */
.option-btn {
  /* btn-outline-dark 쓴 경우 이 부분 없어도 되지만, 더 조절하고 싶다면: */
  color: #030303;
  border-color: #a970f3;
}
.option-btn:hover,
.option-btn:focus {
  background-color: #822ab4;
  color: #fff;
  border-color: #822ab4;
}
</style>
