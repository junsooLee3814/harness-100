#!/usr/bin/env node
/**
 * upload_ebooks.mjs
 * private `ebooks` 버킷을 생성(존재 시 통과)하고 v1.1 EPUB/PDF 를 업로드한다.
 *
 * 필요 env: NEXT_PUBLIC_SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
 *   (.env.local 이 있으면 자동 로드)
 * 사용: node scripts/upload_ebooks.mjs
 */
import { createClient } from "@supabase/supabase-js";
import { readFileSync, existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, "..");

// .env.local 간이 로더 (의존성 없이)
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

const BUCKET = "ebooks";
const buildDir = resolve(root, "..", "build");
const TARGETS = [
  {
    local: resolve(buildDir, "알뜰폰의_다음_10년_internal_v1.1.epub"),
    key: "mvno-next-10y_internal_v1.1.epub",
    contentType: "application/epub+zip",
  },
  {
    local: resolve(buildDir, "알뜰폰의_다음_10년_internal_v1.1.pdf"),
    key: "mvno-next-10y_internal_v1.1.pdf",
    contentType: "application/pdf",
  },
];

const admin = createClient(url, serviceKey, {
  auth: { persistSession: false, autoRefreshToken: false },
});

// 1) private 버킷 생성 (이미 있으면 통과)
{
  const { error } = await admin.storage.createBucket(BUCKET, { public: false });
  if (error && !/already exists/i.test(error.message)) {
    console.error(`버킷 생성 실패: ${error.message}`);
    process.exit(1);
  }
  console.log(`버킷 확인: ${BUCKET} (private)`);
}

// 2) 파일 업로드 (upsert)
for (const t of TARGETS) {
  if (!existsSync(t.local)) {
    console.error(`파일 없음: ${t.local}`);
    process.exit(1);
  }
  const body = readFileSync(t.local);
  const { error } = await admin.storage.from(BUCKET).upload(t.key, body, {
    contentType: t.contentType,
    upsert: true,
  });
  if (error) {
    console.error(`업로드 실패 (${t.key}): ${error.message}`);
    process.exit(1);
  }
  console.log(`업로드 완료: ${t.key} (${body.length.toLocaleString()} bytes)`);
}

console.log("완료 — /api/download 가 이 키로 60초 서명 URL 을 발급합니다.");
