# GGOF Portfolio daily news run

Produce the GGOF portfolio morning brief. This file is the stored, labeled definition of the
workflow — invoke it on demand with `/ggof-daily-news`, and the scheduled weekday Routine
follows it too. Positions are treated as live exposure (holdings, not just a watchlist).

## Inputs
- `watchlist.md` at the repo root is the source of truth for coverage. Read it first.
- Lookback: news since the previous run (normally the past 24 hours; on Mondays cover the
  weekend since Friday). Always add a short "week in context" thread where a single day is
  meaningless (macro, commodities).

## Research
- Your training data predates the run date — every claim must come from live web search.
- Fan out parallel research agents by watchlist group (rails/shipping/financials;
  luxury-consumer-Korea-autos-energy-alts; small-cap/special sits; futures/macro; US large caps).
- For each name: what happened (with source URL and date), a MATTERS / NOISE / QUIET verdict,
  and upcoming catalysts in the next 2 weeks (earnings dates especially).
- Full sweep: every name in the watchlist gets at least a status line.
- Pay special attention to dated position mechanics: option expiries, futures delivery months
  and rolls, merger outside dates, record dates.

## Output structure (5 sections)
1. **Top of the stack** — the 3–5 developments that most demand attention today, one short
   paragraph each on why they matter to a holder.
2. **What matters, by group** — sections matching the watchlist groups; real news gets prose,
   quiet names get a line.
3. **Probably noise** — headlines the reader will see that are safely ignorable, with one-line
   reasoning.
4. **Time-sensitive / positions watch** — option/futures mechanics needing decisions, plus a
   dated catalyst calendar table for the next ~2 weeks and a list of undated-but-live events.
5. **Follow-up questions to investigate** — open questions the day's news raises, tied to
   specific names.

Style: prose and short paragraphs, bullets where helpful, written for an investment
professional. Inline links on every factual claim so sources can be traced. Flag anything
that could not be verified.

## Deliverables
- `outputs/ggof-brief-YYYY-MM-DD.md` (markdown source)
- `outputs/ggof-brief-YYYY-MM-DD.docx` (Word) and `.pdf` — the owner cannot open raw .md files.
  Environment notes: pandoc and LibreOffice conversion are NOT available here. Generate the
  .docx with the `docx` npm library (npm install docx if needed; US Letter page size; tables
  need columnWidths + per-cell DXA widths). Generate the .pdf by converting the markdown to
  styled HTML (marked npm library) and printing with headless Chromium:
  `/opt/pw-browsers/chromium --headless --no-sandbox --print-to-pdf=... --no-pdf-header-footer file.html`.
  Verify output visually (Chromium --screenshot + read the image) before finishing.
- Commit all three files with a clear message and push to branch
  `claude/portfolio-morning-brief-1g844t` (`git push -u origin <branch>`; retry with backoff
  on network errors). Do not open a pull request.
- **Email delivery:** if a Gmail/email tool is available in the session (check with ToolSearch),
  send the Word and PDF versions to **randel.freeman@gam.com**, **randyfreeman2@gmail.com**, and
  **randel@randelfreeman.com** with the day's top items as the message body. If no email tool is
  available, state that clearly in the end-of-run summary so the owner knows the report is only
  in the repo.

## Maintenance rules
- If an instrument in the watchlist has expired (e.g., an option past expiry, a futures
  contract past delivery), note it in the brief and flag that `watchlist.md` needs updating —
  do not silently drop or edit the list.
- If a ticker cannot be identified, say so in the brief rather than guessing.
