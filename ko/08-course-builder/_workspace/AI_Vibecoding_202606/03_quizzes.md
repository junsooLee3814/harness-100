# AI 활용 바이브코딩 — 퀴즈 & 평가 문항 v2

> **구성**: 강별 형성평가(3~5문항) + 모듈별 총괄평가(10문항) + 최종 총괄평가(20문항)
> **블룸 수준 범례**: ①기억 ②이해 ③적용 ④분석 ⑤평가 ⑥창조

---

## 형성평가 — 강별 퀴즈

### 1강 형성평가: 바이브코딩 & 첫 코드 체험

**Q1 [①기억]** 바이브코딩(Vibe Coding)이라는 용어를 처음 사용한 사람은 누구인가?
- ① Sam Altman
- ② **Andrej Karpathy** ✓
- ③ Elon Musk
- ④ Geoffrey Hinton

> **해설**: 테슬라 AI 책임자·OpenAI 공동창업자인 Andrej Karpathy가 2025년 초 "AI에게 원하는 것을 설명하고 결과를 검증하는" 개발 방식을 '바이브코딩'이라 명명했다.

---

**Q2 [②이해]** 다음 중 바이브코딩에서 개발자의 역할을 가장 잘 설명한 것은?

- ① 코드를 직접 타이핑하는 사람
- ② 알고리즘을 암기하는 사람
- ③ **무엇을 만들지 정의하고 AI 결과를 검증하는 사람** ✓
- ④ AI가 만든 코드를 그대로 사용하는 사람

> **해설**: 바이브코딩은 코드 작성 역할을 AI에게 위임하지만, '무엇을 만들지 정의'하고 '결과를 검증'하는 책임은 여전히 개발자에게 있다.

---

**Q3 [②이해]** 이 과정에서 사용하는 두 가지 AI 생태계는?

- ① Microsoft(Copilot) + Apple(Siri)
- ② **Anthropic(Claude) + Google(Gemini·AI Studio·NotebookLM)** ✓
- ③ OpenAI(GPT) + Meta(Llama)
- ④ Anthropic(Claude) + Amazon(Alexa)

---

**Q4 [③적용]** 에이전트팀·하네스 시연에서 강사가 한 입력은 무엇이었는가?

- ① 20페이지 기획서를 붙여넣었다
- ② 코드를 직접 작성했다
- ③ **주제 한 줄만 입력했다** ✓
- ④ 아무것도 입력하지 않았다

> **해설**: 하네스의 핵심 특징은 최소 입력으로 에이전트팀이 자율 협업하여 결과물을 만든다는 것이다.

---

**Q5 [④분석]** Claude와 Gemini의 결과물을 비교했을 때 차이가 나는 이유로 가장 적절한 것은?

- ① 한 AI가 다른 AI보다 나쁘기 때문이다
- ② **AI마다 학습 데이터·아키텍처·설계 목표가 달라 '스타일'이 다르기 때문이다** ✓
- ③ Gemini가 Claude보다 항상 빠르기 때문이다
- ④ 두 AI가 같은 회사 제품이기 때문이다

---

### 2강 형성평가: STAR 프롬프트 & 스킬

**Q1 [①기억]** STAR 프롬프트 프레임워크에서 'T'는 무엇을 의미하는가?

- ① Technology (기술 스택)
- ② **Task (작업/목표)** ✓
- ③ Testing (테스트)
- ④ Template (템플릿)

---

**Q2 [②이해]** 다음 두 프롬프트를 비교할 때 STAR 관점에서 더 좋은 프롬프트는?

**A**: "계산기 만들어줘"
**B**: "HTML, CSS, JS로 4칙연산 계산기를 만들어줘. 다크 테마, 4×4 그리드, 0나누기 시 Error 표시. 하나의 HTML 파일로."

- ① A가 더 좋다 (AI의 창의성을 살려줌)
- ② **B가 더 좋다 (Situation·Task·Action·Result 정보 포함)** ✓
- ③ 둘 다 같다
- ④ 두 프롬프트 모두 개선이 필요하다

---

**Q3 [②이해]** Claude Co-work(Projects)가 일반 Claude Chat과 다른 핵심 차이는?

- ① 응답 속도가 더 빠르다
- ② 코드를 직접 실행할 수 있다
- ③ **시스템 지침(스킬)과 파일이 대화간 유지된다** ✓
- ④ 더 많은 언어를 지원한다

---

**Q4 [③적용]** AI가 "버튼을 클릭해도 아무 반응이 없다"는 기대와 다른 결과를 냈다. 교정 재프롬프팅 'Pinpoint' 패턴을 적용한 올바른 예는?

- ① "다시 만들어줘"
- ② "다른 방법으로 해줘"
- ③ **"버튼 클릭 시 `console.log('클릭됨')`도 안 뜹니다. 이벤트 리스너가 없는 것 같아요. 수정해주세요."** ✓
- ④ "코드를 더 작게 분리해줘"

> **해설**: Pinpoint는 구체적 오류 지점을 지적한다. '다시 만들어줘'는 같은 결과를 낸다.

---

**Q5 [⑤평가]** 스킬(Skill)의 정의로 가장 적절한 것은?

- ① AI가 스스로 학습하는 능력
- ② API 호출 코드의 집합
- ③ **AI에게 전문 역할·작업 방식·출력 형식을 부여하는 재사용 지침** ✓
- ④ Claude Co-work의 유료 기능

---

### 3강 형성평가: VS Code + Claude Code CLI

**Q1 [①기억]** VS Code에서 내장 터미널을 여는 단축키(Windows)는?

- ① Ctrl + T
- ② Ctrl + Shift + T
- ③ **Ctrl + `** ✓
- ④ Ctrl + Alt + T

---

**Q2 [①기억]** Claude Code CLI를 npm으로 설치하는 올바른 명령어는?

- ① `npm install claude-code`
- ② `npm install claude`
- ③ **`npm install -g @anthropic-ai/claude-code`** ✓
- ④ `npm install -g claude-cli`

---

**Q3 [②이해]** Claude Chat과 Claude Code CLI(에이전트)의 가장 큰 차이는?

- ① CLI는 한국어를 지원하지 않는다
- ② CLI는 유료다
- ③ **CLI는 파일을 직접 생성·수정할 수 있는 자율 실행 에이전트다** ✓
- ④ Chat은 코드를 생성하지 못한다

---

**Q4 [②이해]** MCP(Model Context Protocol)를 USB에 비유한 이유는?

- ① 물리적 포트이기 때문
- ② 전원 공급 기능이 있기 때문
- ③ **표준 규격으로 다양한 도구를 AI에 연결할 수 있기 때문** ✓
- ④ 데이터 전송 속도가 빠르기 때문

---

**Q5 [③적용]** Claude Code CLI로 `portfolio` 폴더에 HTML 파일을 만든 후 브라우저에서 바로 보려면 VS Code 확장 중 무엇을 사용하는가?

- ① Prettier
- ② ESLint
- ③ Korean Language Pack
- ④ **Live Server** ✓

---

**Q6 [③적용]** GitHub Pages로 사이트를 배포한 후 URL `https://[사용자명].github.io/portfolio`에 접속이 안 된다. 확인해야 할 곳은?

- ① GitHub → Issues 탭
- ② **GitHub → Settings → Pages → Deploy from branch (main) 설정 확인 후 2~3분 대기** ✓
- ③ VS Code의 Live Server 재시작
- ④ Node.js 재설치

> **해설**: GitHub Pages는 활성화 설정 후 배포에 2~3분 소요된다. Settings → Pages에서 Branch를 main으로 지정했는지 확인하는 것이 첫 번째 단계.

---

### 4강 형성평가: Google AI 생태계

**Q1 [①기억]** Google AI Studio에서 Gemini API 키를 발급받는 위치는?

- ① Google Play Console
- ② Google Cloud Console만 가능
- ③ **AI Studio 왼쪽 사이드바 "Get API key"** ✓
- ④ Gmail 설정에서 발급

---

**Q2 [②이해]** Google AI Studio의 Temperature 파라미터를 0에 가깝게 설정하면 어떻게 되는가?

- ① 응답이 빠라진다
- ② 응답이 더 길어진다
- ③ **응답이 일관적이고 예측 가능해진다 (코드 생성에 적합)** ✓
- ④ 한국어 응답이 우선된다

---

**Q3 [②이해]** NotebookLM의 "Audio Overview(오디오 개요)" 기능이 생성하는 것은?

- ① 배경 음악이 있는 슬라이드
- ② **AI 두 명이 대화하는 팟캐스트 형식의 오디오** ✓
- ③ 텍스트 음성 변환(TTS) 낭독
- ④ 유튜브 자막 파일

---

**Q4 [④분석]** 다음 중 Gemini가 Claude보다 유리한 상황은?

- ① 복잡한 Python 에이전트 코딩
- ② 200,000 토큰 이상의 긴 문서 분석
- ③ **Gmail·Google Drive 등 Google 서비스와 직접 연동** ✓
- ④ 안전성이 중요한 의료 문서 작성

---

**Q5 [③적용]** Google AI Studio의 System Instruction과 Claude Co-work의 시스템 지침(스킬)의 관계는?

- ① 전혀 다른 개념이다
- ② System Instruction이 더 고급 기능이다
- ③ 스킬이 System Instruction보다 항상 낫다
- ④ **이름은 다르지만 'AI에게 역할과 행동 방식을 부여한다'는 동일한 개념이다** ✓

---

### 5강 형성평가: 웹페이지 제작 심화

**Q1 [①기억]** REST API에서 서버가 응답할 때 주로 사용하는 데이터 형식은?

- ① XML
- ② **JSON** ✓
- ③ CSV
- ④ HTML

---

**Q2 [②이해]** 아래 코드의 문제점은?
```javascript
const data = fetch("https://api.weather.com/today");
console.log(data.temperature);  // undefined
```

- ① URL이 틀렸다
- ② fetch() 함수가 없다
- ③ **`await`를 빠뜨려 Promise가 완료되기 전에 다음 줄을 실행했다** ✓
- ④ console.log를 쓰면 안 된다

---

**Q3 [③적용]** OpenWeather API를 사용하는 코드에서 갑자기 401 Unauthorized 오류가 발생했다. 원인으로 가능성이 가장 낮은 것은?

- ① API 키가 만료됐다
- ② API 키를 잘못 입력했다
- ③ **HTML 파일의 배경색 CSS가 잘못됐다** ✓
- ④ API 키 발급 직후 10분 미만 대기 시간

---

**Q4 [④분석]** AI가 생성한 코드에서 Deprecated API 사용 여부를 확인하는 가장 좋은 방법은?

- ① 무조건 코드를 실행해보고 오류가 나면 고친다
- ② AI가 최신 정보를 알고 있으므로 확인 불필요
- ③ **AI에게 "이 코드에서 2024년 이후 deprecated 또는 유료 전환된 API·라이브러리가 있으면 알려줘"라고 별도 리뷰를 요청한다** ✓
- ④ Stack Overflow에서 수동으로 검색한다

---

**Q5 [⑤평가]** 다크모드 사용자 선택을 새로고침 후에도 유지하려면 어떤 Web API를 사용해야 하는가?

- ① sessionStorage (탭 닫으면 삭제)
- ② **localStorage (브라우저에 영구 저장)** ✓
- ③ Cookie (서버 전송용)
- ④ IndexedDB (대용량 DB용)

---

### 6강 형성평가: AI 코드 리뷰 & 디버깅

**Q1 [①기억]** JavaScript에서 `SyntaxError`가 발생하는 원인은?

- ① 변수가 선언되지 않았을 때
- ② **괄호, 따옴표, 세미콜론 등 문법 규칙을 어겼을 때** ✓
- ③ 서버 연결이 실패했을 때
- ④ 배열 인덱스가 범위를 벗어났을 때

---

**Q2 [②이해]** 아래 코드의 XSS 취약점 원인은?
```javascript
document.getElementById('result').innerHTML = "안녕, " + name;
```

- ① `name` 변수가 너무 길다
- ② innerHTML보다 innerText가 빠르다
- ③ **innerHTML은 HTML을 렌더링하므로 악의적 스크립트 삽입이 가능하다** ✓
- ④ getElementById가 느리다

> **해설**: 사용자 입력에 `<script>alert('XSS')</script>` 같은 코드가 있으면 실행된다. 해결: `textContent` 사용.

---

**Q3 [③적용]** API 키를 안전하게 관리하기 위해 `.env` 파일과 함께 반드시 해야 하는 것은?

- ① API 키를 주석으로 감춘다
- ② `.env` 파일을 암호화한다
- ③ **`.gitignore`에 `.env`를 추가해 Git 추적에서 제외한다** ✓
- ④ API 키를 Base64로 인코딩한다

---

**Q4 [④분석]** Claude Code CLI로 멀티파일 디버깅이 유리한 이유는?

- ① 인터넷 없이 동작하기 때문
- ② **전체 코드베이스를 인식하여 파일 간 의존성까지 추적할 수 있기 때문** ✓
- ③ Claude Chat보다 응답이 빠르기 때문
- ④ JavaScript만 지원하기 때문

---

**Q5 [⑤평가]** 다음 중 코드 리뷰 AI 프롬프트로 가장 효과적인 것은?

- ① "이 코드 고쳐줘"
- ② "버그 있어?"
- ③ **"이 코드를 보안·성능·가독성 3관점에서 검토하고, 각 관점에서 문제점 2가지와 개선 방법을 알려줘"** ✓
- ④ "코드 리뷰해줘"

---

### 7강 형성평가: AI 앱 제작 · Supabase 풀스택

**Q1 [①기억]** Supabase에서 Auth(인증), Database, Storage를 한 번에 제공하는 데이터베이스 엔진은?

- ① MySQL
- ② **PostgreSQL** ✓
- ③ SQLite
- ④ MongoDB

> **해설**: Supabase는 PostgreSQL 기반 오픈소스 BaaS(Backend as a Service)다. Auth는 회원가입·로그인, Storage는 파일 업로드, RLS(Row Level Security)는 데이터 접근 제어를 담당한다.

---

**Q2 [②이해]** Supabase의 RLS(Row Level Security)를 활성화하는 목적은?

- ① 데이터베이스 쿼리 속도를 높이기 위해
- ② 테이블 컬럼 수를 늘리기 위해
- ③ **본인 데이터만 접근하도록 정책을 설정해 다른 사용자의 데이터 무단 접근을 막기 위해** ✓
- ④ Supabase 무료 플랜 해제를 위해

> **해설**: RLS가 없으면 anon key를 아는 사람 누구나 모든 행에 접근할 수 있다. `auth.uid() = user_id` 정책을 설정하면 본인 데이터만 CRUD 가능하다.

---

**Q3 [③적용]** Flask 서버에서 아래 코드의 목적은?
```python
from flask_cors import CORS
CORS(app)
```

- ① 서버 속도를 높인다
- ② SSL 인증서를 추가한다
- ③ **브라우저의 교차 출처 요청 차단을 허용하여 프론트엔드에서 API 호출이 가능하게 한다** ✓
- ④ 데이터베이스를 연결한다

---

**Q4 [④분석]** Supabase 클라이언트를 초기화할 때 `anon (public)` 키를 사용하고 `service_role` 키를 피해야 하는 이유는?

- ① anon 키가 더 길기 때문이다
- ② service_role 키는 무료 플랜에서 없기 때문이다
- ③ **service_role 키는 RLS를 우회하는 관리자 키여서, 프론트엔드에 노출되면 모든 데이터가 탈취될 수 있기 때문이다** ✓
- ④ anon 키가 더 빠르기 때문이다

---

**Q5 [⑤평가]** Feature Creep 경고가 MVP 개발에서 중요한 이유는?

- ① 기능이 많으면 코드가 너무 길어진다
- ② AI가 복잡한 기능을 못 만들기 때문이다
- ③ **기능을 많이 추가하다가 핵심 기능 하나도 완성하지 못하는 위험이 있기 때문이다** ✓
- ④ 서버 비용이 늘어나기 때문이다

---

### 8강 형성평가: 배포 & 하네스 실행

**Q1 [①기억]** 프로덕션(Production) 환경의 특성으로 틀린 것은?

- ① 전 세계 사용자가 접근한다
- ② 안정성이 최우선이다
- ③ **실험적 기능을 자유롭게 테스트한다** ✓
- ④ 실제 서비스가 운영된다

> **해설**: 실험적 테스트는 개발(localhost) 또는 스테이징 환경에서 한다.

---

**Q2 [②이해]** CI/CD에서 CD(Continuous Deployment)의 의미는?

- ① 코드가 자동으로 작성된다
- ② **테스트 통과 시 코드가 자동으로 프로덕션에 배포된다** ✓
- ③ 디자인이 자동 생성된다
- ④ 데이터베이스가 자동 백업된다

---

**Q3 [③적용]** Vercel에 배포할 때 API 키를 안전하게 전달하는 방법은?

- ① HTML 파일에 하드코딩
- ② README에 기재
- ③ GitHub 리포에 `.env` 커밋
- ④ **Vercel 대시보드 → Settings → Environment Variables에 별도 등록** ✓

---

**Q4 [④분석]** 하네스(Harness)를 구성하는 3가지 핵심 요소는?

- ① 웹서버 + 데이터베이스 + 프론트엔드
- ② HTML + CSS + JavaScript
- ③ **에이전트팀 + 스킬 + MCP** ✓
- ④ Claude + Gemini + 안티그래비티

---

**Q5 [⑥창조]** 이 과정을 마친 후 나만의 AI 자동화 워크플로우를 만든다고 할 때, 사용할 도구 조합으로 가장 합리적인 선택은?

*(정답 없는 열린 문항 — 서술 평가)*

> **채점 기준**: 도구(Claude Chat/Co-work/Code CLI/Gemini/NotebookLM/하네스/MCP)를 상황에 맞게 조합하고, 그 이유를 설명할 수 있으면 만점.

---

## 총괄평가 1 — 1·2강 (모듈 1: 바이브코딩 & 프롬프팅)

**[각 1점, 총 10점]**

**Q1** 바이브코딩에서 AI가 담당하는 역할은?
- ① 문제 정의 ② 코드 검증 ③ **코드 작성** ✓ ④ 배포

**Q2** Claude Chat에서 다음 대화를 시작하면 이전 대화 내용이 어떻게 되는가?
- ① 유지된다 ② **초기화된다** ✓ ③ 파일로 저장된다 ④ Projects로 이동된다

**Q3** STAR 프롬프트에서 R(Result)에 해당하는 내용은?
- ① 현재 보유한 파일 목록 ② 사용할 기술 스택 ③ 작업의 목적 ④ **출력 형식과 부연 설명 요구사항** ✓

**Q4** "이 CSS를 Flexbox에서 Grid로 바꿔줘. Grid가 내 브라우저에서 깨져서." 이것은 어떤 교정 패턴인가?
- ① Pinpoint ② **Redirect** ✓ ③ Decompose ④ STAR

**Q5** 스킬(Skill) 파일에 들어가는 내용이 아닌 것은?
- ① 역할 정의 ② 응답 방식 ③ 출력 형식 ④ **API 키** ✓

**Q6** Claude Co-work의 시스템 지침에 작성한 내용은 언제 적용되는가?
- ① 첫 번째 대화에서만 ② **해당 Project의 모든 대화에서** ✓ ③ 명시적으로 참조할 때만 ④ 유료 플랜에서만

**Q7** 체인 프롬프팅(Chain Prompting)의 핵심은?
- ① 프롬프트를 길게 쓰는 것 ② **대화를 끊지 않고 단계적으로 구현하는 것** ✓ ③ 여러 AI를 동시에 사용하는 것 ④ 같은 프롬프트를 반복하는 것

**Q8** 에이전트팀의 각 에이전트가 자기 역할을 아는 이유는?
- ① 훈련 때 배웠기 때문 ② 서로 채팅하기 때문 ③ **각 에이전트에게 스킬(업무 매뉴얼)이 있기 때문** ✓ ④ 하나의 AI가 역할을 나누기 때문

**Q9** 같은 프롬프트를 Claude와 Gemini에 입력했을 때 결과가 다른 이유로 옳은 것은?
- ① 한 AI가 고장났다 ② 인터넷 속도 차이 ③ **AI마다 학습 데이터와 아키텍처가 달라 응답 스타일이 다르다** ✓ ④ 가격 차이

**Q10** 이 과정에서 Google 계정 하나로 접근하는 도구로 묶인 것은?
- ① Claude Chat + Co-work + Code CLI ② VS Code + GitHub + Vercel ③ **Gemini + AI Studio + NotebookLM** ✓ ④ Flask + Python + Node.js

---

## 총괄평가 2 — 3·4강 (모듈 2: 개발환경 & Google AI)

**[각 1점, 총 10점]**

**Q1** VS Code에서 파일을 빠르게 열 때 사용하는 단축키(Windows)는?
- ① Ctrl+S ② Ctrl+F ③ **Ctrl+P** ✓ ④ Ctrl+H

**Q2** Node.js를 설치하는 이유는?
- ① 웹 브라우저로 사용하기 위해 ② **Claude Code CLI(npm 패키지) 실행에 필요하기 때문** ✓ ③ Python 실행 환경 ④ VS Code 자체가 Node.js다

**Q3** Claude Code CLI 첫 실행(`claude`) 시 Google OAuth 인증이 필요한 이유는?
- ① Google 계정으로 결제하기 위해 ② **Claude Code가 사용자의 Anthropic 계정과 연동하기 위해** ✓ ③ GitHub 리포에 접근하기 위해 ④ Gemini API를 사용하기 위해

**Q4** Live Server VS Code 확장이 하는 역할은?
- ① 코드 자동 완성 ② Python 실행 ③ **HTML 파일을 저장할 때마다 브라우저를 자동으로 새로고침** ✓ ④ Git 자동 커밋

**Q5** MCP 서버를 Claude에 연결하는 표준 규격의 이름은?
- ① REST API ② GraphQL ③ WebSocket ④ **Model Context Protocol** ✓

**Q6** Google AI Studio에서 Temperature를 1.5로 높이면?
- ① 응답이 더 짧아진다 ② 응답이 더 정확해진다 ③ **응답이 더 다양하고 창의적(때로는 예측 불가)해진다** ✓ ④ 응답 언어가 영어로 고정된다

**Q7** NotebookLM에 소스로 추가할 수 없는 것은?
- ① PDF 파일 ② YouTube URL ③ Google Drive 문서 ④ **실시간 인터넷 검색 결과** ✓

> **해설**: NotebookLM은 업로드한 소스 내에서만 답변한다. 실시간 웹 검색은 지원하지 않는다.

**Q8** Gemini API 키를 받은 후 다시 확인할 수 없는 이유로 올바른 것은?
- ① 서버 오류 ② 유료 기능이기 때문 ③ **보안상 최초 생성 시에만 전체 키를 표시하기 때문** ✓ ④ 30분 후 만료되기 때문

**Q9** Claude Code CLI로 파일을 직접 만들 수 있는 이유는?
- ① Claude Chat의 숨겨진 기능 ② 별도 Python 스크립트 ③ **에이전트로서 파일 시스템에 접근하고 도구를 직접 사용할 수 있기 때문** ✓ ④ GitHub와 연결되어 있어서

**Q10** Google AI Studio의 System Instruction과 Claude Co-work 시스템 지침의 공통점은?
- ① 동일한 회사에서 만들었다 ② 마크다운을 지원하지 않는다 ③ **AI에게 역할·응답 방식·제약을 부여하는 재사용 지침이라는 개념이 같다** ✓ ④ 최대 100자 제한이 같다

---

## 총괄평가 3 — 5·6강 (모듈 3: 실전 웹 개발 & 디버깅)

**[각 1점, 총 10점]**

**Q1** HTML의 역할을 건물에 비유하면?
- ① 인테리어 ② 전기·기계 ③ **뼈대(골조)** ✓ ④ 지붕

**Q2** `async/await`를 사용하는 이유는?
- ① 코드를 짧게 쓰기 위해 ② **비동기 작업(API 요청 등)이 완료될 때까지 다음 코드 실행을 기다리게 하기 위해** ✓ ③ 에러를 자동으로 처리하기 위해 ④ 브라우저 호환성 때문

**Q3** 다음 중 `.gitignore`에 반드시 추가해야 하는 파일은?
- ① index.html ② README.md ③ **`.env`** ✓ ④ package.json

**Q4** API 키가 GitHub에 노출됐을 때 즉시 해야 하는 조치는?
- ① GitHub 계정 탈퇴 ② API 사용 내역 확인 후 관망 ③ **API 제공 서비스에서 즉시 키를 폐기하고 새 키 발급** ✓ ④ private 리포로 변환

**Q5** XSS 공격을 방지하기 위해 innerHTML 대신 사용해야 하는 DOM 속성은?
- ① innerValue ② **textContent** ✓ ③ nodeText ④ safeHTML

**Q6** `TypeError: Cannot read properties of undefined (reading 'map')`의 의미는?
- ① map() 함수가 없다 ② **`undefined`인 변수에 `.map()` 메서드를 호출했다** ✓ ③ 배열이 비어 있다 ④ map 라이브러리가 설치되지 않았다

**Q7** AI 생성 코드를 그대로 사용해서 Deprecated API 오류가 날 수 있는 이유는?
- ① AI가 인터넷에 연결되지 않아서 ② **AI의 학습 데이터 이후에 변경된 API를 알지 못하기 때문** ✓ ③ AI가 고의로 오래된 코드를 사용하기 때문 ④ Deprecated API가 더 빠르기 때문

**Q8** VS Code의 멀티 커서 기능을 사용하는 단축키(Windows)는?
- ① Ctrl+Click ② Shift+Click ③ **Alt+Click** ✓ ④ Ctrl+Shift+Click

**Q9** 코드 리뷰 AI 프롬프트에서 관점을 명시해야 하는 이유는?
- ① AI가 다국어를 이해하기 위해 ② **AI가 어떤 각도에서 검토할지 알아야 적절한 답변을 할 수 있기 때문** ✓ ③ 응답 길이를 줄이기 위해 ④ 비용 절감을 위해

**Q10** localStorage와 sessionStorage의 차이는?
- ① localStorage가 더 빠르다 ② **localStorage는 탭 닫아도 유지, sessionStorage는 탭 닫으면 삭제된다** ✓ ③ sessionStorage 용량이 더 크다 ④ 차이 없다

---

## 총괄평가 4 — 7·8강 (모듈 4: AI 앱 & 배포)

**[각 1점, 총 10점]**

**Q1** Flask 앱에서 `@app.route('/chat', methods=['POST'])`의 의미는?
- ① `/chat` 페이지를 만든다 ② **`/chat` URL로 POST 요청이 오면 이 함수를 실행한다** ✓ ③ 채팅 기록을 저장한다 ④ Claude API를 자동 호출한다

**Q2** Claude API 요청에서 `max_tokens=1024`는?
- ① 입력 최대 글자 수 ② **AI 응답의 최대 토큰(단어 단위) 수** ✓ ③ API 초당 최대 요청 수 ④ 컨텍스트 창 크기

**Q3** MVP 개발에서 'Feature Creep'을 피해야 하는 이유는?
- ① 기능이 많으면 비용이 크다 ② **핵심 기능 하나도 완성 못 할 위험이 있다** ✓ ③ AI가 복잡한 코드를 못 만든다 ④ Vercel 무료 티어 제한 때문

**Q4** Vercel이 GitHub push를 감지해 자동 배포하는 것을 무엇이라 하는가?
- ① MCP ② 하네스 ③ **CI/CD** ✓ ④ API Gateway

**Q5** Supabase 프로젝트 생성 후 JS 클라이언트 초기화에 필요한 두 값은?
- ① API Key + Secret Key ② Username + Password ③ **Project URL + anon public Key** ✓ ④ Database URL + Port

**Q6** 하네스(Harness)를 구성하는 핵심 3요소는?
- ① HTML + CSS + JS ② Claude + Gemini + NotebookLM ③ **에이전트팀 + 스킬 + MCP** ✓ ④ GitHub + Vercel + Flask

**Q7** Python Flask에서 환경 변수를 읽는 올바른 방법은?
```python
# .env: ANTHROPIC_API_KEY=sk-xxxx
```
- ① `os.getenv("ANTHROPIC_API_KEY")` → `from dotenv import load_dotenv; load_dotenv()` 후 ✓
- ② `process.env.ANTHROPIC_API_KEY`
- ③ `import .env; env.ANTHROPIC_API_KEY`
- ④ `.env` 파일을 직접 open()으로 읽기

> **정답: ①** — `python-dotenv` 라이브러리로 `.env`를 로드한 후 `os.getenv()`로 읽는다.

**Q8** 수료 후 "LangGraph·MCP 서버 직접 제작·멀티 에이전트"를 공부하면 어떤 방향인가?
- ① 풀스택 개발자 ② 데이터 분석가 ③ **AI 에이전트 빌더** ✓ ④ UI/UX 디자이너

**Q9** GitHub Pages와 Vercel의 차이로 맞는 것은?
- ① GitHub Pages가 더 빠르다 ② Vercel은 무료 사용 불가 ③ **GitHub Pages는 정적 파일만, Vercel은 서버사이드(Flask/Node.js 등) 포함 배포 가능** ✓ ④ 차이 없다

**Q10** 이 과정에서 배운 5대 핵심 개념 중 "Claude와 외부 도구(GitHub·Notion 등)를 연결하는 표준 규약"은?
- ① 스킬(Skill) ② 에이전트(Agent) ③ 하네스(Harness) ④ **MCP(Model Context Protocol)** ✓

---

## 최종 총괄평가 — 8강 전체 (20문항, 20점)

**이 평가는 과정 전체 이수 후 시행한다.**

**Q1** 바이브코딩에서 AI의 역할로 가장 정확한 것은?
- ① 문제를 스스로 정의하고 해결한다 ② **코드를 생성하며 사람이 검증한다** ✓ ③ 배포까지 자동으로 처리한다 ④ 사용자를 대신해 API를 관리한다

**Q2** STAR 프롬프트에서 'A(Action)'에 포함되는 내용은?
- ① 현재 프로젝트 배경 ② 원하는 결과물 형식 ③ **기술 스택, 구현 방식, 라이브러리 선택** ✓ ④ 타깃 사용자

**Q3** Claude Chat과 Claude Co-work(Projects)를 구분하는 기준은?
- ① 응답 길이 ② 언어 지원 ③ **맥락(스킬·파일)의 대화 간 유지 여부** ✓ ④ API 비용

**Q4** `npm install -g @anthropic-ai/claude-code` 설치 전에 반드시 필요한 것은?
- ① Python 3.x ② Docker ③ **Node.js (npm 포함)** ✓ ④ Git

**Q5** Claude Code CLI에서 `/help` 명령의 용도는?
- ① API 키 확인 ② **사용 가능한 명령 목록 보기** ✓ ③ 파일 목록 보기 ④ 에이전트 상태 확인

**Q6** Google AI Studio에서 Temperature를 0으로 설정하면 적합한 용도는?
- ① 시 창작 ② 브레인스토밍 ③ **코드 생성 (일관된 결과 필요)** ✓ ④ 이야기 생성

**Q7** NotebookLM의 핵심 제약 사항은?
- ① 하루 10개 이상 소스 불가 ② PDF만 지원 ③ 영어만 지원 ④ **업로드한 소스 내에서만 답변 (실시간 검색 불가)** ✓

**Q8** REST API 호출에서 `await`가 필요한 이유는?
- ① 코드를 줄이기 위해 ② API 비용 절감 ③ **네트워크 응답을 기다리지 않으면 undefined를 사용해 오류가 발생하기 때문** ✓ ④ JSON 파싱 자동화

**Q9** Deprecated API 사용의 위험성은?
- ① AI가 동작하지 않는다 ② 코드가 더 느려진다 ③ **AI 학습 데이터 이후 API가 변경·폐지돼 갑자기 오류가 발생할 수 있다** ✓ ④ 법적 문제가 생긴다

**Q10** `innerHTML`의 XSS 취약점을 막는 방법은?
- ① innerHTML을 사용하지 않기 ② 모든 입력을 숫자로 변환 ③ **사용자 입력을 표시할 때 `textContent` 사용** ✓ ④ 서버를 Python으로 교체

**Q11** Supabase의 RLS 정책에서 `auth.uid() = user_id` 조건의 의미는?
- ① 관리자만 접근 가능 ② 익명 사용자도 접근 가능 ③ **현재 로그인한 사용자의 ID와 행의 user_id가 일치할 때만 접근 허용** ✓ ④ 모든 사용자 접근 차단

**Q12** Flask 서버에서 CORS를 설정하는 이유는?
- ① 서버 보안 강화 ② **브라우저가 다른 출처(포트) API 요청을 차단하는 것을 허용** ✓ ③ HTTPS 설정 ④ 속도 향상

**Q13** GitHub Pages와 Vercel 중 Flask 백엔드 배포가 가능한 것은?
- ① GitHub Pages만 ② 둘 다 가능 ③ 둘 다 불가 ④ **Vercel만** ✓

**Q14** Vercel 환경 변수에 API 키를 등록하는 이유는?
- ① 코드에 하드코딩하면 느리기 때문 ② 무료 플랜 요구사항 ③ **코드에 키를 포함하지 않고 서버에서 안전하게 관리하기 위해** ✓ ④ GitHub Actions 요구사항

**Q15** 하네스의 정의로 가장 정확한 것은?
- ① AI와 대화하는 인터페이스 ② Claude Code CLI의 다른 이름 ③ **에이전트팀·스킬·MCP를 묶어 반복 실행하는 자동화 파이프라인** ✓ ④ GitHub Actions 워크플로우

**Q16** 이 과정에서 배운 5대 핵심 개념의 올바른 정의 연결은?
- ① 스킬=에이전트, MCP=하네스 ② **스킬=AI 업무 매뉴얼, 에이전트=자율 실행 AI, MCP=연결 규약, 에이전트팀=협업 구조, 하네스=파이프라인** ✓ ③ 스킬=API 키, 에이전트=사람 ④ MCP=마이크로서비스

**Q17** "코딩 도우미 스킬"의 역할은?
- ① Claude Chat을 빠르게 하는 코드 ② GitHub 커밋 자동화 ③ **Claude Co-work에서 코딩 관련 역할·응답 방식을 정의하는 지침** ✓ ④ Gemini API 호출 코드

**Q18** 다음 중 MCP 서버로 연결 가능한 외부 도구의 예가 아닌 것은?
- ① GitHub ② Notion ③ **날씨 API (OpenWeather)** ✓ ④ Google Drive

> **해설**: OpenWeather는 공개 REST API로, 브라우저에서 `fetch()`로 직접 호출하면 되므로 MCP가 필요 없다. MCP 서버는 인증 상태·컨텍스트가 필요한 도구(Notion 페이지 목록, GitHub 리포 파일, Slack 채널 메시지 등)를 Claude 에이전트가 직접 제어할 때 쓴다. 쉬운 구분 기준: "내 계정 로그인이 필요하고 Claude가 직접 쓰는 도구면 MCP, 공개 API 키로 fetch()하면 REST 직접 호출".

**Q19** AI 도구 선택 기준으로 "복잡한 코딩 + 긴 문서 처리"에 가장 적합한 것은?
- ① Gemini ② NotebookLM ③ 안티그래비티 ④ **Claude (Chat · Co-work · Code CLI)** ✓

**Q20** 이 과정 수료 후 "데이터 분석 자동화"를 더 깊이 배우고 싶다면 추천 방향은?
- ① Next.js + Vercel ② LangGraph + MCP ③ **Python pandas·NumPy + SQL + NotebookLM + Google AI Studio** ✓ ④ Docker + Kubernetes

---

## 단답형 / 서술형 보충 평가

*(강사 선택 사용, 실습 시험 또는 포트폴리오 대체 가능)*

**서술 1** — STAR 프롬프트를 활용해 "Supabase Auth로 로그인하고 게시물을 저장하는 메모장 앱" 개발 요청 프롬프트를 직접 작성하시오.
> **채점 포인트**: S(현재 상황·스택: HTML/JS/Flask/Supabase), T(메모장 핵심 기능: 로그인·게시물 CRUD), A(Supabase supabase-js 클라이언트 사용, RLS 적용), R(출력 형식: 파일 분리) 4요소가 모두 포함됐는지.

**서술 2** — 다음 오류 메시지를 보고, Claude에게 디버깅을 요청하는 프롬프트를 작성하시오.
```
TypeError: data.map is not a function at processData (app.js:45)
```
> **채점 포인트**: 오류 메시지 전달, 코드 컨텍스트(45번 줄 인근), 증상 설명 포함 여부.

**서술 3** — 이 과정에서 배운 도구 중 3가지를 선택해, 본인의 실제 업무·학습에 적용할 수 있는 시나리오를 1개 작성하시오.
> **채점 포인트**: 도구 이름 정확히 사용, 구체적 상황 기술, 도구가 문제 해결에 적합한지 논리 성립.

---

*퀴즈 & 평가 작성 완료 — AI 활용 바이브코딩 8강 전체 v2*
