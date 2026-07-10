#!/usr/bin/env node
/**
 * add_reader.mjs <email> [email...]
 * allowed_readers allowlist 에 열람 허가 이메일을 추가한다 (service role, upsert).
 *
 * 필요 env: NEXT_PUBLIC_SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY (.env.local 자동 로드)
 * 사용: node scripts/add_reader.mjs reader@sunmyung.kr
 */
import { createClient } from "@supabase/supabase-js";
import { readFileSync, existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, "..");

const envFile = resolve(root, ".env.local");
if (existsSync(envFile)) {
  for (const line of readFileSync(envFile, "utf-8").split(/\r?\n/)) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
    if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^["']|["']$/g, "");
  }
}

const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
if (!url || !serviceKey) {
  console.error("ERROR: NEXT_PUBLIC_SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY 가 필요합니다 (.env.local).");
  process.exit(1);
}

const emails = process.argv
  .slice(2)
  .map((e) => e.trim().toLowerCase())
  .filter(Boolean);

if (emails.length === 0) {
  console.error("사용법: node scripts/add_reader.mjs <email> [email...]");
  process.exit(1);
}

const invalid = emails.filter((e) => !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e));
if (invalid.length > 0) {
  console.error(`이메일 형식 오류: ${invalid.join(", ")}`);
  process.exit(1);
}

const admin = createClient(url, serviceKey, {
  auth: { persistSession: false, autoRefreshToken: false },
});

const { error } = await admin
  .from("allowed_readers")
  .upsert(emails.map((email) => ({ email })), { onConflict: "email" });

if (error) {
  console.error(`추가 실패: ${error.message}`);
  process.exit(1);
}
console.log(`허가 목록 추가 완료 (${emails.length}건): ${emails.join(", ")}`);
