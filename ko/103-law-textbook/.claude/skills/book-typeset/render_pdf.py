# -*- coding: utf-8 -*-
"""render_pdf.py — 조판본 HTML을 Paged.js로 렌더링해 PDF 저장 + 페이지 수 보고.

사용:  PYTHONUTF8=1 python render_pdf.py <조판본.html> [검수 스크린샷 폴더]
"""
import sys, os

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from playwright.sync_api import sync_playwright

src = os.path.abspath(sys.argv[1])
shot_dir = sys.argv[2] if len(sys.argv) > 2 else None
out_pdf = os.path.splitext(src)[0] + ".pdf"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 900, "height": 1200})
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto("file:///" + src.replace(os.sep, "/"))
    pg.wait_for_function("window.__pagedDone === true", timeout=480000)
    n = pg.eval_on_selector_all(".pagedjs_page", "e=>e.length")
    print(f"조판 완료: {n}페이지, JS오류 {len(errs)}건")
    if errs:
        print("errors:", errs[:3])
    if shot_dir:
        os.makedirs(shot_dir, exist_ok=True)
        for pn in [1, 2, min(60, n), n]:  # 표지·차례·본문 중간·색인
            el = pg.query_selector(f".pagedjs_page[data-page-number='{pn}']")
            if el:
                el.screenshot(path=os.path.join(shot_dir, f"page_{pn:03d}.png"))
        print(f"screenshots: {shot_dir}")
    pg.emulate_media(media="print")
    pg.pdf(path=out_pdf, prefer_css_page_size=True, print_background=True)
    print(f"PDF: {out_pdf} ({os.path.getsize(out_pdf):,} bytes)")
    b.close()
