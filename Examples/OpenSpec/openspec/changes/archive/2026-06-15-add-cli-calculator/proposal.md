## Why

There is no way to perform quick arithmetic from the terminal within this project. A small, dependency-light CLI calculator gives users immediate command-line math (both one-shot and interactive) without reaching for a separate tool or language REPL.

## What Changes

- Add a CLI entry point that evaluates an arithmetic expression passed as arguments and prints the result (one-shot mode).
- Add an interactive REPL mode (launched when no expression argument is given) that reads expressions line-by-line until the user exits.
- Support the core arithmetic operators `+`, `-`, `*`, `/`, `%`, and `**` (exponent), unary minus, parentheses, and decimal/float numbers with correct operator precedence and associativity.
- Provide clear, non-crashing error messages for invalid syntax and math errors (e.g., division by zero).
- Exit with conventional status codes (`0` success, non-zero on evaluation error in one-shot mode).

## Capabilities

### New Capabilities
- `expression-evaluation`: Parse and evaluate arithmetic expressions into numeric results, honoring operator precedence, associativity, parentheses, and unary minus, with well-defined error handling.
- `calculator-cli`: The terminal interface — one-shot evaluation from CLI arguments and an interactive REPL — including output formatting, exit handling, and error reporting.

### Modified Capabilities
<!-- None. Greenfield project; no existing specs. -->

## Impact

- New source files for the CLI entry point and the expression evaluator.
- New test files covering the evaluator and CLI behavior.
- No external runtime dependencies introduced (standard library only); language/runtime choice is settled in design.md.
