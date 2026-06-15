import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator.evaluator import (  # noqa: E402
    CalcMathError,
    CalcSyntaxError,
    evaluate,
)


class TestOperators(unittest.TestCase):
    def test_addition_and_subtraction(self):
        self.assertEqual(evaluate("2 + 3 - 1"), 4)

    def test_multiplication_and_division(self):
        self.assertEqual(evaluate("6 * 7 / 2"), 21)

    def test_modulo(self):
        self.assertEqual(evaluate("10 % 3"), 1)

    def test_exponentiation(self):
        self.assertEqual(evaluate("2 ** 10"), 1024)


class TestPrecedenceAndAssociativity(unittest.TestCase):
    def test_multiplication_over_addition(self):
        self.assertEqual(evaluate("2 + 3 * 4"), 14)

    def test_left_associative_subtraction(self):
        self.assertEqual(evaluate("10 - 4 - 3"), 3)

    def test_right_associative_exponentiation(self):
        self.assertEqual(evaluate("2 ** 3 ** 2"), 512)


class TestParenthesesAndUnary(unittest.TestCase):
    def test_parentheses_override_precedence(self):
        self.assertEqual(evaluate("(2 + 3) * 4"), 20)

    def test_unary_minus_on_number(self):
        self.assertEqual(evaluate("-5 + 2"), -3)

    def test_unary_minus_on_subexpression(self):
        self.assertEqual(evaluate("-(3 + 4)"), -7)

    def test_unary_plus(self):
        self.assertEqual(evaluate("+5"), 5)


class TestDecimals(unittest.TestCase):
    def test_decimal_operands(self):
        self.assertAlmostEqual(evaluate("0.1 + 0.2"), 0.3)

    def test_non_integer_division(self):
        self.assertEqual(evaluate("7 / 2"), 3.5)

    def test_leading_decimal_point(self):
        self.assertEqual(evaluate(".5 + .5"), 1)


class TestErrors(unittest.TestCase):
    def test_invalid_syntax(self):
        with self.assertRaises(CalcSyntaxError):
            evaluate("2 +")

    def test_unbalanced_parentheses(self):
        with self.assertRaises(CalcSyntaxError):
            evaluate("(2 + 3")

    def test_unknown_character(self):
        with self.assertRaises(CalcSyntaxError):
            evaluate("2 $ 3")

    def test_empty_expression(self):
        with self.assertRaises(CalcSyntaxError):
            evaluate("   ")

    def test_division_by_zero(self):
        with self.assertRaises(CalcMathError):
            evaluate("5 / 0")

    def test_modulo_by_zero(self):
        with self.assertRaises(CalcMathError):
            evaluate("5 % 0")


if __name__ == "__main__":
    unittest.main()
