"""Arithmetic expression evaluator.

A self-contained tokenizer + recursive-descent parser that evaluates
arithmetic expressions without using ``eval``. Supports the binary operators
``+ - * / % **``, unary ``+``/``-``, parentheses, and decimal numbers, with
standard precedence and associativity.

Grammar (precedence climbing):

    expression := term (('+' | '-') term)*
    term       := power (('*' | '/' | '%') power)*
    power      := unary ('**' power)?        # right-associative
    unary      := ('-' | '+') unary | primary
    primary    := NUMBER | '(' expression ')'
"""


class CalcError(Exception):
    """Base class for all recoverable calculator errors."""


class CalcSyntaxError(CalcError):
    """Raised when an expression cannot be tokenized or parsed."""


class CalcMathError(CalcError):
    """Raised when a mathematically invalid operation is attempted."""


# Token kinds
_NUMBER = "NUMBER"
_OP = "OP"
_LPAREN = "LPAREN"
_RPAREN = "RPAREN"
_EOF = "EOF"

_OPERATORS = {"+", "-", "*", "/", "%", "**"}


class _Token:
    __slots__ = ("kind", "value", "pos")

    def __init__(self, kind, value, pos):
        self.kind = kind
        self.value = value
        self.pos = pos

    def __repr__(self):  # pragma: no cover - debugging aid
        return f"Token({self.kind!r}, {self.value!r}, {self.pos})"


def tokenize(expr):
    """Convert *expr* into a list of tokens terminated by an EOF token.

    Raises :class:`CalcSyntaxError` on any unrecognized character.
    """
    tokens = []
    i = 0
    n = len(expr)
    while i < n:
        ch = expr[i]
        if ch.isspace():
            i += 1
            continue
        if ch.isdigit() or ch == ".":
            start = i
            seen_dot = False
            while i < n and (expr[i].isdigit() or expr[i] == "."):
                if expr[i] == ".":
                    if seen_dot:
                        raise CalcSyntaxError(
                            f"Invalid number with multiple decimal points at position {start}"
                        )
                    seen_dot = True
                i += 1
            text = expr[start:i]
            if text == ".":
                raise CalcSyntaxError(f"Invalid number '.' at position {start}")
            tokens.append(_Token(_NUMBER, float(text), start))
            continue
        if ch == "(":
            tokens.append(_Token(_LPAREN, ch, i))
            i += 1
            continue
        if ch == ")":
            tokens.append(_Token(_RPAREN, ch, i))
            i += 1
            continue
        if ch == "*" and expr[i : i + 2] == "**":
            tokens.append(_Token(_OP, "**", i))
            i += 2
            continue
        if ch in "+-*/%":
            tokens.append(_Token(_OP, ch, i))
            i += 1
            continue
        raise CalcSyntaxError(f"Unexpected character {ch!r} at position {i}")
    tokens.append(_Token(_EOF, None, n))
    return tokens


class Parser:
    """Recursive-descent parser that evaluates as it parses."""

    def __init__(self, tokens):
        self._tokens = tokens
        self._index = 0

    @property
    def _current(self):
        return self._tokens[self._index]

    def _advance(self):
        tok = self._tokens[self._index]
        self._index += 1
        return tok

    def parse(self):
        value = self._expression()
        if self._current.kind != _EOF:
            tok = self._current
            raise CalcSyntaxError(
                f"Unexpected token {tok.value!r} at position {tok.pos}"
            )
        return value

    def _expression(self):
        value = self._term()
        while self._current.kind == _OP and self._current.value in ("+", "-"):
            op = self._advance().value
            rhs = self._term()
            value = value + rhs if op == "+" else value - rhs
        return value

    def _term(self):
        value = self._power()
        while self._current.kind == _OP and self._current.value in ("*", "/", "%"):
            op = self._advance().value
            rhs = self._power()
            if op == "*":
                value = value * rhs
            elif op == "/":
                if rhs == 0:
                    raise CalcMathError("Division by zero")
                value = value / rhs
            else:  # "%"
                if rhs == 0:
                    raise CalcMathError("Modulo by zero")
                value = value % rhs
        return value

    def _power(self):
        base = self._unary()
        if self._current.kind == _OP and self._current.value == "**":
            self._advance()
            # Right-associative: recurse into _power for the exponent.
            exponent = self._power()
            try:
                return base ** exponent
            except OverflowError:
                raise CalcMathError("Result too large to compute")
        return base

    def _unary(self):
        if self._current.kind == _OP and self._current.value in ("+", "-"):
            op = self._advance().value
            operand = self._unary()
            return -operand if op == "-" else operand
        return self._primary()

    def _primary(self):
        tok = self._current
        if tok.kind == _NUMBER:
            self._advance()
            return tok.value
        if tok.kind == _LPAREN:
            self._advance()
            value = self._expression()
            if self._current.kind != _RPAREN:
                raise CalcSyntaxError(
                    f"Expected ')' at position {self._current.pos}"
                )
            self._advance()
            return value
        if tok.kind == _EOF:
            raise CalcSyntaxError("Unexpected end of expression")
        if tok.kind == _RPAREN:
            raise CalcSyntaxError(f"Unbalanced ')' at position {tok.pos}")
        raise CalcSyntaxError(f"Unexpected token {tok.value!r} at position {tok.pos}")


def evaluate(expr):
    """Evaluate *expr* and return the numeric result as a ``float``.

    Raises :class:`CalcSyntaxError` for malformed input and
    :class:`CalcMathError` for invalid math (e.g. division by zero).
    """
    if expr is None or expr.strip() == "":
        raise CalcSyntaxError("Empty expression")
    tokens = tokenize(expr)
    return Parser(tokens).parse()
