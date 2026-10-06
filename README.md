
## How the pieces fit together

The app is a single-page application with a tiny hand-written hash router (`#/visualizer`, `#/learn/topic-id`, etc.) — no framework, no build tooling beyond the one Python concatenation script. All source files are plain JavaScript and CSS; `build.py` simply stitches them into one `<style>` block and one `<script>` block inside an HTML shell, in a fixed order (numbered filenames reflect load order and rough dependency order — core utilities first, the EER engine next, then content, then the views that use all of the above).

This means:
- There is **no npm, no bundler, no transpilation step**.
- Editing behavior means editing the relevant `src/*.js` file directly.
- Editing content (topics, practice questions, examples) means editing `src/05a_content.js`, `05b_topics.js`, or `05c_topics.js`, which are plain data/config-style JS.

## Rebuilding from source

Only needed if you change anything under `src/`:

```bash
python3 build.py
```

This regenerates `index.html` from the current contents of `src/`. Requires nothing beyond Python 3's standard library. Commit both the changed source file(s) and the regenerated `index.html` together.

## Deploying

`index.html` is fully static and self-contained — its only external network request is for Google Fonts (with a system-font fallback if that's unreachable). Any static host works:

| Host | Steps |
|---|---|
| **GitHub Pages** | Push this repo → **Settings → Pages** → Source: Deploy from branch `main`, folder `/ (root)` → live at `https://<username>.github.io/<repo>/` |
| **Netlify** | Drag the project folder onto [app.netlify.com/drop](https://app.netlify.com/drop) |
| **Vercel** | Import the repo — no build command or output directory needed (or set build command to `python3 build.py`) |
| **Cloudflare Pages** | Connect the repo, same as Vercel |
| **Any other static host / school server** | Just copy `index.html` into the web root |

## Data & storage

| What | Where | Notes |
|---|---|---|
| Learning progress, quiz history | `localStorage` | Per-browser, never synced |
| Uploaded reference images | `IndexedDB` | Per-browser |
| Admin content (videos, resources, verified questions) | `localStorage` | Exportable as JSON backup |
| AI Quiz questions | Not stored as "real" content | Generated live, clearly tagged, excluded from Competitive Questions |

There are no accounts and no server component. "Editor mode" in Settings is a convenience toggle to show the Admin panel on your own browser — it is **not** a security or access-control mechanism.

## Limitations

- **AI Quiz** and **"Ask Claude to read the diagram"** depend on a Claude runtime capability (`window.claude`) that exists only inside claude.ai or the Claude apps. Outside that environment, these features detect their own unavailability and disable themselves gracefully — everything else (Visualizer, Table/SQL Import, Learn, Examples, Practice bank, Progress, Leaderboard, Admin) works identically in any standard browser.
- The Visualizer's EER model does not currently support composite foreign keys, n-ary relationships, categories (union types), or aggregation.
- The SQL parser understands common `CREATE TABLE` / `ALTER TABLE ... ADD FOREIGN KEY` syntax; unusual or vendor-specific SQL may not parse correctly.
- The leaderboard and all progress tracking are local to a single browser — there is no way to compare across students without a server, which this project intentionally does not include.
- Competitive Questions and Watch & Learn videos start completely empty by design, to avoid ever presenting invented content as if it were a real exam question or a real curated resource.

## Editing content

- **Learn topics** — `src/05b_topics.js` and `src/05c_topics.js`, each topic defined via a `T(id, title, group, {...})` call with fields like `what`, `beg` (beginner explanation), `ex` (worked example), `mist` (common mistakes), and a `quiz` array.
- **Practice questions** — the `PRACTICE` array in `src/05a_content.js`.
- **Worked examples** — the `EXAMPLES` array in the same file.
- **Example EER models** used across the app (Visualizer presets, example diagrams) — the `MODELS` definitions in `src/05a_content.js`.

After any content edit, run `python3 build.py` and commit both the edited source file and the regenerated `index.html`.

## FAQ

**Does this send my data anywhere?**
No. Everything lives in your browser's local storage. There is no backend.

**Why don't AI Quiz / image-reading work when I host it myself?**
They call into a Claude-specific runtime API that only exists when the page is running inside claude.ai or a Claude app. Hosted elsewhere, the app detects this and disables those two features — the rest of the app is unaffected.

**Can I add my own GATE/UGC NET questions?**
Yes, via the Admin panel → Competitive Questions. You'll be asked to mark each one as verified and cite its source — this is intentional, to keep that section trustworthy.

**Can multiple people share progress or a real leaderboard?**
Not currently — that would require a server and accounts, which this project deliberately doesn't have. It's a possible future addition (see Roadmap).

## Roadmap ideas

- Optional lightweight backend for shared/multi-user progress and leaderboards
- Export diagrams as PDF
- More EER modeling constructs (categories, n-ary relationships, aggregation)
- More built-in example models and practice questions

## License

MIT — see `LICENSE` (add one if you haven't yet) or state your preferred license here.
