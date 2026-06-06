# PRD-to-beautiful-HTML workbench research

Status: research complete enough for an MVP direction; do not implement the full workbench until Tomer chooses scope.

## Core finding

The strongest pattern is not “Markdown to static HTML.” It is:

1. Spec or Product Requirements Document (PRD) as source.
2. Beautiful interactive artifact as review surface.
3. Human comments, edits, and highlights.
4. Structured feedback exported back to an AI model or OpenSpec proposal.

That means the A2X version should optimize for round-tripping, not just rendering.

## Relevant public examples

### HTML is the new Markdown

URL: https://www.lennysnewsletter.com/p/html-is-the-new-markdown-how-anthropic

Pattern: engineers use HTML artifacts as interactive plans, throwaway tools, design surfaces, and living implementation aids.

Implication: Position the workbench as “turn your spec into a living artifact,” not as a prettier document export.

### Claude Artifacts

URL: https://www.anthropic.com/news/artifacts

Pattern: model-created apps, documents, tools, and visualizations appear beside the conversation and can be iterated.

Implication: The review surface should feel like an artifact, with sections and interactions, not like a static report.

### ChatGPT Canvas

URL: https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it

Pattern: highlight a section, ask for targeted feedback, revise locally, and restore versions.

Implication: Section-level comments and revision prompts matter more than perfect initial rendering.

### Vercel v0

URL: https://v0.dev/docs

Pattern: prompt or mockup to polished app/code with preview and iteration.

Implication: A PRD workbench could eventually generate UI previews or implementation tickets, but this is beyond the safest first workshop slice.

### Bolt.new

URL: https://bolt.new/

Pattern: prompt-driven app building with design-system awareness.

Implication: Style presets matter. A future A2X workbench should support simple themes.

### Websim

URL: https://websim.com/

Pattern: prompt to browsable simulated sites/apps.

Implication: Specs can become explorable mini-products, not only documents.

### tldraw Make Real

URL: https://github.com/tldraw/make-real

Pattern: sketches/wireframes to working UI.

Implication: Future versions could combine a PRD with a rough sketch, but v1 should stay text-only.

### Observable Framework

URL: https://observablehq.com/framework/

Pattern: Markdown plus code becomes rich interactive reports and dashboards.

Implication: If a PRD includes metrics, funnels, or operational data, render those as cards/charts later.

### HackMD

URL: https://hackmd.io/

Pattern: collaborative Markdown, comments, version history, publishing, and GitHub sync.

Implication: Keep Markdown/OpenSpec as the source of truth. HTML is the review layer.

### Hypothesis

URL: https://hypothes.is/

Pattern: web annotation layer over pages and PDFs.

Implication: Comments can be an overlay. A full editor is not required for the first prototype.

## MVP recommendation

Build a single-file static prototype only after the first giveaway tools are stable:

- Paste PRD/OpenSpec Markdown.
- Parse headings into sections.
- Render a styled review page.
- Add local comments per section using browser state.
- Export a “feedback packet” for the model.
- No backend, no account, no storage beyond the browser, no model Application Programming Interface (API) call.

## Deferred features

- Model-in-the-loop rewriting.
- Multi-user comments.
- GitHub sync.
- Theme designer.
- OpenSpec file writing.
- Wiki/retrieval integration.

## Open decisions

1. Should the prototype be a public workshop giveaway or an internal A2X tool first?
2. Should it round-trip to OpenSpec proposal Markdown, plain PRD Markdown, or both?
3. Should comments be local-only, copy/export-only, or persisted somewhere?
