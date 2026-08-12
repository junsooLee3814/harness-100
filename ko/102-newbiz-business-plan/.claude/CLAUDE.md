# NewBiz Business Plan Harness

신사업 사업계획서 하네스. 신규진출 대상사업의 시장분석 4종 → 최소자본구조(에쿼티·메자닌·론) → 투자조건·철수기준 → **내부 투자심의용 사업계획서 md·html·pptx 3종**을 에이전트 팀이 협업하여 생성한다.

**신사업 성공률 ~25%(베인)를 사전확률로 놓고, 정직한 판정(추진/조건부/보류/철회)을 내리는 것**이 이 하네스의 목표다.

## 구조

```
.claude/
├── agents/  (7명)
│   ├── industry-analyst.md    — 산업분석 (SOM 바텀업 강제 · 44번 계승)
│   ├── competitor-analyst.md  — 경쟁분석 (경쟁자 반응 시나리오 의무 · 44번 계승)
│   ├── consumer-analyst.md    — 소비자분석 (44번 계승)
│   ├── trend-analyst.md       — 트렌드분석 (44번 계승)
│   ├── capital-architect.md   — 자본구조 설계 (소요자금·에쿼티/메자닌/론·시장 눈높이 조건) ★중심축
│   ├── deal-designer.md       — 투자조건 설계 (트랜치·마일스톤·철수기준·밸류에이션)
│   └── plan-writer.md     — 교차검증·12섹션 작성·3종 렌더
├── skills/  (6종)
│   ├── newbiz-business-plan/       — 오케스트레이터 (워크플로우·5모드·에러 핸들링)
│   ├── tam-sam-som-calculator/ — 시장규모 산출 (44번 계승)
│   ├── porter-five-forces/    — 산업 매력도 (44번 계승)
│   ├── capital-structure-guide/ — 조달 벤치마크(CB·BW·RCPS·론)·5단계 로직·건전성 지표
│   ├── decision-framework/    — 12섹션·4단 판정·낙관편향 차단 5호·kill criteria
│   └── plan-renderer/     — 렌더 엔진 (build_html.py · build_pptx.py · slides.sample.json)
└── CLAUDE.md
```

## 사용법

`/newbiz-business-plan` 스킬을 트리거하거나, "신사업 사업계획서 만들어줘" 같은 자연어로 요청한다.
입력 필수 2가지: **대상 사업 + 진출 주체** (없으면 하네스가 질의한다).

## 산출물

- `_workspace/00_input.md` ~ `07_review.md` — 단계별 분석·설계·검증
- `_workspace/YYYY_MM_DD/` — **최종 3종**: `사업계획서_{사업명}.md` / `.html` / `.pptx`

## 헌법 (타협 불가 5조)

1. 사업주 제시값은 벤치마크와 대조해 `부합/낙관/보수` 판정 — 조용한 채택 금지
2. 미제시 수치는 벤치마크 추정 + `[가정]` 태그 + 가정 목록 표 필수
3. 투자조건(금리·만기·전환)은 시장 눈높이 벤치마크 병기 — 근거 없는 조건 금지
4. 표지·푸터에 "내부 검토용 — 투자권유 아님 · 외부 배포 금지" 자동 삽입
5. 한국어 출력 · 수치 출처 명시 · PII 금지

## 범위 주의 — 투자제안서는 별도다

이 하네스의 산출물은 **내부 투자심의용 사업계획서**다. 외부 투자자·대주단에 제시하는 **투자제안서(IM·티저·텀시트)는 이 사업계획서를 입력으로 별도 작성**한다 — 독자·면책·공시 요건이 달라 문서를 겸용하지 않는다. (사내 자산: POI-01 투자요청서 에이전트, dart-investment-proposal 스킬 등이 그 용도)

## 관련 하네스

- **44-market-research** — 분석 4종의 원본. 시장조사만 필요하면 44번 사용
- **101-real-estate-development** — 부동산개발(시행) 전용. 부동산 신사업이면 101번의 사업수지·PF 구조가 더 정밀하다
- **53-financial-modeler** — 일반 기업 재무모델·DCF 심화

## 설계 근거

- `_design/phase3_research_2026-08-03.md` — 2트랙 리서치 (자본조달 시장조건 실측 + IC 표준·실패 교훈)
