import unittest
from lab5 import RowError, parse_rows


class TestParseRows(unittest.TestCase):
    def test_correct(self):
        lines = ["name;score", "Олена;92"]
        self.assertEqual(parse_rows(lines), ([{"name": "Олена", "score": 92}], []))

    def test_error(self):
        lines = ["name;score", "Олена;92", "Андрій;abc"]
        with self.assertRaises(RowError) as e:
            parse_rows(lines)
        self.assertEqual(e.exception.line_no, 3)
        self.assertEqual(str(e.exception), "рядок 3: score не є числом")
        self.assertIsInstance(e.exception.__cause__, ValueError)

    def test_skip(self):
        lines = ["name;score", "Олена;92", "Андрій;abc", "Марта"]
        self.assertEqual(parse_rows(lines, errors="skip"),
                         ([{"name": "Олена", "score": 92}], [3, 4]))

    def test_wrong_columns(self):
        with self.assertRaises(RowError) as e:
            parse_rows(["name;score", "Марта"])
        self.assertEqual(e.exception.line_no, 2)

    def test_unknown_mode(self):
        with self.assertRaises(ValueError):
            parse_rows(["name;score"], errors="ignore")

    def test_empty_table(self):
        with self.assertRaises(RowError):
            parse_rows([])


if __name__ == "__main__":
    unittest.main()
