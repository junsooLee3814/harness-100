import argparse
from pathlib import Path
import markdown

PASTEL_CSS = """/* =====================================================================
   html-pastel-style · Pastel Card Design System
   Clean, document-grade pastel cards. Pretendard + soft tints + depth.
   ===================================================================== */
:root{
  /* ---- neutrals ---- */
  --ink:#19223C; --text:#37415C; --muted:#6C748C; --faint:#9AA1B4;
  --bg:#F3F5FB; --card:#FFFFFF; --line:#E6E9F2; --line2:#EEF1F8;
  --accent:#2F55C6; --accent-soft:#E9EFFD; --accent-ink:#21408F;
  --navy:#16386E; --navy-bg:#EAF1FB; --navy-bg2:#D9E6F6; --navy-bd:#C8DAF1;
  --radius:18px;
  --shadow-sm:0 1px 2px rgba(20,30,60,.05);
  --shadow-md:0 1px 2px rgba(20,30,60,.04), 0 14px 32px rgba(20,30,60,.07);
  --shadow-inset:0 2px 10px rgba(20,30,60,.06);

  /* ---- pastel families: bg / bg2(deeper) / border / accent / deep(ink) ---- */
  --sky-bg:#EAF2FE;   --sky-bg2:#D7E7FD;   --sky-bd:#CBDDFB;   --sky-ac:#3D7BEA;   --sky-dp:#1B4DA0;
  --orange-bg:#FCEBDA; --orange-bg2:#F9D8BC; --orange-bd:#F5CDA6; --orange-ac:#EA6A17; --orange-dp:#A8500F;
  --violet-bg:#F1EAFB;--violet-bg2:#E6DAF7;--violet-bd:#DFD0F5;--violet-ac:#875AD2;--violet-dp:#653A9F;
  --amber-bg:#FBF3D9; --amber-bg2:#F6E8BC; --amber-bd:#F0E0AE; --amber-ac:#D2A11C; --amber-dp:#8A6912;
  --mint-bg:#E6F5EE;  --mint-bg2:#D2EEDE;  --mint-bd:#C8E7D7;  --mint-ac:#2C9F70;  --mint-dp:#1C744E;
  --peach-bg:#FDEEE6; --peach-bg2:#FADFCF; --peach-bd:#F8D6C5; --peach-ac:#E0784C; --peach-dp:#B0512B;
}

*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;
  background:
    radial-gradient(1100px 460px at 50% -240px, #fff 0%, rgba(255,255,255,0) 70%),
    var(--bg);
  color:var(--text);
  font-family:"Pretendard Variable",Pretendard,-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;
  font-size:16px; line-height:1.72; letter-spacing:-.01em;
  -webkit-font-smoothing:antialiased;
}
.page{ max-width:920px; margin:0 auto; padding:40px 22px 96px; }
.doc{
  background:var(--card); border:1px solid var(--line); border-radius:var(--radius);
  box-shadow:var(--shadow-md); padding:clamp(26px,5vw,60px);
}

.cover{ background:var(--navy-bg); border:1px solid var(--navy-bd); border-radius:16px;
  padding:30px 32px 28px; margin:0 0 12px; }
.eyebrow{ font-size:12.5px; font-weight:700; letter-spacing:.14em; text-transform:uppercase;
  color:var(--navy); margin-bottom:18px; }
.cover h1{ font-size:clamp(30px,5.4vw,46px); line-height:1.12; font-weight:800;
  color:var(--navy); margin:0 0 6px; letter-spacing:-.022em; }
.cover-lede{ font-size:clamp(14.5px,2.2vw,17px); color:var(--muted); font-weight:500;
  margin:0 0 24px; max-width:54ch; }
.cover-meta{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px;
  background:#fff; border:1px solid var(--navy-bd); border-radius:12px; padding:8px; }
.cm{ border-radius:14px; padding:14px 16px; display:flex; flex-direction:column; gap:4px;
  border:1px solid transparent; }
.cm-k{ font-size:11px; font-weight:800; letter-spacing:.06em; text-transform:uppercase; opacity:.85; }
.cm-v{ font-size:14.5px; font-weight:800; letter-spacing:-.01em; }
.cm:nth-child(4n+1){ background:var(--sky-bg);    border-color:var(--sky-bd);    color:var(--sky-dp); }
.cm:nth-child(4n+2){ background:var(--orange-bg); border-color:var(--orange-bd); color:var(--orange-dp); }
.cm:nth-child(4n+3){ background:var(--violet-bg); border-color:var(--violet-bd); color:var(--violet-dp); }
.cm:nth-child(4n+4){ background:var(--amber-bg);  border-color:var(--amber-bd);  color:var(--amber-dp); }
.cm-k{ color:inherit; } .cm-v{ color:inherit; }

.sync-badge{ display:inline-block; margin-top:18px; font-size:12px; font-weight:700;
  color:var(--navy); background:#fff; border:1px solid var(--navy-bd);
  padding:8px 14px; border-radius:10px; line-height:1.5; }

h2{ font-size:clamp(20px,3vw,25px); font-weight:800; color:var(--navy);
  letter-spacing:-.02em; line-height:1.25; margin:52px 0 16px; padding-top:24px;
  border-top:1px solid var(--line); position:relative; }
h2::before{ content:""; position:absolute; top:-1px; left:0; width:54px; height:3px;
  background:var(--navy); border-radius:3px; }
h3{ font-size:17.5px; font-weight:800; color:var(--ink); letter-spacing:-.015em;
  margin:28px 0 12px; line-height:1.3; }
p{ margin:0 0 13px; }
strong{ font-weight:700; color:var(--ink); }
em{ font-style:normal; color:#586383; font-weight:500; }
code{ font-family:"SFMono-Regular",ui-monospace,Menlo,Consolas,monospace; font-size:.86em;
  background:var(--accent-soft); color:var(--accent-ink); padding:.16em .5em; border-radius:6px;
  font-weight:600; word-break:keep-all; }

.day-divider{ display:flex; align-items:center; gap:14px; margin:48px 0 8px; padding-top:22px;
  border-top:2px solid var(--navy); }
.day-divider .d-badge{ flex:0 0 auto; font-size:12px; font-weight:800; letter-spacing:.06em;
  color:var(--navy); background:var(--navy-bg); border:1px solid var(--navy-bd); padding:7px 13px; border-radius:9px; }
.day-divider .d-title{ font-size:clamp(18px,2.6vw,22px); font-weight:800; color:var(--navy);
  letter-spacing:-.02em; }

.card{
  --c-bg:#fff; --c-bg2:#F4F6FB; --c-bd:var(--line); --c-ac:var(--accent); --c-dp:var(--ink);
  position:relative; background:var(--c-bg); border:1px solid var(--c-bd);
  border-radius:var(--radius); padding:24px 26px 22px; margin:18px 0;
  box-shadow:var(--shadow-md); overflow:hidden;
}
.card::before{ content:""; position:absolute; top:0; left:0; right:0; height:4px; background:var(--c-ac); }
.card--sky   { --c-bg:var(--sky-bg);    --c-bg2:var(--sky-bg2);    --c-bd:var(--sky-bd);    --c-ac:var(--sky-ac);    --c-dp:var(--sky-dp); }
.card--orange{ --c-bg:var(--orange-bg); --c-bg2:var(--orange-bg2); --c-bd:var(--orange-bd); --c-ac:var(--orange-ac); --c-dp:var(--orange-dp); }
.card--violet{ --c-bg:var(--violet-bg); --c-bg2:var(--violet-bg2); --c-bd:var(--violet-bd); --c-ac:var(--violet-ac); --c-dp:var(--violet-dp); }
.card--amber { --c-bg:var(--amber-bg);  --c-bg2:var(--amber-bg2);  --c-bd:var(--amber-bd);  --c-ac:var(--amber-ac);  --c-dp:var(--amber-dp); }
.card--mint  { --c-bg:var(--mint-bg);   --c-bg2:var(--mint-bg2);   --c-bd:var(--mint-bd);   --c-ac:var(--mint-ac);   --c-dp:var(--mint-dp); }

.sess-head{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin:0 0 4px; }
.sess-no{ font-size:12px; font-weight:800; letter-spacing:.08em; color:var(--c-dp);
  background:rgba(255,255,255,.72); border:1px solid var(--c-bd); padding:4px 11px; border-radius:7px; }
.sess-time{ font-size:13px; font-weight:700; color:var(--c-dp); opacity:.9; }
.sess-title{ flex-basis:100%; font-size:19px; font-weight:800; color:var(--ink);
  letter-spacing:-.015em; margin-top:6px; }

.sess-meta{ font-size:13px; color:var(--text); background:rgba(255,255,255,.66);
  border:1px solid var(--c-bd); border-radius:10px; padding:10px 14px; margin:10px 0 16px; line-height:1.55; }
.sess-meta strong{ color:var(--c-dp); }
.sess-meta em{ color:var(--text); font-weight:600; }

.block-label{ font-size:12px; font-weight:800; letter-spacing:.04em; color:var(--c-dp);
  margin:20px 0 8px; display:flex; align-items:center; gap:7px; }
.block-label::before{ content:""; width:7px; height:7px; border-radius:2px; background:var(--c-ac); }

.module-head{ background:#fff; border:1px solid var(--c-bd); border-left:3px solid var(--c-ac);
  border-radius:10px; padding:10px 14px; margin:16px 0 8px; box-shadow:var(--shadow-sm); }
.module-head strong{ font-size:15px; color:var(--ink); letter-spacing:-.01em; }
.module-head em{ color:var(--muted); font-weight:500; }

ul,ol{ margin:6px 0 16px; padding-left:0; list-style:none; }
li{ position:relative; padding-left:22px; margin:7px 0; line-height:1.66; }
ul > li::before{ content:""; position:absolute; left:4px; top:.66em; width:6px; height:6px;
  border-radius:50%; background:var(--c-ac,var(--accent)); }
ol{ counter-reset:li; }
ol > li{ padding-left:30px; counter-increment:li; }
ol > li::before{ content:counter(li); position:absolute; left:0; top:.05em; width:21px; height:21px;
  background:var(--c-ac,var(--accent)); color:#fff; border-radius:50%; font-size:11px;
  font-weight:800; display:flex; align-items:center; justify-content:center; }
li ul{ margin:6px 0 4px; }
li ul > li{ padding-left:20px; }
li ul > li::before{ width:5px; height:5px; background:var(--faint); top:.62em; }

ul > li.check{ padding-left:28px; margin:6px 0; }
ul > li.check::before{ content:""; left:1px; top:.28em; width:14px; height:14px; border-radius:4px;
  border:1.8px solid var(--c-ac,var(--accent)); background:rgba(255,255,255,.7); }

.tbl-wrap{ overflow:hidden; margin:14px 0 18px; border:1px solid var(--c-bd,var(--line));
  border-radius:12px; background:#fff; box-shadow:var(--shadow-sm); }
table{ width:100%; border-collapse:collapse; font-size:14px; background:#fff; }
thead th{ background:var(--c-bg2,#F4F6FB); color:var(--c-dp,var(--ink)); font-weight:800;
  text-align:left; font-size:12.5px; padding:11px 14px; border-bottom:1px solid var(--c-bd,var(--line)); white-space:nowrap; }
tbody td{ padding:11px 14px; border-bottom:1px solid var(--line2); vertical-align:top;
  line-height:1.6; color:var(--text); }
tbody tr:last-child td{ border-bottom:0; }
tbody td:first-child{ font-weight:700; color:var(--ink); white-space:nowrap; }

.callout{ display:flex; gap:11px; align-items:flex-start; margin:14px 0; padding:13px 16px;
  border-radius:12px; font-size:14.5px; line-height:1.6; border:1px solid transparent; }
.callout .ico{ flex:0 0 auto; width:22px; height:22px; border-radius:7px; color:#fff;
  font-size:13px; font-weight:900; display:flex; align-items:center; justify-content:center; margin-top:1px; }
.callout strong{ color:inherit; }
.callout.info{ background:var(--sky-bg);   border-color:var(--sky-bd);   color:var(--sky-dp); }
.callout.info .ico{ background:var(--sky-ac); }
.callout.tip{  background:var(--amber-bg);  border-color:var(--amber-bd);  color:var(--amber-dp); }
.callout.tip .ico{ background:var(--amber-ac); }
.callout.ok{   background:var(--mint-bg);   border-color:var(--mint-bd);   color:var(--mint-dp); }
.callout.ok .ico{ background:var(--mint-ac); }
.callout.note{ background:var(--violet-bg); border-color:var(--violet-bd); color:var(--violet-dp); }
.callout.note .ico{ background:var(--violet-ac); }
.callout.warn{ background:var(--peach-bg);  border-color:var(--peach-bd);  color:var(--peach-dp); }
.callout.warn .ico{ background:var(--peach-ac); }

blockquote{ margin:14px 0; padding:13px 17px; background:rgba(255,255,255,.6);
  border-left:3px solid var(--c-ac,var(--accent)); border-radius:0 10px 10px 0; color:var(--text); }
blockquote p{ margin:0; font-weight:600; }
blockquote p em{ color:var(--muted); }

hr{ border:0; height:1px; background:transparent; margin:26px 0; }
.footer-note, .doc > p:last-child em{ display:block; margin-top:28px; padding-top:18px;
  border-top:1px solid var(--line); color:var(--faint); font-size:13px; font-weight:500; }

@media (max-width:680px){
  .page{ padding:16px 12px 60px; }
  .cover-meta{ grid-template-columns:repeat(2,1fr); }
  .card{ padding:20px 18px; }
}

@media print{
  body{ background:#fff; }
  .page{ padding:0; max-width:none; }
  .doc{ border:0; box-shadow:none; border-radius:0; padding:0; }
  .card,.tbl-wrap,table,.module-head,blockquote,.callout{
    break-inside:avoid; box-shadow:none; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  h2,h3,.day-divider{ break-after:avoid; }
}

.card h3{ color:var(--c-dp); margin:18px 0 10px; font-size:16px; }
.cover-lede:last-child{ margin-bottom:0; }
.callout .cbody{ flex:1; min-width:0; }
.callout .cbody > :first-child{ margin-top:0; }
.callout .cbody p{ margin:0 0 6px; }
.callout .cbody p:last-child{ margin:0; }
.callout .cbody ul,.callout .cbody ol{ margin:6px 0; }
.callout .cbody strong{ color:inherit; }
.intro{ margin:4px 0 6px; }
"""

COVER_TEMPLATE = """<header class='cover'>
  <div class='eyebrow'>{eyebrow}</div>
  <h1>{title}</h1>
  {lede}
</header>"""

INTRO_TEMPLATE = """<div class='intro'><blockquote><p>{intro}</p></blockquote><hr /></div>"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang='ko'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title>{title}</title>
  <link rel='preconnect' href='https://cdn.jsdelivr.net' crossorigin>
  <link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css'>
  <style>{css}</style>
</head>
<body>
  <div class='page'>
    <div class='doc'>
      {cover}
      {intro}
      {content}
    </div>
  </div>
</body>
</html>"""

MARKDOWN_EXTENSIONS = [
    'tables',
    'fenced_code',
    'codehilite',
    'toc',
    'nl2br',
    'sane_lists',
    'attr_list'
]


def build_html(md_text: str, label: str = None) -> str:
    html_body = markdown.markdown(md_text, extensions=MARKDOWN_EXTENSIONS)

    # wrap cover with label and title extracted from markdown
    lines = md_text.strip().splitlines()
    title = 'Document'
    eyebrow = 'Report'
    lede = ''

    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
    if label:
        eyebrow = label

    if len(lines) > 1 and lines[1].strip():
        lede = f"<p class='cover-lede'>{lines[1].strip()}</p>"

    cover = COVER_TEMPLATE.format(eyebrow=eyebrow, title=title, lede=lede)
    intro = INTRO_TEMPLATE.format(intro='')

    return HTML_TEMPLATE.format(title=title, css=PASTEL_CSS, cover=cover, intro=intro, content=html_body)


def main() -> None:
    parser = argparse.ArgumentParser(description='Convert markdown to pastel-card HTML.')
    parser.add_argument('input_md', type=Path, help='Input markdown file path')
    parser.add_argument('output_html', type=Path, help='Output HTML file path')
    parser.add_argument('label', nargs='?', default='Report', help='Optional cover eyebrow label')
    args = parser.parse_args()

    md_text = args.input_md.read_text(encoding='utf-8')
    html_output = build_html(md_text, label=args.label)
    args.output_html.write_text(html_output, encoding='utf-8')


if __name__ == '__main__':
    main()
