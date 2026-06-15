## Why

The calculator currently supports `+ - * / % **`, parentheses, and unary signs, but offers no way to compute a square root. Square roots are one of the most common operations users reach for beyond basic arithmetic, and `x ** 0.5` is an awkward, error-prone substitute. Adding first-class `sqrt(...)` support closes an obvious gap with minimal grammar impact.

## What Changes

- Add a `sqrt(...)` function call to the expression grammar, accepting any sub-expression as its argument (e.g. `sqrt(9)`, `sqrt(2 + 7)`, `sqrt(x) * 2`).
- Tokenize bare identifiers so the parser can recognize the `sqrt` function name.
- Evaluate `sqrt` over the real domain: return the non-negative root for non-negative operands; raise a math error for negative operands (no complex results).
- Surface clear errors for misuse: missing argument, missing parentheses, or negative radicand.
- No breaking changes — existing expressions continue to evaluate identically.

## Capabilities

### New Capabilities
- `square-root`: Defines the `sqrt(...)` function — its syntax, real-domain evaluation semantics, and error behavior within the expression evaluator.

### Modified Capabilities
<!-- No existing specs in openspec/specs/; square root is introduced as a new capability. -->

## Impact

- **Code**: `calculator/evaluator.py` — tokenizer gains identifier tokens; parser gains function-call handling in the primary/unary layer.
- **Tests**: `tests/test_evaluator.py` — new cases for valid roots, nested expressions, and error paths.
- **APIs**: Public `evaluate()` behavior extended (additive); `CalcSyntaxError` / `CalcMathError` raised for invalid `sqrt` usage.
- **Dependencies**: Uses the standard library `math` module; no new third-party dependencies.
