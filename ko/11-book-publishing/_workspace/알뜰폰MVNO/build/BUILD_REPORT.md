# 빌드 보고서 — 『알뜰폰의 다음 10년 — 1,000만 회선 이후의 생존 전략』 내부 배포판 v1.0

작성: 전자책 빌드 엔지니어 · 2026-07-05
입력: `01_edited_manuscript.md`(원고), `04_metadata.md` §7(OPF 스펙), `05_review_report.md`(배포 전 체크리스트 B·C), `covers/cover_a.png`(1600x2560)

---

## 1. 산출 파일

| 파일 | 크기 | 비고 |
|---|---|---|
| `build/알뜰폰의_다음_10년_internal_v1.0.epub` | 672,411 bytes (657 KB) | EPUB 3, pandoc 생성, 표지 포함 |
| `build/알뜰폰의_다음_10년_internal_v1.0.pdf` | 1,199,735 bytes (1.14 MB) | A4 · **46페이지**(표지 1+본문 45) · 인쇄 여백·머리글·쪽번호 — **v1.0r2 재빌드본** (§8) |
| `build/book_body.md` | 89,950 bytes | 배포용 본문 (부속 문서 5개 섹션 절단본 + Y1 면책 반영) |
| `build/BOOK_UUID.txt` | `e14c68a2-e3be-410d-9c95-35dcbee82762` | 개정판 재사용용 — v1.1 이후에도 동일 UUID 유지, `dcterms:modified`만 갱신 |
| `build/epub_metadata.yaml` | — | pandoc 메타데이터 투입 원본 (04 §7 무축약 매핑) |
| `build/book.html` | — | PDF 렌더 중간 산출물 (표지 div + 워터마크 주입본) |

## 2. 본문 절단 (체크리스트 B-①)

- 절단 기준: 원고의 **이중 구분선(`---` 2연속)** 자동 탐지 — Y1 면책 1문장 삽입으로 행번호가 805→807로 밀렸으나, 행번호가 아닌 패턴 기준으로 절단하여 오차 없음.
- 제외 확인(EPUB 전문 + PDF 전문 검색): 편집 개요 / 제목 후보 비교 / 딜 정보 제거 확인 목록 / 교정교열자 전달 사항 / 표지디자이너 전달 사항 / 메타데이터관리자 전달 사항 — **전부 부재(0건)**.

## 3. 딜 키워드 스캔 (3중 실시 — 전부 0건)

키워드 19종: 101억 · 유상증자 50 · CB 51 · 표면금리 · 표면이자율 · YTM · 만기보장수익 · 리픽싱 · 풋옵션 · 콜옵션 · IRR · 투자요청서 · Project FreeT · 선명법무법인 · 발행단가 · 주당 500원 · 텀시트 · 주금납입 · Sources & Uses

| 대상 | 결과 |
|---|---|
| `book_body.md` (절단 직후) | **0건** |
| EPUB 내 전체 XHTML/NCX 텍스트 | **0건** |
| PDF 전 44페이지 추출 텍스트 (pypdf) | **0건** |

## 4. Y1 해소 — 서문 면책 문장

- 삽입 문안: "본서는 정보 제공 목적으로 작성되었으며, 특정 기업 또는 특정 종목에 대한 투자 권유가 아닙니다."
- 반영 위치: 서문 말미(결론 문장 뒤, "2026년 7월" 서명 앞) — **원본 `01_edited_manuscript.md`와 `build/book_body.md` 양쪽 동일 반영**, EPUB·PDF 본문에 포함 확인.

## 5. EPUB 검사 결과 (체크리스트 B-②·③, C)

| 항목 | 결과 |
|---|---|
| `dc:title`(main) | ✅ `알뜰폰의 다음 10년 — 1,000만 회선 이후의 생존 전략` — 전각 줄표·"1,000만" 쉼표 원형 |
| `dc:title`(subtitle) | ✅ `한국 MVNO 시장의 성숙, 참가자, 소비자, 그리고 독립계의 생존 조건` — MVNO 대문자 |
| `dc:creator` | ✅ 선명그룹 리서치 (role=aut) — 임시 표기 상태 |
| `dc:publisher` / `dc:language` / `dc:date` | ✅ 선명그룹 / ko / 2026-07-05 |
| `dc:rights` | ✅ 04 §7 전문 무축약 일치 (외부 유통 금지 + 투자 권유 아님 문안 포함) |
| `dc:identifier` | ✅ `urn:uuid:e14c68a2-e3be-410d-9c95-35dcbee82762` (BOOK_UUID.txt와 일치) |
| `dc:subject` | ✅ 10종 전량 (알뜰폰~시나리오 플래닝, 04 §4 순서 그대로) |
| 표지 | ✅ `properties="cover-image"` 지정 (cover_a.png → media/file0.png), cover.xhtml 스파인 선두 |
| 목차 | ✅ `--toc --toc-depth=2 --split-level=1` — nav.xhtml + 챕터 분할 ch001~ch011, 부속 문서 챕터 부재 |
| 면책(판권지+서문) | ✅ 본문 내 고정 문안 존재 확인 |

## 6. PDF 검사 결과 (체크리스트 B-②·④) — ⚠️ v1.0 초판 빌드 기록 (v1.0r2로 대체됨, §8 참조)

| 항목 | 결과 |
|---|---|
| 페이지 수 | 44페이지 (A4, print_background=True) |
| 1페이지 | ✅ 전면 표지 — 이미지 XObject 존재, 본문 텍스트 없음(워터마크 텍스트만 추출됨) |
| 워터마크 | ✅ "내부 배포용 — 재배포 금지" — **44/44 전 페이지** pypdf 텍스트 추출로 확인 |
| 푸터 | ✅ "선명그룹 리서치 · 내부 배포용" (html-pastel-style 표지 eyebrow) |
| 본문 시작 | ✅ 2페이지 = 표제·판권지(제목/부제/저자/면책) |
| 부록 C 수록 | ✅ 본문 마지막 = 부록 C 데이터 한계와 정정 이력 |

## 7. 사용 도구

| 도구 | 버전 |
|---|---|
| pandoc (pypandoc-binary 동봉) | 3.9 (pypandoc 1.17) |
| playwright (chromium) | 1.61.0 |
| pypdf | 6.12.2 |
| html-pastel-style build_html.py | `C:/Users/juncp/.claude/skills/html-pastel-style/scripts/build_html.py` (24 섹션 카드) |
| Python | 3.12.10 |

## 8. v1.0r2 — PDF 인쇄 형식 개선 (2026-07-05, 사용자 피드백 반영 재빌드)

EPUB은 변경 없음. `알뜰폰의_다음_10년_internal_v1.0.pdf`만 재생성(덮어쓰기) — **1,199,735 bytes · 총 46페이지**(표지 1 + 본문 45).

### 변경 내역

| 항목 | v1.0(초판 빌드) | v1.0r2 |
|---|---|---|
| 여백 | 0 (HTML 기본) | top 22mm · bottom 18mm · left/right 17mm |
| 머리글 | 없음 | 좌 "알뜰폰의 다음 10년" · 우 "내부 배포용 — 재배포 금지" (8px, #94a3b8, sans-serif, 좌우 17mm 패딩) |
| 바닥글 | 없음 | 중앙 쪽번호 `n / 45` (본문 기준 1부터 — 표지 제외 허용 사양) |
| 워터마크 | position:fixed div (전 페이지) | **제거** — 머리글 우측 표기가 대체 |
| 표지 | 본문 HTML 최상단 img div | **분리 렌더** — `cover.html`(여백 0, A4 전면, object-fit:contain, 배경 #0a1526=표지 가장자리 색 샘플링) 단독 1페이지 PDF → pypdf로 본문 PDF와 병합 |
| 화면용 book.html | .page 920px(스킬 기본) | `@media screen` 한정 오버라이드 `<style>` 주입: max-width 900px + margin auto + 좌우 28px 패딩. **원본 스킬 CSS 파일 무수정**, print 규칙 영향 없음 |

### v1.0r2 검증 결과 (pypdf + Playwright 스크린샷)

| 항목 | 결과 |
|---|---|
| 총 페이지 | 46 (표지 1 + 본문 45) |
| 1페이지(표지) | ✅ 텍스트 추출 결과 공백 — 머리글·쪽번호 **없음**, 표지 이미지 XObject 존재 |
| 머리글 | ✅ 본문 **45/45** 페이지에서 "알뜰폰의 다음 10년" + "내부 배포용 — 재배포 금지" 확인 (공백 정규화 매칭 — pypdf 추출 시 자간 공백 삽입됨) |
| 쪽번호 | ✅ 본문 **45/45** 페이지에서 `n / 45` 패턴 확인, 1부터 시작 |
| 딜 키워드 19종 | ✅ 재빌드본 전문 재스캔 — **0건** |
| 면책 문장 | ✅ 유지 확인 |
| 화면용 HTML | ✅ `_screen_check_top.png` / `_screen_check_mid.png` — 1600px 뷰포트에서 본문 900px 중앙 정렬·카드 레이아웃 정상 육안 확인 |

참고: PDF 페이지 래스터 스크린샷은 pdftoppm 부재로 생략, pypdf 텍스트·병합 구조 검증으로 대체(지시서 허용 대체안).

## 9. 남은 수작업 (05 체크리스트 A — 저자/오케스트레이터 결정)

- [x] **저자명 확정** — 2026-07-05 확정 반영 완료 (§10 v1.1). 저자 "공인회계사 이준수" · 발행처 "선명리서치쎈터"(사용자 원문 표기 유지), 5곳 치환: 원고 표제지·판권지·표지 HTML 2종 재렌더·OPF `dc:creator`·04 §1
- [ ] R1 — 순유출 수치 단위 "명"↔"회선" 통일 여부 결정
- [ ] R5 — "IIJ" vs "IIJmio" 표기 의도 확정
- [ ] 부록 C 4항 "독립계 점유율(약 45%)" 산출 근거 각주 추가 여부
- [ ] 부록 B "뉴스천지" 매체명 정확성 확인
- [ ] 배포 실행: 04 §5 허용 독자 범위·§6 채널 정책 준수 (개별 발송 + 링크 공유 끄기, 발송 메일에 재배포 금지 조건 요약 첨부)
- 참고: 파일명은 빌드 지시서 기준 `알뜰폰의_다음_10년_internal_v*.*`을 사용 — 04 §6 제안명(`내부배포판`)과 다르므로 배포 공지 시 하나로 통일 권장.

## 10. v1.1 — 저자 확정 + 확정 표지 B안 재빌드 (2026-07-05)

**배포 대상은 v1.1** (v1.0 파일 2종은 이력 보존용으로 유지).

| 파일 | 크기 | 비고 |
|---|---|---|
| `알뜰폰의_다음_10년_internal_v1.1.epub` | 166,564 bytes | 표지 B안 — cover_b.png(122 KB)가 cover_a(631 KB)보다 작아 v1.0 대비 축소 |
| `알뜰폰의_다음_10년_internal_v1.1.pdf` | 847,816 bytes | 46페이지(표지 1 + 본문 45) · v1.0r2 인쇄 형식 동일 |

### 반영 내역

1. **저자 확정 치환** — 임시 "선명그룹 리서치" → 저자 **공인회계사 이준수** · 발행처 **선명리서치쎈터**("쎈터" 사용자 원문 표기, "센터" 교정 금지 준수)
   - `01_edited_manuscript.md`: 표제지·판권지(발행처·"© 2026 선명리서치쎈터" 행 신설)·서문 서명("선명리서치쎈터 · 공인회계사 이준수") + 부속 문서 내 표기 3곳
   - `covers/cover_a.html`·`cover_b.html`: 저자 라인 → "선명리서치쎈터 · 공인회계사 이준수", Playwright 1600x2560 재렌더(A·B 모두). **재렌더 중 발견·수정**: 확정 표기가 길어져 저자 라인이 2행으로 꺾이고 배지와 간섭 → 저자 폰트 축소(A 30→22px, B 28→21px)+nowrap, 배지 13px+nowrap. 수정 후 두 안 모두 Read 육안 검수 통과
   - `04_metadata.md`: §1(저자·발행 주체·확정 표지 행 신설), §3-3, §7 OPF(dc:creator="공인회계사 이준수"·file-as="이준수"·role=aut, dc:publisher="선명리서치쎈터", dc:rights ©, belongs-to-collection), §8-1 ©
   - `build/epub_metadata.yaml`: creator·publisher·rights·collection 동기 갱신
2. **확정 표지 B안 전환** — EPUB `--epub-cover-image=covers/cover_b.png`(zip 내 media/file0.png MD5 = covers/cover_b.png 일치 확인), PDF 표지 전용 HTML도 cover_b로 교체 + letterbox 배경을 B안 가장자리 색 `#f5f2ec`(오프화이트, PNG 픽셀 샘플링)으로 재지정. `03_cover_concept.md`·`04_metadata.md`에 "확정 표지: B안" 기록
3. **UUID 재사용** — `urn:uuid:e14c68a2-e3be-410d-9c95-35dcbee82762` (BOOK_UUID.txt, 신규 생성 없음)
4. **PDF 인쇄 형식** — v1.0r2와 동일 (여백 17/22/18mm, 머리글 좌 "알뜰폰의 다음 10년"·우 "내부 배포용 — 재배포 금지", 중앙 쪽번호 n/45, 표지 분리 병합)

### v1.1 검증 결과

| 항목 | 결과 |
|---|---|
| 잔존 스캔 "선명그룹 리서치" | ✅ **0건** — 01·04·book_body·EPUB 전문·PDF 전문 (05·02·BUILD_REPORT 등 기록 문서는 검사 제외 대상) |
| 신규 표기 존재 | ✅ "공인회계사 이준수"·"선명리서치쎈터" — 원고·EPUB·PDF 모두 확인 |
| 딜 키워드 19종 | ✅ book_body·EPUB·PDF 3중 스캔 **0건** |
| EPUB OPF | ✅ creator/publisher/rights(© 선명리서치쎈터)/title 2종/identifier(UUID 동일) 정상, 부속 문서 챕터 부재 |
| PDF 구조 | ✅ 46페이지, 1페이지 표지(텍스트 무, 이미지 XObject), 머리글 45/45, 쪽번호 45/45 |
| 표지 육안 | ✅ A·B 재렌더본 Read 검수 — 저자 라인 1행 표기·배지 간섭 없음, 제목/부제 자획 유지 |

## 11. v1.2 — 저자·발행처 표기 변경 재빌드 (2026-07-05)

**배포 대상은 v1.2** (v1.1 파일은 이력 보존용으로 유지). 사용자 지시: 저자 → "선명리서치센터(SMRC SunMyung Research Center)", "선명그룹(SUNMYUNG GROUP)" 및 "공인회계사 이준수" 표기 제거, "쎈터" → "센터".

| 파일 | 크기 | 비고 |
|---|---|---|
| `알뜰폰의_다음_10년_internal_v1.2.epub` | 164,999 bytes | 표지 B안 재렌더본(1600x2560, Playwright deviceScaleFactor 2) |
| `알뜰폰의_다음_10년_internal_v1.2.pdf` | 847,003 bytes | 46페이지(표지 1 + 본문 45) · v1.0r2 인쇄 형식 동일. 저자 표기 **"선명리서치센터(SMRC SunMyung Research Center)" 풀네임 — EPUB과 통일**(2026-07-05 사용자 재지시로 단독 표기판을 풀네임판으로 재빌드·덮어쓰기). 표제지·판권지 저자/발행처·서문 서명 풀네임, © 2026 선명리서치센터 |

### 반영 내역

1. **표기 치환** — 저자·발행처: "선명리서치센터(SMRC SunMyung Research Center)" / 발행처 단독 표기 "선명리서치센터" / © 2026 선명리서치센터
   - `build/book_body.md`·`01_edited_manuscript.md`: 표제지·판권지·서문 서명 + 부속 문서 기록 3곳
   - `covers/cover_a.html`·`cover_b.html`: 저자 라인 → 오버라인 "SMRC · SUNMYUNG RESEARCH CENTER" + "선명리서치센터", A·B 재렌더
   - `build/epub_metadata.yaml`: creator·publisher·rights·belongs-to-collection
   - `04_metadata.md`: §1·§3-3·§7 OPF(file-as "선명리서치센터")·§8 고지 동기 갱신
2. **UUID 재사용** — `urn:uuid:e14c68a2-e3be-410d-9c95-35dcbee82762` (변경 없음)
3. **PDF 재빌드 완료 (2026-07-05 추가 지시)** — `build/book.html` 표기 치환(저자: 선명리서치센터 · eyebrow/판권지/서문 서명 갱신) 후 v1.0r2 형식 재현: cover.html(cover_b 신판) 단독 1p + 본문(여백 17/22/18mm, 머리글 좌 "알뜰폰의 다음 10년"·우 "내부 배포용 — 재배포 금지", 중앙 쪽번호 n/45) pypdf 병합. 검증: 46p, 1p 텍스트 무, 머리글 45/45, 쪽번호 45/45, 잔존 표기("이준수"·"선명그룹"·"SUNMYUNG GROUP"·"쎈터") 0건.

### v1.2 검증 결과

| 항목 | 결과 |
|---|---|
| 잔존 스캔 "이준수"·"선명그룹"·"SUNMYUNG GROUP"·"쎈터" | ✅ **0건** — EPUB 전체 XHTML/OPF/NCX |
| OPF | ✅ dc:creator="선명리서치센터(SMRC SunMyung Research Center)" · dc:publisher="선명리서치센터" · dc:rights © 갱신 · UUID 동일 |
| 표지 육안 | ✅ cover_b.png Read 검수 — 오버라인+저자 라인 정상, 배지 간섭 없음 |
