import { createServerClient, type CookieOptions } from "@supabase/ssr";
import { cookies } from "next/headers";
import { supabaseEnv } from "@/lib/env";

/**
 * 서버 컴포넌트/라우트 핸들러용 Supabase 클라이언트 (요청 쿠키 기반, 런타임 lazy 생성).
 * env 미설정 시 null 반환 — 호출부에서 graceful 처리.
 */
export async function createSupabaseServerClient() {
  const { url, anonKey, configured } = supabaseEnv();
  if (!configured) return null;

  const cookieStore = await cookies();
  return createServerClient(url!, anonKey!, {
    cookies: {
      getAll() {
        return cookieStore.getAll();
      },
      setAll(
        cookiesToSet: { name: string; value: string; options: CookieOptions }[],
      ) {
        try {
          cookiesToSet.forEach(({ name, value, options }) =>
            cookieStore.set(name, value, options),
          );
        } catch {
          // 서버 컴포넌트에서 호출된 경우 쿠키 쓰기가 불가 — 미들웨어가 세션을 갱신하므로 무시 가능
        }
      },
    },
  });
}
