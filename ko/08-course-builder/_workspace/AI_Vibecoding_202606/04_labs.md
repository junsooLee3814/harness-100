# AI 활용 바이브코딩 — 실습과제 & 캡스톤 v2

> **구성**: 강별 실습과제(8개) + 캡스톤 프로젝트(최종)
> **제출 방법**: GitHub Pages URL 또는 스크린샷 + 코드 파일

---

## 강별 실습과제

### Lab 01: 나를 소개하는 페이지 (1강 과제)
**블룸 수준**: ③적용 | **소요 시간**: 30~60분 | **도구**: Claude Chat

**목표**: Claude Chat으로 첫 HTML 페이지를 만들고 브라우저에서 실행한다.

**요구사항:**
- [ ] Claude Chat에 아래 프롬프트(또는 본인 버전)를 입력한다
- [ ] 결과 코드를 `intro.html`로 저장하고 브라우저에서 연다
- [ ] **이름·직업·관심사** 3가지 이상이 포함된 소개 페이지

**스타터 프롬프트 (입문자용):**
```
나를 소개하는 한 페이지 웹사이트를 HTML로 만들어줘.
- 이름: [내 이름]
- 직업 또는 하고 싶은 것: [내용]
- 관심사 3가지: [목록]
- 디자인: 깔끔하고 밝은 느낌, 배경 흰색
- 완성된 전체 HTML 코드로 줘
```

**고급자 추가 도전:**
- [ ] 같은 주제로 Gemini에도 요청해 두 결과물을 나란히 비교
- [ ] Claude Chat에서 "이 코드의 장점 2가지와 개선할 점 2가지"를 요청하고 개선 버전 받기

**제출:** `intro.html` 파일 + 브라우저 실행 스크린샷

**채점 기준 (10점):**
| 항목 | 배점 | 기준 |
|------|------|------|
| 요청한 콘텐츠 포함 | 4점 | 이름·직업·관심사 3개 이상 |
| 브라우저 실행 확인 | 3점 | 스크린샷에서 정상 표시 |
| 본인 맞춤화 | 2점 | 기본 더미 텍스트를 실제 내용으로 교체 |
| 1강 하네스 시연 묘사 | 1점 | 1~3문장 서술 (발표 대비) |

---

### Lab 02: Co-work 스킬 + STAR 계산기 (2강 과제)
**블룸 수준**: ③적용 | **소요 시간**: 45~75분 | **도구**: Claude Co-work

**목표**: 스킬이 담긴 Co-work Project를 만들고 STAR 프롬프트로 계산기 앱을 완성한다.

**요구사항:**
- [ ] Claude Co-work에 "내 코딩 도우미" Project 생성
- [ ] 시스템 지침(스킬) 작성 — 아래 항목 필수 포함
  - 역할 정의 (1줄)
  - 응답 방식 (코드 제공 방식, 언어 설정)
  - 기술 스택 (HTML/CSS/JS 명시)
- [ ] STAR 프롬프트로 계산기 완성 (최소 4칙연산, 다크/라이트 테마 중 선택)
- [ ] 체인 프롬프팅으로 단계별 구현 (최소 3단계)

**체인 프롬프팅 예시 (3단계):**
```
[1단계] "계산기 HTML 골격만 잡아줘. 버튼 숫자 레이아웃은 실제 계산기와 동일하게."
[2단계] "CSS 추가해줘. 다크 테마, 버튼 hover 효과 포함."
[3단계] "JS 로직 추가해줘. 4칙연산, AC 버튼(초기화), 0나누기 시 Error 표시."
```

**고급자 추가 도전:**
- [ ] 키보드 입력 지원 (`keydown` 이벤트)
- [ ] 계산 이력 표시 (마지막 5개)
- [ ] 교정 재프롬프팅 3패턴(Pinpoint·Redirect·Decompose) 중 1개를 실제 대화에서 사용하고 해당 대화 스크린샷 포함

**제출:** Co-work 시스템 지침 텍스트 + `calculator.html` + 브라우저 스크린샷

**채점 기준 (15점):**
| 항목 | 배점 | 기준 |
|------|------|------|
| Co-work 시스템 지침 작성 | 4점 | 역할·응답방식·기술스택 포함 |
| STAR 요소 확인 | 3점 | 제출 프롬프트에 S·T·A·R 모두 있는지 |
| 계산기 4칙연산 동작 | 4점 | 실제 계산 결과 정확 |
| AC 버튼 & Error 처리 | 2점 | 기능 동작 확인 |
| 체인 프롬프팅 3단계 | 2점 | 단계별 대화 스크린샷 |

---

### Lab 03: 포트폴리오 GitHub Pages 배포 (3강 과제)
**블룸 수준**: ③적용 | **소요 시간**: 60~90분 | **도구**: VS Code + Claude Code CLI + GitHub

**목표**: VS Code·Claude Code CLI로 포트폴리오 페이지를 만들고 GitHub Pages에 배포한다.

**요구사항:**
- [ ] Node.js + Claude Code CLI 설치 완료
- [ ] VS Code에서 `portfolio` 폴더 생성, `claude` 명령으로 에이전트 실행
- [ ] `index.html` 생성 (소개·기술스택·프로젝트·연락처 4섹션)
- [ ] GitHub 리포 `portfolio` 생성 → 커밋·푸시
- [ ] GitHub Pages 활성화 → 공개 URL 생성
- [ ] 더미 텍스트를 본인 내용으로 교체 (VS Code에서 직접 수정)

**Claude Code CLI 요청 프롬프트:**
```
portfolio 폴더에 내 포트폴리오 HTML을 만들어줘.
파일명: index.html
섹션: 소개(이름·역할), 기술 스택(3가지), 프로젝트(2개), 연락처
디자인: 현대적, 반응형, 배경 흰색, 섹션마다 다른 배경색
텍스트: 나중에 수정할 수 있도록 [이름], [역할] 같은 플레이스홀더 사용
```

**고급자 추가 도전:**
- [ ] CSS 애니메이션 — 스크롤 시 섹션 페이드인
- [ ] 다크모드 토글 버튼 추가
- [ ] GitHub Actions로 자동 배포 파이프라인 설정

**제출:** GitHub Pages URL (`https://[사용자명].github.io/portfolio`)

**채점 기준 (15점):**
| 항목 | 배점 | 기준 |
|------|------|------|
| GitHub Pages URL 작동 | 5점 | 브라우저에서 접속 가능 |
| 4개 섹션 포함 | 4점 | 소개·기술·프로젝트·연락처 |
| 본인 내용으로 교체 | 3점 | 플레이스홀더 → 실제 내용 |
| 반응형 (모바일) | 2점 | 창 크기 줄여도 레이아웃 유지 |
| Claude Code CLI 사용 증거 | 1점 | 터미널 스크린샷 |

---

### Lab 04: NotebookLM 팟캐스트 제작 (4강 과제)
**블룸 수준**: ③적용 | **소요 시간**: 30~45분 | **도구**: NotebookLM

**목표**: 관심 분야 문서를 NotebookLM에 업로드하고 AI 팟캐스트 1편을 만든다.

**요구사항:**
- [ ] NotebookLM 노트북 1개 생성 (이름: "[주제] 연구")
- [ ] 소스 2개 이상 추가 (PDF·URL·YouTube 중 선택)
- [ ] Study Guide 생성 확인
- [ ] Audio Overview (팟캐스트) 생성
- [ ] AI Q&A — 소스 내용 관련 질문 3개 이상

**소스 아이디어 (선택):**
- 관심 있는 산업 분야 뉴스 기사 URL 3개
- 공개 PDF 논문 (구글 학술검색에서 다운로드)
- 강의 소개 자료 PDF (강사 배포)
- 본인 회사/학교 보고서 PDF

**선택 활동 — Gemini vs Claude 비교:**
```
동일한 텍스트(300자 이상)를 양쪽에 붙여넣고:
"이 텍스트의 핵심 인사이트 3가지를 알려줘"
결과를 비교 워크시트에 기록
```

**제출:** NotebookLM 팟캐스트 생성 스크린샷 + 소스 목록(2개 이상) + 비교 워크시트(선택)

**채점 기준 (10점):**
| 항목 | 배점 | 기준 |
|------|------|------|
| 소스 2개 이상 업로드 | 3점 | 다양한 소스 유형 우대 |
| Audio Overview 생성 | 4점 | 팟캐스트 완성 스크린샷 |
| Q&A 3개 이상 | 2점 | 실제 질문·답변 스크린샷 |
| Study Guide 생성 | 1점 | 스크린샷 |

---

### Lab 05: 인터랙티브 날씨 앱 배포 (5강 과제)
**블룸 수준**: ③적용 | **소요 시간**: 60~90분 | **도구**: Claude Code CLI + VS Code

**목표**: OpenWeather API를 연동한 날씨 앱을 완성하고 GitHub Pages에 재배포한다.

**요구사항:**
- [ ] `portfolio` 프로젝트에 `weather.html` 추가 또는 `index.html`에 통합
- [ ] OpenWeather API 가입 + API 키 발급
- [ ] 기능: 도시명 입력 → 현재 날씨(온도·상태·습도) 표시
- [ ] 에러 처리: 잘못된 도시명 시 메시지 표시
- [ ] GitHub Pages에 재배포

**필수 기능 구현:**
```javascript
// 아래 코드 구조를 참고해 Claude Code CLI로 구현
async function getWeather(city) {
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=YOUR_KEY&units=metric&lang=kr`;
  const response = await fetch(url);
  if (!response.ok) throw new Error("도시를 찾을 수 없습니다");
  const data = await response.json();
  // 화면에 표시하는 로직 추가
}
```

**고급자 추가 도전:**
- [ ] 5일 예보 추가 (`/forecast` 엔드포인트)
- [ ] 날씨 아이콘 표시 (`https://openweathermap.org/img/wn/{icon}@2x.png`)
- [ ] 자동 위치 감지 (`navigator.geolocation`)
- [ ] Deprecated API 리뷰 프롬프트 사용 후 결과 보고서 첨부

**제출:** GitHub Pages URL (날씨 앱 포함) + OpenWeather API 키 발급 스크린샷

**채점 기준 (15점):**
| 항목 | 배점 | 기준 |
|------|------|------|
| 도시명 입력 → 날씨 표시 | 6점 | 온도·날씨상태·습도 3개 모두 |
| 에러 처리 | 3점 | 잘못된 도시명에서 메시지 표시 |
| async/await 사용 | 2점 | 코드에 async/await 있음 |
| GitHub Pages 재배포 | 3점 | URL 접속 가능 |
| Deprecated 리뷰 (고급) | +3점 보너스 | 리뷰 보고서 첨부 시 |

---

### Lab 06: AI 코드 리뷰 보고서 (6강 과제)
**블룸 수준**: ④분석 | **소요 시간**: 45~60분 | **도구**: Claude Chat + Claude Code CLI

**목표**: 5강 과제 코드를 AI 코드 리뷰하고 보안·성능·가독성 보고서를 작성한다.

**요구사항:**
- [ ] 5강 과제 날씨 앱 코드를 Claude Chat에 붙여넣어 3관점 리뷰 요청
- [ ] 리뷰 보고서 작성 (아래 양식)
- [ ] API 키 `.env` 분리 여부 확인 + `.gitignore` 점검
- [ ] 버그 수정 1건 이상 적용

**리뷰 프롬프트:**
```
아래 코드를 보안·성능·가독성 3관점에서 검토해줘.
각 관점에서 문제점 2가지와 개선 방법을 제시해줘.
[날씨 앱 코드 전체 붙여넣기]
```

**제출 보고서 양식:**
```markdown
## 5강 과제 코드 리뷰 보고서

### 보안 관점
- 문제 1: [내용] → 개선 방법: [내용]
- 문제 2: [내용] → 개선 방법: [내용]

### 성능 관점
- 문제 1: ...
- 문제 2: ...

### 가독성 관점
- 문제 1: ...
- 문제 2: ...

### 적용한 개선사항
- [실제 수정한 항목과 수정 전/후 코드 스니펫]

### API 키 보안 상태
- .env 분리 여부: O / X
- .gitignore 등록 여부: O / X
```

**고급자 추가 도전:**
- [ ] `formatPrice(price)` 함수에 대한 단위 테스트 3케이스 작성 (경계값·정상·오류)
- [ ] GitHub 커밋 이력에서 API 키 노출 여부 확인 방법 조사

**제출:** 리뷰 보고서 `.md` 파일

**채점 기준 (15점):**
| 항목 | 배점 | 기준 |
|------|------|------|
| 보안 관점 2건 | 3점 | 실제 코드의 문제 지적 |
| 성능 관점 2건 | 3점 | 구체적 개선 방법 포함 |
| 가독성 관점 2건 | 3점 | 실행 가능한 제안 |
| 개선사항 1건 이상 적용 | 4점 | 수정 전/후 코드 스니펫 |
| API 키 보안 상태 | 2점 | .env + .gitignore 확인 |

---

### Lab 07: AI 앱 MVP 제출 (7강 과제)
**블룸 수준**: ⑥창조 | **소요 시간**: 90~120분 | **도구**: Claude Code CLI + Flask + Supabase

**목표**: Supabase Auth·DB와 AI API를 결합한 MVP를 기획서와 함께 제출한다.

**패키지 설치 (VS Code 터미널에서 먼저 실행):**
```bash
pip install flask flask-cors anthropic python-dotenv supabase
python server.py
```

**요구사항:**
- [ ] 기획서 작성 (Claude Co-work 사용, Supabase 스키마 포함)
- [ ] Supabase 프로젝트 생성 + `SUPABASE_URL` · `SUPABASE_ANON_KEY` `.env`에 저장
- [ ] 스타터킷 A(챗봇+대화저장)·B(AI게시판)·C(AI요약기) 중 1개 선택 또는 본인 아이디어
- [ ] Flask 서버 실행 (`python server.py`)
- [ ] 핵심 기능 1개 이상 동작 확인
- [ ] API 키 + Supabase 키 `.env` 분리

**기획서 양식 (Co-work에서 작성):**
```markdown
## [앱 이름] 기획서

### 문제 정의
누가(타깃), 어떤 불편함을 겪는가?

### 핵심 기능 (우선순위 순)
1. [기능 1] ← 오늘 구현할 것
2. [기능 2]
3. [기능 3]

### 기술 스택
- 프론트: HTML/CSS/JS
- 백엔드: Flask (Python)
- DB + Auth: Supabase (PostgreSQL + Auth)
- AI: Claude API (claude-sonnet-4-6) 또는 Gemini API

### Supabase 테이블 스키마 (주요 컬럼)
- 테이블명: [예: posts]
- 컬럼: id(uuid) · user_id(uuid, FK→auth.users) · [필드들] · created_at

### 오늘의 MVP 범위
딱 한 가지: [기능 1]

### 화면 구성 (텍스트 와이어프레임)
[로그인/로그아웃 버튼]
─────────────
[인풋창] [버튼]
─────────────
[AI 응답 영역 / 게시물 목록]
```

**제출:**
- 기획서 `.md` 파일 (Supabase 스키마 포함)
- `index.html` + `server.py` (+ `.env.example` — 실제 키 제거 버전)
- Supabase 프로젝트 URL 스크린샷 + Flask 서버 실행 + 기능 동작 스크린샷

**채점 기준 (20점):**
| 항목 | 배점 | 기준 |
|------|------|------|
| 기획서 완성도 | 4점 | 문제 정의·기능·스택·Supabase 스키마·MVP 범위 포함 |
| 핵심 기능 동작 | 7점 | AI 응답이 화면에 표시됨 |
| Supabase 연동 | 4점 | Auth 또는 DB 저장 중 1개 이상 동작 |
| Flask 서버 구조 | 3점 | `/api/...` 엔드포인트, CORS 설정 |
| API·DB 키 보안 | 2점 | `.env` 사용, 코드에 하드코딩 없음 |

---

### Lab 08: Vercel 배포 + 수료 포트폴리오 (8강 과제)
**블룸 수준**: ⑥창조 | **소요 시간**: 60~90분 | **도구**: Vercel + GitHub

**목표**: 7강 MVP를 Vercel에 배포하고 수료 포트폴리오에 통합한다.

**요구사항:**
- [ ] 7강 MVP를 Vercel에 배포 (환경 변수 Vercel 대시보드 설정)
- [ ] 공개 Vercel URL 생성
- [ ] `portfolio/index.html`에 "내가 만든 AI 앱" 섹션 추가 (Vercel URL 링크)
- [ ] 배포 전 보안 체크리스트 완료
  - `.env` → `.gitignore` 확인
  - API 키 + Supabase 키 코드 하드코딩 없음 확인
  - `README.md` 작성 (앱 설명 1단락)

**Vercel 환경 변수 설정 (Settings → Environment Variables):**
```
ANTHROPIC_API_KEY   =   sk-ant-...
SUPABASE_URL        =   https://xxxx.supabase.co
SUPABASE_ANON_KEY   =   eyJhbGci...
```

**보안 체크리스트:**
```bash
# Claude Code CLI에서
.gitignore 파일 확인해줘. 
Python + Node.js + .env 관련 파일이 모두 포함됐는지 체크해줘.
Supabase service_role 키가 코드에 없는지도 확인해줘.
```

**제출:**
- Vercel 배포 URL
- GitHub Pages 포트폴리오 URL (AI 앱 섹션 포함)
- 보안 체크리스트 완료 스크린샷

**채점 기준 (20점):**
| 항목 | 배점 | 기준 |
|------|------|------|
| Vercel 배포 URL 작동 | 8점 | 실제 접속 가능 |
| 환경 변수 Vercel 설정 | 4점 | 대시보드 스크린샷 |
| 포트폴리오 AI 앱 섹션 | 4점 | Vercel URL 링크 있음 |
| 보안 체크리스트 | 3점 | 3항목 모두 완료 |
| README.md | 1점 | 앱 설명 1단락 이상 |

---

## 캡스톤 프로젝트: 나만의 AI 서비스

**제출 시기**: 8강 종료 후 1주 이내 (개인 선택)
**블룸 수준**: ⑥창조 | **소요 시간**: 4~8시간

### 캡스톤 개요

이 과정에서 배운 **모든 도구와 개념**을 통합하여, 실제 문제를 해결하는 AI 서비스를 완성한다.

### 최소 요구사항 (기본 통과)

- [ ] **문제 정의**: 실제 본인의 불편함이나 반복 업무
- [ ] **AI 연동**: Claude API 또는 Gemini API 1개 이상
- [ ] **프론트엔드**: HTML/CSS/JS (반응형)
- [ ] **백엔드**: Flask 또는 Supabase 직접 연동 중 1개
- [ ] **배포**: Vercel (공개 URL) — Flask 백엔드가 있으면 필수, 정적이면 GitHub Pages도 가능
- [ ] **보안**: `.env` + `.gitignore` 적용 (Supabase anon key만 사용, service_role 금지)
- [ ] **스킬 활용**: Claude Co-work 또는 AI Studio System Instruction
- [ ] **문서화**: README.md (문제·해결·사용법·Supabase 테이블 구조 간략 설명)

### 평가 루브릭 (총 50점)

**① 문제 해결력 (15점)**

| 수준 | 점수 | 기준 |
|------|------|------|
| 우수 | 13~15 | 실제 문제 명확, 타깃 사용자 구체적, AI 활용이 문제 해결에 핵심적 역할 |
| 보통 | 8~12 | 문제가 있으나 AI 활용 필요성 약함 |
| 미흡 | 0~7 | 문제 정의 불명확, AI 없어도 되는 기능 |

**② 기술 구현력 (15점)**

| 수준 | 점수 | 기준 |
|------|------|------|
| 우수 | 13~15 | 핵심 기능 완전 동작, 에러 처리, API 보안, 반응형 |
| 보통 | 8~12 | 핵심 기능 동작하나 엣지케이스 처리 미흡 |
| 미흡 | 0~7 | 핵심 기능 미동작 또는 보안 취약 |

**③ 도구 활용도 (10점)**

| 수준 | 점수 | 기준 |
|------|------|------|
| 우수 | 9~10 | Claude 3종 + Google AI 2종 이상 + Claude Code CLI 사용 |
| 보통 | 5~8 | Claude Chat + API 1종 사용 |
| 미흡 | 0~4 | 단일 도구만 사용 |

**④ 프롬프트 엔지니어링 (5점)**

| 수준 | 점수 | 기준 |
|------|------|------|
| 우수 | 5 | STAR 적용, 스킬/System Instruction 설정, 교정 패턴 1종 이상 활용 |
| 보통 | 3~4 | STAR 일부 적용 |
| 미흡 | 0~2 | 단순 질문형 프롬프트만 사용 |

**⑤ 발표 & 문서화 (5점)**

| 수준 | 점수 | 기준 |
|------|------|------|
| 우수 | 5 | README 완성, 3분 이내 발표에서 문제·해결·데모 명확 |
| 보통 | 3~4 | README 있으나 발표 내용 불명확 |
| 미흡 | 0~2 | 문서 없음 또는 발표 불가 |

### 캡스톤 아이디어 뱅크

**입문자 추천:**
- 일정 요약기: 주간 할 일 목록 입력 → Claude가 우선순위 정리
- 독서 도우미: 책 내용 붙여넣기 → AI 요약·핵심 질문 생성 (NotebookLM 연동)
- 회의록 정리기: 텍스트 입력 → 핵심 결정사항·액션아이템 자동 추출

**중급자 추천:**
- 맞춤 레시피 생성기: 냉장고 재료 입력 → 요리법 3가지 제안
- 이력서 피드백 도구: 이력서 텍스트 → 개선점 5가지 + 자소서 초안
- 영어 작문 교정기: 한국어/영어 입력 → 자연스러운 영어 변환 + 설명

**고급자 추천:**
- AI 코드 리뷰 서비스: GitHub Gist URL 입력 → 보안·성능·가독성 리포트
- 기사 팩트체크 도구: URL 입력 → NotebookLM 소스 + Gemini 크로스체크
- 개인 스케줄 최적화: 할 일 목록 + 에너지 패턴 입력 → AI 주간 계획 생성

### 캡스톤 발표 (3분 데모)

**발표 구조:**
1. **문제** (30초): 어떤 불편함을 해결했는가?
2. **데모** (2분): 실제 앱 실행하며 핵심 기능 시연
3. **뒤돌아보기** (30초): 가장 어려웠던 점과 해결 방법

---

## 힌트 시스템

### 모든 과제 공통 힌트

**힌트 Level 1 (막혔을 때 먼저 시도):**
```
Claude Chat에 붙여넣기:
"[현재 코드]에서 [증상]이 발생합니다.
원인 1가지와 수정 방법을 알려줘."
```

**힌트 Level 2 (Level 1 후에도 막힐 때):**
```
"지금 만들고 있는 것을 처음부터 다시 단계별로 설명해줘.
내가 어느 단계에서 막혔는지 찾을 수 있도록."
```

**힌트 Level 3 (최후 수단):**
강사에게 직접 질문 — 에러 메시지 전체 스크린샷과 함께

---

### 과제별 자주 묻는 질문 (FAQ)

**Lab 01~02 공통**
- Q: 코드를 저장했는데 브라우저에서 변경이 안 보여요
- A: Ctrl+Shift+R (강제 새로고침) 또는 시크릿 창에서 열기

**Lab 03**
- Q: `git push` 후 GitHub Pages가 안 열려요
- A: Settings → Pages에서 "Deploy from branch → main" 확인 후 2~3분 대기

**Lab 05**
- Q: OpenWeather API 키 넣었는데 401 오류가 나요
- A: 키 발급 직후 최대 10분까지 활성화 지연 발생. 대기 후 재시도

**Lab 07**
- Q: `python server.py` 실행 시 `ModuleNotFoundError: No module named 'flask'`
- A: `pip install flask flask-cors anthropic python-dotenv supabase` 실행

- Q: Supabase insert 시 `Row level security policy is violated`
- A: Authentication → Policies에서 INSERT 정책이 있는지 확인. SQL Editor에서 `create policy "Users can insert own posts" on posts for insert with check (auth.uid() = user_id);` 실행

- Q: Supabase 연결 시 `Invalid API key` 오류
- A: Settings → API에서 `anon public` 키인지 확인 (service_role 키가 아닌지). `.env` 파일이 저장됐는지 확인

**Lab 08**
- Q: Vercel 배포 후 API가 `undefined` 반환해요
- A: Vercel 대시보드 → Settings → Environment Variables에 `ANTHROPIC_API_KEY`, `SUPABASE_URL`, `SUPABASE_ANON_KEY` 3개 모두 등록됐는지 확인 후 Redeploy

- Q: Vercel 배포 후 Supabase Auth가 작동하지 않아요
- A: Supabase → Authentication → URL Configuration에서 "Site URL"을 Vercel URL(`https://your-app.vercel.app`)로 업데이트

---

*실습과제 & 캡스톤 작성 완료 — AI 활용 바이브코딩 8강 전체 v2*
