import Link from "next/link";
import { redirect } from "next/navigation";
import SignOutButton from "@/components/SignOutButton";
import { getViewer } from "@/lib/auth";

export const dynamic = "force-dynamic";
export const metadata = { title: "열람 — 알뜰폰의 다음 10년" };

export default async function ReadPage() {
  const viewer = await getViewer();

  if (viewer.state === "unconfigured" || viewer.state === "anonymous") {
    redirect("/");
  }
  if (viewer.state === "unauthorized") {
    redirect("/denied");
  }

  return (
    <div className="read-shell">
      <header className="topbar">
        <div className="brand">
          알뜰폰의 다음 10년
          <small>내부 배포판 v1.1 · {viewer.email} 열람 중</small>
        </div>
        <nav>
          <span className="watermark-note">
            열람 기록이 계정 단위로 저장됩니다
          </span>
          <a href="/api/download?f=epub" className="btn btn-ghost-light">
            EPUB
          </a>
          <a href="/api/download?f=pdf" className="btn btn-ghost-light">
            PDF
          </a>
          <Link href="/" className="btn btn-ghost-light">
            홈
          </Link>
          <SignOutButton variant="ghost-light" />
        </nav>
      </header>
      {/* 본문은 public/ 정적 자산이 아닌 인증 게이트 뒤 라우트 핸들러(/api/book)가 서빙 */}
      <iframe
        className="read-frame"
        src="/api/book"
        title="알뜰폰의 다음 10년 — 본문"
      />
    </div>
  );
}
