set -e
cd /tmp/claude-0/-home-user-RF-Stuff/e2c1133f-7df8-5a27-93b4-4d781de9e32f/scratchpad/cpng
python3 - <<'PY'
S="https://gam.prontonlp.com/#/ref/$SENTID_"; D="https://gam.prontonlp.com/#/ref/$DOCID_"; C="https://www.capitaliq.spglobal.com/apisv3/spg-webplatform-core/docviewer?mid="
s=open("memo.html").read().replace("{S}",S).replace("{D}",D).replace("{C}",C)
assert "{S}" not in s and "{D}" not in s and "{C}" not in s
open("memo_built.html","w").write(s)
PY
node render_pdf.js memo_built.html out/Coupang_CPNG_IC_Memo.pdf slides
pdfinfo out/Coupang_CPNG_IC_Memo.pdf | grep Pages
