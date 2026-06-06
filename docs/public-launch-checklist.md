# Public launch checklist

Use this before Tomer approves public visibility or GitHub Pages publishing.

## Required checks

- [ ] Repository visibility is still private until Tomer approves public release.
- [ ] GitHub Pages is not enabled until Tomer approves publishing.
- [ ] `scripts/block-private-files.sh` passes on all changed files.
- [ ] Gitleaks passes locally or in GitHub Actions.
- [ ] No `.env`, keys, credentials, tokens, private notes, client names, or local-only paths are present.
- [ ] Every linked resource appears in `docs/resource-inventory.md`.
- [ ] Every linked resource is classified `publish-now` or explicitly approved after `polish-first` cleanup.
- [ ] No analytics, tracking, lead capture, pricing claims, or strong marketing claims were added.
- [ ] Mobile layout was checked.
- [ ] Desktop layout was checked.
- [ ] GitHub Pages readiness notes in `docs/github-pages-readiness.md` are current.
- [ ] `.nojekyll` is present if publishing through GitHub Pages.

## Prepared but not approved

- Static no-build structure exists at `index.html` plus `resources/*.html`.
- `.nojekyll` is present for future GitHub Pages compatibility.
- Publishing remains blocked until Tomer explicitly approves repository visibility and Pages settings.

## Approval record

Public release approved by: pending.

Date/time: pending.

Scope approved: pending.
