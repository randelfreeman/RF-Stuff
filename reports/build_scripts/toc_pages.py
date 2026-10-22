import json, subprocess, re, sys
pdf, headings_json, out = sys.argv[1], sys.argv[2], sys.argv[3]
heads = [h for h in json.load(open(headings_json)) if h["level"] == 1]
n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
norm = lambda t: re.sub(r"[^0-9a-z]", "", t.lower())
pages = [norm(subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", pdf, "-"], capture_output=True, text=True).stdout) for i in range(1, n + 1)]
start = next(i for i, p in enumerate(pages) if "contents" in p[:200]) + 1
res, cur = {}, start
for h in heads:
    key = norm(h["text"])[:28]
    for i in range(cur, n):
        if key in pages[i]:
            res[h["text"]] = i + 1; cur = i; break
    else:
        print("NOT FOUND:", h["text"])
json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
print(len(res), "of", len(heads), "headings located; pages", min(res.values()), "-", max(res.values()))
