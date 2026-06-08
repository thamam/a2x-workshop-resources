# Public launch checklist

Use this before enabling GitHub Pages or expanding public release scope beyond the already approved repository visibility and website-link launch.

## Required checks

Latest audit: `docs/public-release-audit-2026-06-07.md`.

- [x] Repository visibility was changed to public only after Tomer approved public release on 2026-06-08.
- [x] GitHub Pages was enabled only after Tomer approved Pages publishing on 2026-06-08.
- [x] `scripts/block-private-files.sh` passes on all tracked and untracked files.
- [x] Gitleaks passes locally and in GitHub Actions.
- [x] No `.env`, keys, credentials, tokens, private notes, client names, or local-only paths are present in public-facing content.
- [x] Every linked resource appears in `docs/resource-inventory.md`.
- [x] Every linked resource is classified `publish-now` or explicitly approved after `polish-first` cleanup.
- [x] No analytics, tracking, lead capture, pricing claims, or strong marketing claims were added.
- [x] Mobile layout was checked.
- [x] Desktop layout was checked.
- [x] GitHub Pages readiness notes in `docs/github-pages-readiness.md` are current.
- [x] `.nojekyll` is present if publishing through GitHub Pages later.

## Enabled public surfaces

- Static no-build structure exists at `index.html` plus `resources/*.html`.
- GitHub Pages publishes from `main` branch `/` at `https://thamam.github.io/a2x-workshop-resources/`.
- Direct public source linking for A2X Marketplace and Wiki-LLM remains blocked until cleanup and approval.

## Approval record

Public release approved by: Tomer.

Date/time: 2026-06-08.

Scope approved: switch `thamam/a2x-workshop-resources` from private to public, connect it from the A2X website, and publish the Skill Wizard after the requested evaluation-mode fixes. Direct private/internal source exposure, analytics/tracking, lead capture, pricing claims, and strong marketing claims remain outside this approval.
