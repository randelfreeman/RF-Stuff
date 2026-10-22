# Build scripts — Tokyo Tatemono (8804 JP) report

Reproduce the deliverables from `reports/Tokyo Tatemono 8804 equity research.md` and the research-notes datasets.

1. **Charts** (Python 3, matplotlib, pandas, numpy): run `charts_a.py`, `charts_b.py`, `charts_c.py`, `charts_d.py`, `chart_supply.py` → `reports/figures/*.png` (shared style in `chartkit.py`).
2. **Word report** (Node 22 + `docx` and `marked` npm packages): `node build_docx.js "<report.md>" out.docx meta_tt.json [toc_pages.json]`.
3. **PDF report**: convert the DOCX with LibreOffice (`soffice --headless --convert-to pdf out.docx`); run `toc_pages.py out.pdf out.docx.headings.json toc_pages.json`, rebuild the DOCX with that file to fill the contents page numbers, and convert again.
4. **IC summary deck**: `python3 build_deck.py` (writes `/tmp/lotest/tt_deck.html`; components in `deckkit.py`), then `node pdf_print.js tt_deck.html Tokyo_Tatemono_8804_IC_Summary.pdf` (Playwright/Chromium, 13.33 × 7.5 in pages).
