<template>
  <div class="game-wrapper">
    <!-- 타이핑 게임 영역 -->
    <div class="typing-game-container">
      <h2 style="color:beige;">⌨️ 영화 명대사 타이핑 게임</h2>

      <div class="quote-box">
        <p class="quote">
          <span
            v-for="(char, idx) in currentQuoteChars"
            :key="idx"
            :class="charClass(idx)"
          >
            {{ char }}
          </span>
        </p>
        <p class="movie-title">- {{ currentQuote.movie }} -</p>
      </div>

      <textarea
        v-model="userInput"
        @input="onInput"
        @keydown.enter.prevent="finishGame"
        placeholder="여기에 입력하세요..."
        :disabled="isFinished"
        class="typing-area"
      ></textarea>

      <div class="stats">
        <span style="color:beige;">시간: {{ elapsedTime.toFixed(1) }}초</span>
        <span v-if="isFinished" style="color:beige;">
          정확도: {{ accuracy }}% | WPM: {{ wpm }}
        </span>
      </div>

      <div class="buttons">
        <button @click="restart">다시하기</button>
        <button @click="stopGame" :disabled="isFinished">Stop</button>
      </div>
    </div>

    <!-- 스코어보드 영역 -->
    <div class="scoreboard">
      <h3 style="color:beige;">⏱️ TOP 3</h3>
      <ol>
        <li v-for="(r, i) in topResults" :key="i" style="color:beige;">
           [{{ r.user }}] {{ r.text }}<br />
          <small style="color:beige;">{{ r.time.toFixed(1) }}초</small>
        </li>
        <li v-if="topResults.length === 0" style="color:beige;">아직 기록이 없습니다.</li>
      </ol>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// 1) 하드코딩된 영화 명대사 목록
const quotes = [
  { text: "I'm gonna make him an offer he can't refuse.", movie: 'The Godfather' },
  { text: 'May the Force be with you.', movie: 'Star Wars' },
  { text: "Here's looking at you, kid.", movie: 'Casablanca' },
  { text: 'You talking to me?', movie: 'Taxi Driver' },
  { text: '이게 사람이 할 짓이야?', movie: '살인의 추억' },
  { text: '사는 게 다 그렇지 뭐.', movie: '미나리' },
  { text: '날 쏘고 가라!', movie: '실미도' },
  { text: '내가 니 시다바리가?', movie: '친구' },
  { text: '느그 아부지 뭐하시노', movie: '친구' },
  { text: '묻고 더블로 가!', movie: '타짜' },
  { text: '야 이거 방탄유리야 멋쟁이야!', movie: '아저씨' },
  { text: '꼭 그렇게 다 가져가야만 속이 후련했냐', movie: '해바라기' },
  { text: '어차피 대중들을 개 돼지들입니다.', movie: '내부자들' },
  { text: '아들아, 너는 계획이 다 있구나.', movie: '기생충' },
  { text: '내가 왕이 될 상인가?', movie: '관상' },
  { text: '누구냐 넌?', movie: '올드보이' },
  { text: '어이가 없네', movie: '베테랑' },
  { text: '나 돌아갈래', movie: '박하사탕' },
  { text: '넌 나에게 모욕감을 줬어', movie: '달콤한 인생' },
  { text: '뭣이 중헌디!', movie: '곡성' },
  { text: '지금까지 이런 맛은 없었다. 이것은 갈비인가 통닭인가', movie: '극한직업' },
  { text: '따따따 따 따 따 따따따', movie: '엑시트' },
  { text: 'with great power comes great responsibility', movie: 'Spiderman' },
  { text: 'I want to choose my own path', movie: 'Thor' },
  { text: 'I can do this all day', movie: 'Captain America' },
]

// 2) 익명 닉네임 풀
const ANONYMS = [
  '익명 카페로사 추움','익명 피곤해요','익명 살려주세요',
  '익명 다크서클 울산까지 감', '익명 다리가 저려요','익명 종합병원 몸뚱아리',
  '익명 어지러워요','익명 chatGPT최고다','익명 허리수술비로 탕진','익명 아이디어 고갈',
  '익명 이름뭐할까','익명 디자인귀찮다','익명 한숨나온다','익명 눈물난다','익명 안행복한거같애'
  ,'익명 끝나간다','익명 언제끝나','익명 도망가고싶어요','익명 눈물줄줄','익명 손 얼었어요',
  '익명 코시려워','익명 커피3잔째','익명 마법의 송가락'
]

// reactive state
const currentQuote = ref({ text: '', movie: '' })
const userInput    = ref('')
const startTime    = ref(0)
const elapsedTime  = ref(0)
const isFinished   = ref(false)
// 각 레코드에 { text, time, user }
const records      = ref([])
const tickId = ref(null)


// 랜덤으로 명대사 선택
function pickQuote() {
  const idx = Math.floor(Math.random() * quotes.length)
  currentQuote.value = quotes[idx]
}

// 텍스트 분할
const currentQuoteChars = computed(() => currentQuote.value.text.split(''))

// 3) 타이머 로직: 사용자 첫 입력 시 시작
function onInput() {
  if (!startTime.value) {
    startTime.value = performance.now()
    tick()
  }
}

// tick: requestAnimationFrame 으로 시간 갱신
function tick() {
  if (!isFinished.value) {
    elapsedTime.value = (performance.now() - startTime.value) / 1000
    tickId.value = requestAnimationFrame(tick)  // ✅ 이 줄!
  }
}

// 4) 랜덤 익명 생성기
function getRandomAnonym() {
  const i = Math.floor(Math.random() * ANONYMS.length)
  return ANONYMS[i]
}

// 5) Enter 키로 게임 종료 및 “정확히 일치할 때만” 기록
function finishGame() {
  if (isFinished.value) return
  if (userInput.value !== currentQuote.value.text) return

  isFinished.value = true

  // 로그인 유저 이름이 전역에 있으면 쓰고, 없으면 랜덤 익명
  const user =
    window.currentUser && typeof window.currentUser === 'string'
      ? window.currentUser
      : getRandomAnonym()

  records.value.push({
    text: currentQuote.value.text,
    time: elapsedTime.value,
    user
  })
}

// 6) 다시하기: 완전 초기화 + 랜덤 명대사
function restart() {
  // 타이머 멈추기
  if (tickId.value) {
    cancelAnimationFrame(tickId.value)
    tickId.value = null
  }

  userInput.value   = ''
  startTime.value   = 0
  elapsedTime.value = 0
  isFinished.value  = false
  pickQuote()
}

// 자동으로 Top3 계산
const topResults = computed(() =>
  records.value
    .slice()
    .sort((a, b) => a.time - b.time)
    .slice(0, 3)
)

// 글자별 스타일 클래스
function charClass(i) {
  const txt = currentQuote.value.text
  if (!userInput.value[i]) return ''
  return userInput.value[i] === txt[i] ? 'correct' : 'incorrect'
}

// 정확도 & WPM 계산
const accuracy = computed(() => {
  const total = currentQuote.value.text.length
  let correct = 0
  for (let i = 0; i < userInput.value.length; i++) {
    if (userInput.value[i] === currentQuote.value.text[i]) correct++
  }
  return total ? ((correct / total) * 100).toFixed(1) : '0.0'
})
const wpm = computed(() => {
  const words   = userInput.value.length / 5
  const minutes = elapsedTime.value / 60
  return minutes ? (words / minutes).toFixed(1) : '0.0'
})

// 초기 마운트 시 대사 뽑기
onMounted(() => pickQuote())

function stopGame() {
  if (isFinished.value) return
  isFinished.value = true

  if (tickId.value) {
    cancelAnimationFrame(tickId.value)
    tickId.value = null
  }
}






</script>

<style scoped>
/* 기존 CSS 그대로 유지 */
.game-wrapper {
  display: flex;
  align-items: flex-start;
  gap: 2rem;
  margin: auto;
}
.typing-game-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 2rem;
  background: #444340;
  border-radius: 8px;
}
.quote-box {
  width: 100%;
  padding: 1rem;
  background: #353434;
  color: #fff;
  border-radius: 4px;
  min-height: 100px;
}
.quote { margin: 0; font-size: 1.2rem; word-wrap: break-word; }
.movie-title { margin-top: 0.5rem; font-size: 0.9rem; text-align: right; opacity: 0.7; }
.correct { background-color: rgba(0,200,0,0.3); }
.incorrect { background-color: rgba(200,0,0,0.3); }
.typing-area {
  width: 100%; height: 4rem; padding: 0.5rem;
  font-size: 1rem; border-radius: 4px; resize: none;
}
.stats { display: flex; gap: 1rem; font-size: 1rem; }
.buttons { display: flex; gap: 1rem; }
button {
  padding: 0.6rem 1.2rem; 
  background: linear-gradient(to right, #614385  0%, #516395  100%);
  transition: 0.5s;
  color: #fff; border: none; border-radius: 4px; cursor: pointer;
  background-size: 200% auto;
}

button:hover{
  background-position: 100% 0%;
  color: #fff;
  text-decoration: none;
}

button:disabled { opacity: 0.6; cursor: not-allowed; }
.scoreboard {
  width: 250px; background: #444340; padding: 1rem;
  border-radius: 8px;
}
.scoreboard h3 { margin: 0 0 1rem; font-size: 1.1rem; text-align: center; }
.scoreboard ol { padding-left: 1.2rem; }
.scoreboard li { margin-bottom: 1rem; font-size: 0.95rem; }
.scoreboard small { color: #555; }
</style>
