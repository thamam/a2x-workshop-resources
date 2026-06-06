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

Status: polish-first  
Hub path: homepage placeholder card.  
Source: existing public A2X site resource at `public/resources/claude-code-at-scale.html`.  
Safety notes: likely public-safe, but should be reviewed before copying wholesale.  
Next action: extract a concise “harness, not model” handout.

### A2X Marketplace

Status: polish-first  
Hub path: homepage placeholder card.  
Source: unknown.  
Safety notes: must confirm public URL, positioning, and whether any private plugin/tool details are exposed.  
Next action: locate source repo/docs or get source from Tomer.

### Prompt Magician

Status: polish-first  
Hub path: homepage placeholder card.  
Source: unknown.  
Safety notes: setup instructions must avoid private keys, internal endpoints, and local-only paths.  
Next action: locate source repo or setup doc.

### Presentation editor

Status: polish-first  
Hub path: homepage placeholder card.  
Source: unknown.  
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
