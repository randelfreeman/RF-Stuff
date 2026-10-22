(function () {
  "use strict";
  const { useState, useEffect, useRef, useMemo, useCallback, Fragment } = React;
  const html = htm.bind(React.createElement);
  const DATA = JSON.parse(document.getElementById("dash-data").textContent);
  const CH = DATA.charts;

  /* ---------------- formatting ---------------- */
  const n1 = (v) => (Math.abs(v) >= 1000 ? Math.round(v).toLocaleString("en-US") : v.toFixed(1));
  const pct = (v, d = 1) => v.toFixed(d) + "%";
  const sgn = (v, d = 0) => (v > 0 ? "+" : v < 0 ? "-" : "") + Math.abs(v).toFixed(d);
  function fmtDate(iso) {
    const t = Date.parse(iso);
    if (!isFinite(t)) return "";
    return new Date(t).toLocaleString("en-GB", { day: "numeric", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit" });
  }
  function fmtWeek(iso) {
    const t = Date.parse(iso);
    return isFinite(t) ? "Week of " + new Date(t).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" }) : iso;
  }

  /* ---------------- sanitizer: report HTML and saved edits are rendered through an allowlist ---------------- */
  const KEEP = new Set(["P", "BR", "UL", "OL", "LI", "B", "STRONG", "I", "EM", "A", "SUP", "SUB", "SPAN", "CODE"]);
  const DROP = new Set(["SCRIPT", "STYLE", "TEMPLATE", "IFRAME", "OBJECT", "EMBED", "SVG", "MATH", "NOSCRIPT", "TEXTAREA", "SELECT", "INPUT", "BUTTON", "FORM"]);
  const SPAN_CLASSES = new Set(["ok", "unv"]);
  const sanitizeCache = new Map();
  function sanitize(src) {
    if (typeof src !== "string") return "";
    if (sanitizeCache.has(src)) return sanitizeCache.get(src);
    const doc = new DOMParser().parseFromString("<div>" + src + "</div>", "text/html");
    const out = document.createElement("div");
    const walk = (node, parent) => {
      for (const ch of Array.from(node.childNodes)) {
        if (ch.nodeType === 3) { parent.appendChild(document.createTextNode(ch.nodeValue)); continue; }
        if (ch.nodeType !== 1) continue;
        const tag = ch.tagName;
        if (DROP.has(tag)) continue;
        if (tag === "DIV") { const p = document.createElement("p"); walk(ch, p); if (p.childNodes.length) parent.appendChild(p); continue; }
        if (!KEEP.has(tag)) { walk(ch, parent); continue; }
        const el = document.createElement(tag.toLowerCase());
        if (tag === "A") {
          const h = (ch.getAttribute("href") || "").trim();
          if (/^https:\/\//i.test(h)) { el.setAttribute("href", h); el.setAttribute("target", "_blank"); el.setAttribute("rel", "noopener noreferrer"); }
        }
        if (tag === "SPAN") {
          const c = (ch.getAttribute("class") || "").split(/\s+/).filter((x) => SPAN_CLASSES.has(x));
          if (c.length) el.setAttribute("class", c.join(" "));
        }
        walk(ch, el);
        parent.appendChild(el);
      }
    };
    walk(doc.body.firstChild || doc.body, out);
    const res = out.innerHTML;
    if (sanitizeCache.size < 4000) sanitizeCache.set(src, res);
    return res;
  }
  const textOf = (h) => h.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&").replace(/&nbsp;/g, " ").trim();
  const isNumCell = (h) => { const t = textOf(h); return t.length > 0 && t.length < 34 && /^[~≈(+\-−–]?\s?(US\$|EUR|GBP|KRW|CNY|HKD|JPY|\$)?\s?[(]?-?[\d.,]+/.test(t); };

  /* ---------------- commentary persistence ---------------- */
  const LKEY = "cpng-dashboard-commentary-v1";
  function loadLocal() { try { const s = localStorage.getItem(LKEY); const o = s ? JSON.parse(s) : {}; return o && typeof o === "object" ? o : {}; } catch (e) { return {}; } }
  function saveLocal(m) { try { localStorage.setItem(LKEY, JSON.stringify(m)); return true; } catch (e) { return false; } }
  const docId = (id) => String(id).replace(/[^A-Za-z0-9_\-.~:@+]/g, "-").slice(0, 180);

  function useStore() {
    const [st, setSt] = useState({ mode: "init", overrides: {}, canWrite: null, readOnly: false, uid: null, err: null });
    const caps = useRef({ db: null, user: null });
    useEffect(() => {
      let unsub = null, dead = false;
      const goLocal = () => { if (!dead) setSt((s) => ({ ...s, mode: "local", overrides: loadLocal() })); };
      const c = window.claude;
      if (!c || typeof c.use !== "function") { goLocal(); return; }
      (async () => {
        let db = null, user = null;
        try { [db, user] = await Promise.all([c.use("db"), c.use("user")]); } catch (e) { db = null; }
        if (dead) return;
        if (!db) { goLocal(); return; }
        caps.current = { db, user };
        let uid = null, can = null;
        if (user) {
          try { uid = await user.id(); } catch (e) { uid = null; }
          try { can = await user.can("data.write"); } catch (e) { can = null; }
        }
        if (dead) return;
        setSt((s) => ({ ...s, mode: "shared", uid, canWrite: can }));
        try {
          unsub = db.collection("commentary").onSnapshot(
            (snap) => {
              const o = {};
              snap.docs.forEach((d) => { if (!d.exists) return; const v = d.data(); if (v && typeof v.html === "string") o[d.id] = v; });
              setSt((s) => ({ ...s, overrides: o }));
            },
            (e) => setSt((s) => ({ ...s, err: (e && e.code) || "unavailable" }))
          );
        } catch (e) { setSt((s) => ({ ...s, err: "unavailable" })); }
      })();
      return () => { dead = true; if (unsub) unsub(); };
    }, []);

    const write = useCallback(async (id, body) => {
      const key = docId(id);
      if (st.mode === "shared") {
        const ref = caps.current.db.doc("commentary/" + key);
        const attempt = () => (body === null ? ref.delete() : ref.set(body));
        try { await attempt(); return { ok: true }; } catch (e) {
          const code = e && e.code;
          if (code === "invalid_argument" || code === "not_granted" || code === "revoked" || code === "capability_disabled") {
            setSt((s) => ({ ...s, readOnly: true }));
            return { ok: false, msg: "You can read this dashboard but not change its commentary." };
          }
          if (code === "quota_exceeded") return { ok: false, msg: "The commentary store is full. Restore a few edited sections to the original, then save again." };
          if (code === "unavailable") {
            await new Promise((r) => setTimeout(r, 500 + Math.random() * 700));
            try { await attempt(); return { ok: true }; } catch (e2) { /* fall through */ }
          }
          return { ok: false, msg: "The edit was not saved. Check your connection and try again." };
        }
      }
      const m = loadLocal();
      if (body === null) delete m[key]; else m[key] = body;
      if (saveLocal(m)) { setSt((s) => ({ ...s, overrides: m })); return { ok: true }; }
      return { ok: false, msg: "This browser blocks local storage, so the edit cannot be kept." };
    }, [st.mode]);

    const save = useCallback((id, raw) => write(id, { html: sanitize(raw), by: st.uid || null, at: new Date().toISOString() }), [write, st.uid]);
    const reset = useCallback((id) => write(id, null), [write]);
    return { ...st, save, reset, user: caps.current.user };
  }

  function useNames(user, ids) {
    const [names, setNames] = useState({});
    const key = ids.slice().sort().join("|");
    useEffect(() => {
      if (!user || !ids.length) return;
      let dead = false;
      user.profiles(ids).then((ps) => {
        if (dead) return;
        const o = {};
        ids.forEach((id) => { o[id] = (ps && ps[id] && ps[id].name) || ""; });
        setNames(o);
      }).catch(() => {});
      return () => { dead = true; };
    }, [user, key]);
    return names;
  }

  /* ---------------- editable commentary ---------------- */
  function Commentary({ block, store, names }) {
    const key = docId(block.id);
    const ov = store.overrides[key];
    const current = ov ? ov.html : block.html;
    const safe = useMemo(() => sanitize(current), [current]);
    const [editing, setEditing] = useState(false);
    const [init, setInit] = useState("");
    const [busy, setBusy] = useState(false);
    const [msg, setMsg] = useState("");
    const ed = useRef(null);
    const canEdit = store.mode !== "init" && !store.readOnly && store.canWrite !== false;

    useEffect(() => {
      if (editing && ed.current) {
        ed.current.focus();
        const r = document.createRange(); r.selectNodeContents(ed.current); r.collapse(false);
        const sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
      }
    }, [editing]);

    const start = () => { setInit(safe); setMsg(""); setEditing(true); };
    const save = async () => {
      if (!ed.current) return;
      setBusy(true);
      const r = await store.save(block.id, ed.current.innerHTML);
      setBusy(false);
      if (r.ok) { setEditing(false); setMsg(""); } else setMsg(r.msg);
    };
    const restore = async () => { setBusy(true); const r = await store.reset(block.id); setBusy(false); if (!r.ok) setMsg(r.msg); };
    const cmd = (c) => { try { document.execCommand(c, false, null); } catch (e) { /* ignore */ } if (ed.current) ed.current.focus(); };
    const onKey = (e) => {
      if (e.key === "Escape") { e.preventDefault(); setEditing(false); setMsg(""); }
      if ((e.metaKey || e.ctrlKey) && e.key === "Enter") { e.preventDefault(); save(); }
    };
    const keep = (e) => e.preventDefault();
    const who = ov && ov.by ? names[ov.by] || "a colleague" : "";
    const edited = ov ? (store.mode === "local" ? "Edited in this browser" : "Edited" + (who ? " by " + who : "")) + (ov.at ? " · " + fmtDate(ov.at) : "") : "";

    return html`<div className=${"cm" + (editing ? " cm-editing" : "") + (ov ? " cm-edited" : "")}>
      ${editing
        ? html`<${Fragment}>
            <div className="cm-bar" role="toolbar" aria-label="Edit commentary">
              <button type="button" className="btn" onMouseDown=${keep} onClick=${() => cmd("bold")} aria-label="Bold"><b>B</b></button>
              <button type="button" className="btn" onMouseDown=${keep} onClick=${() => cmd("italic")} aria-label="Italic"><i>I</i></button>
              <button type="button" className="btn" onMouseDown=${keep} onClick=${() => cmd("insertUnorderedList")}>Bullets</button>
              <span className="sp"></span>
              <button type="button" className="btn pri" onClick=${save} disabled=${busy}>${busy ? "Saving…" : "Save"}</button>
              <button type="button" className="btn" onClick=${() => { setEditing(false); setMsg(""); }}>Cancel</button>
            </div>
            <div ref=${ed} className="prose cm-body" contentEditable="true" suppressContentEditableWarning=${true}
              role="textbox" aria-multiline="true" aria-label="Analyst commentary" onKeyDown=${onKey}
              dangerouslySetInnerHTML=${{ __html: init }}></div>
          </${Fragment}>`
        : html`<div className="prose cm-body" dangerouslySetInnerHTML=${{ __html: safe }}></div>`}
      <div className="cm-meta">
        ${ov ? html`<span className="chip">${edited}</span>` : null}
        ${!editing && canEdit ? html`<button type="button" className="lbtn ed" onClick=${start}>Edit commentary</button>` : null}
        ${!editing && ov && canEdit ? html`<button type="button" className="lbtn" onClick=${restore} disabled=${busy}>Restore original</button>` : null}
        ${editing ? html`<span>Esc cancels · Ctrl/⌘ + Enter saves</span>` : null}
        ${msg ? html`<span className="err" role="alert">${msg}</span>` : null}
      </div>
    </div>`;
  }

  /* ---------------- tables ---------------- */
  function Table({ block }) {
    const head = useMemo(() => block.head.map(sanitize), [block]);
    const rows = useMemo(() => block.rows.map((r) => r.map((c) => ({ h: sanitize(c), num: isNumCell(c) }))), [block]);
    return html`<div className="tbl-wrap"><table className="tbl">
      ${head.some((h) => textOf(h)) ? html`<thead><tr>${head.map((h, i) => html`<th key=${i} dangerouslySetInnerHTML=${{ __html: h }}></th>`)}</tr></thead>` : null}
      <tbody>${rows.map((r, ri) => html`<tr key=${ri}>${r.map((c, ci) => html`<td key=${ci} className=${c.num && ci > 0 ? "num" : ""} dangerouslySetInnerHTML=${{ __html: c.h }}></td>`)}</tr>`)}</tbody>
    </table></div>`;
  }

  /* ---------------- chart kit ---------------- */
  function useWidth(initial) {
    const ref = useRef(null);
    const [w, setW] = useState(initial || 640);
    useEffect(() => {
      const el = ref.current;
      if (!el || typeof ResizeObserver === "undefined") return;
      const ro = new ResizeObserver((es) => { for (const e of es) { const cw = Math.floor(e.contentRect.width); if (cw > 0) setW(cw); } });
      ro.observe(el);
      return () => ro.disconnect();
    }, []);
    return [ref, w];
  }
  function lin(d0, d1, r0, r1) { const k = (r1 - r0) / (d1 - d0 || 1); const f = (v) => r0 + (v - d0) * k; f.inv = (p) => d0 + (p - r0) / k; return f; }
  function ticks(min, max, count) {
    const span = max - min || 1, raw = span / (count || 5), p = Math.pow(10, Math.floor(Math.log10(raw))), e = raw / p;
    const step = (e >= 7.5 ? 10 : e >= 3.5 ? 5 : e >= 1.5 ? 2 : 1) * p, out = [];
    for (let v = Math.ceil(min / step) * step; v <= max + step * 1e-6; v += step) out.push(+v.toFixed(10));
    return out;
  }
  const openUrl = (u) => { if (u) window.open(u, "_blank", "noopener"); };
  function Mark({ url, label, onEnter, onLeave, children }) {
    // Each data mark links to its source document where the tool returned one.
    if (url) return html`<a href=${url} target="_blank" rel="noopener noreferrer" className="mark" aria-label=${label} onMouseEnter=${onEnter} onMouseLeave=${onLeave} onFocus=${onEnter} onBlur=${onLeave}>${children}</a>`;
    return html`<g className="mark" tabIndex="0" role="img" aria-label=${label} onMouseEnter=${onEnter} onMouseLeave=${onLeave} onFocus=${onEnter} onBlur=${onLeave}>${children}</g>`;
  }
  function Tip({ tip, w }) {
    if (!tip) return null;
    const left = Math.max(4, Math.min(tip.x + 14, w - 250));
    const top = Math.max(0, tip.y - 12);
    return html`<div className="tip" style=${{ left: left + "px", top: top + "px" }}>
      <div className="h">${tip.h}</div>${tip.b ? html`<div>${tip.b}</div>` : null}
      <div className="src">${tip.url ? "Click to open the source" : tip.sn || "Source link unavailable ‡"}</div></div>`;
  }
  function Frame({ title, legend, source, children, controls, id }) {
    return html`<figure className="chart" id=${id}>
      <figcaption className="chart-h"><span className="chart-t">${title}</span>
        ${legend ? html`<span className="legend">${legend.map((l) => html`<span className="lg" key=${l.t}><i className=${l.line ? "ln" : ""} style=${{ background: l.c }}></i>${l.t}</span>`)}</span>` : null}
        ${controls || null}</figcaption>
      ${children}
      ${source ? html`<div className="chart-src">${source}</div>` : null}
    </figure>`;
  }
  function YAxis({ y, tk, x0, x1, f }) {
    return html`<g className="ax">${tk.map((t) => html`<g key=${t}><line x1=${x0} x2=${x1} y1=${y(t)} y2=${y(t)} className=${t === 0 ? "base" : ""}></line><text x=${x0 - 6} y=${y(t) + 4} textAnchor="end">${f ? f(t) : t}</text></g>`)}</g>`;
  }

  /* Generic vertical bars: one or more series per category */
  function Bars({ cats, series, h, fmt, yfmt, labels, ariaLabel }) {
    const [ref, w] = useWidth();
    const [tip, setTip] = useState(null);
    const H = h || 230, m = { l: 44, r: 8, t: 18, b: 26 };
    const vals = series.flatMap((s) => s.values.map((v) => v.v));
    const lo = Math.min(0, ...vals), hi = Math.max(0, ...vals);
    const pad = (hi - lo) * 0.14 || 1;
    const y = lin(lo < 0 ? lo - pad * 0.6 : 0, hi + pad, H - m.b, m.t);
    const tk = ticks(lo < 0 ? lo - pad * 0.6 : 0, hi + pad, 4);
    const bw = (w - m.l - m.r) / cats.length, gw = Math.min(bw * 0.72, 30 * series.length + 8), sw = gw / series.length;
    return html`<div className="chart-box" ref=${ref}>
      <svg viewBox=${`0 0 ${w} ${H}`} width="100%" role="img" aria-label=${ariaLabel}>
        <${YAxis} y=${y} tk=${tk} x0=${m.l} x1=${w - m.r} f=${yfmt} />
        ${cats.map((c, i) => {
          const cx = m.l + bw * i + bw / 2;
          return html`<g key=${c}>
            ${series.map((s, j) => {
              const d = s.values[i]; if (!d || d.v === null || d.v === undefined) return null;
              const x = cx - gw / 2 + sw * j + 1, y0 = y(Math.max(0, d.v)), y1 = y(Math.min(0, d.v)), hh = Math.max(1, y1 - y0);
              const col = typeof s.color === "function" ? s.color(d.v) : s.color;
              const lab = `${c} · ${s.name}: ${fmt(d.v)}`;
              const enter = () => setTip({ x: x + sw / 2, y: y0, h: `${c} · ${s.name}`, b: fmt(d.v) + (d.note ? " · " + d.note : ""), url: d.url, sn: s.srcNote });
              return html`<${Mark} key=${s.name} url=${d.url} label=${lab} onEnter=${enter} onLeave=${() => setTip(null)}>
                <rect x=${x} y=${y0} width=${Math.max(2, sw - 2)} height=${hh} rx="2" style=${{ fill: col }}></rect>
                <rect x=${x - 2} y=${m.t} width=${sw + 2} height=${H - m.t - m.b} style=${{ fill: "transparent" }}></rect>
                ${labels && series.length === 1 ? html`<text className="vlab" x=${x + sw / 2 - 1} y=${d.v >= 0 ? y0 - 4 : y1 + 12} textAnchor="middle">${fmt(d.v)}</text>` : null}
              </${Mark}>`;
            })}
            <text className="vlab" x=${cx} y=${H - 8} textAnchor="middle" style=${{ fill: "var(--muted)" }}>${c}</text>
          </g>`;
        })}
      </svg><${Tip} tip=${tip} w=${w} /></div>`;
  }

  /* Generic lines over categories with end labels */
  function Lines({ cats, series, h, fmt, yfmt, domain, ariaLabel }) {
    const [ref, w] = useWidth();
    const [tip, setTip] = useState(null);
    const H = h || 230, m = { l: 40, r: 64, t: 14, b: 26 };
    const vals = series.flatMap((s) => s.values.map((v) => v.v));
    const lo = domain ? domain[0] : Math.min(0, ...vals), hi = domain ? domain[1] : Math.max(...vals) * 1.15;
    const x = (i) => m.l + ((w - m.l - m.r) * (cats.length === 1 ? 0.5 : i / (cats.length - 1)));
    const y = lin(lo, hi, H - m.b, m.t), tk = ticks(lo, hi, 4);
    return html`<div className="chart-box" ref=${ref}>
      <svg viewBox=${`0 0 ${w} ${H}`} width="100%" role="img" aria-label=${ariaLabel}>
        <${YAxis} y=${y} tk=${tk} x0=${m.l} x1=${w - m.r} f=${yfmt} />
        ${cats.map((c, i) => html`<text key=${c} className="vlab" x=${x(i)} y=${H - 8} textAnchor="middle" style=${{ fill: "var(--muted)" }}>${c}</text>`)}
        ${series.map((s) => {
          const d = s.values.map((v, i) => (i ? "L" : "M") + x(i).toFixed(1) + "," + y(v.v).toFixed(1)).join("");
          const last = s.values[s.values.length - 1];
          return html`<g key=${s.name}>
            <path d=${d} style=${{ fill: "none", stroke: s.color, strokeWidth: 2 }}></path>
            ${s.values.map((v, i) => html`<${Mark} key=${i} url=${v.url} label=${`${cats[i]} · ${s.name}: ${fmt(v.v)}`}
                onEnter=${() => setTip({ x: x(i), y: y(v.v), h: `${cats[i]} · ${s.name}`, b: fmt(v.v), url: v.url })} onLeave=${() => setTip(null)}>
                <circle cx=${x(i)} cy=${y(v.v)} r="4.5" style=${{ fill: s.color, stroke: "var(--panel)", strokeWidth: 2 }}></circle>
                <circle cx=${x(i)} cy=${y(v.v)} r="12" style=${{ fill: "transparent" }}></circle>
              </${Mark}>`)}
            <text className="dlab" x=${x(s.values.length - 1) + 9} y=${y(last.v) + 4} style=${{ fill: s.color }}>${fmt(last.v)}</text>
          </g>`;
        })}
      </svg><${Tip} tip=${tip} w=${w} /></div>`;
  }

  /* ---------------- specific charts ---------------- */
  function PriceChart() {
    const d = CH.price;
    const [ref, w] = useWidth(720);
    const [range, setRange] = useState("all");
    const [tip, setTip] = useState(null);
    const [cross, setCross] = useState(null);
    const pts = useMemo(() => d.series.map(([t, c]) => ({ t: Date.parse(t), c, ds: t })), []);
    const last = pts[pts.length - 1].t;
    const start = range === "1y" ? last - 365.25 * 864e5 : range === "3y" ? last - 3 * 365.25 * 864e5 : pts[0].t;
    const vis = pts.filter((p) => p.t >= start);
    const H = w < 560 ? 250 : 330, m = { l: 40, r: 12, t: 16, b: 26 };
    const x = lin(vis[0].t, last, m.l, w - m.r);
    const ymax = Math.max(...vis.map((p) => p.c)) * 1.12;
    const y = lin(0, ymax, H - m.b, m.t);
    const line = vis.map((p, i) => (i ? "L" : "M") + x(p.t).toFixed(1) + "," + y(p.c).toFixed(1)).join("");
    const area = line + `L${x(last).toFixed(1)},${y(0)}L${x(vis[0].t).toFixed(1)},${y(0)}Z`;
    const evs = d.events.map((e) => {
      const t = Date.parse(e.date);
      const near = pts.reduce((a, p) => (Math.abs(p.t - t) < Math.abs(a.t - t) ? p : a), pts[0]);
      return { ...e, t: near.t, c: near.c };
    }).filter((e) => e.t >= vis[0].t);
    const years = [];
    for (let yr = new Date(vis[0].t).getUTCFullYear() + 1; yr <= new Date(last).getUTCFullYear(); yr++) years.push(Date.UTC(yr, 0, 1));
    const months = range === "1y" ? [0, 3, 6, 9].flatMap((mo) => [2025, 2026].map((yr) => Date.UTC(yr, mo, 1))).filter((t) => t > vis[0].t && t < last).sort() : null;
    const onMove = (ev) => {
      const r = ev.currentTarget.getBoundingClientRect();
      const px = ((ev.clientX - r.left) / r.width) * w;
      if (px < m.l || px > w - m.r) { setCross(null); return; }
      const t = x.inv(px);
      let best = vis[0];
      for (const p of vis) if (Math.abs(p.t - t) < Math.abs(best.t - t)) best = p;
      setCross(best);
    };
    const tri = (e) => {
      const cx = x(e.t), cy = y(e.c) + (e.dir > 0 ? -12 : 12), s = 6;
      return e.dir > 0 ? `M${cx},${cy - s}L${cx + s},${cy + s * 0.8}L${cx - s},${cy + s * 0.8}Z` : `M${cx},${cy + s}L${cx + s},${cy - s * 0.8}L${cx - s},${cy - s * 0.8}Z`;
    };
    const controls = html`<span className="seg" role="group" aria-label="Time range">
      ${[["all", "Since IPO"], ["3y", "3 years"], ["1y", "1 year"]].map(([k, t]) => html`<button type="button" key=${k} aria-pressed=${range === k} onClick=${() => setRange(k)}>${t}</button>`)}</span>`;
    return html`<${Frame} id="price-chart" title="Share price since IPO with catalysts (weekly close, US$)" controls=${controls}
        legend=${[{ t: "Weekly close", c: "var(--s1)", line: true }, { t: "▲ positive catalyst", c: "var(--good)" }, { t: "▼ negative catalyst", c: "var(--bad)" }]}
        source=${html`<span>Prices: ${d.source}. Catalyst markers link to the cited filing or call; click one to open it.</span>`}>
      <div className="chart-box" ref=${ref}>
        <svg viewBox=${`0 0 ${w} ${H}`} width="100%" role="img" aria-label="Coupang weekly closing price since the March 2021 IPO, with catalyst markers" onMouseMove=${onMove} onMouseLeave=${() => setCross(null)}>
          <${YAxis} y=${y} tk=${ticks(0, ymax, 4)} x0=${m.l} x1=${w - m.r} f=${(t) => "$" + t} />
          <g className="ax">${(months || years).map((t) => html`<text key=${t} x=${x(t)} y=${H - 8} textAnchor="middle">${months ? new Date(t).toLocaleDateString("en-GB", { month: "short", year: "2-digit", timeZone: "UTC" }) : new Date(t).getUTCFullYear()}</text>`)}</g>
          <path d=${area} style=${{ fill: "var(--s1)", opacity: 0.1 }}></path>
          <path d=${line} style=${{ fill: "none", stroke: "var(--s1)", strokeWidth: 2 }}></path>
          ${cross ? html`<g><line x1=${x(cross.t)} x2=${x(cross.t)} y1=${m.t} y2=${H - m.b} style=${{ stroke: "var(--line-2)" }}></line>
            <circle cx=${x(cross.t)} cy=${y(cross.c)} r="4.5" style=${{ fill: "var(--s1)", stroke: "var(--panel)", strokeWidth: 2 }}></circle></g>` : null}
          ${evs.map((e) => html`<${Mark} key=${e.date} url=${e.url} label=${e.text}
              onEnter=${() => setTip({ x: x(e.t), y: y(e.c), h: fmtWeek(e.date), b: e.text, url: e.url })} onLeave=${() => setTip(null)}>
              <path d=${tri(e)} style=${{ fill: e.dir > 0 ? "var(--good)" : "var(--bad)", stroke: "var(--panel)", strokeWidth: 1.5 }}></path>
              <circle cx=${x(e.t)} cy=${y(e.c) + (e.dir > 0 ? -12 : 12)} r="13" style=${{ fill: "transparent" }}></circle>
            </${Mark}>`)}
        </svg>
        ${tip ? html`<${Tip} tip=${tip} w=${w} />` : cross ? html`<div className="tip" style=${{ left: Math.max(4, Math.min(x(cross.t) + 14, w - 190)) + "px", top: Math.max(0, y(cross.c) - 46) + "px" }}>
          <div className="h">${fmtWeek(cross.ds)}</div><div>Close US$${cross.c.toFixed(2)}</div></div>` : null}
      </div>
    </${Frame}>`;
  }

  function AnnualCharts() {
    const a = CH.annual, yrs = a.years;
    const pt = (arr, f) => arr.map(([v, url]) => ({ v: f ? f(v) : v, url }));
    const mg = (num) => num.map(([v, url], i) => ({ v: (v / a.rev[i][0]) * 100, url }));
    return html`<div className="pair">
      <${Frame} title="Revenue (US$bn)" source="S&P Capital IQ annual filings; click a bar for the source.">
        <${Bars} cats=${yrs} series=${[{ name: "Revenue", color: "var(--s1)", values: pt(a.rev, (v) => v / 1000) }]} labels=${true} fmt=${(v) => v.toFixed(1)} yfmt=${(t) => t} ariaLabel="Revenue by fiscal year, US$bn" />
      </${Frame}>
      <${Frame} title="Margins (% of revenue) [d]" legend=${[{ t: "Gross", c: "var(--s1)", line: true }, { t: "EBITDA (S&P)", c: "var(--s2)", line: true }, { t: "EBIT", c: "var(--s3)", line: true }]}
          source="Margins derived from S&P Capital IQ gross profit, EBITDA and operating income; points link to the numerator's source.">
        <${Lines} cats=${yrs} series=${[{ name: "Gross margin", color: "var(--s1)", values: mg(a.gp) }, { name: "EBITDA margin", color: "var(--s2)", values: mg(a.ebitda) }, { name: "EBIT margin", color: "var(--s3)", values: mg(a.ebit) }]}
          fmt=${(v) => pct(v)} yfmt=${(t) => t + "%"} domain=${[-8, 34]} ariaLabel="Gross, EBITDA and EBIT margin by fiscal year" />
      </${Frame}>
    </div>`;
  }

  function QuarterlyCharts() {
    const q = CH.quarterly;
    return html`<div className="pair">
      <${Frame} title="Quarterly revenue (US$bn)" source="S&P Capital IQ quarterly data; click a bar for the source.">
        <${Bars} cats=${q.q} series=${[{ name: "Revenue", color: "var(--s1)", values: q.rev.map(([v, url]) => ({ v: v / 1000, url })) }]} labels=${true} fmt=${(v) => v.toFixed(2)} ariaLabel="Quarterly revenue, US$bn" />
      </${Frame}>
      <${Frame} title="GAAP operating income (US$m)" legend=${[{ t: "Profit", c: "var(--pos)" }, { t: "Loss", c: "var(--neg)" }]} source="S&P Capital IQ quarterly data. Q2'26 includes ~US$410m of PIPC fines.">
        <${Bars} cats=${q.q} series=${[{ name: "Operating income", color: (v) => (v >= 0 ? "var(--pos)" : "var(--neg)"), values: q.op.map(([v, url]) => ({ v, url })) }]} labels=${true} fmt=${(v) => Math.round(v).toLocaleString("en-US")} ariaLabel="Quarterly GAAP operating income, US$m" />
      </${Frame}>
    </div>`;
  }

  function SegmentCharts() {
    const s = CH.segments, pv = (arr) => arr.map(([v, url]) => ({ v, url }));
    const lg = [{ t: "Product Commerce", c: "var(--s1)" }, { t: "Developing Offerings", c: "var(--s2)" }];
    return html`<div className="pair">
      <${Frame} title="Segment revenue (US$bn)" legend=${lg} source=${"Company disclosures via ProntoNLP. " + s.notes}>
        <${Bars} cats=${s.years} series=${[{ name: "Product Commerce", color: "var(--s1)", values: pv(s.pc_rev) }, { name: "Developing Offerings", color: "var(--s2)", values: pv(s.do_rev) }]} fmt=${(v) => "US$" + v.toFixed(1) + "bn"} ariaLabel="Segment revenue by year" />
      </${Frame}>
      <${Frame} title="Segment adjusted EBITDA (US$bn)" legend=${lg} source="Company disclosures via ProntoNLP; click a bar for the cited sentence.">
        <${Bars} cats=${s.years} series=${[{ name: "Product Commerce", color: "var(--s1)", values: pv(s.pc_ebitda) }, { name: "Developing Offerings", color: "var(--s2)", values: pv(s.do_ebitda) }]} fmt=${(v) => "US$" + v.toFixed(2) + "bn"} ariaLabel="Segment adjusted EBITDA by year" />
      </${Frame}>
    </div>`;
  }

  function MarginChart() {
    const g = CH.margins, pv = (arr) => arr.map(([v, url]) => ({ v, url }));
    return html`<${Frame} title="Margin reset after the Nov-25 data incident (adj. EBITDA margin, %)" legend=${[{ t: "Product Commerce", c: "var(--s1)", line: true }, { t: "Consolidated", c: "var(--s2)", line: true }]} source="Earnings calls via ProntoNLP; each point links to the cited sentence.">
      <${Lines} cats=${g.q} series=${[{ name: "Product Commerce", color: "var(--s1)", values: pv(g.pc) }, { name: "Consolidated", color: "var(--s2)", values: pv(g.cons) }]} fmt=${(v) => pct(v)} yfmt=${(t) => t + "%"} domain=${[0, 10]} ariaLabel="Quarterly adjusted EBITDA margins" />
    </${Frame}>`;
  }

  function SentimentCharts() {
    const r = CH.sentiment.rows, cats = r.map((x) => x.call);
    return html`<div className="pair">
      <${Frame} title="ProntoNLP call sentiment (-1 to +1)" legend=${[{ t: "Before the incident", c: "var(--s1)" }, { t: "Below 0.6", c: "var(--neg)" }]} source="ProntoNLP document sentiment per earnings call; click a bar to open the transcript.">
        <${Bars} cats=${cats} series=${[{ name: "Sentiment", color: (v) => (v < 0.6 ? "var(--neg)" : "var(--s1)"), values: r.map((x) => ({ v: x.sent, url: x.url, note: "call on " + x.date })) }]} labels=${true} fmt=${(v) => v.toFixed(2)} h=${220} ariaLabel="Earnings call sentiment score by quarter" />
      </${Frame}>
      <${Frame} title="Negative events as % of polar events [d]" source="Derived from ProntoNLP positive and negative event counts per call.">
        <${Lines} cats=${cats} series=${[{ name: "Negative share", color: "var(--s2)", values: r.map((x) => ({ v: (x.neg / (x.neg + x.pos)) * 100, url: x.url })) }]} fmt=${(v) => pct(v, 0)} yfmt=${(t) => t + "%"} domain=${[0, 35]} h=${220} ariaLabel="Share of negative events per call" />
      </${Frame}>
    </div>`;
  }

  function RegressionChart() {
    const g = CH.regression;
    const [ref, w] = useWidth();
    const [tip, setTip] = useState(null);
    const H = w < 560 ? 280 : 340, m = { l: 40, r: 12, t: 12, b: 34 };
    const pts = g.points.filter((p) => !g.excluded.includes(p.name));
    const x = lin(-5, 25, m.l, w - m.r), y = lin(0, 4.8, H - m.b, m.t);
    const fit = (v) => g.a + g.b * v;
    const show = new Set(["Amazon", "MercadoLibre", "NAVER", "PDD Holdings", "E-MART", "Allegro", "Walmart"]);
    const dot = (p, col, r, lab, labDx, labDy) => html`<${Mark} key=${p.name} url=${p.url} label=${`${p.name}: EBIT margin ${pct(p.x)}, EV/Sales ${p.y.toFixed(2)}x`}
        onEnter=${() => setTip({ x: x(p.x), y: y(p.y), h: p.name, b: `EBIT margin ${pct(p.x)} · EV/Sales ${p.y.toFixed(2)}x · line implies ${fit(p.x).toFixed(2)}x`, url: p.url })} onLeave=${() => setTip(null)}>
        <circle cx=${x(p.x)} cy=${y(p.y)} r=${r} style=${{ fill: col, stroke: "var(--panel)", strokeWidth: 2 }}></circle>
        <circle cx=${x(p.x)} cy=${y(p.y)} r="12" style=${{ fill: "transparent" }}></circle>
        ${lab ? html`<text className=${col === "var(--peer)" ? "vlab" : "dlab"} x=${x(p.x) + (labDx || 7)} y=${y(p.y) + (labDy || -7)} textAnchor=${labDx < 0 ? "end" : "start"} style=${{ fill: col === "var(--peer)" ? "var(--muted)" : col }}>${lab}</text>` : null}
      </${Mark}>`;
    return html`<${Frame} id="regression-chart" title="EV/Sales vs EBIT margin, listed peers (LTM)"
        legend=${[{ t: "Peers", c: "var(--peer)" }, { t: "Coupang LTM", c: "var(--s2)" }, { t: "Coupang FY25", c: "var(--s1)" }, { t: "OLS fit", c: "var(--muted)", line: true }]}
        source=${`OLS: EV/Sales = ${g.a.toFixed(2)} + ${g.b.toFixed(3)} × EBIT margin (%), R² = ${g.r2.toFixed(2)}, n = ${g.n} (Jumia excluded). S&P Capital IQ LTM financials; points link to each company's operating-income source.`}>
      <div className="chart-box" ref=${ref}>
        <svg viewBox=${`0 0 ${w} ${H}`} width="100%" role="img" aria-label="Scatter of EV to sales against EBIT margin for listed peers, with Coupang highlighted">
          <${YAxis} y=${y} tk=${[0, 1, 2, 3, 4]} x0=${m.l} x1=${w - m.r} f=${(t) => t + "x"} />
          <g className="ax">${[-5, 0, 5, 10, 15, 20, 25].map((t) => html`<text key=${t} x=${x(t)} y=${H - 16} textAnchor="middle">${t}%</text>`)}
            <text x=${(m.l + w - m.r) / 2} y=${H - 2} textAnchor="middle">EBIT margin, LTM</text></g>
          <line x1=${x(-5)} y1=${y(fit(-5))} x2=${x(25)} y2=${y(fit(25))} style=${{ stroke: "var(--muted)", strokeWidth: 1.5, strokeDasharray: "5 4" }}></line>
          ${pts.map((p) => dot(p, "var(--peer)", 5, show.has(p.name) && w > 480 ? p.name : null, p.name === "Allegro" || p.name === "PDD Holdings" ? -7 : 7))}
          ${dot(g.fy25, "var(--s1)", 6.5, "Coupang FY25", 8, 18)}
          ${dot({ ...g.cpng, name: "Coupang LTM" }, "var(--s2)", 6.5, "Coupang LTM", -8)}
        </svg><${Tip} tip=${tip} w=${w} /></div>
    </${Frame}>`;
  }

  function HistChart() {
    const g = CH.hist;
    return html`<${Frame} title="EV/Sales at each year-end: Coupang vs core-peer median [d]" legend=${[{ t: "Coupang", c: "var(--s1)" }, { t: "Core-peer median", c: "var(--s2)" }]}
        source="Derived from ProntoNLP year-end prices and S&P Capital IQ revenue, net debt and diluted shares. Core peers: Amazon, MercadoLibre, Sea, NAVER, E-MART, Lotte Shopping.">
      <${Bars} cats=${g.lab.map((l) => l.replace(" (LTM)", ""))} series=${[{ name: "Coupang", color: "var(--s1)", srcNote: "Derived [d] from cited inputs", values: g.cpng.map((v) => ({ v })) }, { name: "Core-peer median", color: "var(--s2)", srcNote: "Derived [d] from cited inputs", values: g.peer.map((v) => ({ v })) }]}
        fmt=${(v) => v.toFixed(2) + "x"} yfmt=${(t) => t + "x"} ariaLabel="EV to sales at each year-end for Coupang and the core-peer median" />
    </${Frame}>`;
  }

  function BridgeChart() {
    const st = CH.bridge.steps;
    const [ref, w] = useWidth();
    const [tip, setTip] = useState(null);
    const H = 260, m = { l: 48, r: 8, t: 22, b: 40 };
    const y = lin(0, 2900, H - m.b, m.t), bw = (w - m.l - m.r) / st.length;
    let run = 0;
    return html`<${Frame} id="bridge-chart" title="Base case: adjusted EBITDA bridge, FY26E to FY28E (US$m) [e]" legend=${[{ t: "Total", c: "var(--s1)" }, { t: "Increase", c: "var(--s3)" }]} source="Analyst model [e]; see section 11 for the assumptions.">
      <div className="chart-box" ref=${ref}><svg viewBox=${`0 0 ${w} ${H}`} width="100%" role="img" aria-label="Waterfall of adjusted EBITDA from FY26E to FY28E">
        <${YAxis} y=${y} tk=${[0, 500, 1000, 1500, 2000, 2500]} x0=${m.l} x1=${w - m.r} f=${(t) => t.toLocaleString("en-US")} />
        ${st.map(([lab, v, k], i) => {
          const cx = m.l + bw * i + bw / 2, bwid = Math.min(bw * 0.6, 70);
          const b0 = k === "total" ? 0 : run, b1 = k === "total" ? v : run + v;
          if (k === "total") run = v; else run += v;
          const yTop = y(Math.max(b0, b1)), hh = Math.abs(y(b0) - y(b1));
          const words = lab.split(" "), half = Math.ceil(words.length / 2);
          return html`<g key=${lab}>
            <${Mark} label=${`${lab}: ${v.toLocaleString("en-US")}`} onEnter=${() => setTip({ x: cx, y: yTop, h: lab, b: (k === "total" ? "" : "+") + v.toLocaleString("en-US") + " US$m [e]" })} onLeave=${() => setTip(null)}>
              <rect x=${cx - bwid / 2} y=${yTop} width=${bwid} height=${Math.max(1, hh)} rx="2" style=${{ fill: k === "total" ? "var(--s1)" : "var(--s3)" }}></rect>
            </${Mark}>
            <text className="vlab" x=${cx} y=${yTop - 5} textAnchor="middle" style=${{ fontWeight: 700 }}>${(k === "total" ? "" : "+") + v.toLocaleString("en-US")}</text>
            <text className="vlab" x=${cx} y=${H - 22} textAnchor="middle" style=${{ fill: "var(--muted)" }}>${words.slice(0, half).join(" ")}</text>
            <text className="vlab" x=${cx} y=${H - 9} textAnchor="middle" style=${{ fill: "var(--muted)" }}>${words.slice(half).join(" ")}</text>
          </g>`;
        })}
      </svg><${Tip} tip=${tip ? { ...tip, url: null, sn: "Analyst estimate [e]" } : null} w=${w} /></div>
    </${Frame}>`;
  }

  function Scenarios() {
    const d = CH.scenarios;
    const [pBear, setBear] = useState(25);
    const [pBull, setBull] = useState(25);
    const pBase = Math.max(0, 100 - pBear - pBull);
    const v = Object.fromEntries(d.rows.map((r) => [r.k, r.v]));
    const pw = (pBear * v.bear + pBase * v.base + pBull * v.bull) / 100;
    const up = pw / d.price - 1;
    const [ref, w] = useWidth(360);
    const H = 190, m = { l: 34, r: 8, t: 18, b: 24 };
    const y = lin(0, 36, H - m.b, m.t), bw = (w - m.l - m.r) / 3;
    const col = { bear: "var(--s2)", base: "var(--s1)", bull: "var(--s3)" };
    const setB = (val) => { const b = Math.min(100, Math.max(0, +val)); setBear(b); if (b + pBull > 100) setBull(100 - b); };
    const setU = (val) => { const u = Math.min(100, Math.max(0, +val)); setBull(u); if (u + pBear > 100) setBear(100 - u); };
    return html`<div className="card scn" id="scenario-panel">
      <h3>Scenario value, 12 months (US$ per share) [e]</h3>
      <div className="pw">US$${pw.toFixed(1)}<small>${sgn(up * 100, 0)}% vs US$${d.price.toFixed(2)}</small></div>
      <div className="legend" style=${{ margin: "4px 0 2px" }}>
        <span className="lg"><svg width="18" height="6" aria-hidden="true"><line x1="0" x2="18" y1="3" y2="3" style=${{ stroke: "var(--ink-2)", strokeDasharray: "5 4", strokeWidth: 1.5 }}></line></svg>Price US$${d.price.toFixed(2)}</span>
        <span className="lg"><svg width="18" height="6" aria-hidden="true"><line x1="0" x2="18" y1="3" y2="3" style=${{ stroke: "var(--accent)", strokeDasharray: "2 3", strokeWidth: 1.8 }}></line></svg>Probability-weighted US$${pw.toFixed(1)}</span>
      </div>
      <div className="chart-box" ref=${ref}><svg viewBox=${`0 0 ${w} ${H}`} width="100%" role="img" aria-label="Bear, base and bull value per share with the current price and the probability-weighted value">
        <${YAxis} y=${y} tk=${[0, 10, 20, 30]} x0=${m.l} x1=${w - m.r} f=${(t) => "$" + t} />
        ${d.rows.map((r, i) => {
          const cx = m.l + bw * i + bw / 2, bwid = Math.min(bw * 0.56, 64);
          return html`<g key=${r.k}><rect x=${cx - bwid / 2} y=${y(r.v)} width=${bwid} height=${y(0) - y(r.v)} rx="2" style=${{ fill: col[r.k] }}></rect>
            <text className="vlab" x=${cx} y=${y(r.v) - 5} textAnchor="middle" style=${{ fontWeight: 700 }}>$${r.v.toFixed(1)}</text>
            <text className="vlab" x=${cx} y=${H - 7} textAnchor="middle" style=${{ fill: "var(--muted)" }}>${r.label}</text></g>`;
        })}
        <line x1=${m.l} x2=${w - m.r} y1=${y(d.price)} y2=${y(d.price)} style=${{ stroke: "var(--ink-2)", strokeDasharray: "5 4", strokeWidth: 1.3 }}></line>
        <line x1=${m.l} x2=${w - m.r} y1=${y(pw)} y2=${y(pw)} style=${{ stroke: "var(--accent)", strokeDasharray: "2 3", strokeWidth: 1.6 }}></line>
      </svg></div>
      <div className="sl"><label htmlFor="p-bear">Bear</label><input id="p-bear" type="range" min="0" max="100" step="5" value=${pBear} onInput=${(e) => setB(e.target.value)} onChange=${(e) => setB(e.target.value)} /><output htmlFor="p-bear">${pBear}%</output></div>
      <div className="sl"><span>Base</span><input type="range" min="0" max="100" value=${pBase} disabled aria-label="Base probability (100% less bear and bull)" /><output>${pBase}%</output></div>
      <div className="sl"><label htmlFor="p-bull">Bull</label><input id="p-bull" type="range" min="0" max="100" step="5" value=${pBull} onInput=${(e) => setU(e.target.value)} onChange=${(e) => setU(e.target.value)} /><output htmlFor="p-bull">${pBull}%</output></div>
      <div className="scn-why">${d.rows.map((r) => html`<div key=${r.k}><b style=${{ color: "var(--ink)" }}>${r.label}</b><span>${r.why}</span></div>`)}</div>
      <div className="note">Move the bear and bull weights; base takes the remainder. House view: 25 / 50 / 25 gives US$20.8. Values are our estimates on NTM sales at Oct-2027 (section 22).</div>
    </div>`;
  }

  function SupplyChain() {
    const g = CH.supplychain;
    return html`<${Frame} id="supply-chain" title="Value chain: upstream inputs to the end customer" source=${g.legend + " ✓ = named in filings or calls; [u] = unverified, illustrative."}>
      <div className="sc">${g.stages.map((s) => html`<div key=${s.title} className=${"sc-col" + (s.core ? " core" : "")}><h4>${s.title}</h4>
        ${s.items.map((it, i) => html`<p key=${i} dangerouslySetInnerHTML=${{ __html: sanitize(it) }}></p>`)}</div>`)}</div>
      <div className="sc-boxes">${g.boxes.map((b) => html`<div key=${b.title} className="sc-box"><h4>${b.title}</h4><div dangerouslySetInnerHTML=${{ __html: sanitize(b.html) }}></div></div>`)}</div>
    </${Frame}>`;
  }

  function Chart({ k }) {
    switch (k) {
      case "price": return html`<p className="jump">The weekly price chart with catalyst markers is at the <a href="#price-chart">top of the page</a>.</p>`;
      case "scenarios": return html`<p className="jump">Adjust the scenario weights in the <a href="#scenario-panel">scenario panel</a> at the top of the page.</p>`;
      case "bridge": return html`<${BridgeChart} />`;
      case "annual": return html`<${Fragment}><${AnnualCharts} /><${QuarterlyCharts} /></${Fragment}>`;
      case "segments": return html`<${SegmentCharts} />`;
      case "margins": return html`<${MarginChart} />`;
      case "sentiment": return html`<${SentimentCharts} />`;
      case "regression": return html`<${RegressionChart} />`;
      case "hist": return html`<${HistChart} />`;
      case "supplychain": return html`<${SupplyChain} />`;
      default: return null;
    }
  }

  /* ---------------- page ---------------- */
  function Section({ sec, store, names }) {
    return html`<section id=${sec.id} className="sec" aria-labelledby=${sec.id + "-h"}>
      <header className="sec-h"><span className="sec-num">${sec.num || "·"}</span><h2 id=${sec.id + "-h"}>${sec.title}</h2></header>
      ${sec.blocks.map((b, i) =>
        b.t === "c" ? html`<${Commentary} key=${b.id} block=${b} store=${store} names=${names} />`
        : b.t === "table" ? html`<${Table} key=${"t" + i} block=${b} />`
        : b.t === "h" ? html`<h3 key=${"h" + i} id=${b.id} className=${"sub-h lvl" + b.level}>${b.text}</h3>`
        : b.t === "chart" ? html`<${Chart} key=${"c" + i} k=${b.key} />` : null)}
    </section>`;
  }

  function useActive(ids) {
    const [active, setActive] = useState(ids[0]);
    useEffect(() => {
      if (typeof IntersectionObserver === "undefined") return;
      const seen = new Map();
      const io = new IntersectionObserver((es) => {
        es.forEach((e) => seen.set(e.target.id, e.isIntersecting ? e.boundingClientRect.top : null));
        const vis = [...seen.entries()].filter(([, t]) => t !== null).sort((a, b) => a[1] - b[1]);
        if (vis.length) setActive(vis[0][0]);
      }, { rootMargin: "-70px 0px -55% 0px" });
      ids.forEach((id) => { const el = document.getElementById(id); if (el) io.observe(el); });
      return () => io.disconnect();
    }, []);
    return active;
  }

  function StatusPill({ store }) {
    if (store.mode === "init") return html`<span className="pill st-init">Connecting commentary…</span>`;
    if (store.readOnly || store.canWrite === false) return html`<span className="pill st-ro" title="You can read the commentary but not change it">Commentary: read-only</span>`;
    if (store.mode === "shared") return html`<span className="pill st-shared" title="Edits are saved for everyone who opens this dashboard">Commentary edits: shared</span>`;
    return html`<span className="pill st-local" title="Edits are kept in this browser only">Commentary edits: this browser only</span>`;
  }

  function App() {
    const store = useStore();
    const editorIds = useMemo(() => [...new Set(Object.values(store.overrides).map((o) => o && o.by).filter((x) => typeof x === "string"))], [store.overrides]);
    const names = useNames(store.user, editorIds);
    const secs = DATA.sections;
    const active = useActive(secs.map((s) => s.id));
    const M = DATA.meta;
    const nEdited = Object.keys(store.overrides).length;
    const toc = (cls) => html`<ol>${secs.map((s) => html`<li key=${s.id}><a href=${"#" + s.id} className=${cls && active === s.id ? "on" : ""}><span className="n">${s.num || "·"}</span><span>${s.title}</span></a></li>`)}</ol>`;
    return html`<div className="cp-app">
      <div className="cp-top">
        <span className="nm">${M.company}<span>${M.ticker}</span></span>
        <span className="pill buy">${M.rating}</span>
        <span className="pill">Target US$${M.target.toFixed(0)} · ${sgn((M.target / M.price - 1) * 100, 0)}%</span>
        <span className="pill">US$${M.price.toFixed(2)} · ${M.priceDate}</span>
        <span className="grow"></span>
        <${StatusPill} store=${store} />
        ${nEdited ? html`<span className="pill">${nEdited} edited section${nEdited > 1 ? "s" : ""}</span>` : null}
      </div>
      <div className="band"><div className="band-in">
        <div>
          <div className="eyebrow">Institutional equity research · ${M.asOf} · ${M.conviction}</div>
          <h1>A temporary glitch, priced as a permanent one</h1>
          <p className="sub">Coupang's customers came back after the Nov-25 data incident; margins, the won and the regulators have not yet. At 0.79x sales the stock prices today's 1-2% margins as permanent. Every figure links to its S&P Capital IQ or ProntoNLP source; commentary is editable in place.</p>
        </div>
        <div className="tiles">${M.tiles.map((t) => html`<div className="tile" key=${t.k}><div className="k">${t.k}</div>
          <div className="v">${t.url ? html`<a href=${t.url} target="_blank" rel="noopener noreferrer">${t.v}</a>` : t.v}</div><div className="s">${t.s}</div></div>`)}</div>
      </div></div>
      <div className="cp-layout">
        <nav className="toc" aria-label="Report sections"><h2>Contents</h2>${toc(true)}</nav>
        <main className="cp-main">
          <details className="toc-m"><summary>Jump to a section</summary>${toc(false)}</details>
          <div className="overview">
            <div className="card"><${PriceChart} /></div>
            <${Scenarios} />
          </div>
          ${secs.map((s) => html`<${Section} key=${s.id} sec=${s} store=${store} names=${names} />`)}
          <section className="sec" id="provenance" aria-labelledby="provenance-h">
            <header className="sec-h"><span className="sec-num">·</span><h2 id="provenance-h">Data provenance</h2></header>
            <div className="prov">
              <dl>
                <dt>Sources</dt><dd>S&P Global Capital IQ (financials, deal targets, peers) and ProntoNLP (filings, transcripts, sentiment, prices, consensus). No web browsing, no SQL.</dd>
                <dt>Tool calls</dt><dd>${M.calls.total} logged calls: ${M.calls.sp} to S&P Capital IQ and ${M.calls.pronto} to ProntoNLP (${M.calls.errors} returned errors). The full log is in the separate data-provenance document.</dd>
                <dt>Freshness</dt><dd>S&P annual data to FY2025 and quarterly to Q2'26 (30-Jun-2026); prices to 9-Oct-2026; latest call 4-Aug-2026 (Q2'26).</dd>
                <dt>Symbols</dt><dd>‡ figure returned without a source link · [d] derived from cited inputs · [e] our estimate · [u] unverified, context only.</dd>
              </dl>
            </div>
          </section>
          <p className="foot-note">Prepared ${M.asOf}. Not investment advice. Commentary edits are attributed to the editor and can be restored to the original text at any time.</p>
        </main>
      </div>
    </div>`;
  }

  ReactDOM.createRoot(document.getElementById("cp-root")).render(html`<${App} />`);
})();
