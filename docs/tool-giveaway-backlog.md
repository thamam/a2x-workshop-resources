# Tool giveaway backlog

This backlog captures candidate tools Tomer can give workshop attendees as practical follow-ups. The guiding principle: small, useful tools that reduce the blank-page burden without making attendees feel like they need a heavy software-development lifecycle process.

## Selection criteria

- Practical in the room: usable during or immediately after the workshop.
- Lightweight: brief prompts, short outputs, minimal ceremony.
- OpenSpec-aware where relevant, but not noisy or bureaucratic.
- Public-safe: no private links, client material, credentials, or internal-only context.
- Demo-friendly: each tool should have a clear before/after moment.
- Extensible: can start as a static prompt/workflow page, then become a richer script or mini-app.

## 1. Product brief generator

Status: v1 static page created — high priority.

Goal: Help a user move from a rough product idea into a concise product brief that can seed a spec.

What it does:

- Runs a short brainstorming flow.
- Helps clarify user, problem, scope, constraints, and success signals.
- Produces a compact product brief, not a heavy product requirements document.
- Keeps the user focused on practical decisions.

Preferred output shape:

- One-sentence product idea.
- Target user.
- Problem / pain.
- Proposed workflow.
- What is explicitly out of scope.
- Success signal.
- Open questions.
- Next step toward a spec.

Workshop value:

- Good first giveaway because it gives attendees a productive starting point.
- Supports the move from “I have an idea” to “I can ask an agent to help build this.”

Implementation options:

- First version: static workflow page with copyable prompt.
- Better version: small form that generates the prompt and final brief scaffold.
- Advanced version: interactive interviewer that asks only missing high-impact questions.

## 2. PRD generator / OpenSpec proposal starter

Status: v1 static page created — high priority, depends on product brief flow.

Goal: Turn a product brief plus context into a more explicit Product Requirements Document (PRD) or OpenSpec-ready proposal draft.

Assumption: Tomer said “pure de generator”; interpreted here as “PRD generator.”

What it does:

- Accepts a product brief.
- Accepts optional context, examples, or constraints.
- Drafts a concise PRD suitable for moving into OpenSpec.
- If major details are missing, invokes or links to the interviewer flow rather than inventing details.
- Produces an OpenSpec proposal starter when enough information exists.

Preferred output shape:

- Problem.
- Goal.
- Users.
- Non-goals.
- User stories or key flows.
- Requirements.
- Risks and assumptions.
- OpenSpec proposal outline.
- Missing high-impact questions.

Workshop value:

- Shows how product thinking connects to agentic implementation.
- Makes OpenSpec feel useful rather than heavy.

Implementation options:

- First version: prompt template paired with the product brief generator.
- Better version: form-driven mini-app with “ask interviewer if missing details” mode.
- Advanced version: scriptable tool that writes an OpenSpec proposal skeleton.

## 3. OpenSpec-aware interviewer

Status: v1 static page created — high priority.

Goal: Identify major missing details and structural risks without pestering the user about tiny details.

What it does:

- Reviews a brief, PRD, or proposal draft.
- Asks only high-leverage questions.
- Avoids low-value nitpicks.
- Acknowledges that OpenSpec will handle change structure later.
- Focuses on blockers that would cause the implementation agent to make wrong assumptions.

Question policy:

- Ask at most 3–5 questions per pass.
- Prefer questions that change architecture, scope, user experience, data model, or acceptance criteria.
- Avoid small wording or formatting questions.
- Offer assumptions when a question is not worth interrupting the user.

Workshop value:

- Teaches attendees how to unblock agents without turning specification into bureaucracy.
- Reinforces “ask for the missing context that matters.”

Implementation options:

- First version: reviewer prompt.
- Better version: reusable checklist plus prompt.
- Advanced version: integrated module for product brief and PRD generators.

## 4. Prompt improver / Prompt Magician

Status: v1 static page created; richer Prompt Magician remains polish-first.

Goal: Help users refine prompts while converting negative corrections into constructive instructions.

What it does:

- Accepts a rough prompt.
- Identifies unclear goals, missing context, ambiguous constraints, and risky wording.
- Converts “don’t do X” corrections into positive desired behavior when possible.
- Avoids adding unnecessary attention weights to unwanted behavior.
- Can optionally use A2X wiki or knowledge-base context to improve accuracy for tentative requests.

Example transformation:

- User says: “Don’t make it too corporate.”
- Better prompt wording: “Use direct, practical language with a warm expert tone. Prefer concrete examples over marketing phrasing.”

Knowledge-base option:

- Checkbox concept: “Use A2X wiki context.”
- If enabled, the tool may pull relevant concepts, terminology, or examples from the wiki.
- If disabled, it should improve only the user-provided prompt.

Workshop value:

- Very demo-friendly.
- Directly supports the workshop’s message about instructions, feedback, and reusable workflows.

Implementation options:

- First version: static prompt-improvement workflow.
- Better version: mini-app with correction-to-positive rewrites.
- Advanced version: knowledge-base assisted version using Wiki-LLM or another retrieval path.

## 5. PRD-to-beautiful-HTML workbench

Status: research memo created — potentially high value.

Goal: Turn a PRD into a beautiful, interactive HTML artifact that humans can read, comment on, revise, and then feed back to a model.

Assumption: Tomer said “HDL”; interpreted here as “HTML.”

What it might do:

- Convert a PRD or OpenSpec proposal into a styled HTML document.
- Make sections easier to scan visually.
- Support comments, edits, or change requests.
- Export the revised artifact or a structured summary back to the model.
- Provide style customization so the artifact feels designed, not like raw Markdown.
- Use deterministic functions where possible to reduce the talking burden.
- Optionally let Claude or another model operate inside a skeleton/workbench.

Related idea:

- Similar spirit to prompt guardrails/handrails: the tool highlights places where wording, examples, constraints, or acceptance criteria would improve the model’s result, and explains why.

Research questions before implementation:

- What existing “HTML is the new Markdown” tools or demos already solve part of this?
- Is there a lightweight open-source workbench we can adapt?
- Can this be implemented as a skill plus script rather than a full app?
- Does interactive commenting require a backend, or can it be done locally in browser state?
- Does model-in-the-loop editing need an external token, or can the workflow use the attendee’s local Claude Code / model environment?

Research memo: `docs/prd-html-workbench-research.md`.

Workshop value:

- Strong “wow” potential.
- Useful to Tomer personally.
- More complex than the other candidates, so it should not block the first giveaway set.

Implementation options:

- First version: research memo plus static HTML prototype.
- Better version: single-file browser workbench that accepts PRD text, renders styled sections, and lets users add comments.
- Advanced version: model-assisted workbench that calls a local or configured model to rewrite sections and produce follow-up prompts.

## Suggested first-release bundle

Built as static v1 pages:

1. Product brief generator.
2. OpenSpec-aware interviewer.
3. Prompt improver.
4. PRD generator / OpenSpec proposal starter.

Research before building:

5. PRD-to-beautiful-HTML workbench.

Reasoning: the first four can ship as lightweight, public-safe, practical workshop tools. The HTML workbench is exciting but needs scope selection before implementation.

## Current first-release flow

1. Open with the harness idea.
2. Give attendees rules they can use today.
3. Turn repetition into infrastructure.
4. Use the product brief generator, OpenSpec interviewer, prompt improver, and PRD starter as the first practical giveaway set.
5. Research existing PRD-to-HTML / interactive spec workbench patterns before implementation.
6. Decide whether future richer versions live as `resources/*.html`, scripts, or skill/plugin packages.
