# Mobile viewport review

Date: 2026-06-06  
Viewport tested: 390 × 844 mobile emulation with Google Chrome Headless.

## Method

1. Started a local static server with `python3 -m http.server 8765 --bind 127.0.0.1`.
2. Verified HTTP 200 responses for the hub and PRD starter.
3. Captured 390 × 844 screenshots for the hub and giveaway pages under `tmp/mobile-review/`.
4. Used Chrome DevTools Protocol to measure horizontal overflow and interactive element counts at the same viewport.

## Pages checked

| Page | Title observed | Horizontal overflow | Links | Buttons | Textareas |
| --- | --- | ---: | ---: | ---: | ---: |
| `index.html` | A2X Workshop Resources | no | 11 | 0 | 0 |
| `resources/product-brief-generator.html` | Product Brief Generator · A2X | no | 1 | 2 | 8 |
| `resources/openspec-interviewer.html` | OpenSpec-Aware Interviewer · A2X | no | 1 | 2 | 3 |
| `resources/prompt-improver.html` | Prompt Improver · A2X | no | 1 | 2 | 5 |
| `resources/prd-openspec-starter.html` | PRD & OpenSpec Starter · A2X | no | 1 | 2 | 5 |

## Evidence command output

```text
index.html 200 text/html
resources/prd-openspec-starter.html 200 text/html
```

```text
{"path":"index.html","title":"A2X Workshop Resources","viewportWidth":390,"bodyScrollWidth":390,"docScrollWidth":390,"overflow":false,"links":11,"buttons":0,"textareas":0}
{"path":"resources/product-brief-generator.html","title":"Product Brief Generator · A2X","viewportWidth":390,"bodyScrollWidth":390,"docScrollWidth":390,"overflow":false,"links":1,"buttons":2,"textareas":8}
{"path":"resources/openspec-interviewer.html","title":"OpenSpec-Aware Interviewer · A2X","viewportWidth":390,"bodyScrollWidth":390,"docScrollWidth":390,"overflow":false,"links":1,"buttons":2,"textareas":3}
{"path":"resources/prompt-improver.html","title":"Prompt Improver · A2X","viewportWidth":390,"bodyScrollWidth":390,"docScrollWidth":390,"overflow":false,"links":1,"buttons":2,"textareas":5}
{"path":"resources/prd-openspec-starter.html","title":"PRD & OpenSpec Starter · A2X","viewportWidth":390,"bodyScrollWidth":390,"docScrollWidth":390,"overflow":false,"links":1,"buttons":2,"textareas":5}
```

## Result

Mobile smoke review passed for the hub and first-release giveaway pages: all checked pages fit a 390px-wide viewport with no horizontal overflow.

## Notes

- Screenshots were generated as temporary local artifacts under `tmp/mobile-review/`; they are not intended for commit.
- This was a layout smoke test, not a full accessibility audit.
