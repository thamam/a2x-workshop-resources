# Goal operating model

This document defines the standing goals and autonomy rules for Yunes while building the A2X workshop resource hub.

It borrows the useful parts of Codex `/goal`: persisted objectives, explicit statuses, automatic continuation while active, strict completion checks, and clear stop states.

## Goal status legend

- `active`: Yunes should keep making progress whenever there is unblocked work.
- `paused`: Tomer or Yunes intentionally stopped progress for now.
- `blocked`: the same blocker has repeated and no meaningful progress remains without outside input.
- `approval-required`: progress is possible only after Tomer approves a public, external, or sensitive action.
- `complete`: the goal is achieved and verified.

## Standing goals

### G1. Security-first public-ready repository

Status: active.

Objective: Keep `a2x-workshop-resources` safe to make public later by preventing secrets, private materials, local-only notes, and accidental internal links from entering the repo.

Completion evidence:

- Private-file blocker passes.
- Secret scanning passes locally or in GitHub Actions.
- Public-release audit checklist exists.
- New content follows the inventory classification rules.

### G2. Attendee-worthy workshop hub

Status: active.

Objective: Build a useful, branded, phone-friendly resource hub that workshop attendees will want to open, revisit, and share.

Completion evidence:

- `index.html` has clear sections, useful cards, and safe placeholders or links.
- The hub explains what each resource helps attendees do.
- Mobile and desktop rendering are checked.
- No unapproved public publishing is performed.

### G3. Resource inventory and safety classification

Status: active.

Objective: Maintain a concrete inventory of workshop resource candidates, their source locations, public-safety status, and next action.

Completion evidence:

- Every known candidate has a status: `publish-now`, `polish-first`, `private`, or `defer`.
- Each candidate has source, safety notes, and next action where known.
- Unknown source locations are treated as blockers for that item only, not for the whole sprint.

### G4. Workshop usage map

Status: active.

Objective: Map workshop moments to the exact resources Tomer should show or send attendees.

Completion evidence:

- A usage map exists under `docs/`.
- Resources are prioritized by live workshop value.
- Each map entry says when to use it, why it matters, and what attendee action it supports.

### G5. Public launch readiness

Status: approval-required.

Objective: Prepare the repo and page so Tomer can approve making the hub public with minimal last-minute work.

Completion evidence:

- GitHub Pages-compatible structure is ready.
- Launch checklist exists.
- Approval gates are explicit.
- No public visibility or public deployment happens without Tomer.

## Autonomy loop

At the start of each work cycle, Yunes should:

1. Inspect the current repo state.
2. Read this file and `docs/execution-dag.md`.
3. Pick the highest-priority `active` goal with unblocked work.
4. Make concrete progress, not just restate plans.
5. Run relevant verification.
6. Commit and push safe private-repo changes when useful.
7. Send a minimal life-signal log.

If one goal blocks, continue another active goal.

## Completion audit

Before marking any goal complete, verify it against current evidence.

Do not rely on intent, memory, or plausible progress. Use files, command output, GitHub checks, rendered pages, or other authoritative evidence.

For every explicit requirement, identify whether the evidence proves completion, contradicts it, shows incomplete work, is weak, or is missing.

Only call a goal complete when all required evidence is strong.

## Blocked audit

Do not mark a goal blocked the first time a blocker appears.

Use `blocked` only when the same blocker repeats across multiple work cycles and no meaningful alternative work remains inside that goal.

Prefer item-level blockers over sprint-level blockers.

## Approval gates

Yunes must not do these without Tomer:

- Make the repository public.
- Enable or publish GitHub Pages.
- Link private or internal resources publicly.
- Add analytics, tracking, pricing claims, lead capture, or strong marketing claims.
- Deploy production changes to the main A2X website.

## Life-signal log format

Use sparse, human-readable progress logs in Telegram while work is active.

Do not spam. Emit logs at big enough task transitions, roughly every five minutes during sustained work, or when a major task starts/finishes.

Preferred forms:

- `Started working on <task>.`
- `Working on <task>; <short status>.`
- `Finished working on <task>; <evidence or result>.`

Use the fuller diagnostic format only when blockers, approvals, or verification state matter:

`LOG HH:MM — task: <short task>; status: <current state>; next: <next action>; blocker: <none or blocker>`
