# 🏭 하네스 출하 보고서 — 102-newbiz-business-plan

작성일 2026-08-03 · 제조 공장 `/llm-dependent-agent-create` (V3.5) 공정, 출하 포장은 Harness 100 형식

---

## 1. 제조 개요

| 항목 | 내용 |
|---|---|
| 이름 | `newbiz-business-plan` (하네스 102) |
| 목표 | 신규진출 대상사업 → 시장분석 4종 + 최소자본구조(에쿼티·메자닌·론) + 투자조건 → **내부 투자심의용 사업계획서 md·html·pptx 3종** |
| 판정 체계 | 추진 / 조건부 추진 / 보류 / 철회 — 4단 확정 (신사업 성공률 ~25%를 사전확률로) |
| 인프라 | B · 단일 모드 · 규모 L · Windows (python-pptx 1.0.2) |
| 등재 | `ko/102-newbiz-business-plan/` · `harness-100-cases.md` 확장 절 · `harness-catalog.html` (102종) |

## 2. 구성

```
.claude/agents/ (7명)
  industry / competitor / consumer / trend-analyst   ← 44번 계승 (🟡 재단: SOM 바텀업 강제·
                                                        경쟁자 반응 시나리오 의무·통신 재배선)
  capital-architect   ★중심축 — 소요자금(하이브리드)·5단계 자본구조·시장 눈높이 조건·재무 3시나리오
  deal-designer       — 트랜치·마일스톤·철수기준(kill criteria)·밸류에이션·회수
  plan-writer     — 교차검증·낙관편향 감사·12섹션 작성·3종 렌더

.claude/skills/ (6종)
  newbiz-business-plan            오케스트레이터 (5모드·필수 왕복·에러 핸들링)
  tam-sam-som-calculator     44번 계승 (🟡 — dead reference 수정)
  porter-five-forces         44번 계승 (🟢 그대로)
  capital-structure-guide    🏭 — CB·BW·RCPS·론 벤치마크(2026.7 실측)·5단계 로직·실패 패턴 5
  decision-framework         🏭 — 12섹션·4단 판정·낙관편향 차단 5호·kill criteria 6항목
  plan-renderer          🏭 — build_html.py(파스텔 카드)·build_pptx.py(맥킨지 파스텔 16:9)
```

**BOM**: 🟢 1 (porter) · 🟡 5 (분석 에이전트 4 + tam-sam-som) · 🏭 8 (신규 에이전트 3 + 스킬 3 + 렌더러 2) · 🔴 0 · 🔵 0

**워크플로우**: 1 산업 → 2a 경쟁 ∥ 2b 소비자 → 3 트렌드 → 4 자본구조 → 5 투자조건 → 6 교차검증·렌더
핵심 연결: 소비자→자본(바텀업 매출), 경쟁→자본(보수 시나리오 입력), 자본→조건(현금흐름), 조건→작성(판정 초안)

## 3. 헌법 (타협 불가 5조)

1. 사업주 제시값은 벤치마크 대조 `부합/낙관/보수` 판정 — 조용한 채택 금지 (101번 계승)
2. 미제시 수치는 벤치마크 추정 + `[가정]` 태그 + 가정 목록 표
3. 투자조건(금리·만기·전환)은 시장 눈높이 벤치마크 병기 — 근거 없는 조건 금지
4. "내부 검토용 — 투자권유 아님 · 외부 배포 금지" — **렌더러가 코드 수준에서 강제** (표지 배지 + 전 슬라이드 푸터)
5. 한국어 · 수치 출처 명시 · PII 금지

## 4. 설계 근거 — 2트랙 리서치 (`_design/phase3_research_2026-08-03.md`)

- **트랙 A (자본조달)**: CB 표면 0~2%+YTM 2~5%·RCPS 배당 1%+연복리 6~8%·기업대출 4.2~4.5%·DSCR≥1.2 등 2026.7 실측 벤치마크. 리픽싱 70%·콜옵션 한도·사모 분리형 BW 금지(상장사 한정 구분). 최소자본구조 5단계 로직. 실패 패턴 5건
- **트랙 B (IC 표준)**: 12섹션 목차·Stage-Gate 4단 판정·낙관편향 차단 5호(Lovallo&Kahneman·맥킨지 시너지 통계)·kill criteria 6항목·국내 실패 레퍼런스(웅진·금호·삼성차·LG폰)

## 5. QC 결과 — 자기검증 금지 적용

독립 Verification Subagent 1라운드: **87/100 · Critical 0 · High 1 · 조건부 출하** → 조건 전부 해소.

| 지적 | 조치 | 재검증 |
|---|---|---|
| High: tam-sam-som에 없는 `research-reviewer` 참조 잔존 (44번 계승 시 유입) | plan-writer로 교체 | grep 0건 |
| build_html.py stderr 인코딩 누락 → 콘솔 한글 깨짐 | reconfigure 추가 | 정상 출력 확인 |
| skill.md의 `--allow-warnings`가 html에 미구현 | 구현 | exit 3 → 플래그 시 0 실측 |
| 버퍼 포함/제외 기저 모호 (자기자본 하한 과소 산정 위험) | "버퍼 포함 최종값 기준" 양쪽 명시 | — |
| pptx 입력 오류 시 스택트레이스 | try/except 정형화 | exit 1 + 정형 메시지 실측 |
| 죽은 코드·문서-동작 불일치 3건 (푸터 표지 제외·CDN 명기 등) | 전부 수정 | compile OK |

**렌더러 파손 시험 (검증관 실측)**: meta 삭제·빈 slides·bullet 6개·확장자 오류·미지 layout·H2 없음·경로 오류 — 전부 문서화된 종료 코드(1·3)로 실패. **조용한 오출력 0건.**

**화면 검증 (사람 눈 대리)**: PPTX를 PowerPoint COM으로 열어 슬라이드 PNG 추출 — 표지 면책 배지·액션 타이틀·파스텔 카드·푸터 확인. HTML은 Playwright 스크린샷 — 네이비 표지·카드 순환·표 스타일 확인.

## 6. 사용법

```bash
cp -r ko/102-newbiz-business-plan/.claude/ /경로/내프로젝트/.claude/
```
`/newbiz-business-plan` 또는 "신사업 사업계획서 만들어줘". **필수 입력 2가지: 대상 사업 + 진출 주체** (없으면 질의). 산출: `_workspace/00~07` + `_workspace/YYYY_MM_DD/사업계획서_{사업명}.md/.html/.pptx`

## 7. 미실시 (PO 첫 실사용 시)

- **7인 팀 실호출 E2E** — 실제 신사업 1건으로 풀 파이프라인. 필수 연결(소비자→자본·경쟁→자본)과 낙관편향 감사가 실제로 도는지
- **최종 pptx·html 사람 눈 확인** — 견본은 검증했으나 실데이터 산출물은 PO가 PowerPoint·브라우저로 직접 확인
- **시장금리 웹검색 갱신 확인** — capital-architect가 기준금리·회사채 금리를 실제로 갱신하는지 (스킬 내장치는 2026.7 기준)
