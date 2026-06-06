# 📊 Project Kanban & Workflow Tracker

## Project Context

- **Project Name:** A2X Workshop Resources Hub
- **Active Phase:** Phase 2: Implementation & Public-Readiness Prep
- **Last Updated:** 2026-06-06
- **Source of Truth:** This root file is the canonical project workflow tracker.
- **Previous Board:** `docs/live-kanban.md` is historical context only. Keep active status here.
- **Update Owner:** Yunes
- **Update Cadence:** Update at meaningful task starts/finishes, blocker changes, and roughly every 30 minutes during active autonomous work.

---

## 🧭 Grounding & Update Rules

- Do not mark a story **IN PROGRESS** unless work has actually started with tools or verified repo inspection.
- Do not mark a story **DONE** unless there is concrete evidence: files written, commands run, checks passed, or current repo state inspected.
- Keep stories atomic: each story should normally fit in 1–2 focused tool runs.
- When changing focus, update this file first so state and execution stay aligned.
- Public launch, publishing, analytics, lead capture, and private/internal resource exposure require Tomer approval.
- Sparse chat logs should only announce meaningful starts, sustained work, blockers, and finishes.

---

## 🗺 Milestone / Epic Progress

- [x] **Epic 1: Workflow visibility & operating model** (100% Completed)
  - [x] Story 1.1: Create repo-visible live Kanban draft
  - [x] Story 1.2: Promote root `kanban-status.md` to canonical tracker
  - [x] Story 1.3: Document sparse transition log cadence
  - [x] Story 1.4: Wire autonomous loop to read workflow tracker
  - [x] Story 1.5: Verify tracker-related repository checks
  - [x] Story 1.6: Create HTML view for the canonical Kanban tracker

- [x] **Epic 2: Workshop resource hub foundation** (100% Completed)
  - [x] Story 2.1: Build static hub landing page
  - [x] Story 2.2: Add safe placeholder/resource cards
  - [x] Story 2.3: Add GitHub Pages readiness notes
  - [x] Story 2.4: Complete mobile/phone viewport review
  - [x] Story 2.5: Tune copy against a sanitized workshop example
  - [x] Story 2.6: Verify local static links

- [x] **Epic 3: Giveaway handout bundle** (100% Completed)
  - [x] Story 3.1: Add product brief generator
  - [x] Story 3.2: Add OpenSpec-aware interviewer
  - [x] Story 3.3: Add prompt improver
  - [x] Story 3.4: Add PRD & OpenSpec starter
  - [x] Story 3.5: Run all handouts against one sanitized workshop scenario

- [x] **Epic 4: Resource inventory & public-safety review** (100% Completed)
  - [x] Story 4.1: Create resource inventory
  - [x] Story 4.2: Classify first-release publish-now resources
  - [x] Story 4.3: Create workshop usage map
  - [x] Story 4.4: Audit A2X Marketplace source/public-safe path
  - [x] Story 4.5: Locate Prompt Magician source/setup doc
  - [x] Story 4.6: Locate presentation editor source/setup doc
  - [x] Story 4.7: Audit Wiki-LLM public-safe source path

- [ ] **Epic 5: Public launch readiness** (80% Completed)
  - [x] Story 5.1: Add public launch checklist
  - [x] Story 5.2: Add no-build GitHub Pages notes
  - [x] Story 5.3: Keep repository private/publishing approval-gated
  - [x] Story 5.4: Run final public-release audit
  - [ ] Story 5.5: Publish only after Tomer approval

- [x] **Epic 6: Second-wave public-safe workshop handouts** (100% Completed)
  - [x] Story 6.1: Build static PRD-to-HTML review workbench prototype
  - [x] Story 6.2: Add sanitized Prompt Magician setup overview
  - [x] Story 6.3: Add sanitized Wiki-LLM overview

---

## 🏃 Active State Tracking

### 📥 BACKLOG (Ready for Sprint Selection)

- None right now.

### 📋 TODO (Selected for Next Story)

- None right now.

### 🏃 IN PROGRESS (Currently Active)

- None right now.

### 🚧 BLOCKED / APPROVAL REQUIRED

- [ ] Story 5.5: Publish public site only after Tomer approval
  - Status: approval-required
  - Blocker: public publishing is an explicit approval boundary.
- [ ] Story 4.4: Expose or link A2X Marketplace resources publicly
  - Status: blocked
  - Blocker: public repo is located, but marketplace docs need cleanup or a sanitized overview before the workshop hub should link it.
- [ ] Story 4.7: Expose or link Wiki-LLM resources publicly
  - Status: blocked
  - Blocker: source path is audited, but direct public linking still needs either a sanitized overview page or Tomer-approved software-only release path.

### 🔎 REVIEW (Built/Researched; Needs Review or Tuning)

- None right now.

### ✅ DONE (Completed Stories)

- [x] Story 1.6: Create HTML view for the canonical Kanban tracker
  - Evidence: `kanban-status.html` exists, fetches `kanban-status.md`, renders successfully through a local HTTP server, has no browser console errors, and `index.html` links to it.
- [x] Story 1.2: Promote root `kanban-status.md` to canonical tracker
  - Evidence: root `kanban-status.md` exists; `index.html`, `docs/goal-operating-model.md`, `docs/execution-dag.md`, and the autonomous cron prompt now point future work to root `kanban-status.md` as canonical.
- [x] Story 1.1: Create repo-visible live Kanban draft
  - Evidence: `docs/live-kanban.md` exists and is retained as historical context.
- [x] Story 1.3: Document sparse transition log cadence
  - Evidence: `docs/goal-operating-model.md` contains the life-signal log format.
- [x] Story 1.4: Wire autonomous loop to read workflow tracker
  - Evidence: `docs/goal-operating-model.md` and the autonomous cron prompt now reference root `kanban-status.md` as canonical.
- [x] Story 1.5: Verify tracker-related repository checks
  - Evidence: GitHub Security Checks succeeded for commit `8c63f76`.
- [x] Story 2.1: Build static hub landing page
  - Evidence: `index.html` exists.
- [x] Story 2.2: Add safe placeholder/resource cards
  - Evidence: resource cards and placeholder classifications are documented in `docs/resource-inventory.md`.
- [x] Story 2.3: Add GitHub Pages readiness notes
  - Evidence: `docs/github-pages-readiness.md` exists.
- [x] Story 2.4: Complete mobile/phone viewport review
  - Evidence: `docs/mobile-viewport-review.md` records Chrome Headless 390px checks with no horizontal overflow on the hub and four giveaway pages; `python3 scripts/check-static-links.py`, `scripts/block-private-files.sh $(git ls-files)`, and `gitleaks detect --no-banner --redact --source .` passed on 2026-06-06.
- [x] Story 2.5: Tune copy against a sanitized workshop example
  - Evidence: `index.html` now frames the giveaway tools as a chained workflow checked against the synthetic consultant meeting-prep scenario and links to `docs/giveaway-scenario-test.md`; static-link, private-file, gitleaks, local HTTP, and Chrome Headless 390px overflow checks passed on 2026-06-06.
- [x] Story 2.6: Verify local static links
  - Evidence: `python3 scripts/check-static-links.py` passed on 2026-06-06.
- [x] Story 3.1: Add product brief generator
  - Evidence: `resources/product-brief-generator.html` exists.
- [x] Story 3.2: Add OpenSpec-aware interviewer
  - Evidence: `resources/openspec-interviewer.html` exists.
- [x] Story 3.3: Add prompt improver
  - Evidence: `resources/prompt-improver.html` exists.
- [x] Story 3.4: Add PRD & OpenSpec starter
  - Evidence: `resources/prd-openspec-starter.html` exists.
- [x] Story 3.5: Run all handouts against one sanitized workshop scenario
  - Evidence: `docs/giveaway-scenario-test.md` validates `resources/product-brief-generator.html`, `resources/openspec-interviewer.html`, `resources/prompt-improver.html`, and `resources/prd-openspec-starter.html` against a public-safe synthetic consultant meeting-prep scenario; static-link, private-file, and gitleaks checks passed on 2026-06-06.
- [x] Story 4.1: Create resource inventory
  - Evidence: `docs/resource-inventory.md` exists.
- [x] Story 4.2: Classify first-release publish-now resources
  - Evidence: `docs/resource-inventory.md` lists publish-now and polish-first statuses.
- [x] Story 4.3: Create workshop usage map
  - Evidence: `docs/workshop-usage-map.md` exists.
- [x] Story 4.5: Locate Prompt Magician source/setup doc
  - Evidence: `docs/prompt-magician-source-audit.md` identifies likely public repo `https://github.com/thamam/prompt-enhancer-extension`, records shallow-clone/gitleaks/manual findings, updates inventory and usage map, and keeps hub card unlinked pending a sanitized overview.
- [x] Story 4.6: Locate presentation editor source/setup doc
  - Evidence: `docs/presentation-editor-source-audit.md` identifies public candidate `https://github.com/thamam/talk-auto-slides-generator` and a private/internal document-to-presentation candidate withheld from public docs; records gitleaks/manual scan results, build checks for both candidates, inventory/usage-map updates, and keeps the hub card unlinked pending a curated setup/overview.
- [x] Story 4.4: Audit A2X Marketplace source/public-safe path
  - Evidence: `docs/a2x-marketplace-public-safety-audit.md` locates `https://github.com/thamam/A2X-marketplace`, records shallow-clone scan findings, and keeps the hub card unlinked pending cleanup or a sanitized overview.
- [x] Story 4.7: Audit Wiki-LLM public-safe source path
  - Evidence: `docs/wiki-llm-public-safety-audit.md` records the private candidate split, shallow-clone `gitleaks` results, local-path/setup-doc issues, inventory/usage-map updates, and keeps the hub card unlinked pending a sanitized overview or approved software-only release path.
- [x] Story 5.1: Add public launch checklist
  - Evidence: `docs/public-launch-checklist.md` exists.
- [x] Story 5.2: Add no-build GitHub Pages notes
  - Evidence: `docs/github-pages-readiness.md` and `.nojekyll` exist.
- [x] Story 5.3: Keep repository private/publishing approval-gated
  - Evidence: approval gates are documented in `docs/goal-operating-model.md` and `docs/execution-dag.md`.
- [x] Story 5.4: Run final public-release audit
  - Evidence: `docs/public-release-audit-2026-06-06.md` records repo-private, Pages-not-configured, private-file blocker, gitleaks, static-link, local HTTP, and Chrome Headless smoke checks; `docs/public-launch-checklist.md` points to the audit.
- [x] Story 6.1: Build static PRD-to-HTML review workbench prototype
  - Evidence: `resources/prd-html-review-workbench.html` exists, is linked from `index.html`, listed in `docs/resource-inventory.md`, mapped in `docs/workshop-usage-map.md`, and passed static-link, private-file, gitleaks `--no-git`, local HTTP, Chrome Headless 390px overflow, fixture render, and feedback export checks on 2026-06-06.
- [x] Story 6.2: Add sanitized Prompt Magician setup overview
  - Evidence: `resources/prompt-magician-setup.html` exists, is linked from `index.html`, listed in `docs/resource-inventory.md`, mapped in `docs/workshop-usage-map.md`, and passed `git diff --check`, `python3 scripts/check-static-links.py`, `scripts/block-private-files.sh $(git ls-files --cached --others --exclude-standard)`, `gitleaks detect --no-banner --redact --no-git --source .`, local HTTP status checks, and Chrome Headless mobile-overflow/content checks on 2026-06-06.
- [x] Story 6.3: Add sanitized Wiki-LLM overview
  - Evidence: `resources/wiki-llm-overview.html` exists, is linked from `index.html`, listed in `docs/resource-inventory.md`, mapped in `docs/workshop-usage-map.md`, and passed `git diff --check`, `python3 scripts/check-static-links.py`, `scripts/block-private-files.sh $(git ls-files --cached --others --exclude-standard)`, `gitleaks detect --no-banner --redact --no-git --source .`, local HTTP status checks, and Chrome Headless mobile-overflow/content checks on 2026-06-06.

---

## 🔁 Recent Transitions

- 2026-06-06 — Finished Story 6.3: created `resources/wiki-llm-overview.html`, linked it from the hub, updated inventory/usage map, and verified diff hygiene, static links, private-file blocker, gitleaks `--no-git`, local HTTP, and Chrome Headless mobile/content checks.
- 2026-06-06 — Started Story 6.3: add a sanitized Wiki-LLM overview with a fictional mini-vault example and no private source links.
- 2026-06-06 — Finished Story 6.2: created `resources/prompt-magician-setup.html`, linked it from the hub, updated inventory/usage map, and verified diff hygiene, static links, private-file blocker, gitleaks `--no-git`, local HTTP, and Chrome Headless mobile/content checks.
- 2026-06-06 — Started Story 6.2: add a sanitized Prompt Magician setup overview without private/internal links or direct repo exposure.
- 2026-06-06 — Finished Story 6.1: created `resources/prd-html-review-workbench.html`, linked it from the hub, updated inventory/usage map, and verified static links, private-file blocker, gitleaks `--no-git`, local HTTP, mobile overflow, fixture render, and feedback export.
- 2026-06-06 — Started Story 6.1: build the static PRD-to-HTML review workbench prototype within the scoped public-safe boundaries.
- 2026-06-06 — Finished Story 2.5: tuned `index.html` giveaway copy against the sanitized meeting-prep scenario, added a safe scenario-chain card, and verified static links, private-file blocker, gitleaks, local HTTP, and Chrome Headless 390px overflow.
- 2026-06-06 — Started Story 2.5: tune hub copy against the sanitized workshop example.
- 2026-06-06 — Finished Story 2.4/3.5 review reconciliation: inspected `docs/mobile-viewport-review.md` and `docs/giveaway-scenario-test.md`, confirmed the recorded evidence is strong enough for DONE, and reran static-link, private-file, and gitleaks checks successfully.
- 2026-06-06 — Finished Story 4.7: wrote `docs/wiki-llm-public-safety-audit.md`, updated inventory and usage map, verified shallow-clone gitleaks results for six private candidates, and kept the hub card unlinked pending sanitized overview or approved software-only release path.
- 2026-06-06 — Started Story 4.7: audit Wiki-LLM public-safe source path without exposing local/private paths publicly.
- 2026-06-06 — Finished Story 4.6: located public `thamam/talk-auto-slides-generator` plus a private/internal document-to-presentation candidate, wrote `docs/presentation-editor-source-audit.md`, updated inventory/usage map, verified both candidate builds, and kept the hub card unlinked pending curated setup/overview.
- 2026-06-06 — Started Story 4.6: locate presentation editor source/setup doc.
- 2026-06-06 — Finished Story 4.5: located likely public `thamam/prompt-enhancer-extension`, wrote `docs/prompt-magician-source-audit.md`, updated inventory/usage map, and kept the hub card unlinked pending sanitized setup overview.
- 2026-06-06 — Started Story 4.5: locate Prompt Magician source/setup doc.
- 2026-06-06 — Finished Story 4.4: located public `thamam/A2X-marketplace`, wrote `docs/a2x-marketplace-public-safety-audit.md`, updated inventory, and kept the hub card unlinked pending cleanup/sanitized overview.
- 2026-06-06 — Started Story 4.4: audit A2X Marketplace source/public-safe path.
- 2026-06-06 — Finished Story 5.4: wrote `docs/public-release-audit-2026-06-06.md`; repo-private, Pages-not-configured, private-file, gitleaks, static-link, local HTTP, and Chrome Headless smoke checks passed.
- 2026-06-06 — Started Story 5.4: final public-release audit.
- 2026-06-06 — Finished Story 1.6: created `kanban-status.html`, linked it from the hub, and verified browser rendering.
- 2026-06-06 — Started Story 1.6: create an HTML view for the canonical Kanban tracker.
- 2026-06-06 — Finished Story 2.4: mobile viewport smoke review passed at 390px for hub and giveaway pages.
- 2026-06-06 — Finished Story 3.5: ran the handout bundle against a sanitized consultant meeting-prep scenario.
- 2026-06-06 — Improved `resources/prd-openspec-starter.html` into a form-driven generator and smoke-tested output generation.
- 2026-06-06 — Finished PRD-to-HTML workbench MVP scope decision as a static giveaway prototype with strict approval boundaries.
- 2026-06-06 — Finished Story 1.2: Promoted root `kanban-status.md` to canonical tracker and updated docs/cron references.
- 2026-06-06 — Corrected concurrent overwrite that briefly made root `kanban-status.md` a pointer back to `docs/live-kanban.md`.
- 2026-06-06 — Started Story 1.2: Promote root `kanban-status.md` to canonical tracker.
- 2026-06-06 — Finished Story 1.1: Created `docs/live-kanban.md` and verified tracker-related checks.
- 2026-06-06 — Finished first giveaway handout bundle and PRD-to-HTML research pass.

---

## 📌 Next Safe Action

- If another autonomous cycle has enough run budget, the next safe unblocked story is a curated sanitized overview for either Presentation editor or A2X Marketplace. Keep direct source links approval-gated until each release path is intentionally curated.
