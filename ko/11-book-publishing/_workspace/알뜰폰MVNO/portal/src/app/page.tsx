import Image from "next/image";
import Link from "next/link";
import coverB from "@/assets/cover_b.png";
import AuthErrorNotice from "@/components/AuthErrorNotice";
import LoginForm from "@/components/LoginForm";
import SignOutButton from "@/components/SignOutButton";
import { getViewer } from "@/lib/auth";

export const dynamic = "force-dynamic";

const SHORT_INTRO =
  "2025년 6월 1,011만 회선으로 정점을 찍고 열 달 만에 사상 첫 연속 순유출을 맞은 한국 알뜰폰 시장. 산업 구조·경쟁 참가자·소비자·트렌드를 공개 데이터로 해부하고, 독립계 사업자 사례 연구로 “1,000만 회선 이후”의 생존 조건 7가지와 3단계 로드맵을 제시하는 내부 시장 분석서.";

export default async function HomePage() {
  const viewer = await getViewer();

  return (
    <>
      <header className="topbar">
        <div className="brand">
          알뜰폰의 다음 10년 — 내부 열람 포털
          <small>선명리서치쎈터 · Internal Only</small>
        </div>
        <nav>
          {viewer.state === "authorized" && (
            <>
              <Link href="/read" className="btn btn-teal">
                열람하기
              </Link>
              <SignOutButton variant="ghost-light" />
            </>
          )}
          {viewer.state === "unauthorized" && (
            <SignOutButton variant="ghost-light" />
          )}
        </nav>
      </header>

      <section className="hero">
        <div className="cover-wrap">
          <Image
            src={coverB}
            alt="알뜰폰의 다음 10년 표지 (B안 — 오프화이트·틸 미니멀)"
            priority
            placeholder="empty"
          />
        </div>

        <div>
          <p className="eyebrow">SMAG-RES-2026-MVNO-01 · 내부 한정</p>
          <h1>알뜰폰의 다음 10년 — 1,000만 회선 이후의 생존 전략</h1>
          <p className="subtitle">
            한국 MVNO 시장의 성숙, 참가자, 소비자, 그리고 독립계의 생존 조건
            <br />
            공인회계사 이준수 · 선명리서치쎈터 · 2026년 7월 (내부 배포판 v1.1)
          </p>

          <div className="intro">{SHORT_INTRO}</div>

          {viewer.state === "unconfigured" && (
            <div className="notice-env">
              <strong>환경변수 미설정 안내</strong>
              <br />
              Supabase 연결 정보가 아직 설정되지 않아 로그인·열람 기능이
              비활성화되어 있습니다. 프로젝트 루트에 <code>.env.local</code>{" "}
              파일을 만들고 <code>NEXT_PUBLIC_SUPABASE_URL</code>,{" "}
              <code>NEXT_PUBLIC_SUPABASE_ANON_KEY</code>,{" "}
              <code>SUPABASE_SERVICE_ROLE_KEY</code> 를 입력한 뒤 서버를 다시
              시작해 주세요. (<code>.env.example</code> 참고)
            </div>
          )}

          {viewer.state === "anonymous" && (
            <>
              <AuthErrorNotice />
              <div className="card">
                <h2>임직원 로그인</h2>
                <p className="hint">
                  허가된 임직원 이메일로 1회용 로그인 링크와 6자리 코드를 함께
                  보내 드립니다. 별도 비밀번호는 없습니다.
                </p>
                <LoginForm />
              </div>
            </>
          )}

          {viewer.state === "unauthorized" && (
            <div className="card">
              <h2>열람 권한 확인 필요</h2>
              <p className="hint">
                <strong>{viewer.email}</strong> 계정은 로그인되었지만 아직 열람
                허가 목록에 없습니다. 발행 주체(선명리서치쎈터)에 열람 승인을
                요청해 주세요.
              </p>
              <div className="actions-row">
                <Link href="/denied" className="btn btn-outline">
                  안내 보기
                </Link>
              </div>
            </div>
          )}

          {viewer.state === "authorized" && (
            <div className="card">
              <h2>열람 및 다운로드</h2>
              <p className="signed-in-as">
                <strong>{viewer.email}</strong> 님으로 로그인됨 — 열람 기록이
                계정 단위로 남습니다.
              </p>
              <div className="actions-row">
                <Link href="/read" className="btn btn-teal">
                  웹에서 열람
                </Link>
                <a href="/api/download?f=epub" className="btn btn-navy">
                  EPUB 다운로드
                </a>
                <a href="/api/download?f=pdf" className="btn btn-navy">
                  PDF 다운로드
                </a>
              </div>
            </div>
          )}
        </div>
      </section>

      <section className="policy">
        <div className="card">
          <h2>재배포 금지 고지 (접근 정책 §5)</h2>
          <ol>
            <li>
              파일의 외부 전송(개인 이메일·메신저·클라우드 업로드)을 금합니다.
            </li>
            <li>전체·부분 복제 후 외부 공유를 금합니다.</li>
            <li>
              본문 수치·문장의 외부 인용은 발행 주체의 사전 동의가 필수입니다.
            </li>
            <li>사내 재공유도 허용 독자 범위 내에서만 가능합니다.</li>
          </ol>
        </div>
      </section>
    </>
  );
}
