# AI 활용 바이브코딩 — 8강 강의노트 v2 (강사용)

> **범례**: 🎤 강사 스크립트 | 📺 슬라이드 | 👨‍💻 실습 | ⚠️ 예상 오류 | 📌 레벨 분기

---

## 1강: 바이브코딩의 세계 — Claude Chat + Gemini로 첫 코드 짜기
**일시**: 1주차 1회 | **시간**: 3시간 (이론 1h + 실습 2h)

### 강의 목표 (수강자에게 보여줄 버전)
이 강의를 마치면 여러분은:
- 바이브코딩이 무엇인지, 왜 지금 배워야 하는지 설명할 수 있다
- Claude와 Gemini의 차이를 직접 비교한 경험을 갖는다
- AI에게 코드를 요청하고 결과를 브라우저에서 실행할 수 있다
- 에이전트팀·하네스가 일하는 장면을 눈으로 본다 (4주 뒤에 직접 만든다!)

### 강사 준비물 체크리스트
- [ ] 에이전트팀 하네스 라이브 시연 준비 (사전 실행 테스트 필수)
- [ ] Claude.ai + Gemini 가입 단계별 스크린가이드 PDF (Google 계정 연동 포함)
- [ ] "전통 코딩 vs 바이브코딩" 대비표 슬라이드
- [ ] "AI 도구 전체 지도" 슬라이드 (Claude 3종 + Google AI 4종)
- [ ] 비상용 완성 예제 HTML 파일 (인터넷 불안정 대비)

---

### ① 오리엔테이션 (0:00~0:15)

📺 **슬라이드 1 — "AI 활용 바이브코딩 — 4주 후 여러분의 모습"**
- 수강 전: 코딩 = 두려움 / 수강 후: AI와 대화로 앱 완성
- 최종 프로젝트 갤러리 (이전 기수 샘플)

🎤 **강사 스크립트**
"안녕하세요. 오늘부터 4주 동안 함께할 강사 [이름]입니다. 먼저 한 가지 여쭤볼게요 — 코딩이라는 단어를 들었을 때 가장 먼저 떠오르는 감정이 뭔가요? (잠시 대기) 두렵다, 어렵다, 해보고 싶다 — 어떤 대답이든 괜찮습니다."

"레벨을 먼저 파악하겠습니다. 코딩을 한 번도 해본 적 없으신 분 손 들어주세요. (확인) 코딩은 해봤는데 AI 도구는 처음이신 분? (확인) AI 도구도 써봤는데 더 잘 쓰고 싶으신 분? (확인) 이 과정은 세 그룹 모두를 위해 설계되어 있습니다."

📺 **슬라이드 2 — "오늘의 순서"**
- 0:00 오리엔테이션
- 0:15 라이브 시연 (에이전트팀 & 하네스)
- 0:35 이론: 바이브코딩 + AI 도구 지도
- 1:10 실습 1: Google 계정 + Claude.ai + Gemini 가입
- 1:35 실습 2: Claude vs Gemini 첫 코딩 비교
- 2:20 실습 3: 결과물 평가
- 2:50 정리 & 과제

---

### ② 라이브 시연: 에이전트팀 & 하네스 (0:15~0:35)

🎤 **강사 스크립트**
"지금 슬라이드를 내리겠습니다. 개념 설명 없이 그냥 보세요."

*(하네스 실행 — 예: 뉴스레터 하네스에 주제 1줄 입력 → 큐레이터·작가·편집장 에이전트가 순서대로 동작하며 파일 생성)*

"보이시나요? 지금 AI 5명이 팀을 이뤄 뉴스레터를 만들고 있습니다. 저는 처음에 '뉴스레터 만들어줘'라고 한 줄만 입력했습니다. 이것의 이름을 하네스(Harness)라고 합니다. 개념은 나중에 설명합니다. '뭔지 모르겠지만 멋있다'는 느낌만 갖고 가세요."

*(결과 파일 열어 보여주기)*

"과제입니다. 오늘 끝나고 방금 본 장면을 본인의 말로 1~3문장으로 묘사해 오세요. 다음 강에 3명이 발표합니다."

---

### ③ 이론: 바이브코딩이란? + AI 도구 전체 지도 (0:35~1:10)

📺 **슬라이드 3 — "전통 코딩 vs 바이브코딩"**

| 항목 | 전통 코딩 | 바이브코딩 |
|------|---------|----------|
| 시작점 | 문법 암기 | 목표 설명 |
| 도구 | 에디터 + 구글 검색 | AI와 대화 |
| 막혔을 때 | Stack Overflow | AI에게 물어보기 |
| 결과물까지 | 수개월 학습 | 몇 시간 |
| 필요 역량 | 코드 작성 | 문제 정의 + 검증 |

🎤 **강사 스크립트**
"바이브코딩을 처음 만든 사람은 Andrej Karpathy입니다. 테슬라 AI 책임자이자 OpenAI 공동창업자이기도 한 분이에요. 2025년 초에 이런 말을 남겼습니다. '나는 이제 코드를 직접 쓰지 않는다. AI에게 원하는 것을 설명하고, AI가 만들어주면 내가 검증한다.' 그게 바이브코딩의 핵심입니다."

"중요한 것이 있어요. AI가 코드를 쓴다고 해서 여러분이 아무것도 안 해도 된다는 게 아닙니다. 여러분의 역할이 바뀌는 거예요. '코드를 쓰는 사람'에서 '무엇을 만들지 정의하고 결과를 검증하는 사람'으로요."

📺 **슬라이드 4 — "5대 핵심 개념 한 장 지도" (30초 소개)**

| 개념 | 한 줄 정의 | 처음 배우는 강 |
|------|----------|-------------|
| 스킬 (Skill) | AI에게 역할을 주는 지침 파일 | 2강 |
| 에이전트 (Agent) | 파일을 스스로 만드는 자율 AI | 3강 |
| 에이전트팀 | 에이전트들의 협업 구조 | 1강 (방금 봤음!) |
| MCP | Claude ↔ 외부 도구 연결 규약 | 3강 |
| 하네스 (Harness) | 에이전트팀+스킬+MCP 파이프라인 | 1강 (방금 봤음!) |

🎤 "지금 이 표의 단어들, 기억 안 해도 됩니다. 4주가 지나면 여러분이 직접 쓰게 될 단어들입니다."

📺 **슬라이드 5 — "이 과정에서 쓸 AI 도구 전체 지도"**

| 분류 | 도구 | 역할 | 언제 |
|------|------|------|------|
| Claude | Chat | 빠른 코드 생성·질문 | 지금 바로 |
| Claude | Co-work | 프로젝트 맥락 유지 + 스킬 | 2강 |
| Claude | Code CLI | 파일 직접 수정, 에이전트 | 3강 |
| Google | Gemini | 대화형 AI, Claude 비교 | 지금 + 4강 |
| Google | AI Studio | Gemini API, 프롬프트 실험 | 4강 |
| Google | NotebookLM | 문서 기반 AI 리서치 | 4강 |
| Google | 안티그래비티 | AI 자동화 | 4강 |
| 개발 | VS Code | 코드 에디터 | 3강 |
| 개발 | GitHub | 버전 관리·배포 | 3강 |

🎤 "두 가지 AI 생태계를 씁니다. Anthropic(Claude)과 Google(Gemini·AI Studio·NotebookLM). 두 회사의 도구를 상황에 맞게 선택하는 능력이 4주 후에 생깁니다."

---

### ④ 실습 1: Google 계정 + Claude.ai + Gemini 가입 (1:10~1:35)

👨‍💻 **단계별 지시**

**Google 계정 확인/생성:**
1. accounts.google.com → 기존 계정으로 로그인 (없으면 "계정 만들기")
2. 이 계정 하나로 Gemini·AI Studio·NotebookLM 모두 접근 가능

**Claude.ai 가입:**
1. claude.ai 접속 → "Sign up" 클릭
2. "Continue with Google" 선택 → Google 계정으로 연동
3. 무료 플랜 선택 → 가입 완료
4. 새 Chat 시작 → "안녕하세요"라고 입력 후 응답 확인

**Gemini 가입:**
1. gemini.google.com 접속
2. Google 계정으로 자동 로그인됨
3. 채팅창에 "안녕하세요"라고 입력 후 응답 확인

📌 **레벨 분기**
- **입문자**: Google 계정 생성부터 함께 진행 (강사 스크린가이드 PDF 참고)
- **고급자**: 이미 가입된 경우 → Claude.ai의 플랜 비교 확인, Claude Pro 기능 파악

⚠️ **예상 오류 & 해결**
| 상황 | 원인 | 해결 |
|------|------|------|
| 인증 이메일 미도착 | 스팸 폴더 | 스팸 폴더 확인 |
| "계정이 이미 있습니다" | 이전 가입 이력 | "로그인" 클릭 → 비밀번호 찾기 |
| Gemini 서비스 불가 지역 | VPN 필요 | 강사 백업 계정 제공 |

---

### ⑤ 실습 2: 첫 바이브코딩 — Claude vs Gemini 비교 (1:35~2:20)

📺 **슬라이드 6 — "오늘의 실험 방법"**
- 같은 프롬프트를 Claude Chat과 Gemini에 동시에 입력
- 결과물 코드를 각각 복사해 브라우저에서 실행
- 차이점을 직접 느낀다

👨‍💻 **비교 실험 프롬프트:**
```
다음 조건으로 할 일 목록(Todo List) 앱을 HTML 하나의 파일로 만들어줘.
- 기능: 할 일 추가, 완료 체크, 삭제
- 디자인: 깔끔하고 현대적인 스타일
- 완성된 전체 코드를 주세요
```

**코드 실행 방법 (입문자):**
1. Claude/Gemini 응답에서 코드 블록 전체 복사 (Ctrl+A → Ctrl+C)
2. 바탕화면에 `todo_claude.html` / `todo_gemini.html` 파일 새로 만들기
3. 텍스트 편집기(메모장)에 붙여넣기 → 저장
4. 파일 더블클릭 → 브라우저에서 열기

📌 **레벨 분기**
- **입문자**: 위 기본 프롬프트 그대로 사용, 두 결과만 나란히 열기
- **고급자**: 추가 조건 부여 — "TypeScript로", "localStorage 저장 기능 추가", "다크모드 포함"

🎤 **강사 스크립트**
"두 결과물을 나란히 보세요. 디자인이 다르죠? 코드 구조도 다릅니다. 어느 것이 더 낫다는 게 아니에요. AI마다 '스타일'이 다릅니다. 앞으로 4주 동안 여러분은 도구마다의 강점을 파악하게 됩니다."

⚠️ **예상 오류 & 해결**
| 오류 | 원인 | 해결 |
|------|------|------|
| 화면이 빈 페이지 | HTML 저장 실패 | 파일 확장자가 `.html`인지 확인 |
| "파일을 열 수 없음" | 메모장 기본 저장 형식 | 저장 시 "파일 형식: 모든 파일" 선택 |
| 기능이 동작 안 함 | JS 오류 | Claude Chat에 "이 에러 고쳐줘: [에러 메시지]" |

---

### ⑥ 실습 3: 결과물 평가 (2:20~2:50)

📺 **슬라이드 7 — "AI 코드를 검증하는 3가지 관점"**
1. **기능**: 요청한 기능이 모두 동작하는가?
2. **디자인**: 직관적이고 사용하기 편한가?
3. **코드**: 구조가 이해 가능한가? (HTML·CSS·JS 분리 여부)

👨‍💻 **검증 작업:**
```
방금 만든 코드를 Claude Chat에 붙여넣고 아래 질문을 해보세요:
"이 코드의 장점 2가지와 개선할 점 2가지를 알려줘. 
 초보자도 이해할 수 있는 언어로."
```

📌 **레벨 분기**
- **입문자**: Claude의 평가 내용을 그대로 읽고 이해하기
- **고급자**: Claude 평가를 바탕으로 개선 요청 → 수정 코드 받기 → 재실행

---

### ⑦ 마무리 & 과제 (2:50~3:00)

🎤 **강사 스크립트**
"오늘 여러분은 코딩을 배운 게 아닙니다. AI와 협업하는 첫 경험을 했습니다. Claude와 Gemini라는 두 AI 도구의 느낌을 몸으로 알게 됐고, 에이전트팀·하네스가 일하는 장면도 봤습니다."

**과제:**
- Claude Chat으로 "나를 소개하는 HTML 페이지" 만들어 브라우저에서 실행 후 스크린샷 제출
- 오늘 하네스 시연에서 본 장면을 본인의 말로 1~3문장 묘사 (정답 없음)

---

## 2강: 프롬프트 엔지니어링 & Claude Co-work — 잘 말하고 스킬을 만든다
**일시**: 1주차 2회 | **시간**: 3시간

### 강의 목표 (수강자에게 보여줄 버전)
이 강의를 마치면 여러분은:
- STAR 프롬프트로 AI에게 정밀하게 요청할 수 있다
- 스킬(Skill)이 무엇인지 이해하고 나만의 스킬 3종을 만들 수 있다
- Claude Co-work Projects를 이용해 나만의 AI 도우미를 구성할 수 있다

### 강사 준비물 체크리스트
- [ ] STAR 워크시트 PDF (빈칸 채우기 버전)
- [ ] "나쁜 프롬프트 vs 좋은 프롬프트" 예시 5쌍 슬라이드
- [ ] 스킬 템플릿 3종 파일 (코딩도우미·번역전문가·데이터분석가)

---

### ① 과제 리뷰 + 하네스·에이전트팀 묘사 발표 (0:00~0:15)

🎤 **강사 스크립트**
"지난 시간 과제에서 하네스 장면을 묘사해오셨죠. 3분께서 발표해 주세요. 1분씩, 정답은 없습니다."
*(3명 지명 발표)*
"감사합니다. 다들 조금씩 다르게 봤는데 모두 맞습니다. 앞으로 4주 동안 저 장면이 점점 더 잘 보이게 됩니다."

---

### ② 이론: STAR 프롬프트 설계 (0:15~0:40)

📺 **슬라이드 1 — "나쁜 프롬프트 vs 좋은 프롬프트"**

| # | 나쁜 프롬프트 | 좋은 프롬프트 |
|---|------------|------------|
| 1 | "앱 만들어줘" | "React 없이 바닐라 JS로 날씨 앱을 만들어줘. OpenWeather API 사용. 도시명 입력 → 현재 날씨 표시. 하나의 HTML 파일로." |
| 2 | "에러 고쳐줘" | "아래 코드에서 버튼 클릭 시 아무 반응이 없습니다. 원인을 찾아서 고쳐주세요: [코드]" |
| 3 | "계산기 만들어" | "4칙연산 계산기 HTML을 만들어줘. 다크 테마, 4×4 그리드 버튼, 0으로 나누면 'Error' 표시." |

📺 **슬라이드 2 — "STAR 프롬프트 프레임워크"**
- **S**ituation (상황): 지금 어떤 상황인가? 어떤 파일/코드가 있는가?
- **T**ask (작업): 무엇을 만들어야 하는가? 핵심 기능은?
- **A**ction (방법): 어떤 기술/라이브러리? 어떤 구조로?
- **R**esult (결과): 출력 형식은? 완성 후 부연 설명이 필요한가?

🎤 **강사 스크립트**
"STAR는 외울 필요 없어요. '내가 AI에게 이 4가지를 다 알려줬나?'라고 체크만 하면 됩니다. 빠진 정보가 많을수록 AI는 추측으로 채웁니다. 그 추측이 내가 원하는 것과 다를 때 실망하게 되는 거예요."

---

### ③ 핵심 이론: 스킬(Skill)이란? (0:40~1:00)

📺 **슬라이드 3 — "비밀 공개 — 1강 하네스의 에이전트들이 가진 것"**

🎤 **강사 스크립트**
"지난 시간 하네스 시연 기억나시죠? 5명의 에이전트가 협업했습니다. 큐레이터, 작가, 편집장... 왜 각자가 자기 역할을 알고 있었을까요? 각 에이전트한테 '매뉴얼'이 있었기 때문입니다. 그 매뉴얼이 스킬(Skill)입니다."

"그리고 오늘 여러분이 Claude Co-work에서 작성할 '시스템 지침' — 그게 바로 스킬의 씨앗입니다."

📺 **슬라이드 4 — "스킬 = AI의 업무 매뉴얼"**
- 스킬 없는 AI = 아무것도 모르는 신입사원
- 스킬 있는 AI = 업무 매뉴얼을 숙지한 전문가
- 구성: 역할 정의 + 작업 방법 + 출력 형식 + 제약 조건
- Claude Co-work 시스템 지침 = 가장 쉬운 형태의 스킬

---

### ④ 실습 1: STAR 프롬프트 실험 (1:00~1:40)

👨‍💻 **같은 기능(계산기)을 3가지 수준으로 요청하고 결과 비교**

**프롬프트 A (나쁜):**
```
계산기 만들어줘
```

**프롬프트 B (보통):**
```
HTML로 계산기를 만들어줘. +, -, *, / 기능 포함.
```

**프롬프트 C (STAR 적용):**
```
[S] HTML, CSS, JavaScript 파일을 새로 만들고 있습니다.
[T] 기본 계산기 앱을 만들어주세요.
[A]
- 연산: +, -, *, / 그리고 % (나머지)
- 버튼 레이아웃: 실제 계산기처럼 4×4 그리드
- 스타일: 다크 테마, 버튼에 hover 효과
- 소수점 지원, 연속 계산 지원
- 0으로 나누기 시 'Error' 표시
[R] 하나의 HTML 파일로 전체 코드를 주세요. 동작 방식을 3줄로 설명해주세요.
```

📌 **레벨 분기**
- **입문자**: A→B→C 결과 화면 비교, 차이 메모
- **고급자**: C의 결과물에 "키보드 입력 지원" 추가 요청 (체인 프롬프팅)

⚠️ **예상 오류 & 해결**
| 오류 | 원인 | Claude 디버깅 프롬프트 |
|------|------|----------------------|
| 계산 결과 이상 | 부동소수점 | "0.1+0.2=0.30000000000000004 문제를 toFixed로 해결해줘" |
| 연속 계산 오작동 | 상태 관리 버그 | "5+3=8에서 바로 +2 하면 오작동합니다. 수정해줘" |

---

### ⑤ 실습 2: 나만의 스킬 파일 만들기 (1:40~2:20)

📺 **슬라이드 5 — "Claude Co-work(Projects) — Chat과 무엇이 다른가?"**
- Chat: 새 대화마다 기억 리셋, 매번 배경 설명 필요
- Co-work Projects: 시스템 지침 + 파일 영구 저장
- 비유: Chat = 임시 노트 / Projects = 영구 문서함

👨‍💻 **Co-work Project 생성:**
1. claude.ai → 왼쪽 사이드바 "Projects" 클릭
2. "+ New Project" → 이름: "내 코딩 도우미"
3. "Project Instructions"(시스템 지침) 작성

**[강사 배포용 스킬 템플릿 3종]**

**Template ① — 코딩 도우미:**
```
당신은 나의 전문 코딩 도우미입니다.

## 역할
- 나는 [직업/레벨]이고, [주로 만드는 것]을 AI로 만들고 있습니다.
- 코드 설명은 한국어로, 코드 자체는 영어 변수명으로 작성해주세요.

## 응답 방식
- 코드를 줄 때는 완성된 상태 전체로 주세요
- 수정이 필요하면 변경 부분만 명확히 표시
- 오류 해결: 원인 → 해결책 → 예방법 순서로

## 기술 스택
- HTML, CSS, JavaScript (바닐라)
- Python 3.x (필요 시)
```

**Template ② — 번역 전문가:**
```
당신은 한국어·영어 번역 전문가입니다.

## 역할
- 한국어 ↔ 영어 번역 및 교정
- 원본의 뉘앙스·어조를 유지하며 자연스럽게 번역

## 응답 방식
- 번역 결과를 먼저 제시한 뒤 주요 선택 이유 1~2줄 부연
- 오역 가능성 있는 표현은 대안 2가지 병기
- 전문 용어는 원어 병기: 예) 머신러닝(Machine Learning)

## 제약
- 자연스러운 표현 우선 (직역은 필요 최소한)
```

**Template ③ — 데이터 분석가:**
```
당신은 데이터 분석 전문가입니다.

## 역할
- Python(pandas·matplotlib·seaborn) 기반 분석
- 비전공자도 이해하는 인사이트 도출

## 응답 방식
- 분석 코드는 항상 한국어 주석 포함
- 코드 아래에 예상 출력 예시 설명
- 차트 제목·축 레이블은 한국어

## 제약
- 한글 깨짐 방지 코드 항상 포함 (NanumGothic 폰트)
```

🎤 **강사 스크립트**
"이 시스템 지침이 바로 스킬입니다. 여러분이 방금 에이전트에게 업무 매뉴얼을 쓴 거예요. 저장하면 이 프로젝트의 모든 대화에서 Claude가 이 지침을 기억합니다."

📌 **레벨 분기**
- **입문자**: 3종 중 1개 선택 → [괄호] 부분만 본인에 맞게 채우기
- **고급자**: `.md` 형식으로 별도 작성해 Projects 파일로 업로드

---

### ⑥ 실습 3: 스킬로 체인 프롬프팅 (2:20~2:40)

👨‍💻 **방금 만든 Co-work Project에서 날씨 앱 UI를 4단계로 구성**

**단계 1 — 기획:**
```
날씨 앱 UI를 만들려고 합니다. 필요한 기능 5가지만 제안해줘.
```
**단계 2 — HTML 구조:**
```
좋아. 그 기능 중 1, 2, 3번으로 HTML 골격만 잡아줘. CSS는 아직 없어도 됨.
```
**단계 3 — 스타일:**
```
이제 CSS를 추가해줘. 하늘색·흰색 계열 깔끔한 카드 디자인으로.
```
**단계 4 — 기능 연결:**
```
버튼 클릭하면 콘솔에 "날씨 데이터 요청 중..."이 뜨도록 JS 추가해줘.
실제 API는 다음 강에 연결할 거야.
```

🎤 **강사 스크립트**
"체인 프롬프팅의 핵심은 대화를 끊지 않는 것입니다. 새 채팅을 시작하면 앞 맥락이 사라져요. 단계마다 브라우저에서 결과를 확인하면서 다음 단계로 넘어가세요."

---

### ⑦ AI 교정 재프롬프팅 3패턴 (2:40~2:50)

📺 **슬라이드 6 — "AI 결과가 마음에 안 들 때"**

🎤 **강사 스크립트**
"AI 결과가 기대와 다를 때 '다시 만들어줘'는 최악의 선택입니다. AI가 이전과 같은 결과를 냅니다. 3가지 교정 패턴을 익혀두세요."

**패턴 ① Pinpoint (구체적 오류 지적):**
```
버튼을 클릭해도 숫자가 초기화되지 않아.
AC 버튼 누르면 0으로 돌아오도록 수정해줘.
```

**패턴 ② Redirect (방향 전환):**
```
지금 CSS Grid로 만들었는데 Flexbox로 바꿔줘.
Grid가 내 브라우저에서 레이아웃이 깨져서.
```

**패턴 ③ Decompose (단계 분해):**
```
날씨 앱 전체가 한 번에 잘 안 나왔어.
먼저 도시명 입력창과 검색 버튼 HTML만 만들어줘.
기능은 다음에.
```

---

### ⑧ 마무리 & 과제 (2:50~3:00)

🎤 "오늘의 핵심: STAR는 'AI에게 상황·작업·방법·결과를 다 알려줬나?' 체크리스트입니다. 그리고 오늘 만든 Co-work 시스템 지침 — 그게 스킬의 첫 번째 버전입니다."

**과제:**
- Co-work에 "내 코딩 도우미" 프로젝트 완성 (시스템 지침 작성)
- STAR 프롬프트로 원하는 기능 1개 구현 후 스크린샷 제출
- 다음 강 예고: "Node.js를 설치하고 Claude Code CLI를 설치합니다. AI가 파일을 직접 만드는 순간을 눈앞에서 봅니다."

---

## 3강: VS Code + Claude Code CLI — 개발 환경을 완전히 내 것으로
**일시**: 2주차 1회 | **시간**: 3시간

### 강의 목표 (수강자에게 보여줄 버전)
이 강의를 마치면 여러분은:
- VS Code의 UI 구조와 핵심 단축키 10개를 쓸 수 있다
- Node.js와 Claude Code CLI를 설치하고 Google OAuth 인증을 완료할 수 있다
- Claude Code CLI로 파일을 만들고 수정하면서 에이전트를 실감할 수 있다
- GitHub에 코드를 올리고 GitHub Pages로 배포할 수 있다

### 강사 준비물 체크리스트
- [ ] VS Code 설치 가이드 (Windows·Mac 각각)
- [ ] Node.js LTS 다운로드 URL (nodejs.org)
- [ ] GitHub 가입 + 리포 생성 5분 가이드
- [ ] 포트폴리오 스타터 HTML (인터넷 불안정 대비)
- [ ] MCP 설명 슬라이드 (USB 비유 다이어그램)

---

### ① 과제 리뷰 (0:00~0:15)

🎤 "지난 시간 Co-work 스킬 파일을 만드셨죠. 어떤 템플릿을 선택하셨나요? (2~3명 공유) 오늘은 그 스킬이 파일을 직접 만드는 힘을 갖게 됩니다."

---

### ② VS Code 완전 기초 (0:15~0:45)

📺 **슬라이드 1 — "VS Code — 여러분의 새 작업실"**

🎤 **강사 스크립트**
"VS Code는 마이크로소프트가 만든 무료 코드 에디터입니다. 전 세계 개발자의 70% 이상이 사용합니다. 오늘 여러분의 메인 작업 공간이 됩니다."

**VS Code UI 4대 구역 설명:**
```
┌────────────────────────────────────────┐
│ 메뉴바 (File, Edit, View...)            │
├──────┬─────────────────────────────────┤
│ 활동 │    에디터 영역 (코드 작성)          │
│ 바   │                                  │
│ ①탐색 ├─────────────────────────────────┤
│ ②검색 │    터미널 (명령어 실행)             │
│ ③깃  └─────────────────────────────────┤
│ ④확장│    상태 바 (현재 파일 정보)          │
└──────┴─────────────────────────────────┘
```

| 구역 | 이름 | 역할 |
|------|------|------|
| ① 탐색기 | Explorer | 폴더·파일 목록 보기 |
| ② 검색 | Search | 전체 파일에서 텍스트 검색 |
| ③ 소스 제어 | Source Control | Git 커밋·푸시 |
| ④ 확장 | Extensions | 플러그인 설치 |
| 에디터 | 가운데 큰 공간 | 코드 작성 |
| 터미널 | 아래 패널 | 명령어 실행 (Ctrl+`) |

**핵심 단축키 10개 (반드시 외울 것):**

| 단축키 (Windows) | Mac | 기능 |
|----------------|-----|------|
| `Ctrl + S` | `Cmd + S` | 저장 |
| `Ctrl + Z` | `Cmd + Z` | 되돌리기 |
| `Ctrl + P` | `Cmd + P` | 파일 빠른 열기 |
| `Ctrl + Shift + P` | `Cmd + Shift + P` | 명령 팔레트 |
| `` Ctrl + ` `` | `` Ctrl + ` `` | 터미널 열기/닫기 |
| `Ctrl + D` | `Cmd + D` | 같은 단어 다중 선택 |
| `Alt + Click` | `Option + Click` | 멀티 커서 |
| `Ctrl + F` | `Cmd + F` | 현재 파일 검색 |
| `Ctrl + H` | `Cmd + H` | 검색 후 바꾸기 |
| `Ctrl + /` | `Cmd + /` | 줄 주석 토글 |

👨‍💻 **VS Code 설치 (지금 함께):**

**Windows:**
1. code.visualstudio.com → "Download for Windows" 클릭
2. 설치파일 실행 → "PATH에 추가" 체크 확인 → 설치 완료
3. 시작메뉴에서 "Visual Studio Code" 실행

**Mac:**
1. code.visualstudio.com → "Download for Mac" 클릭
2. `.dmg` 파일 실행 → Applications 폴더로 드래그
3. Launchpad에서 VS Code 실행

**필수 확장 프로그램 설치 (왼쪽 확장 아이콘 클릭 → 검색):**

| 확장명 | 검색어 | 역할 |
|--------|--------|------|
| Korean Language Pack | Korean Language Pack | VS Code 한국어 |
| Prettier | Prettier - Code formatter | 코드 자동 정렬 |
| Auto Save | (VS Code 기본 설정) | 파일 자동 저장 |
| Live Server | Live Server | HTML 실시간 미리보기 |

**Auto Save 설정:** File → Auto Save (체크)

📌 **레벨 분기**
- **입문자**: 핵심 단축키 3개만 먼저 (Ctrl+S, Ctrl+Z, Ctrl+`)
- **고급자**: 추가 확장 설치 — ESLint, GitLens, GitHub Copilot Chat

---

### ③ 핵심 이론: 에이전트 & MCP (0:45~1:00)

📺 **슬라이드 2 — "에이전트(Agent)란?"**

🎤 **강사 스크립트**
"Claude Chat은 '대화'를 합니다. 질문하면 답합니다. 그런데 Claude Code CLI는 다릅니다. 여러분이 '포트폴리오 페이지 만들어줘'라고 하면 — AI가 직접 파일을 열고, 코드를 쓰고, 저장하고, 필요하면 여러 파일을 동시에 수정합니다. 이런 AI를 에이전트(Agent)라고 합니다."

| 구분 | Claude Chat | Claude Code CLI (에이전트) |
|------|-----------|----------------------|
| 역할 | 대화 상대 | 자율 실행자 |
| 할 수 있는 것 | 코드 생성·설명 | 파일 생성·수정·실행 |
| 비유 | 조언해주는 선배 | 직접 일해주는 프리랜서 |

📺 **슬라이드 3 — "MCP(Model Context Protocol)란?"**

🎤 **강사 스크립트**
"MCP는 Claude와 외부 도구를 연결하는 표준 규격입니다. USB를 생각해보세요. USB 규격이 있으면 어떤 마우스든 어떤 컴퓨터에도 꽂을 수 있잖아요. MCP가 바로 그겁니다. Claude에 GitHub MCP를 연결하면 Claude가 GitHub를 직접 열 수 있고, Notion MCP를 연결하면 Notion 문서를 읽고 쓸 수 있습니다. 8강에서 직접 연결해봅니다."

---

### ④ 이론: 전체 아키텍처 + GitHub 개요 (1:00~1:10)

📺 **슬라이드 4 — "전체 개발 아키텍처"**
```
[VS Code] ←→ [Claude Code CLI] ←→ [파일 시스템]
    ↓                                    ↓
[터미널]                            [GitHub 리포]
                                         ↓
                                   [GitHub Pages] ← 전 세계 접근 가능
```

🎤 "VS Code에서 코드를 쓰고, Claude Code CLI가 파일을 만들고, GitHub에 올리면 GitHub Pages로 전 세계에 공개됩니다. 오늘 이 흐름 전체를 경험합니다."

---

### ⑤ 실습 1: Node.js + Claude Code CLI 설치 (1:10~1:50)

👨‍💻 **5단계 설치 과정**

**Step 1 — Node.js 설치:**
1. nodejs.org → LTS 버전 다운로드 클릭
2. 설치파일 실행 → 기본 설정 그대로 "다음" 계속
3. 설치 완료 후 VS Code 재시작

**Step 2 — Node.js 설치 확인:**
VS Code 터미널 열기 (Ctrl+`) 후:
```bash
node -v
# 출력 예시: v22.0.0 (버전 숫자가 나오면 성공)

npm -v
# 출력 예시: 10.0.0
```

**Step 3 — Claude Code CLI 설치:**
```bash
npm install -g @anthropic-ai/claude-code
```
*(설치 시간: 1~3분. 진행 중 메시지가 계속 뜨면 정상)*

**Step 4 — Claude Code CLI 첫 실행 + Google OAuth 인증:**
```bash
claude
```
- 브라우저 팝업이 뜸 → "Claude Code CLI가 계정 접근을 요청합니다"
- **"허용"** 클릭
- 브라우저에 "인증 완료" 메시지 → VS Code 터미널로 돌아옴
- `claude>` 프롬프트가 나타나면 성공

**Step 5 — 기본 명령 확인:**
```bash
claude> /help      # 사용 가능한 명령 목록
claude> /exit      # 종료
```

⚠️ **예상 오류 & 해결**
| 오류 | 원인 | 해결 |
|------|------|------|
| `node: command not found` | PATH 미등록 | VS Code 완전 종료 후 재시작 |
| `EACCES permission denied` | npm 권한 | Mac: `sudo npm install -g ...`, Windows: 관리자 권한 터미널 |
| 브라우저 팝업 미표시 | 팝업 차단 | 주소창에 팝업 허용 아이콘 클릭 |
| OAuth 인증 실패 | Google 계정 미연결 | claude.ai에 Google 계정으로 로그인 후 재시도 |

---

### ⑥ 실습 2: 첫 에이전트 프로젝트 (1:50~2:30)

👨‍💻 **VS Code에서 새 폴더 만들기:**
1. File → Open Folder → 바탕화면에 `portfolio` 폴더 생성 → 선택
2. VS Code 터미널 열기 (Ctrl+`)
3. `claude` 명령으로 에이전트 시작

**Claude Code CLI에게 요청:**
```
portfolio 폴더에 내 포트폴리오 HTML 페이지를 만들어줘.
- 파일명: index.html
- 섹션: 소개(이름, 직업), 기술 스택(3개), 프로젝트(2개), 연락처
- 스타일: 깔끔한 모던 디자인, 반응형, 배경색 흰색
- 모든 텍스트는 내가 나중에 수정할 수 있도록 한국어 더미 텍스트 사용
```

🎤 **강사 스크립트**
"지금 터미널에서 Claude가 파일을 만들고 있습니다. 왼쪽 탐색기를 보세요. `index.html` 파일이 생겼죠? 이게 에이전트입니다. 여러분이 '만들어줘'라고 했더니 AI가 직접 파일을 만들었습니다."

**Live Server로 실시간 확인:**
1. 왼쪽 탐색기에서 `index.html` 우클릭
2. "Open with Live Server" 클릭
3. 브라우저가 자동으로 열리며 포트폴리오 페이지 표시

📌 **레벨 분기**
- **입문자**: 기본 페이지 생성 완료 후 Claude Code CLI로 색상 변경 요청
  ```
  index.html의 배경색을 연한 하늘색으로 바꿔줘
  ```
- **고급자**: 애니메이션 추가 + 스크롤 시 헤더 고정 요청

---

### ⑦ 실습 3: GitHub 연동 — 커밋·푸시·Pages 배포 (2:30~2:50)

👨‍💻 **GitHub 리포지토리 생성:**
1. github.com → 로그인 (없으면 가입)
2. 오른쪽 상단 "+" → "New repository"
3. Repository name: `portfolio`
4. Public 선택 → "Create repository" 클릭

**VS Code에서 GitHub 연결:**

VS Code 소스 제어 패널(③번 아이콘) 클릭:
```
1. "Git 리포지토리 초기화" 클릭
2. 변경 파일(index.html) 옆 "+" 클릭 → 스테이지에 추가
3. 메시지 입력: "첫 포트폴리오 페이지 추가"
4. "커밋" 클릭
5. "브랜치 게시..." 클릭 → GitHub 로그인 → portfolio 리포 선택
```

**GitHub Pages 활성화:**
1. GitHub에서 `portfolio` 리포 → Settings 탭
2. Pages 섹션 → "Deploy from a branch" → `main` 선택 → Save
3. 2~3분 후 `https://[사용자명].github.io/portfolio` URL 접속

---

### ⑧ 마무리 & 과제 (2:50~3:00)

🎤 "오늘 VS Code·Claude Code CLI·GitHub을 모두 연결했습니다. 여러분의 개발 환경이 완성됐습니다. 에이전트가 파일을 만드는 것도 직접 봤고요."

**과제:** GitHub Pages URL이 있는 포트폴리오 페이지 제출 (VS Code + Claude Code CLI로 제작, 내용 본인 것으로 수정)

---

## 4강: Google AI 생태계 완전 정복 — Gemini · AI Studio · NotebookLM · 안티그래비티
**일시**: 2주차 2회 | **시간**: 3시간

### 강의 목표 (수강자에게 보여줄 버전)
이 강의를 마치면 여러분은:
- Google AI Studio에서 Gemini API 키를 발급하고 프롬프트 플레이그라운드를 활용할 수 있다
- NotebookLM에 문서를 업로드하고 AI 팟캐스트·학습 가이드를 생성할 수 있다
- 안티그래비티를 활용해 AI 자동화 워크플로우를 체험할 수 있다
- Claude와 Gemini의 응답 특성 차이를 분석해 적합한 도구를 선택할 수 있다

### 강사 준비물 체크리스트
- [ ] Google AI Studio 화면 데모 슬라이드
- [ ] NotebookLM 실습용 PDF 1종 (강의 소개서 또는 공개 논문)
- [ ] 안티그래비티 계정 및 실습 시나리오 (강사 확인 필수)
- [ ] Claude vs Gemini 비교 실험 프롬프트 목록

---

### ① 과제 리뷰 (0:00~0:20)

🎤 "GitHub Pages URL 제출하신 분들 확인합니다. (3~4개 화면에 띄우기) 와, 포트폴리오들이 멋지네요. 오늘은 이 생태계를 Google 쪽으로 확장합니다."

---

### ② 이론: Google AI 생태계 지도 (0:20~0:50)

📺 **슬라이드 1 — "Google AI 4대 도구 — 역할 분담"**

| 도구 | 접근 | 핵심 역할 | 언제 쓰나 |
|------|------|---------|---------|
| **Gemini** | gemini.google.com | 대화형 AI, Google 서비스 통합 | 빠른 질문·답변, 이미지 분석 |
| **Google AI Studio** | aistudio.google.com | API 키 발급, 프롬프트 실험 | Gemini API 개발, 파라미터 조정 |
| **NotebookLM** | notebooklm.google.com | 문서 기반 AI, 팟캐스트 생성 | 논문·보고서 분석, 강의 자료 연구 |
| **안티그래비티** | (강사 확인) | AI 자동화 특화 | 업무 자동화 워크플로우 |

📺 **슬라이드 2 — "Claude vs Gemini — 언제 무엇을?"**

| 비교 항목 | Claude | Gemini |
|---------|-------|--------|
| 강점 | 긴 문서·코딩·안전성 | Google 서비스 통합·멀티모달 |
| 컨텍스트 | 최대 200K 토큰 | 최대 1M 토큰 (Gemini 1.5 Pro) |
| 코딩 | 매우 강함 | 강함 |
| 이미지 생성 | 없음 | Imagen (Gemini Advanced) |
| Google 연동 | 없음 | Gmail·Drive·YouTube 직접 연동 |
| 추천 사용 | 코딩·문서 작업·에이전트 | 리서치·이미지·Google 서비스 |

🎤 "두 AI는 경쟁이 아닙니다. 강점이 다릅니다. 오늘 여러분이 직접 비교해서 '내 상황에 뭐가 더 맞는지'를 느끼면 됩니다."

---

### ③ 실습 1: Google AI Studio (0:50~1:35)

👨‍💻 **Google AI Studio 시작:**

1. aistudio.google.com 접속 → Google 계정으로 로그인
2. 왼쪽 "Create new" → "New prompt" 클릭
3. 화면 구성 확인:
   - 왼쪽: Model 선택 (Gemini 1.5 Flash / Pro / Ultra)
   - 가운데: Prompt 입력창
   - 오른쪽: Temperature, Top-K, Top-P 파라미터

**파라미터 이해:**
```
Temperature = AI의 "창의성" 조절
- 0.0: 매우 일관된 답변 (코드 생성에 적합)
- 1.0: 다양하고 창의적인 답변 (창작에 적합)
- 2.0: 매우 무작위적 (실험적)

Top-K = 다음 단어 선택 시 고려할 후보 수
Top-P = 누적 확률 기준 단어 선택 범위
```

**System Instruction 작성 (= Claude의 스킬!):**
```
[System Instruction 입력창에:]
당신은 한국어로 응답하는 전문 코딩 튜터입니다.
코드 설명은 항상 초보자도 이해할 수 있게 해주세요.
코드는 항상 완성된 실행 가능한 형태로 제공해주세요.
```

🎤 "보이시나요? Google AI Studio의 System Instruction이 Claude Co-work의 시스템 지침(스킬)과 같은 개념입니다. AI 도구마다 이름은 달라도 개념은 같아요."

**Gemini API 키 발급:**
1. 왼쪽 사이드바 "Get API key" 클릭
2. "Create API key" → "Google AI Studio에서 생성" 선택
3. 생성된 키 복사 → 안전한 곳에 저장 (다시 볼 수 없음!)

**코드 생성 보기:**
프롬프트 입력 후 응답 화면에서:
- "< >" 버튼 클릭 → Python/Node.js/cURL 코드 자동 생성
- 이것이 AI Studio를 "개발자 도구"로 만드는 기능

📌 **레벨 분기**
- **입문자**: System Instruction + 프롬프트 실험만
- **고급자**: API 키 발급 후 VS Code에서 Python으로 Gemini API 호출 테스트
  ```python
  import google.generativeai as genai
  genai.configure(api_key="YOUR_API_KEY")
  model = genai.GenerativeModel('gemini-1.5-flash')
  response = model.generate_content("바이브코딩을 한 문장으로 설명해줘")
  print(response.text)
  ```

---

### ④ 실습 2: NotebookLM (1:35~2:20)

👨‍💻 **NotebookLM 시작:**

1. notebooklm.google.com 접속 → Google 계정 로그인
2. "+ New Notebook" 클릭
3. 노트북 이름: "AI 바이브코딩 강의 자료"

**소스 추가하기 (4가지 방법):**

| 소스 유형 | 방법 | 적합한 상황 |
|---------|------|-----------|
| PDF 파일 | "파일 업로드" | 논문, 보고서, 교재 |
| Google Drive | 연동 선택 | 구글 문서, 스프레드시트 |
| YouTube URL | 링크 붙여넣기 | 강의 영상, 인터뷰 |
| 웹 URL | 링크 붙여넣기 | 블로그, 뉴스 기사 |
| 직접 입력 | 텍스트 붙여넣기 | 메모, 스크랩 내용 |

**실습 — 강사 배포 PDF 업로드:**
1. 강사가 배포한 PDF → "+ 소스 추가" → "파일 업로드"
2. 업로드 완료 후 채팅창에서 질문:
   ```
   이 문서의 핵심 내용을 5가지로 요약해줘.
   ```
3. Study Guide 생성: 상단 "Study Guide" 클릭 → AI가 퀴즈·요약·핵심 개념 자동 생성

**팟캐스트 생성 ("Audio Overview"):**
1. 오른쪽 상단 "오디오 개요" 클릭
2. "생성" 버튼 클릭 (1~3분 소요)
3. AI 2명이 대화하며 문서 내용을 팟캐스트 형식으로 요약

🎤 **강사 스크립트**
"NotebookLM의 팟캐스트는 정말 놀랍습니다. 50페이지짜리 논문을 업로드하면 10분짜리 대화형 팟캐스트가 됩니다. 강의 준비, 보고서 검토, 논문 정리에 매우 강합니다."

📌 **레벨 분기**
- **입문자**: PDF 업로드 → 요약 Q&A → 팟캐스트 생성
- **고급자**: 소스 5개 추가 후 "여러 문서 간의 공통점과 차이점을 분석해줘"

---

### ⑤ 실습 3: 안티그래비티 + Claude vs Gemini 비교 (2:20~2:50)

**[안티그래비티 실습 — 강사 확인 및 직접 구성 필요]**

*(강사가 사전에 안티그래비티 계정·기능·실습 시나리오를 확인한 후 이 섹션을 작성해주세요. 아래는 Claude vs Gemini 비교 실습으로 대체 가능합니다.)*

**Claude vs Gemini 심화 비교 실험:**

동일한 코딩 작업을 두 AI에게 요청하고 결과를 비교한다.

**실험 1 — 코드 생성:**
```
Python으로 간단한 파일명 일괄 변경 스크립트를 만들어줘.
폴더 내 모든 .txt 파일 앞에 날짜(YYYYMMDD) 추가.
```

**실험 2 — 오류 해석:**
```
아래 오류 메시지를 초보자가 이해할 수 있게 설명해줘:
TypeError: Cannot read properties of undefined (reading 'map')
```

**실험 3 — 문서 요약:**
```
아래 텍스트를 3문장으로 요약해줘:
[AI 관련 뉴스 기사 본문 붙여넣기]
```

**비교 결과 작성 워크시트:**
| 항목 | Claude | Gemini | 내 평가 |
|------|-------|--------|-------|
| 코드 품질 | | | |
| 설명 방식 | | | |
| 응답 속도 | | | |
| 내 상황에 적합한 도구 | | | |

---

### ⑥ 마무리 & 과제 (2:50~3:00)

🎤 "오늘 Google AI 4대 도구를 모두 체험했습니다. Google AI Studio는 API의 문, NotebookLM은 문서 분석의 신무기, Gemini는 Claude와 함께 쓰는 보조 AI. 상황마다 최적 도구를 선택하는 눈이 생겼습니다."

**과제:** NotebookLM에 관심 있는 PDF 업로드 → AI 팟캐스트 1편 생성 후 링크 또는 스크린샷 제출

---

## 5강: 웹페이지 제작 심화 — 인터랙티브 UI & API 연동
**일시**: 3주차 1회 | **시간**: 3시간

### 강의 목표 (수강자에게 보여줄 버전)
이 강의를 마치면 여러분은:
- HTML·CSS·JS의 역할 분담을 AI 관점에서 정확히 이해한다
- REST API를 Claude Code CLI와 함께 연동할 수 있다
- VS Code 심화 기능(멀티 커서·터미널 분할)을 실전에 활용한다
- 포트폴리오에 날씨 위젯과 다크모드를 추가해 GitHub Pages에 재배포할 수 있다

### 강사 준비물 체크리스트
- [ ] OpenWeather API 키 발급 가이드 (무료 가입)
- [ ] 강사용 백업 API 키 (수강자 발급 실패 대비)
- [ ] async/await 흐름 다이어그램 슬라이드
- [ ] Deprecated API 사례 인쇄물

---

### ① 과제 리뷰 (0:00~0:20)

🎤 "GitHub Pages URL 확인합니다. 4강 NotebookLM 팟캐스트도 들어보셨나요? (2명 공유) 오늘은 이 포트폴리오에 실제 날씨 데이터를 불러오는 위젯을 붙입니다."

---

### ② 이론: 웹 3대장 + REST API (0:20~0:50)

📺 **슬라이드 1 — "HTML·CSS·JS — AI에게 분리해서 요청하는 법"**

| 역할 | 언어 | 비유 | AI에게 요청할 때 |
|------|------|------|--------------|
| 구조 | HTML | 건물 뼈대 | "HTML 골격만 잡아줘, CSS 없어도 됨" |
| 스타일 | CSS | 인테리어 | "지금 CSS만 바꿔줘, 구조는 그대로" |
| 동작 | JavaScript | 전기·기계 | "버튼 클릭 시 동작하는 JS만 추가해줘" |

🎤 "AI에게 한 번에 전부 요청하면 오류가 쌓입니다. '이번엔 HTML만', '이번엔 CSS만' 이렇게 분리해서 요청하면 디버깅이 쉬워집니다."

📺 **슬라이드 2 — "REST API — 날씨를 가져오는 방법"**
```
[내 웹페이지] ──HTTP 요청──→ [OpenWeather 서버] ──JSON──→ [표시]
```

📺 **슬라이드 3 — "async/await — 기다리는 코드"**
```javascript
// ❌ 문제: 기다리지 않음
const data = fetch("날씨URL");  // 데이터가 안 왔는데 다음 줄 실행

// ✅ 해결: await로 기다림
const response = await fetch("날씨URL");   // 서버 응답 대기
const data = await response.json();        // JSON 파싱 대기
```

🎤 "await는 '기다려'라는 뜻입니다. AI에게 'fetch로 API 요청하는 코드'를 달라고 하면 자동으로 async/await를 씁니다. 개념만 이해하면 됩니다."

**⚠️ 중요: Deprecated API 주의**

📺 **슬라이드 4 — "AI 코드를 그대로 믿으면 안 되는 순간"**

🎤 "AI가 생성한 코드가 동작은 되는데 나중에 갑자기 멈추는 경우가 있습니다. 이유는 Deprecated API입니다. AI의 학습 데이터 이후에 API가 폐지됐으면 AI는 모릅니다."

| API | 변경 내용 | 영향 |
|-----|---------|------|
| OpenWeather 2.5 일부 엔드포인트 | 유료 전환 | 무료 앱에서 401 오류 |
| Twitter API v1.1 (2023.03) | 무료 tier 폐지 | 무료 봇·앱 전면 중단 |
| Facebook Graph API v2.x | 구버전 연도별 종료 | 구버전 코드 즉시 실패 |

**Deprecated 확인 프롬프트:**
```
이 코드에서 사용한 API·라이브러리 중 2024년 이후 deprecated 또는
유료 전환된 것이 있으면 알려줘. 최신 대안도 함께.
```

---

### ③ VS Code 심화 팁 (0:50~1:00)

👨‍💻 **오늘 실전에서 쓸 VS Code 팁:**

**멀티 커서 (Alt+Click):**
- 동시에 여러 줄 편집 가능
- 예: 여러 줄의 변수명을 한 번에 바꿀 때

**터미널 분할:**
- 터미널 오른쪽 상단 "+" 클릭 → 터미널 2개 동시 사용
- 왼쪽: `claude` (Claude Code CLI 실행)
- 오른쪽: 파일 확인·서버 실행

**Ctrl+P (빠른 파일 열기):**
- 프로젝트 내 파일명 타이핑으로 즉시 이동
- 파일이 많아질수록 필수 단축키

---

### ④ 실습 1: 날씨 위젯 제작 (1:00~1:50)

👨‍💻 **OpenWeather API 키 발급:**
1. openweathermap.org → Sign Up (무료)
2. 이메일 인증 완료
3. 내 계정 → API Keys → Default 키 복사

**Claude Code CLI에서 요청:**
```
portfolio 폴더에 날씨 위젯을 만들어줘.
- 파일: weather-widget.html (독립 파일로 먼저)
- 기능: 도시명 입력 → 버튼 클릭 → 현재 날씨(온도·날씨상태·습도) 표시
- OpenWeather API 사용 (https://api.openweathermap.org/data/2.5/weather)
- API 키는 YOUR_API_KEY 자리표시자로 (내가 나중에 바꿀게)
- fetch()와 async/await 사용
- 도시를 못 찾으면 "도시를 찾을 수 없습니다" 표시
- 한국어 인터페이스
```

**API 키 교체:**
생성된 코드에서 `YOUR_API_KEY` → 발급받은 실제 키로 교체

⚠️ **예상 오류 & 해결**
| 오류 | 원인 | Claude 디버깅 프롬프트 |
|------|------|----------------------|
| CORS 오류 | 브라우저 직접 호출 제한 | "CORS 오류 납니다. OpenWeather API로 직접 해결 방법?" → 대부분 허용됨 |
| 401 Unauthorized | API 키 오류 또는 발급 직후 (10분 대기) | "401 에러. 키가 [xxx]인데 맞게 넣었나?" |
| 도시명 한글 불가 | API는 영어만 | "한글 도시명 검색되게 해줘" → Claude가 변환 로직 추가 |

📌 **레벨 분기**
- **입문자**: 강사 백업 API 키 사용, 기본 기능만
- **고급자**: 5일 예보 추가(`/forecast`), 날씨 아이콘 표시, 자동 위치 감지(`navigator.geolocation`)

---

### ⑤ 실습 2: 포트폴리오에 위젯 통합 + 다크모드 (1:50~2:40)

👨‍💻 **Claude Code CLI에서 요청:**
```
portfolio/index.html에 방금 만든 날씨 위젯을 통합해줘.
그리고 다크모드 토글 버튼도 추가해줘:
- 버튼: 오른쪽 상단 ☀️/🌙 아이콘
- 클릭 시 배경/텍스트 색상 반전
- localStorage로 사용자 선택 저장 (새로고침 후에도 유지)
```

---

### ⑥ 실습 3: AI UX 코드 리뷰 (2:40~2:50)

👨‍💻 **Claude Chat에서 요청:**
```
내 포트폴리오 index.html의 UX 문제점 5가지를 찾아줘.
[코드 전체 붙여넣기]
모바일 사용성·접근성·로딩 속도·시각적 계층 관점에서.
```

---

### ⑦ 마무리 & 과제 (2:50~3:00)

**과제:** 공개 API 1개 이상 연동한 인터랙티브 웹페이지를 GitHub Pages에 배포하고 URL 제출

---

## 6강: AI 코드 리뷰 & 디버깅 — 오류 없는 코드의 비밀
**일시**: 3주차 2회 | **시간**: 3시간

### 강의 목표 (수강자에게 보여줄 버전)
이 강의를 마치면 여러분은:
- 에러 메시지 구조를 파악하고 AI에게 효과적으로 전달할 수 있다
- Claude Code CLI로 에러 + 코드 컨텍스트를 제공해 디버깅을 주도할 수 있다
- 보안 취약점(API 키 노출·XSS·SQL 인젝션)을 AI 리뷰로 탐지할 수 있다
- 단위 테스트를 AI에게 위임하고 결과를 검증할 수 있다

### 강사 준비물 체크리스트
- [ ] 의도적 버그 3종 파일 (타입 오류·로직 오류·보안 취약)
- [ ] SQL 인젝션 시연 코드 (교육용)
- [ ] API 키 노출 사고 사례 인쇄물

---

### ① 과제 리뷰 + 오류 사례 수집 (0:00~0:20)

🎤 "5강 과제에서 API 연동하면서 오류 만나신 분 계시나요? (2~3명 공유) 오늘 그 오류들을 AI와 함께 해결하는 체계적인 방법을 배웁니다."

---

### ② 에러 해부학 (0:20~0:45)

📺 **슬라이드 1 — "에러 메시지는 AI에게 보내는 편지"**

🎤 "에러 메시지가 나오면 무서워하지 마세요. AI에게 그대로 붙여넣으면 됩니다. 그런데 더 잘 전달하면 더 빠르게 해결됩니다."

**JavaScript 에러 타입 3가지:**

| 에러 타입 | 예시 | 의미 | Claude 프롬프트 |
|---------|------|------|--------------|
| SyntaxError | `SyntaxError: Unexpected token ')'` | 문법 오류 (괄호, 쉼표 실수) | "이 오류가 어디서 나는지 찾아줘" |
| TypeError | `TypeError: Cannot read properties of undefined` | 없는 것에 접근 | "undefined가 왜 나는지 설명하고 고쳐줘" |
| ReferenceError | `ReferenceError: myFunc is not defined` | 선언 안 된 변수/함수 | "이 함수가 왜 없다고 하는지 찾아줘" |

**브라우저 콘솔 여는 법:**
- Chrome/Edge: F12 → Console 탭
- 빨간 글씨 = 에러, 노란 글씨 = 경고

**효과적인 디버깅 프롬프트 공식:**
```
[현재 코드: {코드 붙여넣기}]
[에러 메시지: {에러 전체 복사}]
[상황: {어떤 동작을 했을 때 오류가 났는지}]

이 오류의 원인을 설명하고 수정 코드를 주세요.
```

---

### ③ 어떤 도구로 디버깅할까? (0:45~1:00)

📺 **슬라이드 2 — "상황별 디버깅 도구 선택"**

| 상황 | 최적 도구 | 이유 |
|------|---------|------|
| 단순 오류 메시지 해석 | Claude Chat | 빠른 설명, 맥락 짧아도 됨 |
| 여러 파일에 걸친 오류 | Claude Code CLI | 전체 코드베이스 인식 |
| 특정 기능 코드 리뷰 | Claude Chat | 코드 붙여넣기 + 관점 지정 |
| 리팩터링 적용 | Claude Code CLI | 직접 파일 수정 |
| 보안 취약점 검토 | Claude Chat | 전문 리뷰어 역할 부여 |

---

### ④ 실습 1: 버그 3종 수정 대회 (1:00~1:45)

🎤 "강사가 배포한 파일에 의도적으로 3종류의 버그를 심어뒀습니다. Claude Code CLI로 최소 대화 횟수에 찾아서 고치는 대결입니다."

👨‍💻 **버그 파일 (강사 배포):**

**bug1.html — 타입 오류 (입문자 수준):**
```html
<script>
  let score = "10";  // 숫자가 문자열로 저장됨
  let bonus = 5;
  let total = score + bonus;  // "105" 가 됨 (원하는 건 15)
  document.getElementById('result').textContent = "총점: " + total;
</script>
```
*의도된 오류: 문자열 + 숫자 = 문자열 연결*

**bug2.js — 로직 오류 (중급 수준):**
```javascript
function findMax(arr) {
  let max = 0;  // 음수 배열에서 항상 0 반환
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) max = arr[i];
  }
  return max;
}
// findMax([-5, -3, -1]) → 0 (틀림, -1이어야 함)
```

**bug3.html — 보안 취약 (XSS — 고급 수준):**
```html
<input id="name" type="text">
<button onclick="greet()">인사</button>
<div id="result"></div>
<script>
  function greet() {
    let name = document.getElementById('name').value;
    document.getElementById('result').innerHTML = "안녕하세요, " + name; // XSS 취약
    // <img src=x onerror="alert('XSS')"> 입력하면 공격 가능
  }
</script>
```

**Claude Code CLI 디버깅 요청:**
```
[bug1.html / bug2.js / bug3.html을 Claude Code CLI로 열고]

이 파일에서 버그를 찾아서 수정해줘.
버그 종류(타입 오류·로직 오류·보안 취약)도 알려줘.
```

📌 **레벨 분기**
- **입문자**: bug1만, Claude가 설명해주는 것 읽고 이해
- **고급자**: 3개 모두, XSS 수정 방법(`textContent` vs `innerHTML`) 설명 요청

---

### ⑤ 실습 2: 코드 리뷰 + .env API 키 분리 (1:45~2:30)

> [!TIP] **잠깐 — 1강에서 본 에이전트팀·하네스 기억하시나요?**
> 지금 우리가 하는 것이 바로 그겁니다. 각자가 다른 역할(버그 수정 → 코드 리뷰 → 보안 점검)을 수행하고, AI가 각 단계의 도구를 제어합니다. 이게 에이전트팀 워크플로우의 축소판입니다. 8강에서 이 구조를 자동화(하네스)로 묶을 예정입니다.

👨‍💻 **5강 과제 코드 Claude Chat + Co-work 리뷰:**

🎤 "오늘 코드 리뷰는 두 가지 방법으로 해봅니다. Claude Chat 일회성 리뷰 vs Co-work 스킬 재사용."

**방법 1 — Claude Chat (일회성):**
```
아래 코드를 보안·성능·가독성 3관점에서 코드 리뷰해줘.
각 관점에서 문제점 2가지씩, 개선 방법 포함.
[5강 과제 코드 전체 붙여넣기]
```

**방법 2 — Claude Co-work (재사용 스킬):**
```
# Co-work 시스템 지침에 추가할 "코드 리뷰어" 스킬:
당신은 시니어 웹 개발자입니다.
코드를 리뷰할 때 항상 보안·성능·가독성 3관점을 적용합니다.
각 관점에서 문제점 2개와 개선 방법을 제시합니다.
심각도(Critical/Major/Minor)를 명시합니다.
```
🎤 "이 스킬을 한 번 만들어두면 앞으로 어떤 코드든 같은 품질로 리뷰받을 수 있습니다. 이게 스킬의 힘입니다."

**API 키 .env 분리 라이브 시연:**

🎤 "실제로 일어난 일을 말씀드립니다. 2023년 한 스타트업 개발자가 AWS 키를 GitHub에 올렸습니다. 30분 만에 봇이 키를 발견하고 비트코인 채굴에 사용했습니다. 하루 만에 수천만 원 청구서. 이걸 막는 게 .env와 .gitignore입니다."

```bash
# Claude Code CLI에서:
.env 파일을 만들어줘. 그리고 index.html에서 API 키를 하드코딩한 부분을
환경변수로 분리하는 방법을 알려줘. (HTML은 직접 .env를 못 읽으니까
서버 없이 하는 방법도 포함해줘)
```

```bash
# .gitignore 추가
.env
.env.local
node_modules/
```

---

### ⑥ 실습 3: AI 단위 테스트 작성 (2:30~2:50)

👨‍💻 **Claude Chat에서 요청:**
```
아래 함수에 대한 단위 테스트를 Jest 없이 순수 JS로 작성해줘.
테스트 케이스: 정상 입력, 경계값, 오류 입력 각각 2개씩.

function formatPrice(price) {
  if (typeof price !== 'number') throw new Error('숫자만 가능');
  return price.toLocaleString('ko-KR') + '원';
}
```

---

### ⑦ 마무리 & 과제 (2:50~3:00)

**과제:** 5강 과제 코드의 AI 코드 리뷰 보고서 작성 (보안·성능·가독성 3관점, 각 문제점 + 개선 방법) 제출

---

## 7강: 나만의 AI 앱 제작 — Supabase + AI API로 풀스택 MVP
**일시**: 4주차 1회 | **시간**: 3시간

### 강의 목표 (수강자에게 보여줄 버전)
이 강의를 마치면 여러분은:
- GitHub·Supabase·Vercel 3종이 현대 풀스택 앱의 표준 인프라임을 이해한다
- Supabase 프로젝트를 생성하고 회원가입·로그인(Auth)과 게시물 저장(Database)을 구현할 수 있다
- Claude Co-work에서 Supabase 스키마가 포함된 기획서를 작성할 수 있다
- 스타터킷 3종 중 하나를 골라 Supabase + AI API를 연동한 MVP를 완성할 수 있다

### 강사 준비물 체크리스트
- [ ] 스타터킷 3종 완성 코드 파일 (챗봇·요약기·게시판 — Supabase 연동 버전)
- [ ] Supabase 가입·프로젝트 생성 단계별 스크린가이드 PDF
- [ ] Claude API vs Gemini API 비교표 슬라이드
- [ ] MVP 기획서 템플릿 (문제·기능·스택·Supabase 스키마·와이어프레임)
- [ ] 강사 백업 Supabase 프로젝트 (수강자 설정 실패 대비)

---

### ① 과제 리뷰 + 프로젝트 주제 1분 발표 (0:00~0:20)

🎤 "6강 코드 리뷰 보고서 제출하셨나요? 오늘은 1~6강에서 배운 모든 것을 합쳐 나만의 AI 앱을 만듭니다. 각자 30초씩 — 어떤 앱을 만들고 싶으신지 한 문장으로 말씀해주세요."

---

### ② 이론: 현대 풀스택 아키텍처 + MVP 설계 (0:20~0:45)

📺 **슬라이드 1 — "GitHub + Supabase + Vercel = 현대 풀스택 3종 세트"**

```
[GitHub]          [Supabase]            [Vercel]
코드 저장소   →   DB + Auth + Storage  →  배포 · 환경변수
버전 관리         PostgreSQL 기반          GitHub push → 자동 배포
CI/CD 소스        무료 플랜 충분           전 세계 CDN
```

🎤 "현업에서 새 프로젝트를 시작할 때 가장 많이 쓰는 조합입니다. 셋 다 무료 플랜이 있고, 오늘 여러분이 전부 연결합니다."

📺 **슬라이드 2 — "Supabase = 백엔드를 코드 없이 만드는 도구"**

| Supabase 기능 | 하는 일 | 비유 |
|-------------|--------|------|
| **Database** | PostgreSQL 테이블 — 게시물·댓글·사용자 데이터 저장 | 엑셀 시트 |
| **Auth** | 회원가입·로그인 (이메일·Google·GitHub OAuth) | 문지기 |
| **Storage** | 이미지·파일 업로드 | 구글 드라이브 |
| **Row Level Security** | 본인 데이터만 접근 허용 | 자물쇠 |

📺 **슬라이드 3 — "풀스택 AI 앱 4계층 구조"**
```
[프론트엔드]  ←→  [Supabase Auth]  ←→  [Supabase DB]
HTML/CSS/JS        로그인·세션             게시물·사용자
     ↕                                        ↕
[AI API]      ←→  [백엔드(선택)]  ←→  [AI 결과 저장]
Claude/Gemini      Flask(필요시)         DB에 AI 요약 저장
```

📺 **슬라이드 4 — "Claude API vs Gemini API"**

| 항목 | Claude API (Anthropic) | Gemini API (Google) |
|------|----------------------|-------------------|
| 주력 모델 | claude-sonnet-4-6 | gemini-1.5-flash |
| 강점 | 코딩·문서·안전성 | 속도·멀티모달·저렴 |
| 무료 크레딧 | 신규 $5 | 분당 무료 요청 있음 |
| API 키 발급 | console.anthropic.com | Google AI Studio |
| 추천 | 코딩 앱·문서 처리 앱 | 빠른 응답·이미지 포함 앱 |

📺 **슬라이드 5 — "MVP의 법칙 — 딱 하나만"**
- MVP = Minimum Viable Product = 핵심 기능 1개로 동작하는 최소 제품
- Feature Creep 경고: "이것도 넣고 싶다, 저것도" → 아무것도 완성 안 됨
- **오늘 MVP 제안**: 로그인 → 게시물 1개 작성 → AI 자동 요약 저장

---

### ③ 실습 1: Supabase 프로젝트 설정 (0:45~1:20)

👨‍💻 **Supabase 계정 생성 & 프로젝트 설정:**

**Step 1 — 가입 & 프로젝트 생성:**
1. supabase.com → "Start your project" → GitHub 계정으로 로그인
2. "New Project" 클릭
3. 이름: `my-ai-app` | 지역: `Northeast Asia (Seoul)` | 비밀번호 입력 → "Create"
4. 프로젝트 생성까지 1~2분 대기

**Step 2 — 연결 정보 복사:**
1. Settings → API
2. `Project URL` 복사 → `.env`에 저장
3. `anon public` 키 복사 → `.env`에 저장

```env
# .env
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
ANTHROPIC_API_KEY=sk-ant-...
```

**Step 3 — Authentication 설정:**
1. Authentication → Providers
2. Email 기본 활성화 확인
3. (고급) Google OAuth → Enable → Client ID/Secret 입력

**Step 4 — Database 테이블 생성 (Table Editor):**
1. Table Editor → "New Table"
2. 테이블명: `posts`
3. 컬럼 추가:

```sql
-- SQL Editor에서 직접 실행도 가능
create table posts (
  id        uuid    default gen_random_uuid() primary key,
  user_id   uuid    references auth.users(id) on delete cascade,
  title     text    not null,
  content   text,
  ai_summary text,          -- Claude가 자동 생성
  created_at timestamptz default now()
);

-- RLS 활성화 (본인 게시물만 접근)
alter table posts enable row level security;

create policy "본인 게시물만 CRUD" on posts
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);
```

**Step 5 — JS 클라이언트 설치:**
```bash
# VS Code 터미널 (또는 Claude Code CLI)
npm install @supabase/supabase-js
```

**Supabase 연결 코드 (supabase.js):**
```javascript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_ANON_KEY
)
export default supabase
```

⚠️ **예상 오류 & 해결**
| 오류 | 원인 | 해결 |
|------|------|------|
| "Invalid API key" | anon key가 아닌 service key 사용 | Settings → API → anon public 키 재확인 |
| RLS 정책 오류 | 로그인 없이 insert 시도 | Auth 상태 확인 후 재시도 |
| CORS 오류 | Supabase URL 오타 | `.env`의 URL 끝에 `/` 없는지 확인 |

📌 **레벨 분기**
- **입문자**: Step 1~3까지 (계정·URL·Key 확보) + 강사 배포 SQL 실행
- **고급자**: RLS 정책 직접 작성 + Google OAuth 연동

---

### ④ 실습 2: Co-work 기획서 + Supabase 스키마 설계 (1:20~1:50)

👨‍💻 **Claude Co-work 새 Project 생성:**
이름: "[내 프로젝트명] 기획"

**기획서 작성 프롬프트:**
```
내 AI 앱 기획을 도와줘. Supabase + Flask + Claude API를 쓸 예정이야.

아이디어: [본인 아이디어 1줄]

아래 항목을 채워줘:
1. 문제 정의: 누가, 어떤 불편함을 겪는가?
2. 타겟 사용자: 구체적으로 누구인가?
3. 핵심 기능 3가지 (우선순위 순)
4. 기술 스택: 프론트(HTML/JS) + 백엔드(Flask) + DB(Supabase) + AI(Claude API)
5. Supabase 테이블 스키마 제안 (컬럼명·타입·설명)
6. 오늘 MVP로 구현할 기능 딱 1가지
7. 화면 구성 (텍스트 와이어프레임)
```

---

### ⑤ 실습 3: MVP 구현 스프린트 (1:50~2:50)

**[스타터킷 3종 — 강사 사전 배포. Supabase 연동 버전]**

---

**★ 스타터킷 A: AI 챗봇 + 대화 이력 저장 (Chatbot)**

**Claude Code CLI에서 요청:**
```
내 프로젝트 폴더에 Claude API 챗봇을 만들어줘.
- 파일: index.html + server.py (Flask)
- 기능: 채팅 입력창 → Claude 응답 → Supabase DB에 대화 이력 저장
- Supabase Auth로 로그인한 사용자만 채팅 가능
- 환경변수: ANTHROPIC_API_KEY, SUPABASE_URL, SUPABASE_ANON_KEY
```

핵심 Python 코드:
```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic, os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_ANON_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    history = data.get('history', [])
    history.append({"role": "user", "content": data['message']})
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=history
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})

    # Supabase에 대화 저장
    supabase.table('chats').insert({
        "user_id": data.get('user_id'),
        "message": data['message'],
        "reply": reply
    }).execute()

    return jsonify({"reply": reply, "history": history})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

**★ 스타터킷 B: AI 게시판 (AI-powered Board)**

**Claude Code CLI에서 요청:**
```
내 프로젝트 폴더에 AI 게시판 앱을 만들어줘.
- 파일: index.html + server.py (Flask)
- 기능:
  1. Supabase Auth로 회원가입/로그인
  2. 게시물 작성 → Supabase DB posts 테이블에 저장
  3. 저장 시 Claude API로 게시물 AI 요약 자동 생성 → ai_summary 컬럼 저장
  4. 게시물 목록 조회 (제목·요약 표시)
- 환경변수: ANTHROPIC_API_KEY, SUPABASE_URL, SUPABASE_ANON_KEY
```

핵심 Python 코드:
```python
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json

    # Claude API로 AI 요약 생성
    summary_response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        messages=[{"role": "user",
                   "content": f"다음 글을 2줄로 요약해줘:\n\n{data['content']}"}]
    )
    ai_summary = summary_response.content[0].text

    # Supabase DB에 저장
    result = supabase.table('posts').insert({
        "user_id": data['user_id'],
        "title": data['title'],
        "content": data['content'],
        "ai_summary": ai_summary
    }).execute()

    return jsonify({"post": result.data[0], "summary": ai_summary})

@app.route('/posts', methods=['GET'])
def get_posts():
    result = supabase.table('posts').select('*').order('created_at', desc=True).execute()
    return jsonify(result.data)
```

---

**★ 스타터킷 C: AI 요약기 (Summarizer)**

```python
import anthropic, os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def summarize(text, lines=3):
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"다음 텍스트를 {lines}줄로 요약해줘:\n\n{text}"
        }]
    )
    return message.content[0].text
```

---

📌 **레벨 분기**
- **입문자**: 스타터킷 B(게시판) 코드 그대로 실행 → Supabase 연결 확인 → 게시물 1개 작성·저장
- **고급자**: 스트리밍 응답(타이핑 효과) + Supabase Storage로 이미지 첨부 + Gemini API 대체 실험

---

### ⑥ 마무리 & 과제 (2:50~3:00)

👨‍💻 **Claude Co-work 새 Project 생성:**
이름: "[내 프로젝트명] 기획"

**기획서 작성 프롬프트:**
```
내 AI 앱 기획을 도와줘.

아이디어: [본인 아이디어 1줄]

아래 항목을 채워줘:
1. 문제 정의: 누가, 어떤 불편함을 겪는가?
2. 타겟 사용자: 구체적으로 누구인가?
3. 핵심 기능 3가지 (우선순위 순)
4. 추천 기술 스택 (HTML+Python / Node.js 등)
5. 오늘 MVP로 구현할 기능 딱 1가지
6. 화면 구성 (텍스트 와이어프레임)
```

---

### ④ 실습 2: MVP 구현 스프린트 (1:40~2:50)

**[스타터킷 3종 — 강사 사전 배포. 입문자는 이 코드 베이스 활용]**

---

**★ 스타터킷 A: AI 챗봇 (Chatbot)**

**Claude Code CLI에서 요청:**
```
내 프로젝트 폴더에 Claude API를 사용한 대화형 챗봇을 만들어줘.
- 파일: index.html + server.py (Flask)
- 기능: 채팅 입력창 → 전송 → Claude가 대화 히스토리 유지하며 응답
- 사용자/AI 말풍선 구분 표시
- Claude API 키는 .env, Flask CORS 포함
```

핵심 Python 코드 (강사 설명용):
```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    history = data.get('history', [])
    history.append({"role": "user", "content": data['message']})
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=history
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply, "history": history})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

**★ 스타터킷 B: AI 요약기 (Summarizer)**

**Claude Code CLI에서 요청:**
```
내 프로젝트 폴더에 Claude API 텍스트 요약 앱을 만들어줘.
- 파일: index.html + server.py (Flask)
- 기능: 텍스트 입력 → "요약해줘" 버튼 → Claude API → 요약 표시
- 요약 길이 선택: 1줄 / 3줄 / 5줄 라디오 버튼
- .env API 키, Flask CORS
```

핵심 Python 코드:
```python
import anthropic, os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def summarize(text, lines=3):
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"다음 텍스트를 {lines}줄로 요약해줘:\n\n{text}"
        }]
    )
    return message.content[0].text
```

---

**★ 스타터킷 C: 데이터 대시보드 (Data Dashboard)**

**Claude Code CLI에서 요청:**
```
CSV 파일 업로드 → pandas 분석 → Chart.js 차트 3개 표시하는 앱 만들어줘.
- 파일: index.html + server.py (Flask)
- 차트: 숫자형 컬럼 평균 막대차트 + 시계열 라인 + 요약 테이블
- Claude API로 "데이터 주요 인사이트 3가지" 자동 분석
- pandas, flask, flask-cors, anthropic 패키지
```

---

📌 **레벨 분기**
- **입문자**: 스타터킷 A·B·C 중 1개 → 강사 코드 그대로 실행 후 AI 역할 프롬프트만 수정
- **고급자**: 스트리밍 응답 (타이핑 효과), 로그인 기능, Gemini API로 대체 실험

---

### ⑤ 마무리 & 과제 (2:50~3:00)

**과제:** 기획서(문제 정의·기능·스택·와이어프레임) + 핵심 기능 1개 동작 스크린샷 제출

---

## 8강: 프로덕션 배포 & 고급 워크플로우 — 세상에 내보내기
**일시**: 4주차 2회 | **시간**: 3시간

### 강의 목표 (수강자에게 보여줄 버전)
이 강의를 마치면 여러분은:
- GitHub → Supabase → Vercel 삼위일체 스택으로 풀스택 앱을 프로덕션에 배포할 수 있다
- Vercel 환경변수로 API 키·Supabase 키를 안전하게 관리할 수 있다
- CI/CD 파이프라인을 이해하고 GitHub push → Vercel 자동 배포를 설정할 수 있다
- 하네스(에이전트팀)를 Claude Code CLI에서 직접 구동할 수 있다
- Claude·Gemini·VS Code·스킬·에이전트·MCP·하네스를 조합한 개인 워크플로우를 체계화할 수 있다

### 강사 준비물 체크리스트
- [ ] Vercel 배포 단계별 스크린가이드 PDF
- [ ] 수강자용 하네스 스타터킷 (2~3 에이전트, 단순 버전)
- [ ] 개인 워크플로우 체계화 템플릿
- [ ] 수료 후 3갈래 로드맵 슬라이드

---

### ① 배포 개념 이론 (0:00~0:20)

📺 **슬라이드 1 — "개발환경 vs 스테이징 vs 프로덕션"**

| 환경 | 특성 | 접근 |
|------|------|------|
| 개발(localhost) | 실험 가능, 혼자만 접근 | 내 컴퓨터에서만 |
| 스테이징 | 프로덕션과 동일, 최종 검증 | 팀 내부 |
| 프로덕션 | 실제 사용자 접근, 안정성 최우선 | 전 세계 |

🎤 "4주 동안 여러분은 개발환경(내 컴퓨터)에서 작업했습니다. 오늘은 그 결과물을 전 세계가 접근할 수 있는 프로덕션으로 내보냅니다."

---

### ② 보안 필수 체크리스트 (0:20~0:40)

📺 **슬라이드 2 — "API 키 노출 사고 사례"**

🎤 "실제로 일어난 일입니다. 2023년 한 스타트업 개발자가 AWS 키를 GitHub에 올렸습니다. 30분 만에 봇이 발견해 비트코인 채굴에 사용했습니다. 하루 청구서: 수천만 원."

**배포 전 보안 체크:**
```bash
# Claude Code CLI에서 자동 생성:
.gitignore 파일 만들어줘. Node.js + Python + 환경변수 파일 모두 포함
```

```
# .gitignore 기본 구성
.env
.env.local
node_modules/
__pycache__/
*.pyc
venv/
```

- [ ] API 키(`ANTHROPIC_API_KEY`, `GEMINI_API_KEY`)가 코드에 하드코딩돼 있지 않은가?
- [ ] Supabase 키(`SUPABASE_URL`, `SUPABASE_ANON_KEY`)가 `.env`에만 있고 코드에 없는가?
- [ ] `.env` 파일이 `.gitignore`에 등록됐는가?
- [ ] 과거 커밋에도 키가 없는지 확인했는가? (`git log -p | grep -i supabase`)
- [ ] Vercel 환경변수에 API 키·Supabase 키를 별도 등록할 것인가?

> [!WARN] Supabase `service_role` 키(관리자 키)는 절대 프론트엔드에 노출 금지 — `anon` 키만 사용하고 RLS로 제어한다

---

### ③ CI/CD 입문 (0:40~1:00)

📺 **슬라이드 3 — "Push하면 자동 배포"**
```
[VS Code] → git push → [GitHub] → [Vercel 자동 감지] → [프로덕션 배포]
```
- CI (Continuous Integration): 코드 변경 시 자동 테스트
- CD (Continuous Deployment): 테스트 통과 시 자동 배포
- 비유: 원고 저장 → 출판사가 자동으로 책 만드는 것

🎤 "오늘 Vercel과 GitHub을 연결하면 자동으로 CI/CD가 됩니다. 이후엔 코드를 push할 때마다 Vercel이 알아서 새로 배포합니다. 현업 개발자들이 매일 쓰는 워크플로우입니다."

---

### ④ 실습 1: Vercel 배포 (1:00~1:40)

👨‍💻 **단계별 지시:**

1. vercel.com → "Continue with GitHub" 로그인
2. "Import Project" → 7강에서 만든 리포 선택
3. **환경변수 설정** (Settings → Environment Variables에서 입력):
   - `ANTHROPIC_API_KEY` = `sk-ant-...`
   - `SUPABASE_URL` = `https://xxxx.supabase.co`
   - `SUPABASE_ANON_KEY` = `eyJhbGci...`
4. "Deploy" 클릭 → 2~3분 → URL 생성
5. 생성된 URL 브라우저에서 확인 → 로그인·게시물 저장 동작 테스트

**배포 후 테스트:**
```bash
# Claude Code CLI에서
내 Vercel 배포 앱에서 API 키가 환경변수로 안전하게 처리됐는지 코드 확인해줘
```

⚠️ **예상 오류 & 해결**
| 오류 | 원인 | Claude 디버깅 프롬프트 |
|------|------|----------------------|
| Build failed | 패키지 설치 오류 | 빌드 로그 전체를 Claude에 붙여넣기 |
| 환경변수 undefined | Vercel 대시보드 설정 누락 | "Vercel 환경변수 설정 방법 알려줘" |
| CORS 오류 (프로덕션) | 도메인 불일치 | "Flask CORS 설정에 Vercel 도메인 추가해줘" |

---

### ⑤ 실습 2: 최종 프로젝트 완성 (1:40~2:20)

🎤 "지금부터 40분, 여러분의 MVP를 최대한 완성하는 시간입니다. Claude Code CLI로 막힌 것들을 해결하세요. 강사와 보조 강사가 돌아다니며 도와드립니다."

👨‍💻 **디버깅 도우미 프롬프트:**
```
내 앱에서 [구체적 문제]가 있어. 
현재 상황: [어떤 동작을 했을 때 문제가 나는지]
에러 메시지: [에러 전체]
수정해줘.
```

---

### ⑥ 실습 3: 하네스 직접 실행 (2:20~2:35)

🎤 **강사 스크립트**
"드디어 왔습니다. 1강에서 제가 보여드린 것 기억하시죠? AI 5명이 팀을 이뤄 뉴스레터를 만들던 장면. 오늘 여러분이 직접 실행합니다."

*(강사가 미리 준비한 하네스 스타터킷 배포)*

👨‍💻 **하네스 실행:**
```bash
# 배포된 하네스 폴더로 이동
cd mini-harness

# Claude Code CLI 실행
claude
```

```
이 하네스를 실행해줘. 주제: "AI 바이브코딩 오늘 배운 것 정리"
에이전트 1(리서처): 오늘 배운 핵심 포인트 3가지 수집
에이전트 2(작가): 뉴스레터 형식으로 정리
에이전트 3(편집자): 검토 후 최종 파일 생성
```

*(에이전트들이 순서대로 실행되며 결과 파일 생성)*

🎤 "어떠세요? 1강에서 보기만 했던 것을 지금 직접 실행했습니다. 에이전트팀이 스킬 파일을 갖고 MCP로 파일을 만들면서 협업했습니다. 4주 동안 배운 모든 개념이 지금 이 화면에 있습니다."

---

### ⑦ 동료 평가 세션 (2:35~2:50)

📺 **슬라이드 — "최종 프로젝트 동료 평가 체크리스트 (4관점)"**
- [ ] **기능**: 요청한 핵심 기능이 동작하는가?
- [ ] **UX**: 사용자가 직관적으로 사용할 수 있는가?
- [ ] **코드 품질**: API 키 노출 없음, 에러 처리 있음
- [ ] **보안**: .env 사용, .gitignore 적용
- 잘한 점 1가지, 개선 제안 1가지

*(짝 활동: 옆 사람 프로덕션 URL 열어서 5분간 평가)*

---

### ⑧ 개인 워크플로우 체계화 & 수료식 (2:50~3:00)

📺 **슬라이드 — "나의 바이브코딩 도구 선택 가이드"**

| 상황 | 최적 도구 |
|------|---------|
| 빠른 아이디어 검증, 1회성 코드 | Claude Chat |
| 프로젝트 맥락 유지, 반복 작업 | Claude Co-work (스킬 설정) |
| 실제 파일 수정, 멀티파일 프로젝트 | Claude Code CLI |
| Google 문서·이미지·서비스 연동 | Gemini |
| 논문·보고서·강의자료 분석 | NotebookLM |
| 여러 AI 에이전트가 협업하는 파이프라인 | 하네스 |
| 외부 도구(GitHub·Notion) Claude에 연결 | MCP 서버 |

📺 **슬라이드 — "수료 후 3갈래 로드맵"**

**① 풀스택 개발자 방향**
- Next.js (React 기반 풀스택) + FastAPI (Python 백엔드)
- Supabase (PostgreSQL DB) + Vercel (배포)
- "Claude Code CLI와 함께하면 1년 걸릴 것을 3개월에"

**② AI 에이전트 빌더 방향**
- LangGraph (에이전트 프레임워크) + MCP 서버 직접 제작
- Claude API 고급 활용 (툴 유즈, 스트리밍, 멀티 에이전트)
- "지금 배운 하네스의 프로 버전"

**③ 데이터 분석가 방향**
- Python pandas·NumPy + SQL
- Tableau / Power BI / Streamlit
- NotebookLM + Google AI Studio로 분석 가속
- "AI로 데이터 분석 자동화"

🎤 **강사 스크립트 (마무리)**
"수료를 축하합니다! 4주 전에 코딩이 두렵다고 하셨던 분들, 지금 프로덕션에 앱이 배포되어 있습니다. Claude Chat·Co-work·Code CLI·Gemini·AI Studio·NotebookLM·VS Code·GitHub·스킬·에이전트·MCP·하네스. 이 도구들을 이해한 사람은 AI 생태계의 언어를 아는 사람입니다. 거기서부터 여러분의 진짜 여정이 시작됩니다."

**수료 선물:**
- 프롬프트 라이브러리 Notion 템플릿
- 바이브코딩 도구 선택 가이드 카드 (위 표)
- 3갈래 로드맵 상세 학습 자료 링크

---

*강의노트 작성 완료 — AI 활용 바이브코딩 8강 전체 v2*
*콘텐츠 작성자: Course Builder Harness Content-Writer*
