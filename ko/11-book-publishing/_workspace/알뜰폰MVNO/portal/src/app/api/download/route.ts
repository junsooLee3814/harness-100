import { NextResponse, type NextRequest } from "next/server";
import { createClient } from "@supabase/supabase-js";
import { getViewer } from "@/lib/auth";
import { serviceRoleKey, supabaseEnv } from "@/lib/env";

export const dynamic = "force-dynamic";

const BUCKET = "ebooks";

/** Storage 오브젝트 키는 ASCII 로 두고, 다운로드 파일명만 한국어로 지정 */
const FILES: Record<string, { key: string; downloadName: string }> = {
  epub: {
    key: "mvno-next-10y_internal_v1.1.epub",
    downloadName: "알뜰폰의_다음_10년_내부배포판_v1.1.epub",
  },
  pdf: {
    key: "mvno-next-10y_internal_v1.1.pdf",
    downloadName: "알뜰폰의_다음_10년_내부배포판_v1.1.pdf",
  },
};

/**
 * GET /api/download?f=epub|pdf
 * 세션 + allowlist 재확인 → private 버킷 서명 URL(60초) 생성 → redirect.
 */
export async function GET(request: NextRequest) {
  const format = request.nextUrl.searchParams.get("f") ?? "";
  const file = FILES[format];
  if (!file) {
    return NextResponse.json(
      { error: "f 파라미터는 epub 또는 pdf 여야 합니다." },
      { status: 400 },
    );
  }

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
      { error: "다운로드 권한이 없습니다. 발행 주체에 승인을 요청해 주세요." },
      { status: 403 },
    );
  }

  const { url } = supabaseEnv();
  const serviceKey = serviceRoleKey();
  if (!url || !serviceKey) {
    return NextResponse.json(
      { error: "SUPABASE_SERVICE_ROLE_KEY 가 설정되지 않았습니다." },
      { status: 503 },
    );
  }

  // 서명 전용 — service role 클라이언트는 요청 스코프에서만 생성/사용
  const admin = createClient(url, serviceKey, {
    auth: { persistSession: false, autoRefreshToken: false },
  });

  const { data, error } = await admin.storage
    .from(BUCKET)
    .createSignedUrl(file.key, 60, { download: file.downloadName });

  if (error || !data?.signedUrl) {
    return NextResponse.json(
      {
        error:
          "서명 URL 생성에 실패했습니다. ebooks 버킷 업로드 여부를 확인해 주세요.",
        detail: error?.message,
      },
      { status: 500 },
    );
  }

  return NextResponse.redirect(data.signedUrl, { status: 302 });
}
