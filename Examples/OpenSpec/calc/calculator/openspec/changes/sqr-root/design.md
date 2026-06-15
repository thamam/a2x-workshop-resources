## Context

`calculator/evaluator.py` is a self-contained tokenizer plus recursive-descent parser that evaluates as it parses. The current grammar is:

```
expression := term (('+' | '-') term)*
term       := power (('*' | '/' | '%') power)*
power      := unary ('**' power)?        # right-associative
unary      := ('-' | '+') unary | primary
primary    := NUMBER | '(' expression ')'
```

Tokens are `NUMBER`, `OP`, `LPAREN`, `RPAREN`, `EOF`. There is no concept of an identifier or a function call, so `sqrt` cannot currently be tokenized or parsed. Errors are modeled with `CalcSyntaxError` (malformed input) and `CalcMathError` (invalid math such as division by zero), both subclasses of `CalcError`. The CLI catches `CalcError` and prints `Error: <message>`.

## Goals / Non-Goals

**Goals:**
- Recognize `sqrt(...)` as a function call returning the real, non-negative square root.
- Accept any sub-expression as the argument and allow `sqrt(...)` anywhere a primary value is valid.
- Reject negative radicands with a `CalcMathError` and malformed usage with a `CalcSyntaxError`.
- Keep all existing expression behavior identical (purely additive change).

**Non-Goals:**
- Complex-number results for negative inputs.
- A general function registry or support for other functions (`sin`, `log`, etc.) — out of scope, though the design should not preclude it.
- Postfix or operator notation (e.g. `√9`); only the `sqrt(expr)` call form is added.

## Decisions

**1. Add an `IDENT` token instead of special-casing the literal `sqrt`.**
The tokenizer will emit an `IDENT` token for any run of letters (and underscores). This keeps the tokenizer general and lets the parser decide which identifiers are valid functions, producing a clear "unknown function" error for anything else. Alternative considered: matching the exact substring `sqrt` in the tokenizer — rejected because it bakes a single function name into the lexer and gives worse error messages for typos like `sqr(9)`.

**2. Handle the function call in `_primary`.**
When `_primary` sees an `IDENT`, it requires a following `LPAREN`, parses a full `_expression` as the argument, requires the closing `RPAREN`, then applies the function. Placing it in `_primary` makes `sqrt(...)` bind exactly like a parenthesized value, so precedence with `**`, `*`, unary `-`, etc. falls out correctly with no other grammar changes. The updated rule:

```
primary := NUMBER | IDENT '(' expression ')' | '(' expression ')'
```

**3. Map function names through a small dispatch table.**
A module-level `_FUNCTIONS = {"sqrt": _sqrt}` keeps the parser logic generic and makes future functions a one-line addition. `_sqrt` checks for a negative operand and raises `CalcMathError` before calling `math.sqrt`, avoiding a `ValueError`/`NaN` leak.

**4. Use `math.sqrt` from the standard library.**
Matches the project's existing float semantics and avoids the `x ** 0.5` floating-point imprecision. No new dependency.

## Risks / Trade-offs

- **`sqrt(9)` returns `3.0`, which `format_result` already renders as `3`.** → Verified against existing CLI formatting; no change needed. Tests assert on the formatted/whole-number value.
- **Negative argument from a sub-expression (e.g. `sqrt(3 - 10)`) must be caught at evaluation, not parse, time.** → The `_sqrt` helper checks the computed value, so both literal and computed negatives are handled uniformly.
- **Introducing `IDENT` could change error messages for previously-unexpected characters (letters were already rejected).** → Letters previously raised "Unexpected character"; they now tokenize and fail later as "unknown function" only when followed by `(`, otherwise still a syntax error. This is a strictly clearer message, not a behavior regression for valid input.
- **Scope creep toward a general function library.** → Mitigated by limiting the dispatch table to `sqrt` and documenting other functions as a non-goal.

## Migration Plan

Additive change to a pure library function; no data, no persisted state, no rollout coordination. Rollback is reverting the commit. Existing expressions are unaffected.
