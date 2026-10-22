"""Find the PDF page of every H1 heading and write toc_pages.json (two-pass static contents table)."""
import json, subprocess, sys
pdf, heads = sys.argv[1], json.loads(subprocess.check_output(['node', 'dump_h1.js'], cwd=sys.path[0]))
n = int([l for l in subprocess.check_output(['pdfinfo', pdf], text=True).splitlines() if l.startswith('Pages')][0].split()[1])
pages = [' '.join(subprocess.check_output(['pdftotext', '-f', str(i), '-l', str(i), pdf, '-'], text=True).split()) for i in range(1, n + 1)]
out, start = [], 2
for h in heads:
    key = ' '.join(h.split())[:38]
    pg = next((i + 1 for i in range(start, n) if key in pages[i]), None)
    out.append({'h': h, 'page': pg or '–'}); start = (pg or start + 1) - 1
json.dump(out, open(sys.path[0] + '/toc_pages.json', 'w'), indent=1, ensure_ascii=False)
print(out)
