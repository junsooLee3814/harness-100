import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // 다중 lockfile 경고 방지 — 워크스페이스 루트를 이 앱으로 고정
  outputFileTracingRoot: __dirname,
  // 책 본문은 src/content/book.generated.ts 로 번들에 포함되므로
  // 별도 파일 트레이싱이 필요 없다. public/ 에는 어떤 책 자산도 두지 않는다.
  poweredByHeader: false,
};

export default nextConfig;
