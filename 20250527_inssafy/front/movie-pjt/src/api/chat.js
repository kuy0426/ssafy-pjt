// src/api/chat.js
import axios from 'axios';

// OpenAI 키는 Vite 환경변수에서 읽습니다.
const OPENAI_KEY = import.meta.env.VITE_OPENAI_KEY;
if (!OPENAI_KEY) {
  console.warn('⚠️ VITE_OPENAI_KEY is not set!');
}

const chatApi = axios.create({
  baseURL: 'https://api.openai.com/v1',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${OPENAI_KEY}`,
  },
});

/**
 * ChatGPT 대화 요청
 * @param {Array<{role: string, content: string}>} messages
 */
export async function fetchChatCompletion(messages) {
  // 1) 시스템 프롬프트: 고정 질문지
  const systemPrompt = {
    role: 'system',
    content: `당신은 영화 매칭 테스트 AI입니다.
아래 두 가지 질문을 차례로 던지고,
사용자가 A/B/C/D 중 하나로 답변하면
최종적으로 '도전·모험형', '분석·계획형',
'관찰·공감형', '여유·감상형' 네 가지 유형
중 하나를 추천해 주십시오.`,
  };
  // 2) 사용자에게 실제 보낼 질문 리스트
  const fixedQuestions = [
    {
      role: 'assistant',
      content: `Q1. 친구들과 큰 여행을 떠난다면 당신은?
A. 미리 루트·일정을 정해두고 계획적으로 움직인다
B. 함께 의견 나누며 당일 계획을 유동적으로 바꾼다
C. 여행지 정보를 철저히 조사한 뒤 한발짝씩 움직인다
D. 여행보다 현지 풍경·사람을 느끼며 여유로운 일정을 즐긴다`,
    },
    {
      role: 'assistant',
      content: `Q2. 새로운 사람들과 처음 만났을 때 당신의 태도는?
A. 적극적으로 다가가 대화를 주도한다
B. 서로 소개하며 공통점을 찾아 친해진다
C. 상대를 관찰하며 대화 포인트를 신중히 고른다
D. 느긋하게 분위기 파악 후 편한 순간에 이야기한다`,
    },
  ];

  // 합치기: 시스템 → 고정 질문 → 누적 대화
  const allMessages = [systemPrompt, ...fixedQuestions, ...messages];

  const res = await chatApi.post('/chat/completions', {
    model: 'gpt-4o-mini',
    messages: allMessages,
  });
  return res.data.choices[0].message.content.trim();
}
