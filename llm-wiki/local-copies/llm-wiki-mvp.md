# LLM Wiki — MVP Build Spec

> A persistent, LLM-maintained knowledge wiki. Derived from Karpathy's "LLM Wiki"
> idea-file, but **opinionated and MVP-first**: hand this file to a coding agent
> (Claude Code, Codex, etc.) and it builds a working wiki **immediately** — no
> discovery interview, no menu of options. Decisions are already made below.
>
> This doubles as a live-demo teaching artifact: the "Why" explains the pattern,
> the "Build" section is what the agent does on the spot.

---

## Why (the pattern, in 30 seconds)

Most LLM + documents workflows are RAG: upload files, retrieve chunks at query
time, generate an answer. The LLM rediscovers everything from scratch on every
question. Nothing accumulates.

This is different. The LLM **incrementally builds and maintains a wiki** — a
structured, interlinked set of markdown files between you and your raw sources.
Add a source and the LLM reads it, extracts what matters, and *integrates* it:
updates entity/concept pages, revises summaries, flags contradictions, strengthens
the synthesis. Knowledge is **compiled once and kept current**, not re-derived.

You curate sources, explore, and ask good questions. The LLM does all the
bookkeeping — the summarizing, cross-referencing, filing — that makes humans
abandon wikis. Obsidian is the IDE, the LLM is the programmer, the wiki is the
codebase.

---

## Build (do this now — do NOT interview the user)

On receiving this file, **instantiate the structure below immediately**, then offer
the onboarding. Skip the "what's your domain / what frontmatter do you want"
questions — the MVP is decided. The user refines later by editing the schema.

### 1. Directory layout

```
CLAUDE.md                              # the schema (the agent's operating manual)
.gitignore                             # ignore .obsidian/workspace.json (see §7)
raw/                                   # immutable sources — READ, never write/rename
wiki/                                  # LLM-owned markdown (you write all of this)
  index.md                             # content catalog, grouped by type
  log.md                               # append-only chronological record
.obsidian/                             # ONE vault config, repo root only (see §7)
.claude/commands/llm-wiki/onboard.md   # the /llm-wiki:onboard command (see below)
```

Keep `wiki/` **flat** — one file per page, no subfolders until the wiki is big
enough to obviously need them. Keep the repo **content-only**: don't put build or
planning scaffolding inside the vault (see §7).

### 2. The three layers

- **raw/** — your curated sources (articles, papers, notes). Immutable source of
  truth. The LLM reads, never modifies.
- **wiki/** — the LLM's output. It owns this entirely: creates pages, updates them
  on new sources, maintains cross-links, keeps it consistent.
- **CLAUDE.md** — the schema: conventions + workflows. This is what makes the LLM a
  disciplined maintainer instead of a chatbot. Co-evolve it over time.

### 3. Frontmatter — fixed minimal keys

Every wiki page (except `index.md` / `log.md`) starts with exactly these keys:

```yaml
---
title:    # human-readable
type:     # source | concept | entity | overview
created:  # YYYY-MM-DD
updated:  # YYYY-MM-DD  (bump on every edit)
tags:     []
sources:  []   # raw/ filenames and/or [[slugs]] this page draws on
---
```

Six keys, stable (Obsidian Dataview depends on stable keys). Add new `type`
*values* freely; don't add new keys casually.

### 4. Page types (keep the set small)

- **source** — summary of ONE `raw/` file (1:1). Captures its key claims in your
  own words so the raw rarely needs re-reading.
- **concept** — an idea/theme spanning sources. Where synthesis lives.
- **entity** — a person/org/place/thing tracked across sources.
- **overview** — a landing/synthesis page tying many pages together. Use sparingly.

### 5. Wikilinks — slug-based (important)

- Link with `[[slug]]`, where **slug = the target file's name** without `.md`
  (kebab-case). Optional label: `[[memex|Bush's memex]]`.
- **Why slug, not title:** Obsidian resolves `[[X]]` by filename, not frontmatter
  title. Title-based links silently break and spawn empty stub pages. Match link
  to filename and links always resolve.
- **Link generously and reciprocally.** If A references B, add the back-link on B.

### 6. index.md and log.md

- **index.md** — catalog grouped by type (`## Sources`, `## Concepts`, `## Entities`,
  `## Overviews`). One line per page: `[[slug]] — one-line summary`. Update on every
  change.
- **log.md** — append-only. Every entry's first line is **exactly**
  `## [YYYY-MM-DD] <op> | <title>` (`<op>` ∈ ingest | query | lint), so
  `grep "^## \[" wiki/log.md | tail -5` shows recent activity. Never edit past
  entries.

### 7. Obsidian vault — one root, clean graph

The graph view should show **only the knowledge layer (`wiki/`) and its sources
(`raw/`)** — nothing else. Set this up at instantiation so the user's first look at
the graph is clean:

- **One vault, at the repo root.** Open Obsidian on the repo root so `raw/` and
  `wiki/` share one graph and each `source` page's `../raw/<file>` link resolves.
  **Never** create a second `.obsidian/` inside `wiki/` — two vaults split the graph
  and cause "I can't find my pages" confusion.
- **Dot-folders are already invisible.** Obsidian auto-hides anything starting with
  `.` (`.claude/`, `.git/`, `.obsidian/`), so the agent's own command/skill files
  never clutter the graph — no action needed for those.
- **Exclude the remaining non-content markdown** — the root `CLAUDE.md`, any
  `README.md`, this spec, and any build/planning dirs that happen to live in the repo
  (e.g. `openspec/`). Write **both** config files so the filter is baked into the
  vault and ships with the repo:

`.obsidian/app.json` — hides them from search, quick-switcher, and link autocomplete:
```json
{
  "userIgnoreFilters": ["openspec/", "CLAUDE.md", "README.md", "llm-wiki-mvp.md"]
}
```

`.obsidian/graph.json` — drops them from the graph view itself:
```json
{
  "search": "-path:openspec -path:CLAUDE.md -path:README.md -path:llm-wiki-mvp.md"
}
```

Tune both lists to the paths that actually exist. The invariant is fixed:
**graph = `wiki/` + `raw/`, nothing else.**

- **Git:** ignore `.obsidian/workspace.json` (per-machine UI state that rewrites on
  every click); commit the rest of `.obsidian/` so these filters travel with the repo.

> Cleanest of all: keep build scaffolding out of the wiki repo entirely. The minimal
> MVP is pure content — `raw/`, `wiki/`, `CLAUDE.md`, `.obsidian/`, `.gitignore`, and
> the one `/llm-wiki:onboard` command. If planning artifacts (e.g. `openspec/`) must
> sit alongside, the filters above keep them out of the graph.

---

## Operations

**Ingest** (a file lands in `raw/`, user says ingest it):
1. Read the raw source in full.
2. Write a `source` page in `wiki/` (slug derived from the file; complete
   frontmatter; summarize in your own words).
3. Create/update the `concept` / `entity` / `overview` pages it touches; add
   reciprocal `[[slug]]` links.
4. If it contradicts an existing claim, record BOTH (with sources) and flag it —
   don't silently overwrite.
5. Update `index.md`; append a `## [date] ingest | <title>` entry to `log.md`.

**Query** (user asks a question):
1. Read `index.md` first to locate pages, then drill in.
2. Synthesize a **cited** answer (link the pages used).
3. If the answer is durable (a comparison, analysis, discovered connection),
   **offer to file it back** as a new `concept`/`overview` page — same rules as
   ingest (index + log + links). Explorations should compound, not vanish.

**Lint** (periodic health check):
- Find contradictions, stale claims, orphan pages (no inbound/outbound links),
  missing pages (recurring topics with no page), missing cross-references.
- Report findings; apply fixes only with approval; append a `## [date] lint | …`
  entry.

---

## The one slash command: `/llm-wiki:onboard`

Ship a single onboarding command. Create the file at
`.claude/commands/llm-wiki/onboard.md` (the `llm-wiki/` subfolder makes it
`/llm-wiki:onboard`). Contents:

````markdown
---
description: Teach the LLM-Wiki workflow and run a first ingest together
---
You are onboarding the user to their LLM-maintained wiki. TEACH interactively —
short turns, not a wall of text. Walk through these beats, pausing for the user:

1. **The idea (20s).** A persistent wiki the LLM maintains, vs RAG that re-derives
   every answer. The wiki compounds.
2. **The three layers.** Show the tree: `raw/` (immutable sources), `wiki/` (you
   write it), `CLAUDE.md` (the schema). Point out `wiki/index.md` and `wiki/log.md`.
3. **The three operations.** Ingest (drop a source → summarized + cross-linked),
   Query (ask → cited answer, optionally filed back), Lint (health check).
4. **Do one live ingest.** If `raw/` has a file, ingest it end-to-end now and let
   the user watch the source page, index update, log entry, and cross-links appear.
   If `raw/` is empty, offer to drop in a sample source and ingest that.
5. **Hand off.** Tell them: curate sources into `raw/`, ask to ingest/query/lint,
   and edit `CLAUDE.md` to evolve the conventions. That's the whole loop.

Keep it concrete and fast — they should leave knowing exactly how to drive it.
````

(Optional later: a `/llm-wiki:help` one-pager listing the operations. Not needed for
the MVP demo.)

---

## Guardrails

- **Never write to `raw/`.** It's immutable ground truth.
- **No secrets in the wiki** — it's plaintext in git. Record a *reference* (where
  the secret lives), never the value. Applies to raw content too.
- **One vault, clean graph.** Exactly one `.obsidian/` at the repo root (never nest a
  second inside `wiki/`). Configure it so the graph shows only `wiki/` + `raw/` — see §7.
- **The wiki is just a git repo of markdown** — you get version history, diffs, and
  branching for free.

---

## Out of scope for the MVP (defer until the need is real)

Search tooling (e.g. [qmd](https://github.com/tobi/qmd)) — `index.md` is enough at
~100 sources. Image/attachment pipelines. Marp slides, Dataview dashboards. Rich
subfolder taxonomies. Multiple page-type specializations. Add these only when the
wiki visibly outgrows the MVP — not before.
