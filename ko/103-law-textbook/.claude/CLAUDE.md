# Law Textbook Harness

법률 실무서 집필 하네스. 대상 법률 1건 → 목차 설계 → 법령·판례 조사 → 5블록 챕터 집필 → 계산사례 기계검산 → 6축 검증으로 **일반인+실무자 이원 독자용 실무서 원고(md)**를 에이전트 팀이 생성한다.

도정법 실무서 18장(70번 workspace)에서 실증된 워크플로우의 공식화 — 상속세및증여세법 교재가 첫 가동 대상이다.

## 구조

```
.claude/
├── agents/  (5명)
│   ├── outline-designer.md    — 목차 설계 (구성방식·표준주제 대조·우선순위)
│   ├── law-researcher.md      — 법령·판례 조사 (확인상태 3단계 · 번호 추측 금지)
│   ├── chapter-writer.md      — 5블록 집필 (이원독자 · [검증필요] 표기)
│   ├── example-builder.md     — 사례·계산 (세법류는 기계검산 의무)
│   └── textbook-reviewer.md   — 6축 검증 (구조·최신성·확인상태·검산·용어·독자)
├── skills/  (5종)
│   ├── law-textbook/          — 오케스트레이터 (장 단위 순환 · 6모드)
│   ├── chapter-template/      — 5블록 장 구조 (도정법 실증 부품)
│   ├── legal-currency-guard/  — 최신성 가드 (기준시행일·확인상태·체크리스트·면책)
│   ├── calc-verify/           — 계산 검산 엔진 (verify_calc.py · cases.sample.json)
│   └── book-typeset/          — 책 조판 (신국판·머리글·바닥글·차례·색인 자동 페이지 → HTML+PDF)
└── CLAUDE.md
```

## 사용법

`/law-textbook` 스킬을 트리거하거나, "○○법 실무서 만들어줘" 같은 자연어로 요청한다.
필수 입력: **대상 법률**. 독자·분량은 기본값(이원 독자·200~300p) 제안 후 확정.

## 산출물

책 1권 = `_workspace/{법률명}/` 하위폴더 1개 (예: `_workspace/상속증여세법/`):

- `{법률명}/00_input.md` · `01_book_outline.md` · `02_verification_checklist.md`
- `{법률명}/03_research/` (장별 조사) · `04_examples/` (사례+cases.json) · `05_review/` (장별 검증)
- `{법률명}/chapters/{NN}_{제목}.md` — **원고 본체**
- `{법률명}/` 루트에 리뷰 보조 산출물(원문대조 작업표 xlsx · 통합 열람본 html · `06_색인어휘.txt`)
- `{법률명}/조판본/` — book-typeset 산출 (책 조판 HTML+PDF, 차례·색인 페이지 자동)

편집·표지·전자책 패키징은 11번 book-publishing 또는 보유 스킬(docx-기본서식·html-pastel-style)로 후속 처리.

## 헌법 (타협 불가 5조)

1. 기준 시행일 명시 + 매 집필 시 웹검색 확인 (실패 시 "미조회")
2. 조사에 없는 조문번호·수치·사건번호 본문 사용 금지 — 미확정은 법리만 + [검증필요]
3. 세법류 계산 사례는 verify_calc.py 통과 전 게재 금지
4. 면책 의무 — 서문·계산 사례·최종 보고 ("전문가 감수는 사람의 몫")
5. 이원 독자 — 일반인 풀이 본문 · 실무자 심화 박스 분리

## 관련 하네스·자산

- **70-legal-research** — 판례 심층 리서치가 필요한 장의 보조. 도정법 실무서 원본(재사용 부품)이 그 workspace에 있다
- **11-book-publishing** — 원고 완성 후 편집·패키징
- **첫 가동 리서치**: `_design/phase3_research_2026-08-12.md` — 상증세법 목차 관행·표준주제 18·최신성 주의 목록(유산취득세 미통과 등)
