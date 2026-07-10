"use client";

import { useEffect, useState } from "react";

/**
 * 매직링크 실패 안내.
 * - /auth/callback 이 붙이는 ?auth_error=... 쿼리
 * - Supabase verify 가 붙이는 #error=access_denied&error_code=otp_expired 해시
 * 둘 다 감지한다 (해시는 서버에서 볼 수 없어 클라이언트에서 처리).
 */
export default function AuthErrorNotice() {
  const [text, setText] = useState<string | null>(null);

  useEffect(() => {
    const url = new URL(window.location.href);
    const qsError = url.searchParams.get("auth_error");
    const hash = new URLSearchParams(url.hash.replace(/^#/, ""));
    const hashCode = hash.get("error_code");
    const hashError = hash.get("error");

    if (qsError) {
      setText(qsError);
    } else if (hashCode === "otp_expired") {
      setText(
        "로그인 링크가 이미 사용되었거나 만료되었습니다. (메일 보안 프로그램이 링크를 먼저 열어 소모하는 경우가 있습니다)",
      );
    } else if (hashError) {
      setText("로그인 링크 처리 중 오류가 발생했습니다.");
    }

    // 주소창 정리 (새로고침 시 반복 표시 방지)
    if (qsError || hashError || hashCode) {
      window.history.replaceState(null, "", url.pathname);
    }
  }, []);

  if (!text) return null;

  return (
    <div className="auth-error" role="alert">
      <strong>로그인 링크 오류</strong>
      <br />
      {text}
      <br />
      아래 로그인 폼에서 <strong>“코드 입력”</strong>으로 다시 시도해 주세요 —
      메일에 표시된 6자리 코드를 입력하면 링크 없이 로그인됩니다.
    </div>
  );
}
