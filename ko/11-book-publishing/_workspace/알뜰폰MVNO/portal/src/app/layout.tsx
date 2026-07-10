import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "알뜰폰의 다음 10년 — 내부 열람 포털",
  description:
    "선명리서치쎈터 내부 배포용 전자책 제한 열람 포털. 허가된 임직원 전용.",
  robots: { index: false, follow: false },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ko">
      <head>
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css"
        />
      </head>
      <body>
        <div className="shell">
          <main>{children}</main>
          <footer className="site-footer">
            내부 배포용 — 재배포 금지 · 정보 제공 목적이며 투자 권유가 아님
            <br />© 2026 선명리서치쎈터. All rights reserved.
          </footer>
        </div>
      </body>
    </html>
  );
}
