-- 001_allowed_readers.sql
-- 내부 전자책 열람 허가 목록 (허용 독자 범위 — 04_metadata §5)
-- 실행: Supabase Dashboard > SQL Editor 또는 `supabase db push`

create table if not exists public.allowed_readers (
  email    text primary key check (email = lower(email)),
  added_at timestamptz not null default now()
);

comment on table public.allowed_readers is
  '알뜰폰의 다음 10년 내부 열람 포털 — 허가 독자 이메일 allowlist (소문자 저장)';

-- RLS: 본인 행만 select 가능. insert/update/delete 는 service role 전용
-- (service role 은 RLS 를 우회하므로 별도 쓰기 정책을 만들지 않는 것이 곧 쓰기 차단)
alter table public.allowed_readers enable row level security;

drop policy if exists "reader can see own row" on public.allowed_readers;
create policy "reader can see own row"
  on public.allowed_readers
  for select
  to authenticated
  using (lower(email) = lower(coalesce(auth.jwt() ->> 'email', '')));

-- anon 역할에는 아무 정책도 없음 → 전면 차단
