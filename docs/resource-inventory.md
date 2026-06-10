# Workshop resource inventory

Status legend:

- `publish-now`: safe and useful now.
- `polish-first`: useful but needs cleanup.
- `private`: do not publish yet.
- `defer`: not needed for first workshop.

## Candidates

### Pre-workshop readiness checklist

Status: publish-now
Hub path: `resources/pre-workshop-readiness-checklist.html`
Source: public-safe static readiness handout drafted in this repo from the current workshop preparation and safety boundaries.
Safety notes: no private source links, credentials, local paths, analytics, lead capture, pricing claims, production website changes, or client material. The checklist explicitly directs attendees toward toy repos, fictional/sanitized samples, stop conditions, and visible verification evidence.
Next action: tune the checklist after observing which setup failures or safety questions appear before the workshop.

### Workshop resource route chooser

Status: publish-now
Hub path: `resources/workshop-resource-chooser.html`
Source: public-safe static navigation aid drafted in this repo from the current hub resource set and workshop usage map.
Safety notes: links only to existing public-safe hub resources and docs; no private source links, credentials, local paths, analytics, lead capture, or client material.
Next action: tune route labels after observing which workshop moments cause attendee confusion.

### Post-workshop action plan

Status: publish-now
Hub path: `resources/post-workshop-action-plan.html`
Source: public-safe static follow-up handout drafted in this repo from the current workshop flow and resource set.
Safety notes: no private source links, credentials, local paths, analytics, lead capture, pricing claims, production website changes, or client material. The worksheet explicitly recommends fictional/sanitized sample inputs and stop conditions before sensitive actions.
Next action: tune the closing worksheet after observing which post-workshop commitments attendees actually make.

### Claude Code credential routing Q&A

Status: publish-now
Hub path: `resources/claude-code-credential-routing.html`
Source: public-safe static optional troubleshooting handout drafted in this repo from the workshop need to distinguish browser login, API-key, environment override, and organization-policy issues.
Safety notes: no credentials, token-shaped examples, account details, billing claims, private links, analytics, lead capture, production website changes, or client material. The page explicitly tells attendees not to paste tokens, account pages, billing screens, shell history, `.env` files, or secrets into prompts/shared docs.
Next action: tune after observing which Claude Code access failures appear before or during the workshop.

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

### Claude Wizard / Skill Wizard

Status: publish-now v1 static inspector
Hub path: `resources/claude-wizard-skill-wizard.html`
Source: public-safe static page drafted in this repo from Tomer's Claude Wizard freebie-tool concept and Anthropic Skill authoring best practices.
Safety notes: no backend, no accounts, no analytics, no model API calls, no localStorage, no private links, no credentials, and no attendee content leaves the browser. The freshness step is a copyable prompt instruction for the user's assistant to check current Anthropic docs before final judgment.
Next action: test with real workshop skill drafts and decide which additional Claude Wizard sub-wizards should follow.

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

### OpenSpec tutorial

Status: publish-now
Hub path: `resources/openspec-tutorial.html`
Source: public-safe blog-style tutorial drafted in this repo to complement the OpenSpec interviewer and PRD starter.
Safety notes: no external links, credentials, client material, local paths, or private examples. It explains proposal gates, decision gates, and agent prompts without requiring a live OpenSpec repository.
Next action: tune wording after Tomer reviews the desired workshop decision-gate language.

### PRD to HTML review workbench

Status: publish-now prototype
Hub path: `resources/prd-html-review-workbench.html`
Source: public-safe static prototype scoped in `docs/prd-html-workbench-mvp-decision.md`.
Safety notes: no backend, no accounts, no analytics, no model API calls, no localStorage, no private A2X links, and no browser filesystem writes. Comments are held only in page memory until the user copies/exports them.
Next action: use only as a second-wave giveaway unless Tomer chooses to feature it live.

### A2X Marketplace

Status: publish-now overview/tutorial; direct source link remains polish-first

Hub paths: `resources/a2x-marketplace-overview.html`, `resources/a2x-marketplace-tutorial.html`

Source: public GitHub repo `https://github.com/thamam/A2X-marketplace`; audit notes in `docs/a2x-marketplace-public-safety-audit.md`.
Safety notes: sanitized overview and tutorial are public-safe and do not directly link the marketplace source repo. They explain the marketplace concept, install mental model, plugin-loading checklist, item types, benefits, and safe exercise with generic placeholders, no local paths, no personal contact details, no plugin internals, and no real credentials. Direct source-repo linking should still wait for cleanup of local-path docs, credential setup framing, and secret-scanner noise.
Next action: if Tomer wants attendees to install real marketplace items, prepare a curated release path or facilitator-owned demo; otherwise use the tutorial as the safe attendee explanation.

### Prompt Magician

Status: publish-now overview; direct repo link remains polish-first

Hub path: `resources/prompt-magician-setup.html`

Source: likely public GitHub repo `https://github.com/thamam/prompt-enhancer-extension`; audit notes in `docs/prompt-magician-source-audit.md`.
Safety notes: sanitized overview is public-safe and does not directly link the source repo. It frames Prompt Magician as optional, prefers local/offline use first, explains remote-provider privacy, avoids secret-looking API-key examples, calls out browser permissions, and suggests shortcut alternatives. Direct source-repo linking should still wait for a curated release path.
Next action: if Tomer wants a live extension demo, prepare a facilitator-curated Chrome/VS Code install path outside this public hub; otherwise keep the overview as an optional second-wave handout.

### Presentation editor

Status: publish-now overview; direct source release remains polish-first

Hub path: `resources/presentation-editor-overview.html`

Source: public candidate `https://github.com/thamam/talk-auto-slides-generator`, plus a private/internal document-to-presentation candidate withheld from the public-ready inventory; audit notes in `docs/presentation-editor-source-audit.md`.
Safety notes: sanitized overview is public-safe and does not directly link either source candidate. It teaches the presentation-generation review loop with a fictional mini-brief, generic API-key placeholders, no customer material, no private/internal repository names, and no local paths. Direct source-repo linking should still wait for curated setup copy and approval.
Next action: if Tomer wants a live slide-generation demo, prepare a facilitator-owned environment and attendee-safe setup notes outside this public hub; otherwise keep the overview as an optional second-wave handout.

### Wiki-LLM

Status: publish-now overview/tutorial; direct source release remains polish-first

Hub paths: `resources/wiki-llm-overview.html`, `resources/wiki-llm-tutorial.html`

Source: local/private candidate projects identified outside this repo; audit notes in `docs/wiki-llm-public-safety-audit.md`. Exact private repository names and absolute paths are intentionally withheld from the public-ready inventory.
Safety notes: sanitized overview and tutorial are public-safe and do not expose private source names, private repository links, local paths, raw notes, or vault contents. They teach the `raw/`, `wiki/`, and operating-contract pattern with a fictional mini-vault and generic prompts. Direct software/plugin repo linking still needs a cleaned, Tomer-approved release path.
Next action: if Wiki-LLM becomes a live advanced demo, prepare a cleaned software-only repo or facilitator-owned package; keep private vault content out of the public hub.

### buildTool decision navigator

Status: publish-now decision aid

Hub path: `resources/buildtool-decision.html`

Source: public-safe static decision aid discovered as an untracked resource during the 2026-06-07 readiness refresh and reconciled into the hub.
Safety notes: contains no private source links, credentials, local paths, customer data, analytics, lead capture, or install instructions. It discusses the native-tool decision conceptually and keeps implementation/source exposure out of the attendee-facing page.
Next action: use only as an advanced optional discussion aid unless Tomer chooses to feature native tool/plugin internals live.
