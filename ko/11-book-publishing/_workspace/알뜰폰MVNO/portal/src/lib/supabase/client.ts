"use client";

import { createBrowserClient } from "@supabase/ssr";
import { supabaseEnv } from "@/lib/env";
import type { SupabaseClient } from "@supabase/supabase-js";

let client: SupabaseClient | null = null;

/** 브라우저용 Supabase 클라이언트 (lazy 싱글턴). env 미설정 시 null. */
export function getSupabaseBrowserClient(): SupabaseClient | null {
  const { url, anonKey, configured } = supabaseEnv();
  if (!configured) return null;
  if (!client) client = createBrowserClient(url!, anonKey!);
  return client;
}
