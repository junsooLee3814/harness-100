# -*- coding: utf-8 -*-
"""build_reading_html — md 원고 전량을 단일 '열람본' HTML로 합쳐 재생성한다.

사용:  PYTHONUTF8=1 python build_reading_html.py <workspace/{법률명} 폴더> [책 제목] [파일명 stem]
입력:  <폴더>/chapters/*.md              — 파일명 앞 숫자 순으로 전량
       <폴더>/04_examples/*/cases.json   — 계산 사례 수 집계 (선택)
출력:  <폴더>/{stem}_열람본.html
       stem 인자가 없으면 폴더에 이미 있는 *_열람본.html 파일명을 그대로 덮어쓴다.

조판본(build_book.py)이 인쇄용 신국판이라면 이쪽은 화면 열람용이다.
디자인은 2026-08-13 수동 제작본의 <head>를 그대로 이식했다 — CSS 변수·파스텔 5색·
좌측 고정 nav·cover·표·blockquote·.vreq 배지 전부 원본 그대로다. 맨 아래 '확장' 블록만
덧붙였는데, 절(##) 하위목차와 콜아웃 박스에 필요한 규칙뿐이며 색은 원본에 이미 선언된
--f0~--f4 파스텔 변수만 쓴다.

원고는 읽기만 한다. 이 스크립트는 렌더링 전용이다.
"""
import sys, os, re, glob, json, html as _h
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE = sys.argv[1] if len(sys.argv) > 1 else "."
TITLE = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(os.path.normpath(BASE)) + " 실무서"
CH_DIR = os.path.join(BASE, "chapters")

# 출력 파일명 — ① 3번째 인자  ② 폴더에 이미 있는 *_열람본.html  ③ 책 제목
if len(sys.argv) > 3:
    OUT = os.path.join(BASE, sys.argv[3] + "_열람본.html")
else:
    _exist = sorted(glob.glob(os.path.join(BASE, "*_열람본.html")))
    OUT = _exist[0] if _exist else os.path.join(BASE, TITLE + "_열람본.html")

# ---------- 원고 로드
def chno_of(path):
    m = re.match(r"(\d+)", os.path.basename(path))
    return int(m.group(1)) if m else 9999

files = sorted(glob.glob(os.path.join(CH_DIR, "*.md")), key=chno_of)
if not files:
    print("ERROR: %s 에 md 원고 없음" % CH_DIR)
    sys.exit(2)

# ---------- 인라인 서식
VREQ_RE = re.compile(r"\[검증필요([^\]]*)\]")

def inline(s):
    """한 줄의 md 인라인 문법 → html. HTML 이스케이프를 먼저 하고 마크업을 심는다."""
    s = _h.escape(s, quote=False)
    s = VREQ_RE.sub(lambda m: '<span class="vreq">⚠ 검증필요' + m.group(1) + "</span>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\*\w])\*(?!\s)([^*\n]+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
    return s

def plain(s, limit=None):
    """nav 라벨용 — 마크업 제거 + 길면 말줄임."""
    s = re.sub(r"[*`]", "", s).strip()
    if limit and len(s) > limit:
        s = s[:limit - 1].rstrip() + "…"
    return _h.escape(s, quote=False)

def callout_class(raw):
    """인용 블록의 성격 판정 — 색은 전부 원본 head에 선언된 파스텔 변수."""
    head = raw[:40]
    if "💡" in head:
        return "tip"
    if "⚠" in head:
        return "warn"
    if "가상의 사례" in raw[:24]:
        return "case"
    if "이 장에서 다루는 것" in head:
        return "intro"
    if "개정 예고" in head or "개정예고" in head:
        return "rev"
    return ""

# ---------- md → html (블록 파서)
def md_to_html(md, chid):
    """본문 md → (html, [(절 앵커, 절 제목)])"""
    out, secs = [], []
    tbl, ul, ol, bq = [], [], [], []
    pre = None

    def flush_tbl():
        if not tbl:
            return
        if len(tbl) >= 2:
            hdr = [c.strip() for c in tbl[0].strip().strip("|").split("|")]
            t = "<div class='tw'><table><tr>" + "".join("<th>%s</th>" % inline(h) for h in hdr) + "</tr>"
            for row in tbl[2:]:
                cells = [c.strip() for c in row.strip().strip("|").split("|")]
                t += "<tr>" + "".join("<td>%s</td>" % inline(c) for c in cells) + "</tr>"
            out.append(t + "</table></div>")
        else:  # 구분선 없는 1줄짜리는 표가 아니다
            out.append("<p>%s</p>" % inline(tbl[0]))
        del tbl[:]

    def flush_ul():
        if ul:
            out.append("<ul>" + "".join("<li>%s</li>" % inline(x) for x in ul) + "</ul>")
            del ul[:]

    def flush_ol():
        if ol:
            out.append("<ol>" + "".join("<li>%s</li>" % inline(x) for x in ol) + "</ol>")
            del ol[:]

    def flush_bq():
        if bq:
            cls = callout_class(" ".join(bq))
            body = "<br>".join(inline(x) for x in bq)
            attr = (" class='%s'" % cls) if cls else ""
            out.append("<blockquote%s>%s</blockquote>" % (attr, body))
            del bq[:]

    def flush_all():
        flush_tbl(); flush_ul(); flush_ol(); flush_bq()

    for ln in md.splitlines():
        s = ln.rstrip()

        # 코드블록 — 내부는 원문 그대로 (ASCII 도표가 많다)
        if pre is not None:
            if s.strip().startswith("```"):
                out.append("<pre>" + _h.escape("\n".join(pre)) + "</pre>")
                pre = None
            else:
                pre.append(ln)
            continue
        if s.strip().startswith("```"):
            flush_all(); pre = []
            continue

        if s.startswith("|"):
            flush_ul(); flush_ol(); flush_bq()
            tbl.append(s)
            continue

        if s.startswith(">"):
            flush_tbl(); flush_ul(); flush_ol()
            bq.append(s.lstrip(">").strip())
            continue

        flush_tbl(); flush_bq()

        h = re.match(r"^(#{1,6})\s+(.*)$", s)
        if h:
            flush_ul(); flush_ol()
            title = h.group(2).strip()
            if len(h.group(1)) <= 2:          # ## 절 → 좌측 목차에 실린다
                sid = "%s-s%d" % (chid, len(secs) + 1)
                secs.append((sid, title))
                out.append("<h2 id='%s'>%s</h2>" % (sid, inline(title)))
            else:
                out.append("<h3>%s</h3>" % inline(title))
        elif re.match(r"^[-*+] ", s):
            flush_ol()
            ul.append(re.sub(r"^\[[ xX]\]\s*", "☐ ", s[2:]))
        elif re.match(r"^\d+\. ", s):
            flush_ul()
            ol.append(re.sub(r"^\d+\.\s*", "", s))
        elif not s.strip() or re.match(r"^(---+|\*\*\*+|___+)$", s.strip()) or s.lstrip().startswith("<!--"):
            flush_ul(); flush_ol()
        elif s.startswith("⚠️") or s.startswith("⚠") or s.startswith("💡"):
            # 인용부호 없이 본문에 놓인 주의·팁 문단도 콜아웃 박스로 통일한다
            flush_ul(); flush_ol()
            out.append("<blockquote class='%s'>%s</blockquote>"
                       % ("tip" if s.startswith("💡") else "warn", inline(s)))
        else:
            flush_ul(); flush_ol()
            out.append("<p>%s</p>" % inline(s))

    flush_all()
    return "".join(out), secs

# ---------- 본문 조립
chapters, nav_parts, body_parts = [], [], []
total_chars = 0
n_secs = 0

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    total_chars += len(text)
    lines = text.splitlines()
    if lines and lines[0].lstrip().startswith("# "):
        ch_title = re.sub(r"^#\s*", "", lines[0]).strip()
        rest = lines[1:]
    else:
        ch_title = os.path.splitext(os.path.basename(path))[0]
        rest = lines
    no = chno_of(path)
    chid = "ch%02d" % no
    body, secs = md_to_html("\n".join(rest), chid)
    n_secs += len(secs)
    chapters.append((no, ch_title))

    body_parts.append("<div class='ch' id='%s'><h1 class='cht'>%s</h1>%s</div>"
                      % (chid, inline(ch_title), body))
    nav_parts.append("<div class='navch'><a class='navtop' href='#%s'>%s</a>%s</div>"
                     % (chid, plain(ch_title, 38),
                        "".join("<a class='navsec' href='#%s'>%s</a>" % (sid, plain(st, 30))
                                for sid, st in secs)))

nav_html = "".join(nav_parts)

# ---------- 통계
n_vreq = sum(1 for _ in re.finditer(r'<span class="vreq">', "".join(body_parts)))
n_body_ch = sum(1 for no, _ in chapters if no < 90)
n_apx = len(chapters) - n_body_ch

n_cases = 0
for cp in sorted(glob.glob(os.path.join(BASE, "04_examples", "*", "cases.json"))):
    try:
        with open(cp, "r", encoding="utf-8") as f:
            d = json.load(f)
        n_cases += len(d.get("cases", [])) if isinstance(d, dict) else len(d)
    except (OSError, ValueError) as e:
        print("  경고: %s 읽기 실패 (%s)" % (os.path.basename(os.path.dirname(cp)), e))

now = datetime.now().strftime("%Y-%m-%d %H:%M")
sub = "전 %d장" % n_body_ch + (" + 부록" if n_apx else "")

# ---------- 서식 — 2026-08-13 수동 제작본 <head> 원본 그대로 (아래 '확장' 블록만 추가)
CSS = """
:root{--ink:#19223C;--text:#37415C;--muted:#6C748C;--bg:#F3F5FB;--line:#E6E9F2;
--navy:#16386E;--navy-bg:#EAF1FB;--navy-bd:#C8DAF1;
--f0-bg:#EAF2FE;--f0-ac:#3D7BEA;--f0-dp:#1B4DA0;--f1-bg:#FCEBDA;--f1-ac:#EA6A17;--f1-dp:#A8500F;
--f2-bg:#F1EAFB;--f2-ac:#875AD2;--f2-dp:#653A9F;--f3-bg:#FBF3D9;--f3-ac:#D2A11C;--f3-dp:#8A6912;
--f4-bg:#E6F5EE;--f4-ac:#2C9F70;--f4-dp:#1C744E;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-size:15.5px;line-height:1.75;
font-family:"Pretendard Variable",Pretendard,-apple-system,"Malgun Gothic",sans-serif}
.wrap{display:flex;max-width:1280px;margin:0 auto;gap:0}
nav{width:270px;flex:none;position:sticky;top:0;height:100vh;overflow-y:auto;
background:#fff;border-right:1px solid var(--line);padding:18px 14px}
nav h2{font-size:13px;color:var(--navy);margin:14px 0 6px;letter-spacing:.05em}
nav a{display:block;font-size:13px;color:var(--text);text-decoration:none;
padding:3px 8px;border-radius:6px;margin-bottom:1px}
nav a:hover{background:var(--navy-bg);color:var(--navy)}
main{flex:1;min-width:0;padding:30px 40px 100px;background:#fff}
.cover{background:var(--navy-bg);border:1px solid var(--navy-bd);border-radius:16px;
padding:28px 30px;margin-bottom:26px}
.cover h1{font-size:32px;color:var(--navy);margin:0 0 8px;font-weight:800}
.cover p{color:var(--muted);margin:4px 0}
.badge{display:inline-block;background:#FDEEE6;border:1px solid #F8D6C5;color:#B0512B;
border-radius:10px;padding:8px 12px;font-size:12.5px;font-weight:600;margin-top:10px}
.ch{margin:44px 0;border-top:3px solid var(--navy-bg);padding-top:8px}
h1.cht{font-size:24px;color:var(--navy);font-weight:800;margin:12px 0}
h2{font-size:18px;font-weight:800;margin:26px 0 10px;padding-left:10px;border-left:4px solid var(--f0-ac);color:var(--f0-dp)}
h3{font-size:15.5px;font-weight:800;color:var(--ink);margin:18px 0 8px}
blockquote{background:var(--navy-bg);border:1px solid var(--navy-bd);border-radius:10px;
padding:10px 16px;margin:12px 0;color:var(--navy);font-size:14.5px}
table{border-collapse:collapse;width:100%;font-size:13.5px;margin:10px 0}
th{background:var(--f0-ac);color:#fff;padding:7px 11px;text-align:left}
td{padding:6px 11px;border-top:1px solid var(--line);vertical-align:top}
tr:nth-child(even) td{background:#FAFBFE}
ul{padding-left:20px}
li{margin-bottom:4px}
code{background:#F0F2F8;padding:1px 5px;border-radius:5px;font-size:13px}
pre{background:#F7F8FC;border:1px solid var(--line);border-radius:10px;padding:12px 16px;
overflow-x:auto;font-size:13px;line-height:1.6}
strong{color:var(--ink)}
.vreq{background:#FDEEE6;border:1px solid #F8D6C5;color:#B0512B;border-radius:6px;
padding:1px 7px;font-weight:700;font-size:13px}
.topbtn{position:fixed;bottom:24px;right:24px;background:var(--navy);color:#fff;
border-radius:999px;padding:10px 16px;font-size:13px;text-decoration:none}
@media print{nav,.topbtn{display:none}main{padding:0}.ch{break-before:page}
*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
@media (max-width:900px){nav{display:none}main{padding:20px}}
/* ===== 확장 — 절 하위목차·콜아웃·번호목록. 색은 위 --f0~--f4 그대로 ===== */
nav .navch{margin:0 0 7px;padding-bottom:5px;border-bottom:1px solid var(--line)}
nav a.navtop{font-weight:700;color:var(--ink);line-height:1.45}
nav a.navsec{font-size:12px;color:var(--muted);padding:2px 8px 2px 19px;line-height:1.45}
nav a.navsec:hover{background:var(--f0-bg);color:var(--f0-dp)}
.cover .stat{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 4px}
.cover .stat span{background:#fff;border:1px solid var(--navy-bd);border-radius:10px;
padding:7px 14px;font-size:12px;color:var(--muted);text-align:center;min-width:96px}
.cover .stat b{display:block;font-size:18px;color:var(--navy);font-weight:800;line-height:1.35}
.tw{overflow-x:auto;margin:10px 0}
.tw table{margin:0}
ol{padding-left:22px;margin:10px 0}
blockquote.tip{background:var(--f4-bg);border-color:#BCE3D2;color:var(--f4-dp)}
blockquote.warn{background:var(--f1-bg);border-color:#F3C9A8;color:var(--f1-dp)}
blockquote.case{background:var(--f2-bg);border-color:#DBCBF3;color:var(--f2-dp)}
blockquote.intro{background:var(--f0-bg);border-color:#C3D9F8;color:var(--f0-dp)}
blockquote.rev{background:var(--f3-bg);border-color:#EDD79B;color:var(--f3-dp)}
blockquote.tip strong,blockquote.warn strong,blockquote.case strong,
blockquote.intro strong,blockquote.rev strong{color:inherit}
blockquote code{background:rgba(255,255,255,.65)}
em{font-style:italic;color:var(--muted)}
"""

doc = """<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s — 열람본</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>%(css)s</style></head>
<body><div class="wrap">
<nav><h2>목차</h2>%(nav)s</nav>
<main id="top">
<div class="cover"><h1>%(title)s</h1>
<p>일반인·실무자 이원 독자용 — %(sub)s (2026년 시행 법령 기준)</p>
<p>검토용 열람본 · <span class="vreq">⚠ 검증필요</span> 표시 %(vreq)d건은 「원문대조_작업표.xlsx」와 연동</p>
<div class="stat"><span><b>%(nch)d</b>장(부록 포함)</span><span><b>%(chars)s</b>자</span>\
<span><b>%(secs)d</b>절</span><span><b>%(cases)d</b>계산 사례</span>\
<span><b>%(vreq)d</b>검증필요</span><span><b>%(now)s</b>생성</span></div>
<span class="badge">본 원고는 감수 전 검토본이며 세무·법률 자문을 대체하지 않습니다. 외부 배포 금지.</span></div>
%(body)s
</main></div><a class="topbtn" href="#top">↑ 맨 위로</a></body></html>""" % {
    "title": _h.escape(TITLE, quote=False),
    "css": CSS,
    "nav": nav_html,
    "sub": sub,
    "nch": len(chapters),
    "chars": format(total_chars, ","),
    "secs": n_secs,
    "cases": n_cases,
    "vreq": n_vreq,
    "now": now,
    "body": "".join(body_parts),
}

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(doc)

print("OK: %s" % OUT)
print("  장 %d개(본문 %d + 부록 %d) · 절 %d개" % (len(chapters), n_body_ch, n_apx, n_secs))
print("  원고 글자수 %s자 · 계산 사례 %d건 · [검증필요] %d건" % (format(total_chars, ","), n_cases, n_vreq))
print("  출력 %s KB" % format(os.path.getsize(OUT) // 1024, ","))
