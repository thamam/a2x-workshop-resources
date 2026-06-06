# A2X workshop live Kanban

Last updated: 2026-06-06 19:29 IDT  
Maintainer: Yunes  
Update cadence: at least every 30 minutes during active work, and whenever a meaningful task finishes or a new one starts.

## How to read this board

- `todo`: planned, not started.
- `doing`: currently active or next in the active sequence.
- `blocked`: needs Tomer approval or missing source/context.
- `review`: built/researched and needs live review or tuning.
- `done`: completed and verified against repo state or command output.

## Doing

### K1. Maintain live Kanban board

Status: doing  
Goal: Keep this board current enough that Tomer can see planned tasks, current work, blockers, and finished work without reconstructing the state from chat logs.  
Evidence: `docs/live-kanban.md` exists, is linked from the hub, and the autonomous work loop prompt requires updates on starts/finishes and scheduled refreshes.  
Next: Wire board updates into the operating docs and cron prompt.

## Todo

### K2. Tune giveaway pages with a real workshop example

Status: todo  
Goal: Run the product brief generator, OpenSpec interviewer, prompt improver, and PRD starter against one sanitized workshop scenario.  
Next: Use the output to improve wording and question policies.

### K3. Improve giveaway page visual consistency

Status: todo  
Goal: Bring the PRD/OpenSpec starter page closer to the interactive page style used by the other giveaway tools.  
Next: Decide whether it should become form-driven like the other three pages.

### K4. Scope the PRD-to-HTML workbench MVP

Status: todo  
Goal: Convert the research memo into a concrete MVP decision: public giveaway, internal A2X tool, or deferred prototype.  
Next: Choose round-trip format: OpenSpec Markdown, plain PRD Markdown, or both.

### K5. Continue public-safety inventory review

Status: todo  
Goal: Reduce polish-first placeholders by finding public-safe sources or explicitly deferring them.  
Next: Continue with A2X Marketplace, Prompt Magician, presentation editor, and Wiki-LLM.

### K6. Mobile review of the hub and giveaway pages

Status: todo  
Goal: Verify the hub and handouts work on phone-sized viewports before public approval.  
Next: Use browser screenshots at a narrow viewport if available, otherwise document desktop-only limitation.

## Blocked / approval required

### K7. Public launch / publishing

Status: approval-required  
Goal: Make the hub public or publish GitHub Pages.  
Blocker: Requires Tomer approval.  
Next: Prepare launch checklist only; do not publish.

### K8. Private/source-linked advanced tools

Status: blocked  
Goal: Link or expose A2X Marketplace, richer Prompt Magician, presentation editor, or Wiki-LLM sources.  
Blocker: Public-safe source locations and exposure boundaries are not confirmed.  
Next: Keep placeholders safe until sources are audited.

## Review

### K9. Static giveaway tool bundle

Status: review  
Goal: Validate the first practical giveaway set with Tomer’s workshop framing.  
Evidence: `resources/product-brief-generator.html`, `resources/openspec-interviewer.html`, `resources/prompt-improver.html`, and `resources/prd-openspec-starter.html` exist; local link check and browser smoke tests passed in the previous work sequence.  
Next: Tomer can review wording; Yunes can continue tuning with sanitized examples.

## Done

### K10. Workshop giveaway backlog captured

Status: done  
Evidence: `docs/tool-giveaway-backlog.md` captures the five tool ideas, first-release bundle, and PRD-to-HTML research-first path.

### K11. PRD-to-HTML research memo created

Status: done  
Evidence: `docs/prd-html-workbench-research.md` summarizes the research direction and relevant public examples.

### K12. GitHub Pages readiness notes prepared

Status: done  
Evidence: `docs/github-pages-readiness.md` and `docs/public-launch-checklist.md` exist; publishing remains approval-gated.

## Recent transitions

- 2026-06-06 19:29 IDT — Started live Kanban setup.
- 2026-06-06 19:27 IDT — Finished first giveaway tool bundle and PRD-to-HTML research pass.
