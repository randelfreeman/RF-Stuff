"""Assemble the single-file dashboard page (artifact body) and a standalone test copy."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
data = open(os.path.join(D, "data.json")).read().replace("</", "<\\/")
css = open(os.path.join(D, "style.css")).read()
js = open(os.path.join(D, "app.js")).read()
page = f"""<title>Coupang Investment Case</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap">
<style>
{css}
</style>
<div id="cp-root"><div style="padding:24px 16px;font-family:system-ui,sans-serif">Loading the Coupang dashboard…</div></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.3.1/umd/react.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.3.1/umd/react-dom.production.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/htm@3.1.1/dist/htm.umd.js"></script>
<script type="application/json" id="dash-data">{data}</script>
<script>
{js}
</script>
"""
out = os.path.join(D, "Coupang_CPNG_Dashboard.html")
open(out, "w").write(page)
test = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style></head><body>' + page + '</body></html>')
open(os.path.join(D, "test_page.html"), "w").write(test)
open(os.path.join(D, "Coupang_CPNG_Dashboard_standalone.html"), "w").write(test)
print(out, os.path.getsize(out))
