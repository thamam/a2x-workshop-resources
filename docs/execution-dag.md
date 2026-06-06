# A2X Workshop Resources Execution DAG

This document defines the operating model for autonomous work on the workshop resource hub.

## Operating rule

Do not wait for Tomer acknowledgement to start the next unblocked task. Treat updates as status, not as gates, unless the task crosses an approval boundary.

Do not wait for the next scheduled tick merely because a task finished. A completed task should trigger immediate continuation: choose the next highest-priority safe task, start it, and only stop when run budget, approval boundaries, or genuine lack of useful work require stopping.

Use `docs/goal-operating-model.md` as the standing-goal layer for this sprint. It defines active goals, completion evidence, blocked states, continuation rules, and the life-signal log format in the spirit of Codex `/goal`.

## Approval boundaries

Yunes may do autonomously:

- Work inside the private `a2x-workshop-resources` repository.
- Add docs, static pages, workflows, and checks.
- Commit and push to the private repository.
- Improve security checks.
- Inventory local sources and public links.
- Prepare preview material.

Tomer approval required:

- Making the repository public.
- Deploying or publishing a public GitHub Pages site.
- Linking private/internal resources publicly.
- Adding claims, pricing, analytics, tracking, or lead capture.
- Removing existing A2X website content.

## Task graph

### A. Security foundation

Status: started.

Dependencies: none.

Work:

- Keep `gitleaks` checks passing.
- Keep private-file blocker passing.
- Harden Continuous Integration (CI), meaning automated GitHub checks.
- Add public-release audit checklist.

Unblocks: all public-facing resource work.

### B. Resource inventory

Status: ready.

Dependencies: A started, not completed.

Work:

- Locate source material for Marketplace, Prompt Magician, presentation editor, Wiki-LLM, skills forge, and CLAUDE.md cheat sheet.
- Classify each item as publish-now, polish-first, private, or defer.
- Record source path, public-safety notes, and next action.

Unblocks: content migration and resource cards.

### C. Hub information architecture

Status: ready.

Dependencies: A started.

Work:

- Define the hub sections.
- Draft attendee-facing copy.
- Keep A2X branding visible without making the page feel like an ad.

Unblocks: page implementation.

### D. Static hub implementation

Status: started with skeleton.

Dependencies: A started, C started.

Work:

- Build the landing page.
- Add cards and placeholders safely.
- Keep links inactive until sources pass inventory.
- Verify mobile and desktop rendering.

Unblocks: preview package.

### E. Resource content migration

Status: blocked on inventory details.

Dependencies: B item classified publish-now or polish-first.

Work:

- Copy, rewrite, or link public-safe resources.
- Remove secrets, private names, local-only paths, and fragile assumptions.
- Add setup instructions.

Unblocks: final workshop resource set.

### F. GitHub Pages readiness

Status: ready.

Dependencies: A started, D started.

Work:

- Prepare GitHub Pages-compatible structure.
- Add no-build deployment notes.
- Do not enable public publishing without Tomer approval.

Unblocks: approved deployment.

### G. Workshop usage map

Status: ready.

Dependencies: B started, C started.

Work:

- Create a map from talk moments to resource links.
- Identify when Tomer should send attendees to the hub.
- Prioritize resources used live.

Unblocks: stable workshop flow.

### H. Live Kanban maintenance

Status: started.

Dependencies: none.

Work:

- Keep `docs/live-kanban.md` updated with planned tasks, active work, blockers, review items, done items, and recent transitions.
- Refresh at least every 30 minutes during active work.
- Update immediately when a meaningful task finishes or a new meaningful task starts.
- Link the board from the hub.

Unblocks: Tomer visibility and autonomous-work trust.

## Current priority order

1. Keep live Kanban current.
2. Harden security checks.
3. Inventory sources.
4. Improve hub skeleton and copy.
5. Create workshop usage map.
6. Prepare GitHub Pages readiness.
7. Migrate resources as each source becomes safe.

## Blocked-task rule

If a task blocks on missing source material, continue with security, hub structure, preview, and usage-map work. Do not idle.
