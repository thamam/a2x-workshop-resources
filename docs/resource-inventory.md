# Workshop resource inventory

Status legend:

- `publish-now`: safe and useful now.
- `polish-first`: useful but needs cleanup.
- `private`: do not publish yet.
- `defer`: not needed for first workshop.

## Candidates

### CLAUDE.md cheat sheet

Status: publish-now  
Hub path: `resources/claude-md-cheat-sheet.html`  
Source: existing public A2X site resource at `public/resources/karpathy-rules.html`; homepage card copy in `public/index.html`.  
Safety notes: current hub page is a short public-safe rewrite. No private links, credentials, or local paths.  
Next action: compare against the full source page and decide whether to migrate more examples.

### Build your first skill

Status: publish-now  
Hub path: `resources/first-skill.html`  
Source: existing public A2X site resource at `public/resources/skills-forge.html`; homepage card copy in `public/index.html`.  
Safety notes: current hub page is a short public-safe rewrite. No private links, credentials, or local paths.  
Next action: decide whether to keep as quick workshop handout or expand into a full guided exercise.

### Claude Code harness map

Status: publish-now
Hub path: `resources/claude-code-harness-map.html`
Source: existing public A2X site resource at `public/resources/claude-code-at-scale.html`.  
Safety notes: current hub page is a short public-safe rewrite and does not copy analytics/tracking from the source page.
Next action: review wording live after the workshop opener and expand only if it remains useful.

### Product brief generator

Status: publish-now
Hub path: `resources/product-brief-generator.html`
Source: public-safe static prompt/workflow drafted in this repo from the tool giveaway backlog.
Safety notes: no external links, credentials, client material, local paths, or private examples.
Next action: test live with one sanitized workshop idea and tune the question policy.

### OpenSpec-aware interviewer

Status: publish-now
Hub path: `resources/openspec-interviewer.html`
Source: public-safe static prompt/workflow drafted in this repo from the tool giveaway backlog.
Safety notes: no external links, credentials, client material, local paths, or private examples.
Next action: pair with the product brief generator in the workshop flow.

### Prompt improver

Status: publish-now
Hub path: `resources/prompt-improver.html`
Source: public-safe static prompt/workflow drafted in this repo from the tool giveaway backlog.
Safety notes: no external links, credentials, client material, local paths, or private examples.
Next action: compare against any future Prompt Magician source before replacing the richer placeholder.

### PRD & OpenSpec starter

Status: publish-now
Hub path: `resources/prd-openspec-starter.html`
Source: public-safe static prompt/workflow drafted in this repo from the tool giveaway backlog.
Safety notes: no external links, credentials, client material, local paths, or private examples.
Next action: test after the product brief generator and tune the acceptance-criteria guidance.

### PRD to HTML review workbench

Status: publish-now prototype
Hub path: `resources/prd-html-review-workbench.html`
Source: public-safe static prototype scoped in `docs/prd-html-workbench-mvp-decision.md`.
Safety notes: no backend, no accounts, no analytics, no model API calls, no localStorage, no private A2X links, and no browser filesystem writes. Comments are held only in page memory until the user copies/exports them.
Next action: use only as a second-wave giveaway unless Tomer chooses to feature it live.

### A2X Marketplace

Status: polish-first  
Hub path: homepage placeholder card.  
Source: public GitHub repo `https://github.com/thamam/A2X-marketplace`; audit notes in `docs/a2x-marketplace-public-safety-audit.md`.
Safety notes: repo is already public, but a shallow-clone audit found local absolute paths, API-key setup docs, personal maintainer metadata, and gitleaks noise in a bundled/minified `code-research` server script. Keep the hub card unlinked until the marketplace repo is cleaned up or a sanitized overview is written.
Next action: decide whether to clean/link the existing public repo or publish a short public-safe overview page without installation details.

### Prompt Magician

Status: publish-now overview; direct repo link remains polish-first

Hub path: `resources/prompt-magician-setup.html`

Source: likely public GitHub repo `https://github.com/thamam/prompt-enhancer-extension`; audit notes in `docs/prompt-magician-source-audit.md`.
Safety notes: sanitized overview is public-safe and does not directly link the source repo. It frames Prompt Magician as optional, prefers local/offline use first, explains remote-provider privacy, avoids secret-looking API-key examples, calls out browser permissions, and suggests shortcut alternatives. Direct source-repo linking should still wait for a curated release path.
Next action: if Tomer wants a live extension demo, prepare a facilitator-curated Chrome/VS Code install path outside this public hub; otherwise keep the overview as an optional second-wave handout.

### Presentation editor

Status: polish-first  
Hub path: homepage placeholder card.  
Source: public candidate `https://github.com/thamam/talk-auto-slides-generator`, plus a private/internal document-to-presentation candidate withheld from the public-ready inventory; audit notes in `docs/presentation-editor-source-audit.md`.
Safety notes: public candidate builds and has no shallow-clone gitleaks findings, but README/setup copy still needs workshop-safe framing around Gemini API-key setup and AI Studio boilerplate. Private/internal candidate builds, but gitleaks reports a hardcoded Supabase publishable key plus synthetic credential-heavy fixtures, and internal project notes are present. Keep the hub card unlinked until a curated public setup page exists.
Next action: decide whether the first workshop wants a public slide-generator setup page or a sanitized document-to-slides overview; do not expose the private/internal source publicly.

### Wiki-LLM

Status: publish-now overview; direct source release remains polish-first

Hub path: `resources/wiki-llm-overview.html`

Source: local/private candidate projects identified outside this repo; audit notes in `docs/wiki-llm-public-safety-audit.md`. Exact private repository names and absolute paths are intentionally withheld from the public-ready inventory.
Safety notes: sanitized overview is public-safe and does not expose private source names, private repository links, local paths, raw notes, or vault contents. It teaches the `raw/`, `wiki/`, and operating-contract pattern with a fictional mini-vault. Direct software/plugin repo linking still needs a cleaned, Tomer-approved release path.
Next action: if Wiki-LLM becomes a live advanced demo, prepare a cleaned software-only repo or facilitator-owned package; keep private vault content out of the public hub.

### Credential tracer / authentication routing

Status: defer  
Hub path: none yet.  
Source: existing public A2X site resource at `public/resources/credential-tracer.html`.  
Safety notes: useful, but not part of the highest-priority first workshop path unless auth/billing comes up.  
Next action: keep as optional Q&A resource.
