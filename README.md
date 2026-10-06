# EER Lab — Generalization & Specialization Visualizer

An interactive DBMS/EER (Enhanced Entity-Relationship) learning platform: a diagram
visualizer, a table/SQL-to-EER import workbench, a 30-topic Learn path, worked
examples, a practice question bank, an AI-generated quiz, a competitive-questions
section, and progress tracking — all client-side, no server required.

## Quick start

Just open **`index.html`** in any browser. That's the whole app — no build step
needed to *use* it. Everything (progress, quiz history, uploaded images) is stored
in that browser only, via `localStorage` and `IndexedDB`.

## Repo structure

```
index.html        ← the built, ready-to-deploy app (open this)
build.py           ← concatenates src/ into index.html
src/
  01_style.css      ← design system, layout, diagram styling
  02_core.js        ← DOM helpers, storage (LS/DB/IDB), toasts/modals, router
  03_eer.js         ← EER data model, layout engine, SVG rendering, relational mapping
  04_import.js      ← CSV/paste parsing, SQL DDL parser, structure-detection heuristics
  05a_content.js    ← example models, worked examples, try-yourself scenarios, practice bank
  05b_topics.js     ← Learn path topics 1–12 (ER basics → generalization/specialization)
  05c_topics.js     ← Learn path topics 13–30 (constraints → mapping → exam prep)
  06_views1.js      ← app shell/nav, interactive widgets, Home view, Visualizer view
  07_views2.js      ← Table/SQL import workbench, Learn view, Examples view
  08_views3.js       ← Practice, quiz engine, AI Quiz, Competitive Questions, Progress,
                       Leaderboard, Admin/Content Manager, Help, Search, boot()
```

## Rebuilding from source

If you edit anything under `src/`, regenerate `index.html`:

```bash
python3 build.py
```

This just concatenates the CSS and JS files in order into a single self-contained
HTML file (no bundler, no npm dependencies — pure Python stdlib).

## Deploying

`index.html` is fully static and self-contained (fonts load from Google Fonts with
a system-font fallback; everything else is inline). Any static host works:

- **GitHub Pages** — push this repo, then Settings → Pages → Deploy from branch
  `main`, folder `/ (root)`.
- **Netlify** — drag the repo folder onto app.netlify.com/drop.
- **Cloudflare Pages / Vercel** — connect the repo, no build command needed
  (or set build command to `python3 build.py`, output directory `.`).

## What doesn't work outside Claude

The **AI Quiz** and **"Ask Claude to read the diagram"** features call a Claude
runtime capability (`window.claude`) that only exists inside claude.ai/Claude
apps. Outside that environment these features detect their own unavailability
and hide/disable themselves; everything else (Visualizer, Table/SQL import,
Learn, Examples, Practice bank, Progress, Leaderboard, Admin) works identically
in any browser.

## Data & honesty notes

- No accounts, no server: all data is per-browser (`localStorage` + `IndexedDB`).
- The Leaderboard is explicitly labeled as personal/single-browser, not a real
  multi-user ranking.
- **Competitive Questions** starts empty. Nothing is pre-filled — real GATE/UGC
  NET questions must be added (with source) via the Admin panel after being
  checked against an official paper.
- **AI Quiz** questions are generated live and always labeled AI-generated;
  they are never presented as real exam questions.
- No videos are pre-filled (YouTube links must be added and verified via Admin).

## License

Add a license of your choice here (e.g. MIT) before making the repo public.
