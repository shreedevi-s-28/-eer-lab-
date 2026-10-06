# EER Lab — Generalization & Specialization Visualizer

An interactive, browser-based learning platform for the Enhanced Entity-Relationship (EER) model — the part of database design that covers superclass/subclass hierarchies, generalization, specialization, inheritance, and constraints like disjoint/overlapping and total/partial.

At its core is a live diagram visualizer: build an EER diagram by hand, or import existing tables/SQL and let the app detect the structure — then watch the relational schema and SQL generate automatically underneath it. Around that sits a full learning path, worked examples, a practice question bank, an AI-generated quiz, and progress tracking.

No installation, no backend, no accounts. Open `index.html` and it runs.

---

## Features

**Visualizer** — Add entities and attributes, mark keys. Generalize (combine entities with shared attributes into a superclass) or specialize (split an entity into subclasses). Set disjoint/overlapping and total/partial constraints using standard EER notation. The relational schema and SQL regenerate live, with four selectable mapping strategies. Includes undo/redo, auto-layout, pan/zoom, and PNG/SVG/SQL export.

**Table / SQL Import workbench** — Paste tables, upload a CSV, or paste SQL `CREATE TABLE` statements. The app analyzes column names and patterns to suggest entities, relationships, and possible generalization groupings. Every suggestion must be reviewed and confirmed before anything is generated.

**Learn path** — 30 topics from ER fundamentals through full EER mapping, each with a plain-language explanation, a worked example, common mistakes, and a mini quiz.

**Examples** — 8 fully worked EER models with problem statement, analysis, diagram, and generated schema/SQL.

**Practice bank** — Standalone practice questions with hints and explanations, filterable by topic and difficulty.

**AI Quiz** — Generates fresh multiple-choice questions on demand for a chosen topic and difficulty. Always labeled AI-generated, never presented as a real past exam question.

**Competitive Questions** — A section for genuine GATE / UGC NET questions. Starts empty; questions appear only once added and marked verified with a source, via the Admin panel.

**Progress & Leaderboard** — Tracks accuracy per topic, flags weak topics, and shows a leaderboard of your own quiz attempts (personal to your browser, not a multi-user ranking).

**Admin / Content Manager** — Add reference videos, images, and resources per topic; add and verify Competitive Questions; export or import a full backup as JSON.

---

## Quick start

Open `index.html` in any browser. That's the whole app.

All data — progress, quiz history, uploaded images, admin content — is stored locally via `localStorage` and `IndexedDB`. Nothing is uploaded or synced anywhere.

---

## Project structure
