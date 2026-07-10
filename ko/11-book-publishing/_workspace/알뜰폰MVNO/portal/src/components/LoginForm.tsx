"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { getSupabaseBrowserClient } from "@/lib/supabase/client";

type Step = "request" | "verify";

export default function LoginForm() {
  const router = useRouter();
  const [step, setStep] = useState<Step>("request");
  const [email, setEmail] = useState("");
  const [code, setCode] = useState("");
  const [busy, setBusy] = useState(false);
  const [sentOnce, setSentOnce] = useState(false);
  const [message, setMessage] = useState<
    { kind: "ok" | "err"; text: string } | null
  >(null);

  async function requestLink(e: React.FormEvent) {
    e.preventDefault();
    const supabase = getSupabaseBrowserClient();
    if (!supabase) {
      setMessage({
        kind: "err",
        text: "환경변수가 설정되지 않아 로그인을 사용할 수 없습니다.",
      });
      return;
    }
    setBusy(true);
    setMessage(null);

    const siteUrl =
      process.env.NEXT_PUBLIC_SITE_URL || window.location.origin;
    const { error } = await supabase.auth.signInWithOtp({
      email: email.trim(),
      options: {
        emailRedirectTo: `${siteUrl}/auth/callback?next=/read`,
        shouldCreateUser: true,
      },
    });
    setBusy(false);

    if (error) {
      setMessage({
        kind: "err",
        text: `메일 발송에 실패했습니다: ${error.message}`,
      });
    } else {
      setSentOnce(true);
      setStep("verify");
      setMessage({
        kind: "ok",
        text: "로그인 메일을 보냈습니다. 메일의 로그인 링크를 클릭하거나, 메일에 표시된 6자리 코드를 아래에 입력하세요. 링크가 만료됐다는 오류가 나오면 코드 입력을 사용하세요.",
      });
    }
  }

  async function verifyCode(e: React.FormEvent) {
    e.preventDefault();
    const supabase = getSupabaseBrowserClient();
    if (!supabase) {
      setMessage({
        kind: "err",
        text: "환경변수가 설정되지 않아 로그인을 사용할 수 없습니다.",
      });
      return;
    }
    setBusy(true);
    setMessage(null);

    const { error } = await supabase.auth.verifyOtp({
      email: email.trim(),
      token: code.trim(),
      type: "email",
    });
    setBusy(false);

    if (error) {
      setMessage({
        kind: "err",
        text: `코드 확인에 실패했습니다: ${error.message} — 코드가 만료되었으면 메일을 다시 요청해 주세요.`,
      });
    } else {
      setMessage({ kind: "ok", text: "로그인 성공 — 이동 중입니다…" });
      router.push("/read");
      router.refresh();
    }
  }

  if (step === "verify") {
    return (
      <form
        className="login-form login-form-col"
        onSubmit={verifyCode}
        aria-label="6자리 코드 입력"
      >
        <input
          type="email"
          required
          placeholder="회사 이메일 주소"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          disabled={busy}
        />
        <div className="code-row">
          <input
            type="text"
            inputMode="numeric"
            autoComplete="one-time-code"
            pattern="[0-9]{6}"
            maxLength={6}
            required
            placeholder="6자리 코드"
            value={code}
            onChange={(e) => setCode(e.target.value.replace(/\D/g, ""))}
            disabled={busy}
            aria-label="메일로 받은 6자리 코드"
          />
          <button type="submit" className="btn btn-teal" disabled={busy}>
            {busy ? "확인 중…" : "코드 확인"}
          </button>
        </div>
        <p className="code-hint">
          메일의 로그인 링크를 클릭하거나, 메일에 표시된 6자리 코드를
          입력하세요. 링크가 만료됐다는 오류가 나오면 코드 입력을 사용하세요.
        </p>
        <div className="form-links">
          <button
            type="button"
            className="linklike"
            onClick={() => {
              setStep("request");
              setCode("");
              setMessage(null);
            }}
            disabled={busy}
          >
            ← 메일 다시 요청하기
          </button>
        </div>
        {message && (
          <p
            className={`form-msg ${message.kind}`}
            role={message.kind === "err" ? "alert" : "status"}
          >
            {message.text}
          </p>
        )}
      </form>
    );
  }

  return (
    <form className="login-form" onSubmit={requestLink} aria-label="이메일 로그인">
      <input
        type="email"
        required
        placeholder="회사 이메일 주소"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        disabled={busy}
      />
      <button type="submit" className="btn btn-teal" disabled={busy}>
        {busy ? "발송 중…" : sentOnce ? "메일 다시 보내기" : "로그인 메일 받기"}
      </button>
      <div className="form-links">
        <button
          type="button"
          className="linklike"
          onClick={() => {
            setMessage(null);
            setStep("verify");
          }}
          disabled={busy}
        >
          이미 메일로 6자리 코드를 받으셨나요? 코드 입력 →
        </button>
      </div>
      {message && (
        <p
          className={`form-msg ${message.kind}`}
          role={message.kind === "err" ? "alert" : "status"}
        >
          {message.text}
        </p>
      )}
    </form>
  );
}
