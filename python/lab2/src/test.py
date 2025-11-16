import unittest

from main import is_correct_bracket_sequence


class BracketSequenceTests(unittest.TestCase):
    def test_correct_simple(self) -> None:
        self.assertTrue(is_correct_bracket_sequence("()"))

    def test_correct_examples(self) -> None:
        self.assertTrue(is_correct_bracket_sequence("(()())()"))

    def test_incorrect_extra_close(self) -> None:
        self.assertFalse(is_correct_bracket_sequence("(()))"))

    def test_incorrect_misordered(self) -> None:
        self.assertFalse(is_correct_bracket_sequence(")())("))

    def test_empty_is_correct(self) -> None:
        self.assertTrue(is_correct_bracket_sequence(""))

    def test_single_open_is_incorrect(self) -> None:
        self.assertFalse(is_correct_bracket_sequence("("))

    def test_single_close_is_incorrect(self) -> None:
        self.assertFalse(is_correct_bracket_sequence(")"))

    def test_non_bracket_characters(self) -> None:
        self.assertFalse(is_correct_bracket_sequence("(a)"))
        self.assertFalse(is_correct_bracket_sequence("()()x"))
        self.assertFalse(is_correct_bracket_sequence("x"))

    def test_long_correct(self) -> None:
        self.assertTrue(is_correct_bracket_sequence("((()())(()()))"))


if __name__ == "__main__":
    unittest.main()
