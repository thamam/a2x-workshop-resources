# Public launch checklist

Use this before Tomer approves public visibility or GitHub Pages publishing.

## Required checks

Latest audit: `docs/public-release-audit-2026-06-07.md`.

- [x] Repository visibility is still private until Tomer approves public release.
- [x] GitHub Pages is not enabled until Tomer approves publishing.
- [x] `scripts/block-private-files.sh` passes on all changed files.
- [x] Gitleaks passes locally or in GitHub Actions.
- [x] No `.env`, keys, credentials, tokens, private notes, client names, or local-only paths are present.
- [x] Every linked resource appears in `docs/resource-inventory.md`.
- [x] Every linked resource is classified `publish-now` or explicitly approved after `polish-first` cleanup.
- [x] No analytics, tracking, lead capture, pricing claims, or strong marketing claims were added.
- [x] Mobile layout was checked.
- [x] Desktop layout was checked.
- [x] GitHub Pages readiness notes in `docs/github-pages-readiness.md` are current.
- [x] `.nojekyll` is present if publishing through GitHub Pages.

## Prepared but not approved

- Static no-build structure exists at `index.html` plus `resources/*.html`.
- `.nojekyll` is present for future GitHub Pages compatibility.
- Publishing remains blocked until Tomer explicitly approves repository visibility and Pages settings.

## Approval record

Public release approved by: pending.

Date/time: pending.

Scope approved: pending.
