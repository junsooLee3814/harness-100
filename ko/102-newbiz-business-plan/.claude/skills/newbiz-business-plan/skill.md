---
name: newbiz-business-plan
description: "신사업 사업계획서 풀 파이프라인. 신규진출 대상사업의 산업·경쟁·소비자·트렌드 분석 → 최소자본구조(에쿼티·메자닌·론) 설계 → 투자조건·철수기준 설계 → 내부 투자심의용 사업계획서를 YYYY_MM_DD 폴더에 md·html·pptx 3종으로 생성한다. '신사업 검토', '신사업 사업계획서', '사업계획서 만들어줘', '신규 진출 타당성', '자본구조 설계', '투자심의 자료', 'IC 자료', '신사업 투자 검토' 등에 이 스킬을 사용한다. 단, 실제 투자 실행, 법인 설립, **외부 제출용 투자제안서(IM·티저·텀시트 — 본 사업계획서를 입력으로 별도 작성)**, 부동산개발 사업수지(101번)는 이 스킬의 범위가 아니다."
---

# NewBiz Business Plan — 신사업 사업계획서 파이프라인

신규진출 대상사업 1건을 받아, 시장분석 4종 → 자본구조 → 투자조건 → **내부 투자심의용 사업계획서 3종(md·html·pptx)**을 생성한다.

**신사업 성공률은 약 25%다.** 이 하네스의 목표는 잘 팔리는 문서가 아니라, 그 현실 위에서 **정직한 판정(추진/조건부/보류/철회)**을 내리는 문서다.

## 실행 모드

**에이전트 팀** — 7명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| industry-analyst | `.claude/agents/industry-analyst.md` | 시장규모(SOM 바텀업)·산업구조·규제 | general-purpose |
| competitor-analyst | `.claude/agents/competitor-analyst.md` | 경쟁 매핑·SWOT·**경쟁자 반응 시나리오** | general-purpose |
| consumer-analyst | `.claude/agents/consumer-analyst.md` | 세그먼트·구매여정·지불의사 | general-purpose |
| trend-analyst | `.claude/agents/trend-analyst.md` | PESTLE·시나리오 전제 | general-purpose |
| capital-architect | `.claude/agents/capital-architect.md` | 소요자금·**최소자본구조·시장 눈높이 조건**·재무 3시나리오 | general-purpose |
| deal-designer | `.claude/agents/deal-designer.md` | 트랜치·마일스톤·**철수 기준**·밸류에이션·회수 | general-purpose |
| plan-writer | `.claude/agents/plan-writer.md` | 교차검증·12섹션 작성·**3종 렌더** | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **대상 사업**: 진출하려는 사업·제품·서비스 (필수 — 없으면 질의)
    - **진출 주체**: 어느 회사/조직이 진출하나 (자사 자산·역량 판단의 전제)
    - **지리 범위**: 국내/해외
    - **소요자금 (선택)**: 사업주 제시값 — 있으면 벤치마크 검증, 없으면 하이브리드 추정
    - **투자 형태 선호 (선택)**: 자체 사업부/신설 법인/JV
    - **기존 자료 (선택)**: 보유 시장분석·사업계획 초안
2. **대상 사업과 진출 주체 중 하나라도 없으면 질의한다** — "왜 우리가"는 진출 주체 없이 답할 수 없다
3. `_workspace/` 생성, 입력을 `_workspace/00_input.md`에 저장 (미제공 항목 `[미제공]` 명시)
4. 기존 분석 자료가 있으면 해당 단계를 건너뛴다 (44번 패턴)

### Phase 2: 팀 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|:-:|------|------|------|--------|
| 1 | 산업 분석 | industry-analyst | 없음 | `01_industry_analysis.md` |
| 2a | 경쟁 분석 | competitor-analyst | 1 | `02_competitor_analysis.md` |
| 2b | 소비자 분석 | consumer-analyst | 1 | `03_consumer_analysis.md` |
| 3 | 트렌드 분석 | trend-analyst | 1·2a·2b | `04_trend_analysis.md` |
| 4 | 자본구조 설계 | capital-architect | 1~3 | `05_capital_structure.md` |
| 5 | 투자조건 설계 | deal-designer | 4 | `06_deal_terms.md` |
| 6 | 교차검증·사업계획서·렌더 | plan-writer | 전부 | `07_review.md` + `YYYY_MM_DD/` 3종 |

2a·2b는 **병렬 실행** (44번 검증 패턴).

**팀원 간 소통 흐름 (핵심 연결):**
- consumer → capital: 지불의사 가격·목표 고객수 (바텀업 매출의 입력)
- competitor → capital: 경쟁자 반응 시나리오 손익 (보수 시나리오의 입력)
- trend → capital: 낙관/기준/보수 시나리오의 시장 전제
- capital → deal: 조달 구조·시나리오 현금흐름·추가 출자 필요액
- deal → writer: 트랜치·kill criteria·판정 초안
- writer가 낙관편향 감사 위반 발견 시 → 해당 에이전트 수정 요청 (최대 2회)

### Phase 3: 최종 산출

1. 오늘 날짜로 `_workspace/YYYY_MM_DD/` 생성 (예: `2026_08_03`. 기존재 시 `_v2`)
2. plan-writer가 `plan-renderer`로 3종 생성:
   - `사업계획서_{사업명}.md` (원본)
   - `사업계획서_{사업명}.html` (파스텔 카드)
   - `사업계획서_{사업명}.pptx` (맥킨지 파스텔 14~18장)
3. 교차 검증 확인:
    - [ ] 매출 추정 = 소비자분석 바텀업 산식과 일치
    - [ ] 보수 시나리오에 경쟁자 반응 반영
    - [ ] 소요자금 = 조달 구조 합계 = 트랜치 합계
    - [ ] 낙관편향 감사 5호 전수 통과 (decision-framework)
    - [ ] kill criteria 명문화 (없으면 미완성)
    - [ ] 판정이 4단 중 하나로 확정
    - [ ] 3종 파일 생성 + 렌더러 exit 0
4. 사용자에게 판정·핵심 수치·파일 경로·가정 목록 요약 보고

## 작업 규모별 모드

| 요청 패턴 | 모드 | 투입 |
|---|---|---|
| "신사업 검토·사업계획서 전체" | **풀 파이프라인** | 7명 전원 |
| "시장분석만" | 분석 모드 | 분석 4명 (44번과 동일 범위) |
| "자본구조만 설계해줘" (분석 있음) | 자본 모드 | capital + deal |
| "이 계획서를 3종으로 만들어줘" | 렌더 모드 | plan-writer 단독 |
| "두 사업 비교" | 비교 모드 | 7명 × 2건 + 비교표 |

## 헌법 (타협 불가 5조)

1. **사업주 제시값 검증** — 제시값은 벤치마크와 대조해 `부합/낙관/보수` 판정. 조용한 채택 금지
2. **`[가정]` 태그 의무** — 미제시 수치는 벤치마크 추정 + 태그 + 가정 목록 표
3. **시장 눈높이 병기** — 투자조건(금리·만기·전환)은 벤치마크 병기. 근거 없는 조건 금지 (capital-structure-guide)
4. **내부 검토용 명시** — 표지·푸터에 "투자권유 아님·외부 배포 금지" 자동 삽입 (렌더러가 강제)
5. **한국어 출력 · 수치 출처 명시 · PII 금지**

## 에러 핸들링

| 에러 유형 | 전략 |
|---|---|
| 대상 사업·진출 주체 불명 | 작업 중단 후 질의. 임의 가정 금지 |
| 웹 검색 실패 (시장·금리) | 스킬 내장 기준치(기준 시점 명시) + "미조회" 표기 |
| 분석 산출물 누락 | 해당 섹션 "미작성" 표기. 추정으로 메우지 않음 |
| 렌더 실패 | md 보존 + 실패 사유 명시. pptx 실패가 md·html을 막지 않음 |
| 에이전트 실패 | 1회 재시도 → 결손 명시하고 진행 |
| 판정 근거 상충 | knock-out 우선 (재무 좋아도 knock-out 위반이면 철회/보류) |
| 낙관편향 감사 위반 | 수정 요청 2회 → 미해소 시 감사표에 위반 기록 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "우리 회사(중견 식품제조)가 프리미엄 반려동물 사료 시장에 진출하려고 해. 신사업 사업계획서 만들어줘"
**기대**: 분석 4종(SOM 바텀업·경쟁자 반응 포함) → 자본구조(에쿼티/시설대출/RCPS + 벤치마크) → 트랜치·kill criteria → `2026_08_03/` 3종 파일 + 판정

### 부분 흐름
**프롬프트**: "시장분석은 이미 있어. 자본구조랑 투자조건만 설계해줘" + 파일
**기대**: 기존 분석을 01~04로 복사, capital + deal + writer만 투입

### 에러 흐름
**프롬프트**: "뭔가 새로운 사업 하고 싶은데"
**기대**: 대상 사업·진출 주체 질의. 후보 제안은 하되 임의 진행 금지

## 에이전트별 확장 스킬

| 스킬 | 대상 | 역할 |
|------|------|------|
| `tam-sam-som-calculator` | industry | TAM/SAM/SOM 산출 방법론 (44번 계승) |
| `porter-five-forces` | industry, competitor | 산업 매력도 (44번 계승) |
| `capital-structure-guide` | capital-architect | 조달 벤치마크·5단계 로직·건전성 지표 |
| `decision-framework` | capital, deal, writer | 12섹션·4단 판정·낙관편향 차단 5호·kill criteria |
| `plan-renderer` | plan-writer | md→html·json→pptx 렌더 엔진 |
