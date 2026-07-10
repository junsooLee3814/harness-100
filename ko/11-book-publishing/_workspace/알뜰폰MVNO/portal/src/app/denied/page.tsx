import Link from "next/link";

export const metadata = { title: "접근 권한 없음 — 내부 열람 포털" };

export default function DeniedPage() {
  return (
    <div className="center-page">
      <h1>접근 권한 없음</h1>
      <p>
        본 자료는 선명그룹 내부·제한 배포용으로, 발행 주체가 승인한 임직원만
        열람할 수 있습니다.
        <br />
        열람이 필요한 경우 발행 주체(선명리서치쎈터)에 열람 승인을 요청해
        주세요. 승인 후 동일한 이메일로 다시 로그인하면 열람할 수 있습니다.
      </p>
      <p>
        <Link href="/" className="btn btn-outline">
          홈으로 돌아가기
        </Link>
      </p>
    </div>
  );
}
