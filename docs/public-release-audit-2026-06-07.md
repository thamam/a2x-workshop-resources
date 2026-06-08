# Public release audit — 2026-06-07

Scope: safety/readiness refresh for the A2X Workshop Resources Hub after Tomer-approved public visibility, Tomer-approved GitHub Pages publishing for the fixed Skill Wizard, and the later hub backlink to the A2X website. This audit did **not** add analytics/tracking/lead capture, add pricing or marketing claims, change repository visibility, change Pages configuration, or expose private/internal resource sources.

## Summary

- Repository visibility is public by approval: `gh repo view thamam/a2x-workshop-resources --json nameWithOwner,isPrivate,visibility,url` returned `visibility=PUBLIC`, `isPrivate=false`, and URL `https://github.com/thamam/a2x-workshop-resources`.
- GitHub Pages is enabled by approval and built from `main` branch `/`: `https://thamam.github.io/a2x-workshop-resources/`.
- GitHub Security Checks completed successfully for current HEAD `b01996aa375ac1514fe1575ec500d1d3ad33c570` (`databaseId` 27153624110); the Pages build/deployment workflow also completed successfully (`databaseId` 27153622859).
- Local safety checks passed for the current tree: static links for 19 HTML files, private-file blocker, gitleaks `--no-git`, and `git diff --check`.
- Public smoke checks returned HTTP 200 for the workshop hub, the Skill Wizard page, and the approved A2X website backlinks. The A2X website smoke used a browser-style User-Agent after a default Python urllib request returned 403.
- The latest public-launch state is recorded in `kanban-status.md`: Tomer approved switching `thamam/a2x-workshop-resources` from private to public, connecting it from the A2X website, and publishing the fixed Skill Wizard on 2026-06-08.
- Remaining source-release gates still apply: direct public source linking for A2X Marketplace and Wiki-LLM remains blocked until cleanup and approval.

## Evidence

Audit timestamp from local environment:

```text
2026-06-08 22:01 IDT
```

Current HEAD inspected in this refresh:

```text
b01996aa375ac1514fe1575ec500d1d3ad33c570
```

Latest commit subject at audit start:

```text
b01996a Refresh current public readiness evidence
```

### Repository visibility

Command:

```bash
gh repo view thamam/a2x-workshop-resources --json nameWithOwner,visibility,isPrivate,url
```

Result:

```json
{"isPrivate":false,"nameWithOwner":"thamam/a2x-workshop-resources","url":"https://github.com/thamam/a2x-workshop-resources","visibility":"PUBLIC"}
```

Interpretation: the repository is public after the approval recorded in `kanban-status.md`.

### GitHub Pages state

Command:

```bash
gh api repos/thamam/a2x-workshop-resources/pages --jq '{status:.status, html_url:.html_url, source:.source}'
```

Result:

```json
{"html_url":"https://thamam.github.io/a2x-workshop-resources/","source":{"branch":"main","path":"/"},"status":"built"}
```

Interpretation: GitHub Pages is configured and built from `main` branch `/` after Tomer's approval to publish the fixed Skill Wizard.

### Public page smoke

Command:

```bash
python3 - <<'PY'
import urllib.request
for url in [
 'https://thamam.github.io/a2x-workshop-resources/',
 'https://thamam.github.io/a2x-workshop-resources/resources/claude-wizard-skill-wizard.html',
 'https://a2xautonomy.com/',
 'https://a2xautonomy.com/#resources',
]:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Yunes public-readiness smoke)'})
    with urllib.request.urlopen(req, timeout=20) as r:
        body = r.read(2000).decode('utf-8', 'ignore')
        print(url, r.status, r.headers.get_content_type(), 'marker=', 'A2X' in body or 'Skill Wizard' in body or 'resources' in body.lower())
PY
```

Result:

```text
https://thamam.github.io/a2x-workshop-resources/ 200 text/html marker= True
https://thamam.github.io/a2x-workshop-resources/resources/claude-wizard-skill-wizard.html 200 text/html marker= True
https://a2xautonomy.com/ 200 text/html marker= True
https://a2xautonomy.com/#resources 200 text/html marker= True
```

### GitHub checks

Command:

```bash
sha=$(git rev-parse HEAD)
gh run list --commit "$sha" --limit 10 --json databaseId,workflowName,status,conclusion,headSha --jq ".[] | select(.headSha == \"$sha\")"
```

Result:

```json
{"conclusion":"success","createdAt":"2026-06-08T16:59:46Z","databaseId":27153624110,"headSha":"b01996aa375ac1514fe1575ec500d1d3ad33c570","status":"completed","updatedAt":"2026-06-08T17:00:01Z","url":"https://github.com/thamam/a2x-workshop-resources/actions/runs/27153624110","workflowName":"Security checks"}
{"conclusion":"success","createdAt":"2026-06-08T16:59:45Z","databaseId":27153622859,"headSha":"b01996aa375ac1514fe1575ec500d1d3ad33c570","status":"completed","updatedAt":"2026-06-08T17:00:10Z","url":"https://github.com/thamam/a2x-workshop-resources/actions/runs/27153622859","workflowName":"pages-build-deployment"}
```

Interpretation: current pushed HEAD has green Security Checks and green Pages build/deployment checks.

### Local checks

Commands and results:

```bash
python3 scripts/check-static-links.py
# Static link check passed for 19 HTML files.

scripts/block-private-files.sh $(git ls-files --cached --others --exclude-standard)
# exit 0

gitleaks detect --no-banner --redact --no-git --source .
# no leaks found
# exit 0

git diff --check
# exit 0
```

### Current evidence-refresh diff inspected

Command:

```bash
git show --stat --oneline --name-only HEAD
git show --unified=3 --no-ext-diff -- docs/public-release-audit-2026-06-07.md kanban-status.md
```

Result summary: HEAD `b01996a` updates only `docs/public-release-audit-2026-06-07.md` and `kanban-status.md` to refresh public-readiness evidence for the approved public repository and Pages site. No private/internal source links, analytics, lead capture, pricing claims, repository visibility changes, or Pages configuration changes were added.

## Remaining gates

- Do not link private/internal resource sources publicly.
- Do not add analytics, tracking, lead capture, pricing claims, or strong marketing claims without approval.
- Direct public source linking for A2X Marketplace and Wiki-LLM remains blocked until cleanup and approval.
