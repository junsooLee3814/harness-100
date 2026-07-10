# 알뜰폰의 다음 10년 — 내부 제한 열람 포털

『알뜰폰의 다음 10년 — 1,000만 회선 이후의 생존 전략』(선명리서치쎈터, 내부 배포판 v1.1)을
**허가된 임직원만 이메일 매직링크 로그인 후 열람·다운로드**할 수 있는 웹 포털.

- 인프라: Vercel(팀 `smb-investments-projects`) + Supabase
- **운영 URL**: https://ebook-portal-mvno.vercel.app (2026-07-05 프로비저닝 완료 — 상세는 `.provisioning_notes.md`, 로컬 전용)
- 스택: Next.js 15 App Router + TypeScript + `@supabase/ssr` + `@supabase/supabase-js`
- 문서 등급: 내부 한정(Internal Only) — 재배포 금지 · 정보 제공 목적이며 투자 권유가 아님

## 동작 구조

| 경로 | 역할 |
|---|---|
| `/` | 표지 B안 + 150자 소개 + 매직링크 로그인 폼. 로그인·허가 상태에 따라 열람/다운로드 버튼 표시. env 미설정 시 안내 배너 |
| `/read` | 열람 셸(서버 컴포넌트에서 세션 + allowlist 검사) → `/api/book` iframe |
| `/api/book` | 책 본문 HTML 서빙 라우트 핸들러. 본문은 `public/`이 아닌 서버 번들 문자열(`src/content/book.generated.ts`)로만 존재하며, 요청마다 세션 + `allowed_readers` 재확인 후 `no-store`로 반환 |
| `/api/download?f=epub\|pdf` | 세션 + allowlist 재확인 → private `ebooks` 버킷 60초 서명 URL 생성 → 302 redirect |
| `/auth/callback` | 매직링크 콜백 (PKCE `code` / `token_hash` 모두 지원) |
| `/denied` | 미허가 계정 안내 페이지 |

접근 판정(`src/lib/auth.ts`): 로그인 세션 확인 후, **사용자 자신의 세션(anon key + RLS)** 으로
`allowed_readers`를 조회한다. RLS가 본인 이메일 행만 select 허용하므로 행이 조회되면 곧 허가.
쓰기(허가 추가/삭제)는 service role 전용.

## 로컬 개발

```bash
npm install
cp .env.example .env.local   # 값 입력 (없어도 dev/build 는 동작 — 홈에 미설정 안내 표시)
npm run dev
```

책 본문(`../build/book.html`)이 개정되면:

```bash
npm run extract:book   # src/content/book.generated.ts 재생성 후 커밋
```

## 배포 절차 (처음부터 끝까지)

### 1. Supabase 프로젝트 생성

1. https://supabase.com/dashboard → New project (리전: Northeast Asia 권장)
2. Project Settings > API 에서 3개 값 확보:
   - Project URL → `NEXT_PUBLIC_SUPABASE_URL`
   - anon public key → `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - service_role key → `SUPABASE_SERVICE_ROLE_KEY` (서버 전용, 절대 노출 금지)
3. Authentication > Providers > Email: **Email OTP/매직링크 활성** (기본값), 비밀번호 로그인 불필요
4. Authentication > URL Configuration:
   - Site URL: 배포 도메인 (예: `https://mvno-portal.vercel.app`)
   - Redirect URLs: `https://<배포 도메인>/auth/callback`, `http://localhost:3000/auth/callback`

### 2. 마이그레이션 (allowed_readers 테이블 + RLS)

Supabase Dashboard > SQL Editor 에 `supabase/migrations/001_allowed_readers.sql` 내용을 붙여 실행.
(또는 Supabase CLI: `supabase link --project-ref <ref>` 후 `supabase db push`)

### 3. 전자책 업로드 + 열람 허가자 등록

```bash
# .env.local 에 3개 env 입력 후:
npm run upload:ebooks              # private ebooks 버킷 생성 + v1.1 EPUB/PDF 업로드
npm run add:reader -- reader@sunmyung.kr   # 허가 이메일 추가 (여러 개 나열 가능)
```

### 4. Vercel 환경변수 설정 + 배포

```bash
vercel link --scope smb-investments-projects   # 프로젝트 연결 (최초 1회)

vercel env add NEXT_PUBLIC_SUPABASE_URL production
vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY production
vercel env add SUPABASE_SERVICE_ROLE_KEY production   # Sensitive 로 저장됨

vercel --prod --scope smb-investments-projects
```

배포 후 Supabase URL Configuration 의 Site URL/Redirect URLs 를 실제 도메인으로 갱신.

### 5. 배포 후 점검 체크리스트

- [ ] 비로그인 상태에서 `/read`, `/api/book`, `/api/download?f=pdf` 접근 시 차단(리다이렉트/401) 확인
- [ ] 허가 목록에 **없는** 이메일로 로그인 → `/denied` (접근 권한 없음) 확인
- [ ] 허가 이메일로 로그인 → 열람 + EPUB/PDF 다운로드(60초 서명 URL) 확인
- [ ] 모든 페이지 하단 고지문 노출 확인: "내부 배포용 — 재배포 금지 · 정보 제공 목적이며 투자 권유가 아님"

## 보안 메모

- `SUPABASE_SERVICE_ROLE_KEY` 는 서버 라우트(`/api/download`)와 프로비저닝 스크립트에서만 사용. 클라이언트 번들에 포함되지 않음
- `ebooks` 버킷은 private — 접근 경로는 60초 만료 서명 URL 뿐
- 책 본문·파일은 `public/` 에 일절 두지 않음 (표지 이미지는 비민감 자산으로 정적 임포트)
- 매직링크로 누구나 계정 생성은 가능하지만, `allowed_readers` 에 없으면 콘텐츠 접근 전면 차단
- 열람 로그: Supabase Auth 로그(로그인 기록) + Vercel 액세스 로그로 계정 단위 추적 (04_metadata §5 "열람 기록" 정책 대응)
