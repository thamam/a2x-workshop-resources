# Workshop resource inventory

Status legend:

- `publish-now`: safe and useful now.
- `polish-first`: useful but needs cleanup.
- `private`: do not publish yet.
- `defer`: not needed for first workshop.

## Candidates

### CLAUDE.md cheat sheet

Status: publish-now  
Hub path: `resources/claude-md-cheat-sheet.html`  
Source: existing public A2X site resource at `public/resources/karpathy-rules.html`; homepage card copy in `public/index.html`.  
Safety notes: current hub page is a short public-safe rewrite. No private links, credentials, or local paths.  
Next action: compare against the full source page and decide whether to migrate more examples.

### Build your first skill

Status: publish-now  
Hub path: `resources/first-skill.html`  
Source: existing public A2X site resource at `public/resources/skills-forge.html`; homepage card copy in `public/index.html`.  
Safety notes: current hub page is a short public-safe rewrite. No private links, credentials, or local paths.  
Next action: decide whether to keep as quick workshop handout or expand into a full guided exercise.

### Claude Code harness map

Status: publish-now
Hub path: `resources/claude-code-harness-map.html`
Source: existing public A2X site resource at `public/resources/claude-code-at-scale.html`.  
Safety notes: current hub page is a short public-safe rewrite and does not copy analytics/tracking from the source page.
Next action: review wording live after the workshop opener and expand only if it remains useful.

### A2X Marketplace

Status: polish-first  
Hub path: homepage placeholder card.  
Source: private/local backup snapshot named `A2X-backup-20260326` contains marketplace README and installation notes; no public-ready source confirmed in this repo.
Safety notes: backup material includes local setup assumptions and plugin details that need review before public linking. Do not expose private backup paths or copy installation steps wholesale.
Next action: identify the public marketplace URL/repo and rewrite a short public-safe overview card or handout.

### Prompt Magician

Status: polish-first  
Hub path: homepage placeholder card.  
Source: not found in the local repository scan; mentioned only in the A2X-site handoff as a desired workshop resource.
Safety notes: setup instructions must avoid private keys, internal endpoints, and local-only paths.  
Next action: locate source repo or setup doc before creating an active link.

### Presentation editor

Status: polish-first  
Hub path: homepage placeholder card.  
Source: not found in the local repository scan; mentioned only in the A2X-site handoff as a desired workshop resource.
Safety notes: must avoid exposing private slide content or client examples.  
Next action: locate source repo or setup doc.

### Wiki-LLM

Status: polish-first  
Hub path: homepage placeholder card.  
Source: local private candidate projects identified outside this repo; exact absolute paths intentionally withheld from the public-ready inventory.
Safety notes: treat local project material as private until audited. Do not copy content or expose local-only paths yet.
Next action: inspect candidate project structure outside this repo, identify the public-safe advanced guide source, and redact local/private material before publishing.

### Credential tracer / authentication routing

Status: defer  
Hub path: none yet.  
Source: existing public A2X site resource at `public/resources/credential-tracer.html`.  
Safety notes: useful, but not part of the highest-priority first workshop path unless auth/billing comes up.  
Next action: keep as optional Q&A resource.
