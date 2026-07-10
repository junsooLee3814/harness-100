import { NextResponse } from "next/server";
import { getViewer } from "@/lib/auth";
import { BOOK_DOCUMENT } from "@/content/book.generated";

export const dynamic = "force-dynamic";

/**
 * 책 본문 서빙 라우트 핸들러.
 * 본문 HTML 은 public/ 정적 자산이 아니라 서버 번들 내부 문자열로만 존재하며,
 * 요청마다 세션 + allowed_readers allowlist 를 재확인한 뒤에만 반환한다.
 */
export async function GET() {
  const viewer = await getViewer();

  if (viewer.state === "unconfigured") {
    return NextResponse.json(
      { error: "서버 환경변수가 설정되지 않았습니다." },
      { status: 503 },
    );
  }
  if (viewer.state === "anonymous") {
    return NextResponse.json({ error: "로그인이 필요합니다." }, { status: 401 });
  }
  if (viewer.state === "unauthorized") {
    return NextResponse.json(
      { error: "열람 권한이 없습니다. 발행 주체에 승인을 요청해 주세요." },
      { status: 403 },
    );
  }

  return new NextResponse(BOOK_DOCUMENT, {
    status: 200,
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "private, no-store",
      "X-Robots-Tag": "noindex, nofollow",
      "X-Frame-Options": "SAMEORIGIN",
    },
  });
}
