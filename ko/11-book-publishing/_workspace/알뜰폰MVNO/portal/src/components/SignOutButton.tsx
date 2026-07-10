"use client";

import { useRouter } from "next/navigation";
import { getSupabaseBrowserClient } from "@/lib/supabase/client";

export default function SignOutButton({
  variant = "outline",
}: {
  variant?: "outline" | "ghost-light";
}) {
  const router = useRouter();

  async function onClick() {
    const supabase = getSupabaseBrowserClient();
    if (supabase) await supabase.auth.signOut();
    router.push("/");
    router.refresh();
  }

  return (
    <button
      type="button"
      className={`btn ${variant === "ghost-light" ? "btn-ghost-light" : "btn-outline"}`}
      onClick={onClick}
    >
      로그아웃
    </button>
  );
}
