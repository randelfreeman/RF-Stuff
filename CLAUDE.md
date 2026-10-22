# RF-Stuff research repository

## One folder per query

Every new request (equity research report, IC memo, activist screen, holdco analysis,
thematic note, etc.) gets its own new folder at the repository root:

```
YYYY-MM-DD_<Company>_<Ticker>/     e.g. 2026-10-21_Nippon_TV_9404_JP/
YYYY-MM-DD_<Topic>/                e.g. 2026-10-14_KOSPI_Activist_Screen/
```

- Date is the day the request is made. Use underscores, no spaces. Tickers use the
  exchange suffix (`_JP`, `_KS`, `_MK`, `_LN`, `_FP`, `_HK`, `_TT`, `_IJ`, ...).
- Everything the query produces goes inside that folder: final reports (DOCX/PDF/HTML/MD),
  IC memos, charts, data pulls, provenance logs, research notes and build scripts.
  Nothing is written to the repository root.
- If the folder name is already taken, append `_v2`, `_v3`, ...
- Follow-ups that refine the same piece of work ("add a PDF", "fix the SOTP") go into that
  work's existing folder. A new company or topic gets a new folder, even within the same
  session.
- Do not modify another query's folder unless asked to.
- Build scripts and documents should reference files by paths relative to the query
  folder, not absolute paths, so folders stay self-contained if moved.

## Exceptions

The daily news runs (`/em-daily-news`, `/ggof-daily-news`, `/japan-daily-news`, defined in
`.claude/commands/`) keep their own layout: they read `watchlist*.md` at the repository
root and write briefs to `outputs/`.
