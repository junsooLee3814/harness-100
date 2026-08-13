# -*- coding: utf-8 -*-
"""check_edit_integrity.py — 교열 전/후 원고의 사실관계 불변 검증.

사용법:  python check_edit_integrity.py <교열 전 파일> <교열 후 파일>
exit 0 = PASS, 1 = FAIL, 2 = 사용법 오류

검사 항목:
  1) 수치 다중집합 일치 (세율·금액·날짜·기간 — 표기 변경 포함 일체 불변)
  2) 조문 인용 일치 (제N조/제N조의N/제N항/제N호/§N)
  3) 사건번호 일치 (예: 2020두12345)
  4) [검증필요] 마커 건수 일치
  5) 콜아웃(💡/⚠️)·상호참조(→) 개수 일치
  6) 글자수 ≥ 원문의 97% (분량 삭감 금지)
"""
import re
import sys
from collections import Counter
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RX = {
    "수치": re.compile(r"\d+(?:,\d{3})*(?:\.\d+)?"),
    "조문": re.compile(r"제\d+조(?:의\d+)?|제\d+항|제\d+호|§\s?\d+(?:의\d+)?"),
    "사건번호": re.compile(r"\d{2,4}[가-힣]{1,3}\d{3,6}"),
}
COUNTS = ["[검증필요", "💡", "⚠️", "→"]
MIN_LENGTH_RATIO = 0.97


def read(path):
    return Path(path).read_text(encoding="utf-8-sig")


def diff_counter(before, after):
    b, a = Counter(before), Counter(after)
    missing = b - a   # 원문에 있었는데 사라짐/변형됨
    added = a - b     # 교열본에 새로 생김
    return missing, added


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    before_raw, after_raw = read(argv[1]), read(argv[2])
    ok = True

    for name, rx in RX.items():
        missing, added = diff_counter(rx.findall(before_raw), rx.findall(after_raw))
        if missing or added:
            ok = False
            print(f"[FAIL] {name} 불일치")
            for v, n in sorted(missing.items()):
                print(f"       원문에서 사라짐: {v!r} x{n}")
            for v, n in sorted(added.items()):
                print(f"       교열본에 추가됨: {v!r} x{n}")
        else:
            print(f"[PASS] {name} 일치 ({sum(Counter(rx.findall(before_raw)).values())}건)")

    for token in COUNTS:
        nb, na = before_raw.count(token), after_raw.count(token)
        if nb != na:
            ok = False
            print(f"[FAIL] {token} 개수 변동: {nb} → {na}")
        else:
            print(f"[PASS] {token} 개수 일치 ({nb}건)")

    ratio = len(after_raw) / max(1, len(before_raw))
    if ratio < MIN_LENGTH_RATIO:
        ok = False
        print(f"[FAIL] 글자수 {len(before_raw)} → {len(after_raw)} ({ratio:.1%}) — 97% 미만, 분량 삭감 금지")
    else:
        print(f"[PASS] 글자수 {len(before_raw)} → {len(after_raw)} ({ratio:.1%})")

    print("== PASS ==" if ok else "== FAIL ==")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
