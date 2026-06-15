## 1. Project scaffolding

- [x] 1.1 Create the `calculator/` package with `__init__.py`
- [x] 1.2 Create the `tests/` directory for unit tests
- [x] 1.3 Add a `calc` entry point (`calculator/__main__.py` calling `cli.main`) so the tool runs as `python -m calculator`

## 2. Expression evaluator (capability: expression-evaluation)

- [x] 2.1 Define `CalcError` base and `CalcSyntaxError` / `CalcMathError` subclasses in `calculator/evaluator.py`
- [x] 2.2 Implement `tokenize(expr)` producing NUMBER (int/decimal), operator (`+ - * / % **`), and paren tokens; raise `CalcSyntaxError` on unknown characters
- [x] 2.3 Implement a recursive-descent `Parser` for the grammar in design.md (expression → term → power → unary → primary)
- [x] 2.4 Enforce precedence and associativity: left-assoc for `+ - * / %`, right-assoc for `**`
- [x] 2.5 Support parentheses and unary minus/plus, raising `CalcSyntaxError` on unbalanced parens or incomplete expressions
- [x] 2.6 Implement evaluation including division-by-zero and modulo-by-zero detection (raise `CalcMathError`)
- [x] 2.7 Expose `evaluate(expr) -> float` as the public entry point

## 3. CLI and REPL (capability: calculator-cli)

- [x] 3.1 Implement shared result formatter: integer-valued results print without `.0`, others as decimals
- [x] 3.2 Implement one-shot mode in `cli.main`: join args into one expression, print result to stdout, exit 0
- [x] 3.3 Implement one-shot error handling: print `CalcError` message to stderr, exit non-zero
- [x] 3.4 Implement REPL mode (no args): prompt, evaluate each line, print result; errors print to stderr and the loop continues
- [x] 3.5 Implement REPL exit on `quit`/`exit` keyword and on EOF (Ctrl-D), exiting with status 0

## 4. Tests

- [x] 4.1 `tests/test_evaluator.py`: cover all `expression-evaluation` scenarios (operators, precedence, associativity, parens, unary minus, decimals, float tolerance)
- [x] 4.2 `tests/test_evaluator.py`: cover error scenarios (invalid syntax, unbalanced parens, unknown char, division by zero)
- [x] 4.3 `tests/test_cli.py`: cover one-shot success, one-shot error (exit code + stderr), and output formatting (`6/2` → `3`, `7/2` → `3.5`)
- [x] 4.4 `tests/test_cli.py`: cover REPL evaluate, error-does-not-terminate, and exit-on-quit/EOF behaviors

## 5. Verification

- [x] 5.1 Run the full test suite (`python -m unittest discover tests`) and confirm all pass
- [x] 5.2 Manually verify one-shot (`python -m calculator "2 + 3 * 4"` → `14`) and REPL flows
