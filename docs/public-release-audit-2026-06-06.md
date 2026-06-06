# Public release audit — 2026-06-06

Scope: local and GitHub preflight audit for the private `a2x-workshop-resources` repository. This does **not** approve or perform public release.

## Result

Technical preflight is green for the current private-repo state. Public release remains approval-gated: Tomer still needs to approve repository visibility and GitHub Pages publishing before any public launch.

## Evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Repository visibility | Pass | `gh repo view --json isPrivate,nameWithOwner,url,homepageUrl` returned `isPrivate: true` for `thamam/a2x-workshop-resources`. |
| GitHub Pages status | Pass | `gh api repos/:owner/:repo/pages --include` returned `HTTP/2.0 404 Not Found`, meaning Pages is not configured. |
| Private-file blocker | Pass | `scripts/block-private-files.sh $(git ls-files)` exited 0. |
| Secret scan | Pass | `gitleaks detect --no-banner --redact --source .` scanned 16 commits and reported `no leaks found`. |
| Static links | Pass | `python3 scripts/check-static-links.py` reported `Static link check passed for 9 HTML files.` |
| Public-facing local links | Pass | Parsed `index.html`, `kanban-status.html`, and `resources/*.html`: all links are local/relative or anchors; no external links found. |
| Local HTTP smoke | Pass | Local server returned HTTP 200 `text/html` for 9 HTML pages. |
| Mobile/desktop render smoke | Pass | Chrome Headless dumped DOM for `index.html` at 390×844 and 1440×1000; previous mobile viewport review also records no horizontal overflow for the hub and giveaway pages. |
| Launch checklist/readiness docs | Pass | `docs/public-launch-checklist.md` and `docs/github-pages-readiness.md` exist and retain approval gates. |

## Pages served during HTTP smoke

- `index.html` — 200 `text/html`
- `kanban-status.html` — 200 `text/html`
- `resources/claude-md-cheat-sheet.html` — 200 `text/html`
- `resources/first-skill.html` — 200 `text/html`
- `resources/claude-code-harness-map.html` — 200 `text/html`
- `resources/product-brief-generator.html` — 200 `text/html`
- `resources/openspec-interviewer.html` — 200 `text/html`
- `resources/prompt-improver.html` — 200 `text/html`
- `resources/prd-openspec-starter.html` — 200 `text/html`

## Remaining approval gates

- Do not make the repository public until Tomer approves.
- Do not enable or publish GitHub Pages until Tomer approves.
- Do not link A2X Marketplace, Prompt Magician, presentation editor, or Wiki-LLM sources publicly until their public-safe source paths are audited.

## Notes

- Advanced-demo cards on the hub are placeholders with no outbound links.
- Resource inventory still lists A2X Marketplace, Prompt Magician, presentation editor, and Wiki-LLM as `polish-first`; this does not block the current hub because those entries are not linked publicly.
