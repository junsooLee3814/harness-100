# -*- coding: utf-8 -*-
"""알뜰폰MVNO_v2 탭형 HTML 빌더 — 7탭 (산업/경쟁/소비자/트렌드/생존전략/요약/별첨-계열사)"""
import markdown, html, pathlib, re

BASE = pathlib.Path(__file__).parent

# (tab_id, 라벨, 파일, 이모지)
TABS = [
    ("summary",    "요약",        "06_review_report.md",        "📊"),
    ("industry",   "산업분석",     "01_industry_analysis.md",    "🏭"),
    ("competitor", "경쟁자",       "02_competitor_analysis.md",  "⚔️"),
    ("consumer",   "소비자",       "03_consumer_analysis.md",    "👥"),
    ("trend",      "트렌드",       "04_trend_analysis.md",       "📈"),
    ("survival",   "생존전략",     "05_survival_strategy.md",    "🧭"),
    ("appendix",   "별첨·계열사",  "07_appendix_affiliates.md",  "🔗"),
]

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])

def convert(path):
    text = path.read_text(encoding="utf-8")
    md.reset()
    body = md.convert(text)
    return body

panels = []
navbtns = []
for i, (tid, label, fname, emoji) in enumerate(TABS):
    body = convert(BASE / fname)
    active = " active" if i == 0 else ""
    panels.append(f'<section id="{tid}" class="panel{active}">{body}</section>')
    navbtns.append(
        f'<button class="tab{active}" data-tab="{tid}"><span class="tab-emoji">{emoji}</span>{label}</button>'
    )

nav = "\n".join(navbtns)
panels_html = "\n".join(panels)

DOC = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>알뜰폰 MVNO · 프리텔레콤 분석</title>
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
:root{{
  --ink:#19223C; --text:#37415C; --muted:#6C748C; --faint:#9AA1B4;
  --bg:#F3F5FB; --card:#FFFFFF; --line:#E6E9F2; --line2:#EEF1F8;
  --navy:#16386E; --navy-bg:#EAF1FB; --navy-bd:#C8DAF1;
  --sky-bg:#EAF2FE; --sky-bd:#CBDDFB; --sky-dp:#1B4DA0; --sky-ac:#3D7BEA;
  --orange-bg:#FCEBDA; --orange-bd:#F5CDA6; --orange-dp:#A8500F;
  --violet-bg:#F1EAFB; --violet-bd:#DFD0F5; --violet-dp:#653A9F;
  --amber-bg:#FBF3D9; --amber-bd:#F0E0AE; --amber-dp:#8A6912;
  --mint-bg:#E6F5EE; --mint-bd:#C8E7D7; --mint-dp:#1C744E;
  --red-bg:#FCEAEA; --red-bd:#F3C6C6; --red-dp:#A32A2A;
  --radius:16px;
  --shadow-md:0 1px 2px rgba(20,30,60,.04), 0 14px 32px rgba(20,30,60,.07);
}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%; scroll-behavior:smooth}}
body{{
  margin:0; background:radial-gradient(1100px 460px at 50% -240px,#fff 0%,rgba(255,255,255,0) 70%),var(--bg);
  color:var(--text);
  font-family:"Pretendard Variable",Pretendard,-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;
  font-size:15.5px; line-height:1.72; letter-spacing:-.01em; -webkit-font-smoothing:antialiased;
}}
.wrap{{max-width:1080px; margin:0 auto; padding:28px 20px 100px;}}

/* ===== Cover ===== */
.cover{{background:var(--navy-bg); border:1px solid var(--navy-bd); border-radius:18px; padding:30px 30px 26px; margin-bottom:18px;}}
.eyebrow{{font-size:12px; font-weight:800; letter-spacing:.14em; text-transform:uppercase; color:var(--navy); margin-bottom:12px;}}
.cover h1{{font-size:clamp(26px,4.6vw,40px); line-height:1.14; font-weight:800; color:var(--navy); margin:0 0 8px; letter-spacing:-.022em;}}
.cover p{{margin:0 0 18px; color:var(--muted); font-weight:500; max-width:70ch;}}
.cover-meta{{display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:8px;}}
.cm{{border-radius:12px; padding:12px 14px;}}
.cm-k{{font-size:10.5px; font-weight:800; letter-spacing:.05em; text-transform:uppercase; opacity:.85;}}
.cm-v{{font-size:14px; font-weight:800; letter-spacing:-.01em; margin-top:2px;}}
.cm:nth-child(4n+1){{background:var(--sky-bg); border:1px solid var(--sky-bd); color:var(--sky-dp);}}
.cm:nth-child(4n+2){{background:var(--orange-bg); border:1px solid var(--orange-bd); color:var(--orange-dp);}}
.cm:nth-child(4n+3){{background:var(--violet-bg); border:1px solid var(--violet-bd); color:var(--violet-dp);}}
.cm:nth-child(4n+4){{background:var(--mint-bg); border:1px solid var(--mint-bd); color:var(--mint-dp);}}

/* ===== Tabs ===== */
.tabbar{{position:sticky; top:0; z-index:20; display:flex; flex-wrap:wrap; gap:6px;
  background:rgba(243,245,251,.9); backdrop-filter:blur(8px); padding:10px 0; margin-bottom:16px; border-bottom:1px solid var(--line);}}
.tab{{display:inline-flex; align-items:center; gap:6px; border:1px solid var(--line); background:var(--card);
  color:var(--muted); font-family:inherit; font-size:14px; font-weight:700; letter-spacing:-.01em;
  padding:9px 15px; border-radius:11px; cursor:pointer; transition:all .15s;}}
.tab:hover{{color:var(--navy); border-color:var(--navy-bd);}}
.tab.active{{background:var(--navy); color:#fff; border-color:var(--navy); box-shadow:0 6px 16px rgba(22,56,110,.25);}}
.tab-emoji{{font-size:15px;}}

/* ===== Panel ===== */
.panel{{display:none; animation:fade .25s ease;}}
.panel.active{{display:block;}}
@keyframes fade{{from{{opacity:0; transform:translateY(6px)}} to{{opacity:1; transform:none}}}}
.panel > *:first-child{{margin-top:0;}}

/* ===== Typography ===== */
h1{{font-size:clamp(22px,3.4vw,30px); font-weight:800; color:var(--navy); letter-spacing:-.02em; line-height:1.2;
  margin:8px 0 14px; padding-bottom:14px; border-bottom:2px solid var(--navy);}}
h2{{font-size:clamp(18px,2.6vw,23px); font-weight:800; color:var(--navy); letter-spacing:-.02em; line-height:1.25;
  margin:38px 0 14px; padding-top:20px; border-top:1px solid var(--line); position:relative;}}
h2::before{{content:""; position:absolute; top:-1px; left:0; width:48px; height:3px; background:var(--navy); border-radius:3px;}}
h3{{font-size:16.5px; font-weight:800; color:var(--ink); letter-spacing:-.015em; margin:24px 0 10px; line-height:1.3;}}
h4{{font-size:15px; font-weight:800; color:var(--sky-dp); margin:18px 0 8px;}}
p{{margin:0 0 12px;}}
strong{{font-weight:750; color:var(--ink);}}
em{{font-style:normal; color:#586383; font-weight:600;}}
a{{color:var(--sky-ac); text-decoration:none;}}
a:hover{{text-decoration:underline;}}
ul,ol{{margin:0 0 14px; padding-left:22px;}}
li{{margin:4px 0;}}
hr{{border:none; border-top:1px solid var(--line); margin:26px 0;}}
code{{font-family:"SFMono-Regular",ui-monospace,Menlo,Consolas,monospace; font-size:.86em;
  background:var(--sky-bg); color:var(--sky-dp); padding:.14em .45em; border-radius:6px; font-weight:600; word-break:keep-all;}}
pre{{background:#0F1B34; color:#D7E3F7; border-radius:12px; padding:16px 18px; overflow-x:auto;
  font-size:13px; line-height:1.6; margin:0 0 16px;}}
pre code{{background:none; color:inherit; padding:0; font-weight:500;}}

/* ===== Tables ===== */
.tbl-scroll{{overflow-x:auto; margin:0 0 18px; border-radius:12px; border:1px solid var(--line); box-shadow:var(--shadow-md);}}
table{{border-collapse:collapse; width:100%; font-size:13.5px; background:var(--card);}}
thead th{{background:var(--navy); color:#fff; font-weight:700; text-align:left; padding:10px 12px; white-space:nowrap; letter-spacing:-.01em;}}
tbody td{{padding:9px 12px; border-top:1px solid var(--line2); vertical-align:top;}}
tbody tr:nth-child(even){{background:#FBFCFE;}}
tbody tr:hover{{background:var(--sky-bg);}}
td strong{{color:var(--navy);}}

/* ===== Blockquote as callout ===== */
blockquote{{margin:0 0 16px; padding:14px 18px; background:var(--amber-bg); border:1px solid var(--amber-bd);
  border-left:4px solid var(--amber-dp); border-radius:0 12px 12px 0; color:#4A3D14;}}
blockquote p{{margin:0 0 6px;}}
blockquote p:last-child{{margin:0;}}
blockquote strong{{color:var(--amber-dp);}}

/* footer */
.foot{{margin-top:40px; padding-top:16px; border-top:1px solid var(--line); font-size:12.5px; color:var(--faint); text-align:center;}}
@media (max-width:640px){{
  .wrap{{padding:16px 12px 80px;}} body{{font-size:14.5px;}}
  .tab{{padding:8px 11px; font-size:13px;}} table{{font-size:12.5px;}}
}}
</style>
</head>
<body>
<div class="wrap">
  <div class="cover">
    <div class="eyebrow">Market Research · 2026-07-23</div>
    <h1>알뜰폰 MVNO 시장 &amp; ㈜프리텔레콤 분석</h1>
    <p>삼화회계법인 DCF 지분가치 평가보고서(2025.12.31 기준)와 프리티 IR BOOK(2026.7)의 <strong>1차 자료</strong> 기반 분석. 관계사 별첨과 프리텔레콤 생존전략 포함.</p>
    <div class="cover-meta">
      <div class="cm"><div class="cm-k">프리텔레콤 영업이익률</div><div class="cm-v">10.7% (업계 1위급)</div></div>
      <div class="cm"><div class="cm-k">지분가치 (삼화 DCF)</div><div class="cm-v">644.5억 원</div></div>
      <div class="cm"><div class="cm-k">모회사 익스포저</div><div class="cm-v">약 215억 (현금 9.6억)</div></div>
      <div class="cm"><div class="cm-k">장려금 커버리지 붕괴</div><div class="cm-v">2028년</div></div>
    </div>
  </div>

  <nav class="tabbar">
    {nav}
  </nav>

  {panels_html}

  <div class="foot">내부 검토용 · 첨부 평가보고서는 배포 제한 문서(대외 인용 금지) · 알뜰폰 MVNO 분석 · Market Research Harness</div>
</div>

<script>
(function(){{
  var tabs = document.querySelectorAll('.tab');
  var panels = document.querySelectorAll('.panel');
  tabs.forEach(function(t){{
    t.addEventListener('click', function(){{
      var id = t.getAttribute('data-tab');
      tabs.forEach(function(x){{x.classList.remove('active');}});
      panels.forEach(function(p){{p.classList.remove('active');}});
      t.classList.add('active');
      var panel = document.getElementById(id);
      if(panel) panel.classList.add('active');
      window.scrollTo({{top:0, behavior:'smooth'}});
    }});
  }});
}})();
</script>
</body>
</html>
"""

# 표를 가로 스크롤 컨테이너로 감싸기
DOC = re.sub(r"<table>", '<div class="tbl-scroll"><table>', DOC)
DOC = re.sub(r"</table>", "</table></div>", DOC)

out = BASE / "freeT_MVNO_v2.html"
out.write_text(DOC, encoding="utf-8")
print("WROTE", out, len(DOC), "bytes")
