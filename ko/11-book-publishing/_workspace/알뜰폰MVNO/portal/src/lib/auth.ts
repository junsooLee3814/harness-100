import { createSupabaseServerClient } from "@/lib/supabase/server";

export type Viewer =
  | { state: "unconfigured" }
  | { state: "anonymous" }
  | { state: "unauthorized"; email: string }
  | { state: "authorized"; email: string };

/**
 * 현재 요청의 열람 자격을 판정한다.
 * 1) Supabase env 미설정 → unconfigured
 * 2) 로그인 세션 없음 → anonymous
 * 3) 로그인했으나 allowed_readers 에 이메일 없음 → unauthorized
 * 4) allowlist 통과 → authorized
 *
 * allowlist 조회는 사용자 자신의 세션(anon key + RLS)으로 수행한다.
 * RLS 정책상 본인 이메일 행만 select 가능하므로, 행이 조회되면 곧 허가된 것.
 */
export async function getViewer(): Promise<Viewer> {
  const supabase = await createSupabaseServerClient();
  if (!supabase) return { state: "unconfigured" };

  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user || !user.email) return { state: "anonymous" };

  const { data: row, error } = await supabase
    .from("allowed_readers")
    .select("email")
    .ilike("email", user.email)
    .maybeSingle();

  if (error || !row) return { state: "unauthorized", email: user.email };
  return { state: "authorized", email: user.email };
}
