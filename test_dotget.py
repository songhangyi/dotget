import unittest

from dotget import dig


class DotgetTest(unittest.TestCase):
    def test_found_and_missing(self) -> None:
        data = {"a": {"b": 1}}
        self.assertEqual(dig(data, "a.b"), 1)
        self.assertEqual(dig(data, "a.c", 0), 0)
        with self.assertRaises(ValueError):
            dig(data, "a..b")


if __name__ == "__main__":
    unittest.main()
