# -*- coding: utf-8 -*-
"""
build_html.py — 사업계획서 HTML 렌더러 (파스텔 카드)

사용:
    python build_html.py <plan.md> <output.html>

규칙 (html-pastel-style 계승):
- 첫 H1 = 표지(네이비 패널), 이후 H2 = 파스텔 카드 순환(하늘·연주황·보라·노랑·민트)
- 표·목록 자동 스타일. 표지에 "내부 검토용 — 투자권유 아님" 배지 자동 삽입
- 단일 파일 산출 (외부 요청은 Pretendard CDN 1건)
"""
import sys
import os
import re
import html as _h

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

CSS = """
:root{--ink:#19223C;--text:#37415C;--muted:#6C748C;--bg:#F3F5FB;--line:#E6E9F2;
--navy:#16386E;--navy-bg:#EAF1FB;--navy-bd:#C8DAF1;
--f0-bg:#EAF2FE;--f0-bd:#CBDDFB;--f0-ac:#3D7BEA;--f0-dp:#1B4DA0;
--f1-bg:#FCEBDA;--f1-bd:#F5CDA6;--f1-ac:#EA6A17;--f1-dp:#A8500F;
--f2-bg:#F1EAFB;--f2-bd:#DFD0F5;--f2-ac:#875AD2;--f2-dp:#653A9F;
--f3-bg:#FBF3D9;--f3-bd:#F0E0AE;--f3-ac:#D2A11C;--f3-dp:#8A6912;
--f4-bg:#E6F5EE;--f4-bd:#C8E7D7;--f4-ac:#2C9F70;--f4-dp:#1C744E;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-size:15.5px;line-height:1.72;
font-family:"Pretendard Variable",Pretendard,-apple-system,"Malgun Gothic",sans-serif;
-webkit-font-smoothing:antialiased;letter-spacing:-.01em}
.page{max-width:960px;margin:0 auto;padding:36px 20px 90px}
.doc{background:#fff;border:1px solid var(--line);border-radius:18px;
box-shadow:0 1px 2px rgba(20,30,60,.04),0 14px 32px rgba(20,30,60,.07);padding:clamp(24px,4vw,52px)}
.cover{background:var(--navy-bg);border:1px solid var(--navy-bd);border-radius:16px;
padding:30px 32px;margin-bottom:22px}
.eyebrow{font-size:12.5px;font-weight:700;letter-spacing:.14em;color:var(--navy);
text-transform:uppercase;margin-bottom:14px}
.cover h1{font-size:clamp(26px,4.6vw,38px);line-height:1.16;font-weight:800;color:var(--navy);
margin:0 0 10px;letter-spacing:-.02em}
.cover .lede{color:var(--muted);font-weight:500;margin:0 0 18px;max-width:60ch}
.badge{display:block;background:#FDEEE6;border:1px solid #F8D6C5;color:#B0512B;
border-radius:12px;padding:10px 14px;font-size:13px;font-weight:600}
.card{border-radius:16px;border:1px solid;padding:22px 24px;margin:16px 0;break-inside:avoid}
.card h2{margin:0 0 12px;font-size:19px;font-weight:800;letter-spacing:-.015em;
display:flex;align-items:center;gap:10px}
.card .no{flex:none;min-width:34px;height:26px;border-radius:8px;display:inline-flex;
align-items:center;justify-content:center;font-size:13px;font-weight:800;color:#fff}
.card h3{font-size:15.5px;font-weight:800;margin:18px 0 8px}
.card p{margin:8px 0}
.card ul{margin:8px 0;padding-left:2px;list-style:none}
.card li{padding-left:18px;position:relative;margin-bottom:6px}
.card li:before{content:"";position:absolute;left:2px;top:.63em;width:6px;height:6px;border-radius:50%}
.tblw{overflow-x:auto;background:#fff;border-radius:12px;border:1px solid var(--line);
margin:10px 0;box-shadow:0 2px 10px rgba(20,30,60,.05)}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th{color:#fff;padding:9px 12px;text-align:left;font-weight:700;white-space:nowrap}
td{padding:8px 12px;border-top:1px solid var(--line);vertical-align:top}
tr:nth-child(even) td{background:#FAFBFE}
strong{color:var(--ink)}
""" + "".join(
    f""".f{i}{{background:var(--f{i}-bg);border-color:var(--f{i}-bd)}}
.f{i} h2{{color:var(--f{i}-dp)}} .f{i} .no{{background:var(--f{i}-ac)}}
.f{i} h3{{color:var(--f{i}-dp)}} .f{i} li:before{{background:var(--f{i}-ac)}}
.f{i} th{{background:var(--f{i}-ac)}}
""" for i in range(5)) + """
@media print{body{background:#fff}.doc{box-shadow:none;border:0;padding:0}
.card{break-inside:avoid}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""


def inline(s):
    s = _h.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def md_to_html(md):
    lines = md.splitlines()
    out, buf_table, buf_list = [], [], []
    title, lede = "사업계획서", ""
    card_open = False
    fam = 0
    sec_no = 0
    i = 0

    def flush_list():
        nonlocal buf_list
        if buf_list:
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in buf_list) + "</ul>")
            buf_list = []

    def flush_table():
        nonlocal buf_table
        if len(buf_table) >= 2:
            hdr = [c.strip() for c in buf_table[0].strip("|").split("|")]
            rows = [[c.strip() for c in r.strip("|").split("|")] for r in buf_table[2:]]
            t = "<div class='tblw'><table><tr>" + "".join(
                f"<th>{inline(h)}</th>" for h in hdr) + "</tr>"
            for r in rows:
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            t += "</table></div>"
            out.append(t)
        buf_table = []

    # 첫 H1과 다음 문단을 표지로
    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("# "):
            title = ln[2:].strip()
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i < len(lines) and not lines[i].startswith("#"):
                lede = lines[i].strip()
                i += 1
            break
        i += 1

    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("|"):
            flush_list()
            buf_table.append(ln)
            i += 1
            continue
        flush_table()
        if ln.startswith("## "):
            flush_list()
            if card_open:
                out.append("</section>")
            sec_no += 1
            out.append(f"<section class='card f{fam}'>"
                       f"<h2><span class='no'>{sec_no:02d}</span>{inline(ln[3:].strip())}</h2>")
            fam = (fam + 1) % 5
            card_open = True
        elif ln.startswith("### "):
            flush_list()
            out.append(f"<h3>{inline(ln[4:].strip())}</h3>")
        elif ln.startswith("- ") or ln.startswith("* "):
            buf_list.append(ln[2:].strip())
        elif ln.startswith("> "):
            flush_list()
            out.append(f"<p><em>{inline(ln[2:].strip())}</em></p>")
        elif not ln.strip():
            flush_list()
        elif ln.startswith("---"):
            flush_list()
        elif ln.startswith("# "):
            flush_list()  # 추가 H1은 H2처럼 처리하지 않고 굵은 문단으로
            out.append(f"<h3>{inline(ln[2:].strip())}</h3>")
        else:
            flush_list()
            out.append(f"<p>{inline(ln.strip())}</p>")
        i += 1
    flush_list()
    flush_table()
    if card_open:
        out.append("</section>")

    return f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{_h.escape(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>{CSS}</style></head><body><div class="page"><div class="doc">
<header class="cover"><div class="eyebrow">신사업 사업계획서 — 내부 투자심의용</div>
<h1>{inline(title)}</h1><p class="lede">{inline(lede)}</p>
<span class="badge">⚠ 본 자료는 내부 의사결정 검토용이며 투자권유가 아닙니다.
수치에는 [가정] 추정이 포함되어 있어 외부 배포를 금합니다.</span></header>
{''.join(out)}
</div></div></body></html>"""


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    allow_warn = "--allow-warnings" in sys.argv
    if len(argv) < 2:
        print("Usage: python build_html.py <plan.md> <output.html> [--allow-warnings]",
              file=sys.stderr)
        sys.exit(1)
    src, dst = argv[0], argv[1]
    if not os.path.exists(src):
        print(f"[ERROR] 입력 md 없음: {src}", file=sys.stderr)
        sys.exit(1)
    with open(src, "r", encoding="utf-8") as f:
        md = f.read()
    html_text = md_to_html(md)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(html_text)
    n_cards = html_text.count("<section class='card")
    print(f"OK: {dst}")
    print(f"cards={n_cards} bytes={len(html_text):,}")
    if n_cards == 0 and not allow_warn:
        print("[WARN] H2 섹션이 하나도 없습니다 — md 구조를 확인하십시오. "
              "의도한 것이면 --allow-warnings.", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
