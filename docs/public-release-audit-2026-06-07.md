# Public release audit — 2026-06-07

Scope: autonomous safety/readiness refresh for the private A2X Workshop Resources Hub. This audit did **not** make the repository public, enable GitHub Pages, publish anything, add analytics/tracking/lead capture, or link private/internal resources publicly.

## Summary

- Repository remains private: `gh repo view --json nameWithOwner,isPrivate --jq '.nameWithOwner + " private=" + (.isPrivate|tostring)'` returned `thamam/a2x-workshop-resources private=true`.
- GitHub Pages remains unconfigured: `gh api repos/:owner/:repo/pages --jq '.status'` returned `HTTP 404 Not Found`, which is expected when Pages is not configured.
- GitHub Security Checks completed successfully for current pushed HEAD `164065d241bfadaebbe098dda4bc2a5d44bcc6bb` (`databaseId` 27090307403).
- Reconciled one discovered untracked public-facing artifact earlier in this cycle: `resources/buildtool-decision.html` has public-safe scope copy, no direct private/source links, mobile overflow fixes, hub/inventory/usage-map wiring, and sanitized public-safe references/tradeoff sections.
- Local safety checks passed for the current tree: static links, private-file blocker, gitleaks `--no-git`, and `git diff --check`.
- Local static-site HTTP smoke passed for all 18 discovered HTML files over `python3 -m http.server`.
- Chrome DevTools DOM/mobile smoke passed for all 18 discovered HTML files at a 390 × 844 viewport, including the canonical Kanban HTML view, public-safe tutorial pages, and the reconciled buildTool decision navigator.
- No safe unblocked implementation story is currently listed in `kanban-status.md`; remaining public publishing/source-linking work is approval-gated.

## Evidence

Audit timestamp from local environment:

```text
2026-06-07 13:58 IDT
```

Current pushed HEAD inspected in this refresh:

```text
164065d241bfadaebbe098dda4bc2a5d44bcc6bb
```

Latest commit subject at audit start:

```text
164065d docs: clarify buildtool audit baseline
```

### Repository visibility

Command:

```bash
gh repo view --json nameWithOwner,isPrivate --jq '.nameWithOwner + " private=" + (.isPrivate|tostring)'
```

Result:

```text
thamam/a2x-workshop-resources private=true
```

Interpretation: the repository is still private.

### GitHub Pages state

Command:

```bash
gh api repos/:owner/:repo/pages --jq '.status'
```

Result excerpt:

```text
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/pages/pages#get-a-apiname-pages-site","status":"404"}gh: Not Found (HTTP 404)
```

Interpretation: Pages is not configured, which matches the approval gate.

### GitHub Security Checks

Command:

```bash
gh run list --commit 164065d241bfadaebbe098dda4bc2a5d44bcc6bb --json databaseId,headSha,status,conclusion,name,displayTitle,createdAt --jq '.[] | [.databaseId,.name,.status,.conclusion,.headSha,.displayTitle,.createdAt] | @tsv'
```

Result:

```text
27090307403	Security checks	completed	success	164065d241bfadaebbe098dda4bc2a5d44bcc6bb	docs: clarify buildtool audit baseline	2026-06-07T10:46:43Z
```

Interpretation: current pushed HEAD has green GitHub Security Checks.

### Local checks

Commands and results:

```bash
python3 scripts/check-static-links.py
# Static link check passed for 18 HTML files.

scripts/block-private-files.sh $(git ls-files --cached --others --exclude-standard)
# exit 0

gitleaks detect --no-banner --redact --no-git --source .
# 1:58PM INF scanned ~357670 bytes (357.67 KB) in 68ms
# 1:58PM INF no leaks found

git diff --check
# exit 0
```

After updating this audit and moving the canonical tracker back to `DONE`, a final self-referential rerun rechecked the same local criteria: static links passed for 18 HTML files, private-file blocker exited 0, gitleaks reported no leaks, and `git diff --check` exited 0.

Maintenance Story M.4 also reran a targeted public-safety/mobile check for the edited `resources/buildtool-decision.html`: targeted text search found no A2X Marketplace GitHub URL, `repos/claude-code`, or user-home absolute-path references; local HTTP returned `200 text/html` for `index.html`, `kanban-status.html`, and `resources/buildtool-decision.html`; Chrome DevTools at `390x844` reported `clientWidth 390`, `scrollWidth 390`, `hasGithubMarketplaceLink false`, `hasLocalPath false`, `hasPublicSafeScope true`, and `hasReferences true`.

### Local HTTP smoke

Served the repo locally with:

```bash
python3 -m http.server 8786 --bind 127.0.0.1
```

HTTP smoke requested every HTML file and verified status `200` and `text/html` content type.

Result:

```text
200 index.html text/html
200 kanban-status.html text/html
200 resources/a2x-marketplace-overview.html text/html
200 resources/a2x-marketplace-tutorial.html text/html
200 resources/buildtool-decision.html text/html
200 resources/claude-code-harness-map.html text/html
200 resources/claude-md-cheat-sheet.html text/html
200 resources/first-skill.html text/html
200 resources/openspec-interviewer.html text/html
200 resources/openspec-tutorial.html text/html
200 resources/prd-html-review-workbench.html text/html
200 resources/prd-openspec-starter.html text/html
200 resources/presentation-editor-overview.html text/html
200 resources/product-brief-generator.html text/html
200 resources/prompt-improver.html text/html
200 resources/prompt-magician-setup.html text/html
200 resources/wiki-llm-overview.html text/html
200 resources/wiki-llm-tutorial.html text/html
HTTP smoke passed for 18 HTML files
```

### Chrome DevTools DOM/mobile smoke

Launched a dedicated headless Chrome with `--remote-debugging-port=9336`, loaded all HTML pages over the local HTTP server, set a `390x844` mobile viewport, and verified body/H1 structure plus no page-level horizontal overflow.

Command:

```bash
BASE_URL=http://127.0.0.1:8786/ CDP_URL=http://127.0.0.1:9336 PAGES='index.html,kanban-status.html,resources/a2x-marketplace-overview.html,resources/a2x-marketplace-tutorial.html,resources/buildtool-decision.html,resources/claude-code-harness-map.html,resources/claude-md-cheat-sheet.html,resources/first-skill.html,resources/openspec-interviewer.html,resources/openspec-tutorial.html,resources/prd-html-review-workbench.html,resources/prd-openspec-starter.html,resources/presentation-editor-overview.html,resources/product-brief-generator.html,resources/prompt-improver.html,resources/prompt-magician-setup.html,resources/wiki-llm-overview.html,resources/wiki-llm-tutorial.html' node <static-dom-mobile-smoke.mjs>
```

Result:

```text
DOM OK index.html (4548 chars, h1='Claude Code workshop resources.', width 390/390)
DOM OK kanban-status.html (50191 chars, h1='Project Kanban, readable at a glance.', width 390/390)
DOM OK resources/a2x-marketplace-overview.html (3016 chars, h1='A2X Marketplace overview.', width 390/390)
DOM OK resources/a2x-marketplace-tutorial.html (3507 chars, h1='A2X Marketplace tutorial.', width 390/390)
DOM OK resources/buildtool-decision.html (8659 chars, h1='Should we ship a first-class buildTool?', width 390/390)
DOM OK resources/claude-code-harness-map.html (1584 chars, h1='The harness, not just the model.', width 390/390)
DOM OK resources/claude-md-cheat-sheet.html (1169 chars, h1='CLAUDE.md & coding rules cheat sheet.', width 390/390)
DOM OK resources/first-skill.html (1081 chars, h1='Build your first skill.', width 390/390)
DOM OK resources/openspec-interviewer.html (527 chars, h1='OpenSpec-aware interviewer.', width 390/390)
DOM OK resources/openspec-tutorial.html (2540 chars, h1='How to use OpenSpec with agents.', width 390/390)
DOM OK resources/prd-html-review-workbench.html (1188 chars, h1='PRD to HTML review workbench.', width 390/390)
DOM OK resources/prd-openspec-starter.html (952 chars, h1='PRD & OpenSpec starter.', width 390/390)
DOM OK resources/presentation-editor-overview.html (3379 chars, h1='Presentation editor overview.', width 390/390)
DOM OK resources/product-brief-generator.html (606 chars, h1='Product brief generator.', width 390/390)
DOM OK resources/prompt-improver.html (578 chars, h1='Prompt improver.', width 390/390)
DOM OK resources/prompt-magician-setup.html (3011 chars, h1='Prompt Magician setup overview.', width 390/390)
DOM OK resources/wiki-llm-overview.html (2804 chars, h1='Wiki-LLM overview.', width 390/390)
DOM OK resources/wiki-llm-tutorial.html (2498 chars, h1='How to work with an LLM Wiki.', width 390/390)
Chrome DevTools DOM/mobile smoke passed for 18 pages at 390x844
```

## Remaining approval gates

Still blocked until Tomer explicitly approves:

- Making the repository public.
- Enabling or publishing GitHub Pages.
- Linking private/internal resources publicly.
- Directly exposing A2X Marketplace or Wiki-LLM source/software release paths before cleanup/review.

## Recommendation

No new safe unblocked implementation story is listed in `kanban-status.md`. Continue only with periodic verification refreshes or with new scope from Tomer; do not publish or expose source links without approval.
