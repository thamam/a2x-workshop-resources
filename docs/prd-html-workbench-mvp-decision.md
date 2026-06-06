# PRD-to-HTML workbench MVP decision

Date: 2026-06-06  
Status: scoped for safe prototype; implementation still optional and should not block the first workshop hub.

## Decision

Build the first PRD-to-HTML workbench as a **public-safe static giveaway prototype**, not as an internal A2X production tool.

The MVP should use **plain PRD Markdown plus optional OpenSpec proposal sections**. Plain PRD Markdown is the default attendee path; OpenSpec is an advanced export shape, not a prerequisite.

Comments should be **local-only in browser memory with explicit copy/export**, not persisted, synced, or sent anywhere.

## Why this scope

The research memo found that the valuable pattern is round-tripping: source spec → beautiful review artifact → human feedback → structured packet back to a model or OpenSpec change. The safest workshop slice demonstrates that pattern without accounts, storage, integrations, or model API calls.

The sanitized giveaway scenario also showed that attendees benefit most from a clear handoff chain before any heavier workbench:

1. Generate a concise product brief.
2. Ask only high-impact missing questions.
3. Improve the build prompt.
4. Convert the brief into PRD/OpenSpec structure.
5. Optionally render that PRD into a review surface.

That makes the workbench a second-wave giveaway, not a blocker for the first workshop kit.

## MVP shape

### Input

- Paste plain Markdown PRD.
- Optional OpenSpec-like sections are allowed if present:
  - `## Why`
  - `## What changes`
  - `## Impact`
  - `## Acceptance criteria`
- Include a sample synthetic PRD fixture so attendees do not need private client material.

### Rendered review surface

- Parse Markdown headings into sections.
- Render a polished single-page review artifact with cards or section panels.
- Highlight missing common sections such as users, non-goals, constraints, acceptance criteria, and risks.
- Keep styles consistent with the existing A2X dark static handouts.

### Feedback loop

- Allow local section comments in browser memory.
- Export a copyable feedback packet:
  - section title
  - comment
  - severity or type: question, change request, risk, acceptance-criteria gap
  - suggested next model instruction
- Do not save comments to disk, backend, localStorage, cloud services, or third-party tools in MVP.

### Output formats

- Primary: copyable Markdown feedback packet for any AI assistant.
- Secondary: OpenSpec proposal feedback shape when the source includes OpenSpec sections.

## Explicit non-goals

- No public publishing or GitHub Pages enablement.
- No backend.
- No account/login.
- No analytics or tracking.
- No lead capture.
- No model API calls.
- No GitHub sync.
- No private A2X resource links.
- No local filesystem writes from the browser.
- No claim that the workbench produces production-ready specs automatically.

## Approval boundaries

Yunes may autonomously create a static prototype file in this private repo if time allows and checks remain green.

Tomer approval is required before:

- Publishing the prototype publicly.
- Presenting it as an official A2X product.
- Connecting it to private A2X systems or internal resources.
- Adding persistence, analytics, capture forms, or model API calls.

## Recommended next build task

If continuing this goal, add `resources/prd-html-review-workbench.html` as a static prototype with:

1. PRD Markdown textarea.
2. “Render review page” button.
3. Section cards parsed from headings.
4. Per-section comment inputs held in memory.
5. “Export feedback packet” button.
6. Synthetic fixture button using the consultant meeting-prep scenario.
7. No network calls, storage, or external links.

## Completion criteria for prototype

- Static link check passes.
- Private-file blocker passes.
- Gitleaks passes or CI covers secret scanning.
- Mobile viewport smoke test passes at 390px.
- Browser smoke test verifies fixture render and feedback export.
