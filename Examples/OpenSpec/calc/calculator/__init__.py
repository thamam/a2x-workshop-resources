"""A small, dependency-free terminal calculator."""

from .evaluator import CalcError, CalcSyntaxError, CalcMathError, evaluate

__all__ = ["CalcError", "CalcSyntaxError", "CalcMathError", "evaluate"]
