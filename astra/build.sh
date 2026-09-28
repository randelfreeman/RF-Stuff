#!/bin/sh
# Render Astra_International_Holdco_Report.html to PDF with headless Chromium
cd "$(dirname "$0")"
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless=new --no-sandbox --disable-gpu \
  --no-pdf-header-footer --print-to-pdf=../Astra_International_Holdco_Report.pdf \
  "file://$(pwd)/Astra_International_Holdco_Report.html"
