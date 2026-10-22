# EM Portfolio daily news run

Produce the EM Portfolio morning brief. This file is the stored, labeled definition of the
workflow — invoke it on demand with `/em-daily-news`, and the scheduled weekday Routine
follows it too. Positions are treated as live exposure (holdings, not just a watchlist).

## Inputs
- `watchlist-em.md` at the repo root is the source of truth for coverage. Read it first.
- Several entries are marked (confirm) or UNRESOLVED — verify identities during research and
  update `watchlist-em.md` with confirmed names as part of the run, flagging changes in the
  brief. Never silently drop or guess a name.
- Lookback: news since the previous run (normally the past 24 hours; on Mondays cover the
  weekend since Friday). Add a short "week in context" thread where a single day is
  meaningless (macro, commodities, EM FX).

## Research
- Your training data predates the run date — every claim must come from live web search.
- Fan out parallel research agents by region/theme (e.g., Korea; Greater China/HK/Taiwan;
  Brazil/LatAm; Middle East/Saudi/UAE; Southeast Asia/India/Africa; metals & mining/US-listed).
- For each name: what happened (with source URL and date), a MATTERS / NOISE / QUIET verdict,
  and upcoming catalysts in the next 2 weeks (earnings dates especially).
- Full sweep: every name in the watchlist gets at least a status line.
- Include an EM macro thread: dollar/EM FX, key EM central banks, China policy, commodity
  complex (copper, silver, oil) — these drive much of this book.
- Pay special attention to dated mechanics: the US T-bill position's maturity, preferred-share
  specifics, closed-end fund discounts (VEIL/VOF), merger/regulatory timelines.

## Output structure (5 sections)
1. **Top of the stack** — the 3–5 developments that most demand attention today.
2. **What matters, by region/theme** — real news gets prose, quiet names get a line.
3. **Probably noise** — ignorable headlines with one-line reasoning.
4. **Time-sensitive / positions watch** — mechanics needing decisions plus a dated catalyst
   calendar for the next ~2 weeks and undated-but-live events.
5. **Follow-up questions to investigate** — tied to specific names.

Style: prose and short paragraphs, bullets where helpful, written for an investment
professional. Inline links on every factual claim. Flag anything unverifiable.

## Deliverables
- `outputs/em-brief-YYYY-MM-DD.md` (markdown source)
- `outputs/em-brief-YYYY-MM-DD.docx` (Word) and `.pdf` — the owner cannot open raw .md files.
  Environment notes: pandoc and LibreOffice conversion are NOT available here. Generate the
  .docx with the `docx` npm library (npm install docx if needed; US Letter page size; tables
  need columnWidths + per-cell DXA widths). Generate the .pdf by converting the markdown to
  styled HTML (marked npm library) and printing with headless Chromium:
  `/opt/pw-browsers/chromium --headless --no-sandbox --print-to-pdf=... --no-pdf-header-footer file.html`.
  Verify output visually (Chromium --screenshot + read the image) before finishing.
- Commit all files with a clear message and push to branch
  `claude/portfolio-morning-brief-1g844t` (`git push -u origin <branch>`; retry with backoff
  on network errors). Do not open a pull request.
- **Email delivery:** if a Gmail/email tool is available in the session (check with ToolSearch),
  send the Word and PDF versions to **randel.freeman@gam.com**, **randyfreeman2@gmail.com**, and
  **randel@randelfreeman.com** with the day's top items as the message body. If no email tool is
  available, state that clearly in the end-of-run summary.

## Maintenance rules
- If an instrument has expired/matured (e.g., the T-bill), note it in the brief and flag that
  `watchlist-em.md` needs updating — do not silently drop it.
- Names marked ⇄GGOF also appear in the GGOF portfolio; cover them here independently.
