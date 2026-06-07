# Public release audit — 2026-06-07

Scope: autonomous safety/readiness refresh for the private A2X Workshop Resources Hub. This audit did **not** make the repository public, enable GitHub Pages, publish anything, add analytics/tracking/lead capture, or link private/internal resources publicly.

## Summary

- Repository remains private: `gh repo view --json nameWithOwner,visibility,isPrivate,defaultBranchRef` returned `visibility=PRIVATE` and `isPrivate=true` for `thamam/a2x-workshop-resources`.
- GitHub Pages remains unconfigured: `gh api repos/:owner/:repo/pages --jq '.status'` returned `HTTP 404 Not Found`, which is expected when Pages is not configured.
- GitHub Security Checks completed successfully for current pushed HEAD `c5a78263651475fbc4cb39fcd1dec013f457bb0f` (`databaseId` 27091671705).
- Local safety checks passed for the current tree: static links, private-file blocker, gitleaks `--no-git`, and `git diff --check`.
- Local static-site HTTP smoke passed for all 18 discovered HTML files over `python3 -m http.server`.
- Chrome DevTools DOM/mobile smoke passed for all 18 discovered HTML files at a 390 × 844 viewport, including the canonical Kanban HTML view and the buildTool decision navigator.
- No safe unblocked implementation story is currently listed in `kanban-status.md`; remaining public publishing/source-linking work is approval-gated.

## Evidence

Audit timestamp from local environment:

```text
2026-06-07 15:01 IDT
```

Current pushed HEAD inspected in this refresh:

```text
c5a78263651475fbc4cb39fcd1dec013f457bb0f
```

Latest commit subject at audit start:

```text
c5a7826 docs: refresh current public readiness evidence
```

### Repository visibility

Command:

```bash
gh repo view --json nameWithOwner,visibility,isPrivate,defaultBranchRef
```

Result:

```json
{"defaultBranchRef":{"name":"main"},"isPrivate":true,"nameWithOwner":"thamam/a2x-workshop-resources","visibility":"PRIVATE"}
```

Interpretation: the repository is still private.

### GitHub Pages state

Command:

```bash
set +e
gh api repos/:owner/:repo/pages --jq '.status'
echo pages_exit=$?
```

Result excerpt:

```text
{"message":"Not Found","documentation_url":"https://docs.github.com/rest/pages/pages#get-a-apiname-pages-site","status":"404"}gh: Not Found (HTTP 404)
pages_exit=1
```

Interpretation: Pages is not configured, which matches the approval gate.

### GitHub Security Checks

Command:

```bash
gh run list --commit c5a78263651475fbc4cb39fcd1dec013f457bb0f --json databaseId,headSha,status,conclusion,name,displayTitle,createdAt --jq '.[] | [.databaseId,.name,.status,.conclusion,.headSha,.displayTitle,.createdAt] | @tsv'
```

Result:

```text
27091671705	Security checks	completed	success	c5a78263651475fbc4cb39fcd1dec013f457bb0f	docs: refresh current public readiness evidence	2026-06-07T11:48:31Z
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
# scanned ~362.68 KB and reported no leaks found
# exit 0

git diff --check
# exit 0
```

These results are from the final local verification pass before updating this audit/tracker evidence.

### Local HTTP smoke

Served the repo locally with:

```bash
python3 -m http.server 8789 --bind 127.0.0.1
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

Launched a dedicated headless Chrome with `--remote-debugging-port=9340`, loaded all HTML pages over the local HTTP server, set a `390x844` mobile viewport, and verified body/H1 structure plus no page-level horizontal overflow.

Command:

```bash
BASE_URL=http://127.0.0.1:8789/ CDP_URL=http://127.0.0.1:9340 PAGES='<all 18 HTML pages>' node <static-dom-mobile-smoke.mjs>
```

Result:

```text
DOM OK index.html (11902 bytes, h1='Claude Code workshop resources.', width 390/390)
DOM OK kanban-status.html (89787 bytes, h1='Project Kanban, readable at a glance.', width 390/390)
DOM OK resources/a2x-marketplace-overview.html (6666 bytes, h1='A2X Marketplace overview.', width 390/390)
DOM OK resources/a2x-marketplace-tutorial.html (7165 bytes, h1='A2X Marketplace tutorial.', width 390/390)
DOM OK resources/buildtool-decision.html (70444 bytes, h1='Should we ship a first-class buildTool?', width 390/390)
DOM OK resources/claude-code-harness-map.html (3313 bytes, h1='The harness, not just the model.', width 390/390)
DOM OK resources/claude-md-cheat-sheet.html (2406 bytes, h1='CLAUDE.md & coding rules cheat sheet.', width 390/390)
DOM OK resources/first-skill.html (2292 bytes, h1='Build your first skill.', width 390/390)
DOM OK resources/openspec-interviewer.html (4912 bytes, h1='OpenSpec-aware interviewer.', width 390/390)
DOM OK resources/openspec-tutorial.html (5755 bytes, h1='How to use OpenSpec with agents.', width 390/390)
DOM OK resources/prd-html-review-workbench.html (12934 bytes, h1='PRD to HTML review workbench.', width 390/390)
DOM OK resources/prd-openspec-starter.html (6135 bytes, h1='PRD & OpenSpec starter.', width 390/390)
DOM OK resources/presentation-editor-overview.html (6823 bytes, h1='Presentation editor overview.', width 390/390)
DOM OK resources/product-brief-generator.html (5606 bytes, h1='Product brief generator.', width 390/390)
DOM OK resources/prompt-improver.html (5185 bytes, h1='Prompt improver.', width 390/390)
DOM OK resources/prompt-magician-setup.html (6420 bytes, h1='Prompt Magician setup overview.', width 390/390)
DOM OK resources/wiki-llm-overview.html (6209 bytes, h1='Wiki-LLM overview.', width 390/390)
DOM OK resources/wiki-llm-tutorial.html (5698 bytes, h1='How to work with an LLM Wiki.', width 390/390)
Representative Chrome DevTools DOM/mobile smoke passed for 18 pages at 390x844
```

## Remaining approval gates

Still blocked until Tomer explicitly approves:

- Making the repository public.
- Enabling or publishing GitHub Pages.
- Linking private/internal resources publicly.
- Directly exposing A2X Marketplace or Wiki-LLM source/software release paths before cleanup/review.

## Recommendation

No new safe unblocked implementation story is listed in `kanban-status.md`. Continue only with periodic verification refreshes or with new scope from Tomer; do not publish or expose source links without approval.
