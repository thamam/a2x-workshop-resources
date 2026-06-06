# Giveaway scenario chain test

Date: 2026-06-06  
Scenario status: public-safe synthetic workshop example.  
Purpose: Validate the first giveaway bundle as a coherent attendee flow before Tomer reviews the wording live.

## Sanitized workshop scenario

**Idea:** A personal meeting-prep assistant for independent consultants.

**Target user:** Solo consultants who have multiple client calls each week and need to prepare quickly without exposing private client data.

**Problem / pain:** Meeting notes, action items, and context are scattered across docs, email summaries, and calendars. Prep often happens ten minutes before the call, so the consultant forgets prior commitments or asks repeated questions.

**Proposed workflow:** The user pastes or selects sanitized notes for one client and upcoming meeting. The tool returns a short prep brief with goals, open commitments, risks, and suggested questions.

**Constraints:** Static or local-first v1. No calendar/email integrations in the first version. No storage of client content. Must produce useful output from pasted text only.

**Out of scope:** Automatic syncing, CRM features, team collaboration, billing, call recording, transcription, and sending messages to clients.

**Success signal:** In a workshop demo, an attendee can paste a short synthetic note bundle and get a useful one-page prep brief in under two minutes.

**Open questions:** Which input sections are mandatory? Should the output be optimized for a pre-call checklist or an after-call follow-up plan?

## Step 1 — Product brief generator result

The current product brief generator prompt handles the scenario well. It asks for a compact brief, labels assumptions, and caps open questions at three.

Expected generated brief from the scenario:

1. **One-sentence product idea:** A local-first meeting-prep assistant that turns pasted, sanitized client notes into a concise pre-call brief for solo consultants.
2. **Target user:** Solo consultants managing multiple weekly client conversations.
3. **Problem / pain:** Context is scattered, prep time is short, and missed commitments can damage trust.
4. **Proposed workflow:** User pastes synthetic or sanitized meeting context; tool returns goals, commitments, risks, and suggested questions.
5. **Non-goals / out of scope:** Integrations, storage, CRM, billing, transcription, call recording, and outbound communication.
6. **Success signal:** Attendee can generate a useful one-page prep brief from pasted notes in under two minutes.
7. **Assumptions:** The v1 can be single-user, paste-only, and ephemeral. The user accepts manual sanitization for demo safety.
8. **Open questions, max 3:** Mandatory input sections; checklist vs follow-up emphasis; whether the tool should include confidence flags when source notes are thin.
9. **Next step toward a spec:** Use the OpenSpec-aware interviewer to resolve the output shape and implementation boundaries.

Finding: no copy change required on this page for the scenario.

## Step 2 — OpenSpec-aware interviewer result

The interviewer prompt correctly focuses on implementation-changing gaps rather than formatting.

High-impact questions surfaced by the scenario:

1. What exact input sections are required for v1: meeting goal, previous commitments, attendee list, recent notes, or all optional pasted context?
2. Should the primary output be a pre-call checklist, an agenda, a risk summary, a follow-up draft, or a fixed combination?
3. How should the tool handle insufficient or conflicting pasted context?
4. What privacy promise is testable in a static/local-first v1: no network calls, no storage, or both?
5. What demo fixture should be included so workshop attendees can try the flow without private client material?

Safe assumptions:

- v1 should be paste-only and client-side/static.
- No integrations or persistence should be included.
- A synthetic demo fixture is acceptable and safer than asking attendees to paste real client notes.

Recommendation: proceed to a concise PRD after answering the output shape and thin-context behavior.

Finding: no copy change required, but the hub should eventually include a synthetic fixture for live demos.

## Step 3 — Prompt improver result

Rough prompt used in the test:

> Make a meeting prep assistant. Don't make it generic. It should use notes and tell me what to ask.

Current prompt improver output shape is useful because it asks the model to convert “don't make it generic” into positive guidance.

Improved prompt target:

> Turn the pasted meeting context into a specific, source-grounded pre-call brief for a solo consultant. Use only the provided notes. Include: meeting objective, relevant prior commitments, likely risks, suggested questions, and missing-context warnings. Keep it to one page. If the notes are too thin, say what is missing instead of inventing client details.

Positive rewrite of negative correction:

- Instead of “don't make it generic,” use: “Make every recommendation traceable to the pasted notes or label it as a missing-context question.”

Finding: no copy change required. The page already explains why positive rewrites matter.

## Step 4 — PRD & OpenSpec starter result

The static PRD starter prompt can accept the generated product brief, but the page is less consistent than the first three giveaway tools because it is not form-driven and cannot generate a customized prompt.

PRD skeleton produced by the scenario:

### Problem

Solo consultants need reliable pre-call context without exposing private client data or spending time on integrations.

### Goal

Provide a static/local-first workflow that turns pasted notes into a one-page prep brief.

### Users

Solo consultants and workshop attendees practicing agent handoffs with synthetic client notes.

### Non-goals

Calendar/email integrations, storage, CRM features, transcription, billing, collaboration, and outbound messaging.

### Key flows

1. User opens the static page.
2. User pastes sanitized notes or demo fixture text.
3. User selects or accepts the pre-call brief output shape.
4. Tool/prompt returns meeting objective, commitments, risks, questions, and missing-context warnings.

### Functional requirements

- Accept pasted notes only.
- Produce a concise one-page prep brief.
- Warn when required context is absent.
- Avoid inventing private client details.
- Keep the v1 static/local-first with no network calls or storage.

### Acceptance criteria

- Given the synthetic demo fixture, the output includes at least one objective, one prior commitment, one risk, and three suggested questions.
- Given thin notes, the output labels missing context instead of fabricating details.
- The page states that users should not paste private client material into public demos.

### OpenSpec proposal outline

- **Why:** reduce rushed meeting prep while preserving privacy boundaries.
- **What changes:** add a paste-only prep brief generator and synthetic fixture.
- **Impact:** attendees get a safe demo path; no integrations or storage are introduced.
- **Acceptance criteria:** fixture path works, thin-context behavior is explicit, and no network/storage behavior is added.

Finding: K3 should convert `resources/prd-openspec-starter.html` into an interactive generator like the first three pages.

## Overall findings

- The first three handouts form a coherent chain for a realistic public-safe workshop scenario.
- The PRD/OpenSpec starter is substantively useful but visually and interaction-wise weaker than the other giveaway pages.
- A future synthetic fixture page or section would make the live demo safer and faster.
- No private links, local paths, client data, credentials, pricing claims, analytics, or publishing changes were introduced in this test.

## Follow-up tasks

1. Convert the PRD/OpenSpec starter into a form-driven generator.
2. Consider adding a reusable synthetic demo fixture after the visual consistency pass.
3. Re-run static link and private-file checks after page changes.
