# Claude Wizard Skill Wizard Implementation Plan

> **For Hermes:** Use medium-large-project-delivery for repo state, verification, and sparse handoff. Use subagent-driven-development only if this expands beyond the static v1.

**Goal:** Add the first Claude Wizard freebie sub-wizard: a Skill Wizard / Skill Inspector that helps attendees review a Claude Skill against current Anthropic best practices and A2X workshop guidance.

**Architecture:** Build a public-safe static HTML page in `resources/` with a client-side textarea analyzer, copyable Claude review prompt, rubric, freshness gate, and sample report format. Wire it into the hub, resource inventory, workshop usage map, and tool giveaway backlog. No backend, no accounts, no analytics, no model API calls, no storage.

**Tech Stack:** Static HTML, inline CSS, vanilla JavaScript, existing repo static checks.

---

## Task 1: Record scope in durable project files

**Objective:** Make Claude Wizard and the first Skill Wizard visible in the repo plan/tracker.

**Files:**
- Modify: `kanban-status.md`
- Modify: `docs/tool-giveaway-backlog.md`
- Modify: `docs/workshop-usage-map.md`
- Modify: `docs/resource-inventory.md`

**Steps:**
1. Add an active/selected story for Claude Wizard Skill Wizard.
2. Add backlog entry explaining Claude Wizard as a freebie tool family and Skill Wizard as the first sub-wizard.
3. Place it in workshop flow after `Build your first skill`.
4. Add resource inventory entry with public-safety notes.

**Verify:** Read back changed sections and confirm no private paths, credentials, or source repo exposure.

---

## Task 2: Build static Skill Wizard page

**Objective:** Create the first useful public-safe page.

**Files:**
- Create: `resources/claude-wizard-skill-wizard.html`

**Page requirements:**
- Explain Claude Wizard as a freebie tool family.
- Present Skill Wizard as the first sub-wizard.
- Include client-side `SKILL.md` quick inspector:
  - name present
  - description present
  - name lowercase/hyphen/≤64 chars
  - reserved words warning
  - description ≤1024 chars
  - description includes what + when/use trigger
  - third-person warning
  - body length / ~500-line guidance
  - progressive disclosure cues
  - script/dependency/runtime warnings
  - time-sensitive prose warning
- Include a copyable Claude prompt for deeper inspection.
- Include freshness gate: tell the assistant to check current Anthropic Skill docs before final judgment.
- Include report template with critical fixes, recommended improvements, optional polish, suggested rewrite.

**Verify:** Use browser/DOM smoke to confirm analyzer runs and copy/export text appears.

---

## Task 3: Wire the page into the hub

**Objective:** Make the page discoverable as a giveaway tool and workshop follow-up.

**Files:**
- Modify: `index.html`
- Modify: `docs/workshop-usage-map.md`
- Modify: `docs/resource-inventory.md`
- Modify: `docs/tool-giveaway-backlog.md`

**Steps:**
1. Add card in giveaway tools section.
2. Mention it in workshop flow step 3 or 4.
3. Update usage map with placement after first-skill exercise.
4. Mark status as v1 static page created.

**Verify:** Run link checker after wiring.

---

## Task 4: Verify static/public-safety quality

**Objective:** Prove the artifact works and remains public-safe.

**Commands:**
- `git diff --check`
- `python3 scripts/check-static-links.py`
- `scripts/block-private-files.sh $(git ls-files --cached --others --exclude-standard)`
- `gitleaks detect --no-banner --redact --no-git --source .`
- Local HTTP smoke for changed HTML page.
- Browser/DOM smoke at mobile width for overflow and analyzer behavior.

**Verify:** All checks pass or blockers are reported clearly.

---

## Task 5: Commit and push

**Objective:** Save the working artifact in git after verification.

**Commands:**
```bash
git add index.html resources/claude-wizard-skill-wizard.html docs/claude-wizard-skill-wizard-plan.md docs/tool-giveaway-backlog.md docs/workshop-usage-map.md docs/resource-inventory.md kanban-status.md
git commit -m "feat: add Claude Wizard skill inspector"
git push
```

**Verify:** `git status --short`, pushed commit hash, and CI/security status if available.
