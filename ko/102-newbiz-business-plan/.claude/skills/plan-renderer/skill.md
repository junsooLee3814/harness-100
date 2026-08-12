---
name: plan-renderer
description: "사업계획서 3종 렌더링 엔진. 완성된 사업계획서 md를 파스텔 카드 HTML로, 슬라이드 JSON을 맥킨지 파스텔 PPTX(16:9)로 변환한다. 'plan-writer' 에이전트가 최종 산출 단계에서 반드시 이 스킬로 렌더한다. 단, 사업계획서 내용의 작성·검증은 이 스킬의 범위가 아니다."
---

# Plan Renderer — 사업계획서 3종 렌더링 엔진

md(원본) → html(열람용) → pptx(보고용). **md가 원본**이고 나머지는 파생이다 — 렌더 실패가 md를 훼손하면 안 된다.

## 사용법

```bash
# 시스템 Python 필요 (openpyxl 아님 — python-pptx 1.0.2 확인됨)
PY="C:/Users/<user>/AppData/Local/Programs/Python/Python312/python.exe"

# ① HTML — 사업계획서 md를 파스텔 카드 문서로
$PY .claude/skills/plan-renderer/build_html.py \
    _workspace/2026_08_03/사업계획서_사업명.md \
    _workspace/2026_08_03/사업계획서_사업명.html

# ② PPTX — 슬라이드 구성 JSON을 16:9 덱으로
$PY .claude/skills/plan-renderer/build_pptx.py \
    _workspace/2026_08_03/slides.json \
    _workspace/2026_08_03/사업계획서_사업명.pptx
```

### 종료 코드 — 반드시 확인

| 코드 | 의미 | 조치 |
|:-:|---|---|
| 0 | 정상 | 진행 |
| 1 | 입력 오류 (파일 없음·meta/slides 누락·확장자 오류) | 입력 수정 |
| 2 | 생성 후 검증 실패 (슬라이드 수 불일치) | 버그 — 산출물 사용 금지 |
| 3 | **규칙 위반 경고** (bullet>4, H2 섹션 0개) | 내용 수정. 불가피하면 `--allow-warnings` + 사유 명시 (양쪽 렌더러 모두 지원) |

## HTML 렌더 (build_html.py)

- 첫 `# H1` + 다음 문단 → **네이비 표지** + 면책 배지(자동 삽입 — md에 없어도 강제)
- `## H2` → 파스텔 카드 순환 (하늘→연주황→보라→노랑→민트) + 번호 배지
- `### H3`·표·불릿·`**굵게**` 자동 스타일. 단일 파일 산출 (외부 요청은 Pretendard CDN 1건 — 오프라인 시 시스템 폰트 폴백)

## PPTX 렌더 (build_pptx.py)

**slides.json 구조** — 견본: `slides.sample.json`

```json
{
  "meta": {"title": "", "subtitle": "", "org": "", "date": "", "eyebrow": ""},
  "slides": [
    {"layout": "kpi",     "title": "구간명", "action_title": "핵심 메시지 한 문장",
     "kpis": [{"label": "", "value": "", "desc": ""}]},
    {"layout": "section", "badge": "PART 1", "title": "구간 표제"},
    {"layout": "content", "title": "", "action_title": "", "bullets": ["≤4개"], "note": ""},
    {"layout": "table",   "title": "", "action_title": "",
     "table": {"headers": [], "rows": [[]]}, "note": ""}
  ]
}
```

### 디자인 규칙 (렌더러가 강제)

| 규칙 | 구현 |
|---|---|
| 1 슬라이드 1 메시지 | 모든 content/table/kpi에 `action_title` — 결론을 문장으로 |
| Bullet ≤ 4 | 초과 시 경고 + exit 3 (5~6개는 그리되 실패 처리) |
| 표지 면책 | "내부 검토용 — 투자권유 아님" 배지 자동 삽입 (json에 없어도 강제 — 헌법 4조) |
| 푸터 | 전 슬라이드에 면책 문구 + 페이지 번호 자동 (**표지 제외** — 표지엔 면책 배지가 별도) |
| 파스텔 순환 | `section` 슬라이드마다 색 패밀리 전환. content는 소속 구간 색 |
| 폰트 | Pretendard (미설치 환경은 시스템 대체 폰트로 열림) |

### 권장 슬라이드 구성 (14~18장)

표지(자동) → kpi(Executive Summary·판정) → section(시장) → content×2~3(SOM 바텀업·경쟁·소비자)
→ section(사업) → content×2(사업모델·GTM) → section(재무·투자) → table×2~3(재무 3시나리오·자본구조·트랜치)
→ content(리스크·kill criteria) → kpi(판정·조건)

## 산출 후 필수 검증 (plan-writer의 의무)

1. 3종 파일 존재 + exit 0
2. pptx `slides=N` 출력이 기대 수와 일치
3. html `cards≥1`
4. **사람 눈 확인** — 최종 산출물은 PO가 PowerPoint·브라우저로 열어 확인하기 전까지 "완료" 선언 금지

## 주의

- 금액·수치는 md/json에 넣기 전에 확정한다 — 렌더러는 계산하지 않는다
- 같은 날짜 폴더가 이미 있으면 `_v2` 폴더에 저장 (덮어쓰기 금지)
- pptx 실패가 md·html 산출까지 막지 않게 한다 (md 먼저 저장 → html → pptx 순서)
