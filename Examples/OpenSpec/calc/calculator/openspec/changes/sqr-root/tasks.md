## 1. Tokenizer

- [ ] 1.1 Add an `_IDENT` token kind and `import math` at the top of `calculator/evaluator.py`
- [ ] 1.2 In `tokenize`, emit an `_IDENT` token for a run of ASCII letters/underscores (storing the identifier text)

## 2. Function dispatch

- [ ] 2.1 Add a module-level `_sqrt` helper that raises `CalcMathError` for negative operands and otherwise returns `math.sqrt(value)`
- [ ] 2.2 Add a `_FUNCTIONS = {"sqrt": _sqrt}` dispatch table

## 3. Parser

- [ ] 3.1 In `_primary`, handle an `_IDENT` token: require a following `LPAREN`, parse a full `_expression` as the argument, require the closing `RPAREN`
- [ ] 3.2 Look up the identifier in `_FUNCTIONS`; raise `CalcSyntaxError` for an unknown function and apply the function to the parsed argument
- [ ] 3.3 Update the grammar docstring at the top of the module to include `IDENT '(' expression ')'` in the `primary` rule

## 4. Tests

- [ ] 4.1 Add tests for valid roots: `sqrt(9)` → 3, `sqrt(0)` → 0, `sqrt(2)` → 1.4142135623730951
- [ ] 4.2 Add tests for compound/nested args and composition: `sqrt(2 + 7)`, `sqrt(16) * 2`, `sqrt(sqrt(16))`
- [ ] 4.3 Add tests for negative operands raising `CalcMathError`: `sqrt(-4)`, `sqrt(3 - 10)`
- [ ] 4.4 Add tests for malformed usage raising `CalcSyntaxError`: `sqrt 9`, `sqrt()`, `foo(9)`

## 5. Verification

- [ ] 5.1 Run the test suite and confirm all existing and new tests pass
- [ ] 5.2 Manually verify via the CLI that `sqrt(9)` prints `3` and `sqrt(-1)` prints a clear error
