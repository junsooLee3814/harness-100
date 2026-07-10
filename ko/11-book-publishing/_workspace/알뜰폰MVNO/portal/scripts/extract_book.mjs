#!/usr/bin/env node
/**
 * extract_book.mjs
 * ../build/book.html 전체 문서를 src/content/book.generated.ts 모듈로 변환한다.
 * 책 본문은 public/ 정적 자산이 아니라 서버 번들 내부 문자열로만 존재하며,
 * 인증을 통과한 요청에만 /api/book 라우트 핸들러가 서빙한다.
 *
 * 사용: node scripts/extract_book.mjs
 * (book.html 개정 시 재실행 후 커밋)
 */
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = resolve(here, "..", "..", "build", "book.html");
const dst = resolve(here, "..", "src", "content", "book.generated.ts");

const html = readFileSync(src, "utf-8");

// 열람 화면 고지 배너를 </body> 직전에 삽입 (04_metadata §8-3 대외 배포 금지 문구 요약)
const notice = `<div style="max-width:860px;margin:24px auto 40px;padding:14px 18px;border:1px solid #d9d3c6;border-radius:12px;background:#faf8f3;color:#5b6e88;font-size:13px;line-height:1.7;text-align:center;">내부 배포용 — 재배포 금지 · 정보 제공 목적이며 투자 권유가 아님<br/>본 자료는 선명그룹 내부·제한 배포용입니다. 허용된 독자 범위 외 제3자 전달·공개·게시를 금하며, 외부 인용은 발행처의 사전 서면 동의가 필요합니다.</div>`;
const withNotice = html.replace("</body>", `${notice}</body>`);

const out = `// 자동 생성 파일 — 직접 수정 금지. 재생성: npm run extract:book
// 원본: ../../build/book.html (${new Date().toISOString()})
export const BOOK_DOCUMENT: string = ${JSON.stringify(withNotice)};
`;

mkdirSync(dirname(dst), { recursive: true });
writeFileSync(dst, out, "utf-8");
console.log(`OK: ${dst} (${Buffer.byteLength(out)} bytes)`);
