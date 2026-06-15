## Context

This is a greenfield project with no existing source code or specs. The proposal calls for a terminal calculator with two modes (one-shot from arguments, and an interactive REPL) that evaluates arithmetic expressions with correct precedence and robust error handling, using only the standard library.

Key constraints:
- No external runtime dependencies.
- Must not crash on bad input — all parse/eval errors are recoverable.
- Evaluation must be safe (no arbitrary code execution).

## Goals / Non-Goals

**Goals:**
- A single CLI entry point (`calc`) supporting one-shot and REPL modes.
- A self-contained expression evaluator: tokenizer → parser → evaluator.
- Correct precedence/associativity for `+ - * / % **`, unary minus, and parentheses.
- Clear, structured errors distinguishing syntax errors from math errors.
- Unit-testable evaluator decoupled from CLI I/O.

**Non-Goals:**
- Variables, assignment, or memory/history.
- Named functions (`sin`, `sqrt`, etc.) or constants (`pi`, `e`).
- Arbitrary-precision/decimal arithmetic beyond native floats.
- Configuration files, plugins, or scientific/RPN modes.

## Decisions

### Language & runtime: Python 3 (standard library only)
- **Why**: Zero-dependency CLI, fast to write and test, `argparse`/`sys` cover argument and I/O needs, `unittest` covers tests. Aligns with the project's Python conventions (snake_case).
- **Alternatives considered**: Node.js (extra packaging overhead for a small tool); Bash (no clean parser, fragile arithmetic); Go/Rust (build step unnecessary for this scope).

### Evaluation strategy: hand-written recursive-descent parser, NOT `eval()`
- **Why**: `eval()` / `exec()` would execute arbitrary Python — a security and correctness hazard. A recursive-descent parser gives explicit control over the supported grammar, precedence, and error messages, and keeps `**` from invoking Python's expensive-int-pow surprises.
- **Alternatives considered**: `ast.literal_eval` (does not support binary operators); `eval()` with restricted globals (still risky and hard to make safe); a third-party parser library (violates the no-dependency goal).

### Grammar (precedence climbing)
```
expression := term (('+' | '-') term)*
term       := power (('*' | '/' | '%') power)*
power      := unary ('**' power)?        # right-associative
unary      := ('-' | '+') unary | primary
primary    := NUMBER | '(' expression ')'
```
A small tokenizer produces NUMBER / operator / paren tokens; numbers parse to `float`. This encodes the precedence and associativity required by the `expression-evaluation` spec.

### Module layout
- `calculator/evaluator.py` — `tokenize()`, `Parser`, and `evaluate(expr) -> float`; raises `CalcError` subclasses (`SyntaxError`-style and `MathError`-style).
- `calculator/cli.py` — `main(argv)`: dispatches one-shot vs REPL, formats output, maps `CalcError` to stderr + exit code.
- `calc` / `__main__.py` — thin entry point calling `cli.main`.
- `tests/` — `test_evaluator.py`, `test_cli.py`.

### Error model
- Two exception types under a common `CalcError` base: one for syntax/parse problems, one for math problems (e.g., division by zero, modulo by zero). The CLI catches `CalcError` only — unexpected exceptions still surface as real bugs.

### Output formatting
- A result equal to its integer cast is printed as an integer (`3`), otherwise as a float (`3.5`). Implemented in one shared formatter used by both modes so the `calculator-cli` formatting scenarios hold consistently.

## Risks / Trade-offs

- **Floating-point imprecision** (e.g., `0.1 + 0.2`) → Spec asserts "approximately"; tests use tolerance. Acceptable for a general calculator; documented as a non-goal to use Decimal.
- **`**` with large exponents could be slow / huge** → Out of scope to cap; native float `**` bounds magnitude via overflow to `inf`, which is reported, not crashed.
- **REPL exit conventions vary** → Support both an explicit `quit`/`exit` keyword and EOF (Ctrl-D); documented in the spec scenarios.
- **Modulo/precedence edge cases** → Covered directly by evaluator unit tests so regressions are caught early.

## Migration Plan

Not applicable — new, additive feature with no existing data, APIs, or users. Rollback is removal of the new files.

## Open Questions

- None blocking. Future enhancement (out of scope now): functions/constants and a `--precision` flag.
