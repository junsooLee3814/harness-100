# 강의 입력 정보

## 과정 주제
AI 활용 바이브코딩 (Vibe Coding with AI)

## 과정 설명
Claude·Gemini 등 AI 도구와 VS Code 개발 환경을 활용하여 코드를 작성하는 "바이브코딩" 방법론을 기초부터 고급까지 단계적으로 학습한다. 프롬프트 엔지니어링, AI 페어 프로그래밍, Google AI 생태계 활용(Gemini · AI Studio · NotebookLM · 안티그래비티), VS Code 개발 환경 기초, 그리고 스킬·에이전트·MCP·하네스 등 AI 자동화 워크플로우까지 포괄한다.

## 대상 학습자
- **입문**: 코딩 경험 없는 일반인 / 비개발자 직장인
- **중급**: 코딩 기초 있는 학습자, AI 도구 처음 접하는 개발자
- **고급**: AI 도구를 실무에 적극 활용하고 싶은 개발자/기획자

## 과정 규모
- 총 8강 × 3시간 = 24시간
- 주 2회 × 4주 (예: 화·목 또는 월·수)
- 1강 구성: 이론 1시간 + 실습 2시간

## 강의 구성 요청
- **커리큘럼**: 8강 전체 구조, 강별 학습목표, 진도표
- **강의노트**: 각 강별 상세 강의노트 (강사용 스크립트 포함)

---

## 실습 환경 (도구 목록)

### Claude 계열 (Anthropic)
| 도구 | 접근 방법 | 역할 |
|------|---------|------|
| Claude Chat | claude.ai 웹 브라우저 | 빠른 코드 생성·질문·아이디어 검증 |
| Claude Co-work (Projects) | claude.ai → Projects 탭 | 프로젝트 맥락 유지, 스킬 파일 저장 |
| Claude Code CLI | 터미널 (`claude` 명령어, npm 설치) | 실제 파일 수정·생성, 에이전트 직접 실행 |

### Google 계열 (Google 계정 공통 인증)
| 도구 | 접근 방법 | 역할 |
|------|---------|------|
| Google 계정 | accounts.google.com | 아래 모든 Google 도구의 공통 로그인 기반 |
| Gemini | gemini.google.com | 대화형 AI — Claude와 비교 체험 |
| Google AI Studio | aistudio.google.com | Gemini API 테스트, 프롬프트 플레이그라운드, API 키 발급 |
| NotebookLM | notebooklm.google.com | 문서 기반 AI 리서치·요약·팟캐스트 생성 |
| 안티그래비티 | 강사 확인 후 기입 | AI 활용 자동화 / 특수 목적 도구 |

### 개발 환경
| 도구 | 접근 방법 | 역할 |
|------|---------|------|
| VS Code | code.visualstudio.com | 주 코드 에디터 — Claude Code CLI 통합 |
| Node.js / npm | nodejs.org (LTS 버전) | Claude Code CLI 설치 의존성 |
| GitHub | github.com | 버전 관리, GitHub Pages 무료 배포 |
| Supabase | supabase.com | PostgreSQL DB + Auth(회원가입·로그인) + Storage, 무료 플랜 |
| Vercel | vercel.com | 풀스택 배포, GitHub 자동 연동, 환경변수 관리 |

> **Google Colab 제외**: Python 실습이 필요한 경우 VS Code 내장 터미널에서 진행한다.
> **설치 최소화**: VS Code·Node.js 외 나머지는 웹 브라우저 접근 우선.
> **GitHub + Supabase + Vercel = 현대 풀스택 3종 세트**: 7·8강에서 통합 실습.

---

## 8강 강의 구성 (개요)
| 주차 | 강 | 주제 |
|------|---|------|
| 1주 | 1강 | 바이브코딩의 세계 — Claude Chat + Gemini로 첫 코드 짜기 |
| 1주 | 2강 | 프롬프트 엔지니어링 & Claude Co-work — 잘 말하고 스킬을 만든다 |
| 2주 | 3강 | VS Code + Claude Code CLI — 개발 환경을 완전히 내 것으로 |
| 2주 | 4강 | Google AI 생태계 완전 정복 — Gemini · AI Studio · NotebookLM · 안티그래비티 |
| 3주 | 5강 | 웹페이지 제작 심화 — 인터랙티브 UI & API 연동 |
| 3주 | 6강 | AI 코드 리뷰 & 디버깅 — 오류 없는 코드의 비밀 |
| 4주 | 7강 | 나만의 AI 앱 제작 — Supabase + AI API로 풀스택 MVP |
| 4주 | 8강 | 프로덕션 배포 & 고급 워크플로우 — 세상에 내보내기 |

---

## 5대 핵심 개념 도입 전략
| 개념 | 한 줄 정의 | 처음 체험 강 | 방식 |
|------|----------|------------|------|
| **스킬 (Skill)** | AI에게 전문 역할을 부여하는 재사용 지침 파일 | 2강 | Co-work 시스템 지침 직접 작성 |
| **에이전트 (Agent)** | 목표를 주면 계획·실행·검증을 자율 수행하는 AI | 3강 | Claude Code CLI 첫 파일 생성 |
| **에이전트팀** | 역할 다른 에이전트들이 협업하는 구조 | 1강 | 강사 라이브 시연 (보기) |
| **MCP** | Claude와 외부 도구를 연결하는 표준 규약 | 3강 (개념) / 8강 (실습) | USB 비유 + 실제 연결 |
| **하네스 (Harness)** | 에이전트팀+스킬+MCP 묶음 반복 실행 파이프라인 | 1강 (시연) / 8강 (직접 실행) | 결과물 감상 → 직접 구동 |

## 실행 모드
풀 파이프라인 (커리큘럼 설계 → 강의노트 작성 → 과정 검증)
