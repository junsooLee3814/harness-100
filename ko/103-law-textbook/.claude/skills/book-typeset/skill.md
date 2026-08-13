---
name: book-typeset
description: md 원고를 진짜 책 조판(신국판 152×225mm · 머리글 · 바닥글 페이지번호 · 차례 · 색인 자동 페이지)으로 변환해 HTML+PDF 생성. "조판해줘", "책처럼 만들어줘", "PDF 책으로" 트리거.
---

# book-typeset — 원고 → 책 조판 (Paged.js)

`_workspace/{법률명}/chapters/*.md` 원고를 **페이지가 있는 진짜 책**으로 조판한다.
페이지 번호는 조판 시점에 자동 부여되고, **차례와 색인의 페이지 숫자는 `target-counter`로
자동 계산**되므로 원고를 수정해도 재실행 한 번이면 전부 갱신된다 (수동 페이지 기입 없음).

## 실행 (2단계 — 반드시 verbatim)

```bash
PY="C:/Users/juncp/AppData/Local/Programs/Python/Python312/python.exe"
# 1) 조판 HTML 생성
PYTHONUTF8=1 $PY .claude/skills/book-typeset/build_book.py "_workspace/{법률명}" "{책 제목}"
# 2) PDF 렌더 + 페이지 수 보고 + 검수 스크린샷(표지·차례·본문·색인)
PYTHONUTF8=1 $PY .claude/skills/book-typeset/render_pdf.py "_workspace/{법률명}/조판본/{책 제목}_조판본.html" "<스크래치>/bookshots"
```

- 출력: `_workspace/{법률명}/조판본/{책 제목}_조판본.html` + `.pdf`
- 렌더는 Playwright Chromium + 로컬 `paged.polyfill.js` (0.4.3, 이 폴더에 동봉)
- 조판은 원고 분량에 따라 수십 초~수 분 — timeout 넉넉히 (render_pdf.py 내부 480초)

## 색인 시스템

- 색인어는 `_workspace/{법률명}/06_색인어휘.txt` — 한 줄 `표제어|변형1|변형2` (# 주석)
- build_book.py가 장마다(제목 포함) 각 표제어의 **첫 등장 위치에 앵커**를 심고,
  책 끝 색인에서 앵커의 페이지 번호를 자동 인쇄 (가나다 그룹핑, 2단)
- 실행 로그의 "본문 미발견 색인어"는 표기 차이(예: 연대납세→연대납부)일 수 있으니
  grep으로 원고 실제 표기를 확인해 변형을 추가할 것

## 곁들이 산출물 — 통합 열람본 HTML

조판본(인쇄용)과 별개로, **화면에서 원고 전체를 훑는 검토용 열람본**을 같은 원고에서 생성한다.

```bash
PYTHONUTF8=1 $PY .claude/skills/book-typeset/build_reading_html.py "_workspace/{법률명}" "{책 제목}"
```

- 출력: `_workspace/{법률명}/{법률약칭}_실무서_열람본.html` (3번째 인자로 파일명 stem 지정 가능,
  생략 시 폴더의 기존 `*_열람본.html`을 자동 감지해 같은 경로로 덮어씀)
- 좌측 고정 nav = 장 + **절(##) 단위 목차**, 커버에 통계칩 자동 표기
  (장 수·글자수·절 수·계산 사례 수·[검증필요] 건수·생성일시)
- `[검증필요]`는 주황 배지, 💡/⚠️/가상의 사례/이 장에서 다루는 것/개정 예고는 색상 콜아웃 박스
- **원고가 바뀌면 재실행만 하면 갱신** — 수동 편집 금지 (수동 제작본은 원고 증량 시 즉시 낡는다)

## 검증 의무 (사람 눈 대행)

렌더 후 스크린샷 4장(표지·차례·본문 중간·색인)을 Read로 열어 반드시 확인:
① 차례 페이지 번호 채워짐 ② 홀수쪽 머리글=장 제목·짝수쪽=책 제목 ③ 바닥글 페이지
④ 색인에 페이지 숫자 인쇄. 하나라도 비면 출하 금지.

## 함정

- 머리글 책 제목은 CSS 리터럴 치환(`__BOOKTITLE__`) — body string-set은 Paged.js에서 전파 안 됨
- 앵커 스캔은 태그 분리 후 텍스트 세그먼트만 치환 (HTML 태그 훼손 금지)
- [검증필요] 마커는 조판본에도 주황 표시로 유지 — **출판 최종본 전에 원문대조로 전부 해소** 필요
- 판형·글꼴 변경 시 페이지 수가 바뀌지만 차례·색인은 자동 추종 — 손볼 것 없음

## 후속

감수 완료 후 최종 출판(표지 시안·ISBN·메타데이터·배포)은 11번 book-publishing 하네스로.
