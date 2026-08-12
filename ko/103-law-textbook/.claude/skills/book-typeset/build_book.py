# -*- coding: utf-8 -*-
"""book-typeset — md 원고를 진짜 책 조판(신국판·머리글·바닥글·페이지번호·목차·색인)으로 변환.

사용:  PYTHONUTF8=1 python build_book.py <workspace/{법률명} 폴더> [책 제목]
입력:  <폴더>/chapters/*.md  +  <폴더>/06_색인어휘.txt (선택)
출력:  <폴더>/조판본/{제목}_조판본.html  (+ render_pdf.py로 PDF)

페이지 번호는 Paged.js가 조판 시 자동 부여 — 목차·색인의 페이지는
target-counter로 계산되므로 원고 수정 후 재실행만 하면 전부 갱신된다.
"""
import sys, os, re, glob, html as _h

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = sys.argv[1] if len(sys.argv) > 1 else "."
TITLE = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(os.path.normpath(BASE)) + " 실무"
CH_DIR = os.path.join(BASE, "chapters")
OUT_DIR = os.path.join(BASE, "조판본")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_H = os.path.join(OUT_DIR, f"{TITLE}_조판본.html")

# ---------- 원고 로드
files = sorted(glob.glob(os.path.join(CH_DIR, "*.md")),
               key=lambda p: int(re.match(r"(\d+)", os.path.basename(p)).group(1)))
if not files:
    print(f"ERROR: {CH_DIR} 에 md 원고 없음"); sys.exit(2)
chapters = []
for p in files:
    with open(p, "r", encoding="utf-8") as f:
        chapters.append((os.path.basename(p), f.read()))

# ---------- 색인어휘 로드
terms = []  # (표제어, [변형들 — 긴 것 우선])
ix_path = os.path.join(BASE, "06_색인어휘.txt")
if os.path.exists(ix_path):
    with open(ix_path, "r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            parts = [x.strip() for x in ln.split("|") if x.strip()]
            variants = sorted(set(parts), key=len, reverse=True)
            terms.append((parts[0], variants))

# ---------- md → html (5블록 원고 문법)
def inline(s):
    s = _h.escape(s, quote=False)
    s = re.sub(r"\[검증필요[::]?\s*([^\]]+)\]", r"<span class='vreq'>⚠ \1</span>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s

def md_body(md):
    out, tbl, lst, pre = [], [], [], None
    def ftbl():
        nonlocal tbl
        if len(tbl) >= 2:
            hdr = [c.strip() for c in tbl[0].strip("|").split("|")]
            t = "<table><tr>" + "".join(f"<th>{inline(h)}</th>" for h in hdr) + "</tr>"
            for row in tbl[2:]:
                cells = [c.strip() for c in row.strip("|").split("|")]
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>"
            out.append(t + "</table>")
        tbl = []
    def flst():
        nonlocal lst
        if lst:
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in lst) + "</ul>")
            lst = []
    for ln in md.splitlines():
        if pre is not None:
            if ln.strip().startswith("```"):
                out.append("<pre>" + _h.escape("\n".join(pre)) + "</pre>"); pre = None
            else:
                pre.append(ln)
            continue
        if ln.strip().startswith("```"):
            ftbl(); flst(); pre = []; continue
        if ln.startswith("|"):
            flst(); tbl.append(ln); continue
        ftbl()
        s = ln.rstrip()
        if s.startswith("# "):
            flst()
        elif s.startswith("## "):
            flst(); out.append(f"<h2>{inline(s[3:])}</h2>")
        elif s.startswith("### "):
            flst(); out.append(f"<h3>{inline(s[4:])}</h3>")
        elif s.startswith("> "):
            flst(); out.append(f"<blockquote>{inline(s[2:])}</blockquote>")
        elif s.startswith("- ") or s.startswith("* "):
            lst.append(re.sub(r"^\[ \]\s*", "☐ ", s[2:]))
        elif s.startswith("---") or s.startswith("<!--"):
            flst()
        elif not s.strip():
            flst()
        else:
            flst(); out.append(f"<p>{inline(s)}</p>")
    ftbl(); flst()
    return "".join(out)

# ---------- 색인 앵커 심기: 장마다 각 표제어의 첫 등장 텍스트에 <span id> 부착
ix_entries = {}  # 표제어 -> [(chno, anchor_id)]
def anchor_terms(html_str, chno):
    if not terms:
        return html_str
    segs = re.split(r"(<[^>]+>)", html_str)          # 태그/텍스트 분리 — 태그 내부 훼손 방지
    pending = {i for i in range(len(terms))}
    for si, seg in enumerate(segs):
        if not pending or seg.startswith("<") or not seg.strip():
            continue
        changed = True
        while changed and pending:
            changed = False
            best = None  # (pos, -len, term_idx, variant)
            for ti in pending:
                for v in terms[ti][1]:
                    pos = seg.find(v)
                    if pos >= 0 and (best is None or (pos, -len(v)) < (best[0], best[1])):
                        best = (pos, -len(v), ti, v)
            if best:
                pos, _, ti, v = best
                aid = f"ix{ti}-c{chno}"
                seg = seg[:pos] + f"<span id='{aid}' class='ix'>{v}</span>" + seg[pos+len(v):]
                ix_entries.setdefault(terms[ti][0], []).append((chno, aid))
                pending.discard(ti)
                changed = True
        segs[si] = seg
    return "".join(segs)

# ---------- 본문 조립
toc_rows, body_parts = [], []
for fname, text in chapters:
    chno = int(re.match(r"(\d+)", fname).group(1))
    title_full = re.sub(r"^#\s*", "", text.splitlines()[0]).strip()
    run_title = re.split(r"\s*[—-]\s*", title_full)[0].strip()  # 머리글용 축약
    aid = f"ch{chno}"
    toc_rows.append((aid, title_full))
    body_html = md_body("\n".join(text.splitlines()[1:]))
    sec_html = (
        f"<h1 class='cht'><span class='runmark'>{_h.escape(run_title)}</span>{inline(title_full)}</h1>"
        f"{body_html}")
    sec_html = anchor_terms(sec_html, chno)   # 제목 포함 전체를 스캔
    body_parts.append(f"<section class='chapter' id='{aid}'>{sec_html}</section>")

# ---------- 목차
toc_html = "".join(
    f"<div class='tocrow'><a class='t' href='#{aid}'>{inline(t)}</a>"
    f"<span class='dots'></span><a class='pg' href='#{aid}'></a></div>"
    for aid, t in toc_rows)

# ---------- 색인 (가나다 그룹)
CHO = ["ㄱ","ㄱ","ㄴ","ㄷ","ㄷ","ㄹ","ㅁ","ㅂ","ㅂ","ㅅ","ㅅ","ㅇ","ㅈ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
def group_of(word):
    c = word[0]
    if "가" <= c <= "힣":
        return CHO[(ord(c) - 0xAC00) // 588]
    return "기타"

ix_rows, cur_grp = [], None
for label in sorted(ix_entries.keys()):
    g = group_of(label)
    if g != cur_grp:
        ix_rows.append(f"<h2 class='ixgrp'>{g}</h2>"); cur_grp = g
    links = " · ".join(f"<a class='pg' href='#{aid}'></a>" for _, aid in sorted(ix_entries[label]))
    ix_rows.append(f"<div class='ixrow'><span>{_h.escape(label)}</span><span class='ixpg'>{links}</span></div>")
index_html = "".join(ix_rows)
missing = [t[0] for t in terms if t[0] not in ix_entries]

# ---------- 템플릿
CSS = """
:root{--navy:#16386E;--ink:#1E2430;--muted:#5A6272;--line:#D8DDE6;--box:#EEF3FA;--boxbd:#C9D8EC}
@page{size:152mm 225mm;margin:19mm 16mm 17mm 16mm;
 @bottom-center{content:counter(page);font-size:8.5pt;color:#666}}
@page:left{@top-left{content:"__BOOKTITLE__";font-size:8pt;color:#888;letter-spacing:.06em}}
@page:right{@top-right{content:string(chaptitle);font-size:8pt;color:#888}}
@page cover{margin:0;@top-left{content:none}@top-right{content:none}@bottom-center{content:none}}
@page front{@bottom-center{content:counter(page,lower-roman);font-size:8.5pt;color:#666}
 @top-left{content:none}@top-right{content:none}}
body{font-family:"Noto Serif KR","Batang",serif;font-size:10pt;line-height:1.72;color:var(--ink);
 string-set:booktitle "__BOOKTITLE__"}
h1,h2,h3,th,.cover,.tocrow,.ixrow,.ixgrp,blockquote strong{font-family:Pretendard,"Malgun Gothic",sans-serif}
/* 표지 */
.cover{page:cover;height:225mm;background:linear-gradient(160deg,#16386E 0%,#25518F 60%,#3D6BAE 100%);
 color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 22mm;break-after:page}
.cover .k{font-size:10pt;letter-spacing:.35em;opacity:.75;margin-bottom:8mm}
.cover h1{font-size:26pt;font-weight:800;line-height:1.35;margin:0 0 6mm}
.cover .sub{font-size:11pt;opacity:.85;line-height:1.7}
.cover .foot{position:absolute;bottom:18mm;left:22mm;right:22mm;font-size:8.5pt;opacity:.7;
 border-top:1px solid rgba(255,255,255,.3);padding-top:4mm}
/* 목차 */
.frontmatter{page:front}
.toc h1,.ixsec h1{font-size:17pt;color:var(--navy);margin:0 0 8mm;font-weight:800}
.tocrow{display:flex;align-items:baseline;font-size:9.5pt;margin-bottom:2.6mm}
.tocrow .t{color:var(--ink);text-decoration:none;max-width:78%}
.tocrow .dots{flex:1;border-bottom:1px dotted #AAB2C0;margin:0 2mm}
a.pg{color:var(--ink);text-decoration:none;white-space:nowrap}
a.pg::after{content:target-counter(attr(href),page)}
.toc{break-after:page}
/* 본문 */
.chapter{break-before:page}
h1.cht{font-size:15.5pt;color:var(--navy);font-weight:800;line-height:1.4;
 border-bottom:2.5px solid var(--navy);padding:0 0 3mm;margin:0 0 6mm}
.runmark{string-set:chaptitle content();display:none}
h2{font-size:11.5pt;font-weight:800;color:var(--navy);margin:6mm 0 2.5mm;
 padding-left:2.2mm;border-left:2.5px solid var(--navy)}
h3{font-size:10.5pt;font-weight:800;margin:4mm 0 2mm}
p{margin:0 0 2.4mm;text-align:justify}
blockquote{background:var(--box);border:1px solid var(--boxbd);border-radius:2mm;
 padding:2.5mm 4mm;margin:0 0 3mm;font-size:9.3pt;break-inside:avoid}
table{border-collapse:collapse;width:100%;font-size:8.6pt;margin:0 0 3.2mm;break-inside:auto}
th{background:var(--navy);color:#fff;padding:1.6mm 2.4mm;text-align:left;font-weight:700}
td{padding:1.4mm 2.4mm;border:.5px solid var(--line);vertical-align:top}
tr:nth-child(even) td{background:#F7F9FC}
ul{margin:0 0 2.6mm;padding-left:5mm}
li{margin-bottom:1mm}
code{font-family:Consolas,monospace;font-size:8.8pt;background:#F0F2F6;padding:0 1mm;border-radius:1mm}
pre{background:#F5F7FA;border:.5px solid var(--line);padding:2.5mm;font-size:8.5pt;
 border-radius:1.5mm;white-space:pre-wrap;break-inside:avoid}
strong{font-weight:700}
.vreq{background:#FDEBDD;border:.5px solid #F3C9A8;color:#9A4E1F;border-radius:1mm;
 padding:0 1.2mm;font-size:8.6pt;font-weight:700}
.ix{/* 색인 앵커 — 서식 변화 없음 */}
/* 색인 */
.ixsec{break-before:page}
.ixsec .cols{column-count:2;column-gap:8mm}
.ixgrp{font-size:11pt;color:var(--navy);border-bottom:1.5px solid var(--navy);
 margin:3.5mm 0 2mm;padding-bottom:.8mm;break-after:avoid}
.ixrow{display:flex;justify-content:space-between;font-size:8.8pt;margin-bottom:1.1mm;break-inside:avoid}
.ixrow .ixpg{color:var(--muted);white-space:nowrap;margin-left:2mm}
"""

doc = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<title>{_h.escape(TITLE)} — 조판본</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700&display=swap">
<style>{CSS.replace("__BOOKTITLE__", TITLE)}</style>
<script>window.PagedConfig={{auto:true,after:()=>{{window.__pagedDone=true}}}};</script>
<script src="{_h.escape(os.path.relpath(os.path.join(HERE,'paged.polyfill.js'), OUT_DIR).replace(os.sep,'/'))}"></script>
</head><body>
<div class="cover"><div class="k">SMB · 실무서 시리즈</div>
<h1>{_h.escape(TITLE)}</h1>
<div class="sub">일반인과 실무자를 위한 이원 구성<br>2026년 시행 법령 기준 · 감수 전 검토판</div>
<div class="foot">본 조판본은 감수 전 검토용입니다. 세무·법률 자문을 대체하지 않으며, 외부 배포를 금합니다.</div></div>
<div class="frontmatter toc"><h1>차례</h1>{toc_html}</div>
{"".join(body_parts)}
<section class="ixsec"><h1>색인</h1>
<p style="font-size:8.8pt;color:#5A6272">숫자는 페이지. 원고 수정 후 재조판 시 자동 갱신된다.</p>
<div class="cols">{index_html}</div></section>
</body></html>"""

with open(OUT_H, "w", encoding="utf-8") as f:
    f.write(doc)
print(f"OK: {OUT_H}")
print(f"장 {len(chapters)}개 · 색인 표제어 {len(ix_entries)}/{len(terms)}개 · 앵커 {sum(len(v) for v in ix_entries.values())}개")
if missing:
    print("본문 미발견 색인어(제외됨): " + ", ".join(missing))
