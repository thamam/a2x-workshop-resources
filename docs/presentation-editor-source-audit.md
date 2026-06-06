# Presentation editor source audit

Date: 2026-06-06  
Story: 4.6 — locate presentation editor source/setup doc

## Summary

Two presentation-related candidates were found:

1. Public GitHub candidate: `https://github.com/thamam/talk-auto-slides-generator`
2. Private/internal GitHub candidate: exact repository link intentionally omitted from this public-ready repo.

Recommendation for the workshop hub: keep the homepage presentation-editor card unlinked for now. If Tomer wants a first-wave public resource, create a short sanitized overview page that links only to the public slide-generator repo after its README/setup copy is reframed for attendees. Do not expose the private/internal candidate unless it is intentionally sanitized and approved.

## Public candidate: talk-auto-slides-generator

Likely fit: **live/interactive slide generation demo**.

Observed setup path:

```bash
npm install
# Set GEMINI_API_KEY in .env.local or hosting secrets
npm run dev
```

Observed local commands:

```bash
npm run build
npm run lint   # script name runs tsc --noEmit
```

Notes from inspection:

- Vite/React app with Express API server (`server.ts`) and Gemini dependency (`@google/genai`).
- README is still AI Studio-style boilerplate and includes an AI Studio app URL.
- Requires `GEMINI_API_KEY`; no real key was found in the shallow clone.
- UI flow starts with manual presentation title/overview/outline, then generates slide content via `/api/generate-slide`.
- This looks closer to a dynamic slide-generation demo than a general-purpose slide editor/export tool.

Safety result:

- `gitleaks detect --source <temporary-public-candidate-audit-dir> --no-banner --redact --exit-code 1` reported **no leaks** for the shallow clone.
- Manual secret-ish scan found only setup references to `GEMINI_API_KEY`, placeholder `.env.example`, package-lock token substrings, and code reading `process.env.GEMINI_API_KEY`.
- `npm ci --ignore-scripts --no-audit --no-fund --silent --prefix <temporary-public-candidate-audit-dir>` completed successfully.
- `npm run build --prefix <temporary-public-candidate-audit-dir>` completed successfully.

Public-readiness concerns before linking:

- Replace AI Studio boilerplate with workshop-safe setup and demo instructions.
- Clarify that attendees need their own Gemini API key or that Tomer will demo it live.
- Avoid implying production reliability, pricing, or broad product claims.
- Confirm the AI Studio app URL is intended to be public before keeping it in attendee-facing docs.

## Private/internal candidate

Likely fit: **document-to-presentation outline/editor prototype**.

Observed setup path from its README:

```bash
npm install
npm run dev
# development server noted as http://localhost:8080
npm run lint
npm test
```

Observed local commands:

```bash
npm run build
npm run typecheck
npm test / npm run test:run
```

Notes from inspection:

- Vite/React/shadcn/Tailwind app for converting documents into interactive presentation outlines.
- Supports upload/edit flows; export/generate-presentation appears marked as a future phase/TODO.
- Includes parser fixtures, benchmark reports, generated test result files, and `.claude` planning/report artifacts.
- Includes Supabase integration code with project URL and publishable key in source, plus internal Claude/project-health notes describing credential cleanup needs.

Safety result:

- `gitleaks detect --source <temporary-private-candidate-audit-dir> --no-banner --redact --exit-code 1` found **5 findings** in the shallow clone:
  - 1 JWT-style finding in `src/integrations/supabase/client.ts` for a hardcoded Supabase publishable key.
  - 4 fixture/report findings in parser test docs/results that appear to be synthetic API-token examples.
- Manual secret-ish scan also surfaced `.claude` internal notes and many synthetic credential examples in test fixtures.
- `npm ci --ignore-scripts --no-audit --no-fund --silent --prefix <temporary-private-candidate-audit-dir>` completed successfully.
- `npm run build --prefix <temporary-private-candidate-audit-dir>` completed successfully.

Public-readiness concerns before linking or copying:

- Do not link this source publicly from the hub while it remains private/internal.
- Do not copy `.claude` notes, benchmark reports, generated fixture outputs, local project-health commentary, or Supabase integration details into public workshop material.
- If this becomes public later, first move environment/config values out of source, prune generated reports/internal notes, and replace synthetic credential-heavy fixtures in public-facing docs.
- For the first workshop, prefer a sanitized overview/demo script over a direct source link.

## Recommended hub treatment

Inventory status should remain `polish-first`.

Suggested attendee-facing framing:

> Presentation editor — a demo pattern for turning outlines or documents into editable slide artifacts. Source and setup are still being cleaned up, so use the workshop-safe summary until the demo repo is ready.

Suggested next action:

- If a presentation demo is needed live: use the public slide-generator repo as the source candidate after README cleanup.
- If a document-to-slides workflow is needed: write a sanitized static overview/resource page without exposing the private/internal repo.
- Keep the homepage placeholder card unlinked until one of those paths is deliberately chosen.
