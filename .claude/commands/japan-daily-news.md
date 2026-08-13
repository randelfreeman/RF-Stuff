# Japan Portfolio daily news run

Produce the Japan Portfolio morning brief. This file is the stored, labeled definition of the
workflow — invoke it on demand with `/japan-daily-news`, and the scheduled weekday Routine
follows it too. Positions are treated as live exposure (holdings, not just a watchlist).

## Inputs
- `watchlist-japan.md` at the repo root is the source of truth for coverage. Read it first.
- Several entries are marked (confirm) or UNRESOLVED — verify identities during research and
  update `watchlist-japan.md` with confirmed names as part of the run, flagging changes in the
  brief. Never silently drop or guess a name.
- Lookback: news since the previous run (normally the past 24 hours; on Mondays cover the
  weekend since Friday). Japan and Korea markets have already closed for the day by the 6am ET
  run time — cover their just-completed session. Add a short "week in context" thread for
  macro (BoJ, yen, JGBs, BoK, won).

## Research
- Your training data predates the run date — every claim must come from live web search.
- Fan out parallel research agents by theme (e.g., megacaps/tech (Sony, SoftBank, Keyence,
  TSMC-adjacent), banks/financials, industrials/autos, Japan small/mid caps, Korea names,
  macro/JGB/FX).
- For each name: what happened (with source URL and date), a MATTERS / NOISE / QUIET verdict,
  and upcoming catalysts in the next 2 weeks (earnings dates especially — note Japan's
  quarterly reporting clusters).
- Full sweep: every name gets at least a status line; small regional banks and micro caps may
  legitimately be QUIET most days — one line suffices.
- Include a macro thread: BoJ policy and JGB yields (the JP1024661QB1 government bond position
  makes this mandatory), yen, Bank of Korea, and Korea market structure news.

## Output structure (5 sections)
1. **Top of the stack** — the 3–5 developments that most demand attention today.
2. **What matters, by theme** — real news gets prose, quiet names get a line.
3. **Probably noise** — ignorable headlines with one-line reasoning.
4. **Time-sensitive / positions watch** — mechanics needing decisions plus a dated catalyst
   calendar for the next ~2 weeks and undated-but-live events.
5. **Follow-up questions to investigate** — tied to specific names.

Style: prose and short paragraphs, bullets where helpful, written for an investment
professional. Inline links on every factual claim. Flag anything unverifiable.

## Deliverables
- `outputs/japan-brief-YYYY-MM-DD.md` (markdown source)
- `outputs/japan-brief-YYYY-MM-DD.docx` (Word) and `.pdf` — the owner cannot open raw .md
  files. Environment notes: pandoc and LibreOffice conversion are NOT available here. Generate
  the .docx with the `docx` npm library (npm install docx if needed; US Letter page size;
  tables need columnWidths + per-cell DXA widths). Generate the .pdf by converting the markdown
  to styled HTML (marked npm library) and printing with headless Chromium:
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
- If an instrument has expired/matured (e.g., the JGB), note it in the brief and flag that
  `watchlist-japan.md` needs updating — do not silently drop it.
- Names marked ⇄GGOF / ⇄EM also appear in the other portfolios; cover them here independently.
