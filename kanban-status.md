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

- [ ] **Epic 2: Workshop resource hub foundation** (67% Completed)
  - [x] Story 2.1: Build static hub landing page
  - [x] Story 2.2: Add safe placeholder/resource cards
  - [x] Story 2.3: Add GitHub Pages readiness notes
  - [ ] Story 2.4: Complete mobile/phone viewport review
  - [ ] Story 2.5: Tune copy against a sanitized workshop example
  - [x] Story 2.6: Verify local static links

- [ ] **Epic 3: Giveaway handout bundle** (80% Completed)
  - [x] Story 3.1: Add product brief generator
  - [x] Story 3.2: Add OpenSpec-aware interviewer
  - [x] Story 3.3: Add prompt improver
  - [x] Story 3.4: Add PRD & OpenSpec starter
  - [ ] Story 3.5: Run all handouts against one sanitized workshop scenario

- [ ] **Epic 4: Resource inventory & public-safety review** (43% Completed)
  - [x] Story 4.1: Create resource inventory
  - [x] Story 4.2: Classify first-release publish-now resources
  - [x] Story 4.3: Create workshop usage map
  - [ ] Story 4.4: Audit A2X Marketplace source/public-safe path
  - [ ] Story 4.5: Locate Prompt Magician source/setup doc
  - [ ] Story 4.6: Locate presentation editor source/setup doc
  - [ ] Story 4.7: Audit Wiki-LLM public-safe source path

- [ ] **Epic 5: Public launch readiness** (60% Completed)
  - [x] Story 5.1: Add public launch checklist
  - [x] Story 5.2: Add no-build GitHub Pages notes
  - [x] Story 5.3: Keep repository private/publishing approval-gated
  - [ ] Story 5.4: Run final public-release audit
  - [ ] Story 5.5: Publish only after Tomer approval

---

## 🏃 Active State Tracking

### 📥 BACKLOG (Ready for Sprint Selection)

- [ ] Story 2.5: Tune hub and handout copy using one sanitized workshop scenario - *Priority: High*
- [ ] Story 3.5: Run product brief, OpenSpec interviewer, prompt improver, and PRD starter as one scenario chain - *Priority: High*
- [ ] Story 2.4: Review hub and handouts on phone-sized viewport - *Priority: High*
- [ ] Story 4.4: Audit A2X Marketplace source/public-safe path - *Priority: Medium*
- [ ] Story 4.5: Locate Prompt Magician source/setup doc - *Priority: Medium*
- [ ] Story 4.6: Locate presentation editor source/setup doc - *Priority: Medium*
- [ ] Story 4.7: Audit Wiki-LLM public-safe source path - *Priority: Medium*
- [ ] Story 5.4: Run final public-release audit - *Priority: Medium*

### 📋 TODO (Selected for Next Story)

- [ ] Story 3.5: Run all handouts against one sanitized workshop scenario (Assigned to: Yunes)

### 🏃 IN PROGRESS (Currently Active)

- None right now.

### 🚧 BLOCKED / APPROVAL REQUIRED

- [ ] Story 5.5: Publish public site only after Tomer approval
  - Status: approval-required
  - Blocker: public publishing is an explicit approval boundary.
- [ ] Story 4.4: Expose or link A2X Marketplace resources publicly
  - Status: blocked
  - Blocker: public-safe source path and exposure rules are not confirmed.
- [ ] Story 4.7: Expose or link Wiki-LLM resources publicly
  - Status: blocked
  - Blocker: local/private candidate material needs audit before public use.

### 🔎 REVIEW (Built/Researched; Needs Review or Tuning)

- [ ] Story 3.1–3.4: Static giveaway handout bundle
  - Evidence: `resources/product-brief-generator.html`, `resources/openspec-interviewer.html`, `resources/prompt-improver.html`, and `resources/prd-openspec-starter.html` exist.
  - Next: run against a sanitized workshop scenario and tune wording.

### ✅ DONE (Completed Stories)

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
- [x] Story 4.1: Create resource inventory
  - Evidence: `docs/resource-inventory.md` exists.
- [x] Story 4.2: Classify first-release publish-now resources
  - Evidence: `docs/resource-inventory.md` lists publish-now and polish-first statuses.
- [x] Story 4.3: Create workshop usage map
  - Evidence: `docs/workshop-usage-map.md` exists.
- [x] Story 5.1: Add public launch checklist
  - Evidence: `docs/public-launch-checklist.md` exists.
- [x] Story 5.2: Add no-build GitHub Pages notes
  - Evidence: `docs/github-pages-readiness.md` and `.nojekyll` exist.
- [x] Story 5.3: Keep repository private/publishing approval-gated
  - Evidence: approval gates are documented in `docs/goal-operating-model.md` and `docs/execution-dag.md`.

---

## 🔁 Recent Transitions

- 2026-06-06 — Finished Story 1.2: Promoted root `kanban-status.md` to canonical tracker and updated docs/cron references.
- 2026-06-06 — Corrected concurrent overwrite that briefly made root `kanban-status.md` a pointer back to `docs/live-kanban.md`.
- 2026-06-06 — Started Story 1.2: Promote root `kanban-status.md` to canonical tracker.
- 2026-06-06 — Finished Story 1.1: Created `docs/live-kanban.md` and verified tracker-related checks.
- 2026-06-06 — Finished first giveaway handout bundle and PRD-to-HTML research pass.

---

## 📌 Next Safe Action

- Start Story 3.5 by running the handout bundle against one sanitized workshop scenario, then update this board before moving the story to IN PROGRESS.
