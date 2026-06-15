# HowTo-OpenSpec — Basic Setup

OpenSpec is useful because it gives an agent a small proposal/spec workflow before it starts changing code. For tomorrow, treat this as **spec-before-code**, not bureaucracy.

## Goal

Create a tiny OpenSpec-style workspace where Claude Code can:

- write a proposal before implementation,
- list scope and non-goals,
- define acceptance criteria,
- capture open questions,
- implement only after the proposal is reviewed.

## Minimal folder tree

Use this structure inside a project repo:

```text
openspec/
  README.md
  project.md
  changes/
    .gitkeep
```

For this workshop repo, an empty starter location exists at:

```text
Examples/OpenSpec/
```

## Setup steps

1. In the project you want to use with Claude Code, create the folders:

   ```bash
   mkdir -p openspec/changes
   touch openspec/changes/.gitkeep
   ```

2. Create `openspec/project.md`:

   ```markdown
   # Project context

   ## What this project does
   [One paragraph.]

   ## Important constraints
   - No secrets in prompts or commits.
   - Human review before production-impacting changes.
   - Keep changes small and reversible.

   ## Verification commands
   - [test command]
   - [link check / preview command]
   ```

3. Create one proposal per change:

   ```text
   openspec/changes/<short-change-name>/proposal.md
   openspec/changes/<short-change-name>/tasks.md
   ```

4. Ask Claude Code to draft the proposal **before editing files**.

## Proposal template

```markdown
# Change proposal: [short name]

## Why
What user or business problem does this solve?

## What changes
- [concrete change]
- [concrete change]

## Non-goals
- [what not to build now]

## Impact
Files, users, workflows, data, integrations, or risks affected.

## Acceptance criteria
- Given..., when..., then...
- Verification step...

## Open questions
Only questions that materially affect implementation.
```

## Claude Code prompt

```text
Read openspec/project.md.
Create an OpenSpec-style proposal for the change below.
Do not edit implementation files yet.

Return:
1. Why
2. Proposed changes
3. Non-goals
4. Impact
5. Acceptance criteria
6. Risks
7. Open questions
8. Recommendation: proceed, split, or clarify first

Change request:
[paste request]
```

## Decision rule

- **Proceed** when scope, risk, and acceptance criteria are clear.
- **Clarify** when one missing answer could change implementation.
- **Split** when the proposal mixes unrelated changes.
- **Stop** when the change touches secrets, production systems, money, private data, or irreversible actions without explicit approval.

## Related local material

- HTML tutorial: [`resources/openspec-tutorial.html`](resources/openspec-tutorial.html)
- Starter example tree: [`Examples/OpenSpec/`](Examples/OpenSpec/)
