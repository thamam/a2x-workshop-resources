# GitHub Pages readiness notes

This repo is structured so Tomer can approve a no-build GitHub Pages launch later, without changing the content layout.

## Current static structure

- `index.html` is the hub entry point.
- `resources/*.html` contains attendee resource pages.
- `docs/*.md` contains operator notes, inventory, usage map, and launch checklists.
- No build step is required for the current hub.

## Approved autonomous prep

Yunes may keep doing these inside the private repo:

- Keep relative links working from `index.html` and `resources/` pages.
- Add public-safe static resource pages.
- Update inventory and workshop usage docs.
- Run local link checks, secret scans, private-file checks, and render screenshots.
- Commit and push safe private-repo changes.

## Approval gate

Do not do any of the following without explicit Tomer approval:

- Make the repository public.
- Enable GitHub Pages in repository settings.
- Publish a public Pages URL.
- Add analytics, tracking, lead capture, pricing, or stronger marketing claims.
- Link private/internal materials or local-only source paths.

## Pre-launch command checklist

Run from the repo root before asking Tomer for final launch approval:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
class LinkParser(HTMLParser):
    def __init__(self): super().__init__(); self.hrefs=[]
    def handle_starttag(self, tag, attrs):
        for k,v in attrs:
            if k == 'href' and v and not v.startswith(('http://','https://','mailto:','#')):
                self.hrefs.append(v)
for file in [Path('index.html'), *Path('resources').glob('*.html')]:
    p=LinkParser(); p.feed(file.read_text())
    for href in p.hrefs:
        target=(file.parent / href).resolve()
        if not target.exists(): raise SystemExit(f'Broken link in {file}: {href} -> {target}')
print('HTML local links OK')
PY
scripts/block-private-files.sh $(git ls-files)
gitleaks detect --no-banner --redact --config .gitleaks.toml
git diff --check
```

If Playwright is available, capture preview screenshots before approval:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
playwright screenshot --browser chromium --viewport-size=390,844 http://127.0.0.1:8765/index.html /tmp/a2x-workshop-mobile.png
playwright screenshot --browser chromium --viewport-size=1440,1000 http://127.0.0.1:8765/index.html /tmp/a2x-workshop-desktop.png
```
