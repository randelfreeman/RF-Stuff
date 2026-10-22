set -e
cd /tmp/claude-0/-home-user-RF-Stuff/e2c1133f-7df8-5a27-93b4-4d781de9e32f/scratchpad/cpng
python3 - <<'PY'
import re
S="https://gam.prontonlp.com/#/ref/$SENTID_"; D="https://gam.prontonlp.com/#/ref/$DOCID_"; C="https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid="
full="".join(open(f).read() for f in ["report_p1.md","report_p2.md","report_p3.md","report_p4.md"])
full=full.replace("{S}",S).replace("{D}",D).replace("{C}",C)
open("report.md","w").write(full)
PY
pandoc report.md -f markdown-tex_math_dollars --columns=100000 -t html5 -s --css report.css --embed-resources --lua-filter filters.lua -o out/report.html
node render_pdf.js out/report.html out/Coupang_CPNG_Research_Report.pdf
pandoc report.md -f markdown-tex_math_dollars --columns=100000 -t docx --reference-doc ref.docx --lua-filter filters.lua --resource-path=. -o out/Coupang_CPNG_Research_Report.docx
pdfinfo out/Coupang_CPNG_Research_Report.pdf | grep Pages
