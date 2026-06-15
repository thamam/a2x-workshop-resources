import io
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator.cli import main  # noqa: E402


def run(argv, stdin_text=""):
    out, err = io.StringIO(), io.StringIO()
    code = main(
        argv,
        stdin=io.StringIO(stdin_text),
        stdout=out,
        stderr=err,
    )
    return code, out.getvalue(), err.getvalue()


class TestOneShot(unittest.TestCase):
    def test_single_argument_expression(self):
        code, out, err = run(["2 + 3 * 4"])
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "14")
        self.assertEqual(err, "")

    def test_multiple_argument_expression(self):
        code, out, _ = run(["2", "+", "3"])
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "5")

    def test_invalid_expression_exit_code_and_stderr(self):
        code, out, err = run(["2 +"])
        self.assertNotEqual(code, 0)
        self.assertEqual(out, "")
        self.assertIn("Error", err)

    def test_division_by_zero(self):
        code, _, err = run(["5 / 0"])
        self.assertNotEqual(code, 0)
        self.assertIn("Division by zero", err)


class TestFormatting(unittest.TestCase):
    def test_integer_result_has_no_decimal(self):
        _, out, _ = run(["6 / 2"])
        self.assertEqual(out.strip(), "3")

    def test_decimal_result(self):
        _, out, _ = run(["7 / 2"])
        self.assertEqual(out.strip(), "3.5")


class TestRepl(unittest.TestCase):
    def test_evaluate_line(self):
        code, out, _ = run([], stdin_text="2 + 3\n")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "5")

    def test_error_does_not_terminate(self):
        code, out, err = run([], stdin_text="2 +\n4 + 4\n")
        self.assertEqual(code, 0)
        self.assertIn("Error", err)
        self.assertEqual(out.strip(), "8")

    def test_exit_on_quit_keyword(self):
        code, out, _ = run([], stdin_text="1 + 1\nquit\n2 + 2\n")
        self.assertEqual(code, 0)
        # Lines after quit are not evaluated.
        self.assertEqual(out.strip(), "2")

    def test_exit_on_eof(self):
        code, out, _ = run([], stdin_text="3 * 3\n")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "9")

    def test_blank_lines_are_skipped(self):
        code, out, _ = run([], stdin_text="\n\n5 + 5\n")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "10")


if __name__ == "__main__":
    unittest.main()
