# Workshop usage map

This map connects talk moments to resources in the hub. It is designed for the first A2X Claude Code workshop.

## Priority 1 — use live

### Opening: "The harness, not just the model"

Resource: `resources/claude-code-harness-map.html`, plus homepage section `How to use this hub live`.

Use when: Tomer explains that Claude Code performance depends on rules, tools, environment, and feedback loops.

Attendee action: Diagnose agent quality through rules, context, tools, reusable workflows, and review gates instead of treating the model as the only variable.

Status: ready draft.

### Before live coding: CLAUDE.md & coding rules

Resource: `resources/claude-md-cheat-sheet.html`.

Use when: Tomer introduces project instructions and why agents need local rules.

Attendee action: Paste the four starter rules into a project and adapt them.

Status: ready draft.

### After first repeated workflow: Build your first skill

Resource: `resources/first-skill.html`.

Use when: Tomer shows that repeated successful workflows should become reusable agent instructions.

Attendee action: Pick one repeated workflow and convert it into a skill.

Status: ready draft.

### Exercise handoff: Product brief generator

Resource: `resources/product-brief-generator.html`.

Use when: attendees need to turn a rough idea into a workable brief before asking an agent to build.

Attendee action: Produce a one-page brief with user, problem, workflow, non-goals, success signal, and next spec step.

Status: ready draft.

### Spec sanity check: OpenSpec-aware interviewer

Resource: `resources/openspec-interviewer.html`.

Use when: Tomer wants to show how to ask only the missing questions that materially affect implementation.

Attendee action: Run a brief or PRD through the interviewer prompt and answer the highest-impact questions.

Status: ready draft.

### Prompt feedback loop: Prompt improver

Resource: `resources/prompt-improver.html`.

Use when: Tomer demonstrates turning rough or negative feedback into clearer positive instructions.

Attendee action: Rewrite a rough prompt into goal, context, constraints, output format, and quality bar.

Status: ready draft.

### Planning handoff: PRD & OpenSpec starter

Resource: `resources/prd-openspec-starter.html`.

Use when: attendees have a brief and need to turn it into implementation-ready structure.

Attendee action: Draft concise PRD sections, concrete acceptance criteria, and an OpenSpec proposal outline.

Status: ready draft.

### Optional review surface: PRD to HTML workbench

Resource: `resources/prd-html-review-workbench.html`.

Use when: attendees have a PRD draft and Tomer wants to demonstrate the feedback loop from source spec to reviewable artifact back to model-ready change requests.

Attendee action: Render the PRD, add local section comments, and export a feedback packet for the next assistant or OpenSpec turn.

Status: ready prototype; second-wave giveaway, not required for the core first workshop flow.

## Priority 2 — show if polished before workshop

### A2X Marketplace

Resource: placeholder card on homepage.

Use when: Tomer wants to signal that A2X builds tools and extensions, not only workshops.

Attendee action: Browse public tools after the session.

Status: polish-first. Needs source and positioning.

### Prompt Magician

Resource: `resources/prompt-magician-setup.html`; likely source is public repo `https://github.com/thamam/prompt-enhancer-extension` with audit notes in `docs/prompt-magician-source-audit.md`.

Use when: Tomer moves from raw requests to reusable prompts.

Attendee action: Understand the optional extension workflow, privacy boundaries, API-key framing, and shortcut setup before trying richer prompt enhancement.

Status: ready overview; direct source-repo linking still needs a curated release path.

### Presentation editor

Resource: placeholder card on homepage; public slide-generator candidate is `https://github.com/thamam/talk-auto-slides-generator`, with audit notes in `docs/presentation-editor-source-audit.md`.

Use when: Tomer demos agentic editing beyond code.

Attendee action: Adapt the workflow to slides or written artifacts.

Status: polish-first. Source candidates located; needs curated workshop-safe setup/overview before direct hub linking.

### Wiki-LLM

Resource: `resources/wiki-llm-overview.html`; source path located with audit notes in `docs/wiki-llm-public-safety-audit.md`.

Use when: Tomer discusses knowledge-base workflows and advanced agent context.

Attendee action: Learn the `raw/`, `wiki/`, and operating-contract pattern using a fictional mini-vault before applying it to their own private notes.

Status: ready overview; direct source/software release still needs cleanup and Tomer approval.

## Priority 3 — defer if time is tight

### Credential tracer / auth routing

Resource source: existing A2X site resource.

Use when: attendees ask about Claude Code account billing, tokens, or environment-variable precedence.

Attendee action: Diagnose which credential route a session is using.

Status: defer for first resource hub unless the talk includes authentication troubleshooting.
