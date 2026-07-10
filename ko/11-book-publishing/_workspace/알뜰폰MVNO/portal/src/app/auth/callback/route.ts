import { NextResponse, type NextRequest } from "next/server";
import { createServerClient, type CookieOptions } from "@supabase/ssr";
import type { EmailOtpType } from "@supabase/supabase-js";

export const dynamic = "force-dynamic";

/**
 * 매직링크 콜백: PKCE `code` 또는 `token_hash` 를 세션으로 교환한 뒤 이동.
 */
export async function GET(request: NextRequest) {
  const { searchParams, origin } = new URL(request.url);
  const code = searchParams.get("code");
  const tokenHash = searchParams.get("token_hash");
  const type = searchParams.get("type") as EmailOtpType | null;
  const next = searchParams.get("next") ?? "/read";
  const safeNext = next.startsWith("/") && !next.startsWith("//") ? next : "/read";

  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const anonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  if (!url || !anonKey) {
    return NextResponse.redirect(`${origin}/`);
  }

  const response = NextResponse.redirect(`${origin}${safeNext}`);
  const supabase = createServerClient(url, anonKey, {
    cookies: {
      getAll() {
        return request.cookies.getAll();
      },
      setAll(
        cookiesToSet: { name: string; value: string; options: CookieOptions }[],
      ) {
        cookiesToSet.forEach(({ name, value, options }) =>
          response.cookies.set(name, value, options),
        );
      },
    },
  });

  if (code) {
    const { error } = await supabase.auth.exchangeCodeForSession(code);
    if (!error) return response;
  } else if (tokenHash && type) {
    const { error } = await supabase.auth.verifyOtp({
      type,
      token_hash: tokenHash,
    });
    if (!error) return response;
  }

  return NextResponse.redirect(
    `${origin}/?auth_error=${encodeURIComponent("로그인 링크가 이미 사용되었거나 만료되었습니다. 메일에 표시된 6자리 코드 입력으로 다시 시도해 주세요.")}`,
  );
}
