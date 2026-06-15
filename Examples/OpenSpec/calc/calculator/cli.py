"""Command-line interface for the calculator.

Two modes:
  * one-shot  - an expression is supplied as CLI arguments; print and exit.
  * REPL      - no arguments; read/evaluate/print expressions line by line.
"""

import sys

from .evaluator import CalcError, evaluate

_PROMPT = "calc> "
_EXIT_WORDS = {"quit", "exit"}


def format_result(value):
    """Render *value* without a trailing ``.0`` when it is whole-numbered."""
    if value == int(value) and value not in (float("inf"), float("-inf")):
        return str(int(value))
    return repr(value)


def _run_once(expression, out, err):
    try:
        result = evaluate(expression)
    except CalcError as exc:
        print(f"Error: {exc}", file=err)
        return 1
    print(format_result(result), file=out)
    return 0


def _run_repl(in_, out, err):
    while True:
        try:
            line = _read_line(in_, out)
        except EOFError:
            break
        if line is None:
            break
        stripped = line.strip()
        if stripped == "":
            continue
        if stripped.lower() in _EXIT_WORDS:
            break
        try:
            result = evaluate(stripped)
        except CalcError as exc:
            print(f"Error: {exc}", file=err)
            continue
        print(format_result(result), file=out)
    return 0


def _read_line(in_, out):
    """Read a single line, writing a prompt when attached to a terminal."""
    if in_ is sys.stdin and out is sys.stdout and out.isatty():
        try:
            return input(_PROMPT)
        except EOFError:
            raise
    line = in_.readline()
    if line == "":
        raise EOFError
    return line.rstrip("\n")


def main(argv=None, *, stdin=None, stdout=None, stderr=None):
    """Entry point. Returns the process exit code."""
    argv = list(sys.argv[1:] if argv is None else argv)
    out = stdout if stdout is not None else sys.stdout
    err = stderr if stderr is not None else sys.stderr
    in_ = stdin if stdin is not None else sys.stdin

    if argv:
        expression = " ".join(argv)
        return _run_once(expression, out, err)
    return _run_repl(in_, out, err)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
