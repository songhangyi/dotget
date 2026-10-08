import unittest

from dotget import dig, dig_all, first_path, has_path, path_count


class DotgetTest(unittest.TestCase):
    def test_found_and_missing(self) -> None:
        data = {"a": {"b": 1}}
        self.assertEqual(dig(data, "a.b"), 1)
        self.assertEqual(dig(data, "a.c", 0), 0)
        self.assertTrue(has_path(data, "a.b"))
        self.assertFalse(has_path(data, "a.c"))
        self.assertEqual(dig_all(data, ["a.b", "a.c"], 0), {"a.b": 1, "a.c": 0})
        self.assertEqual(first_path(data, ["a.c", "a.b"]), "a.b")
        self.assertEqual(first_path(data, ["a.c"]), "")
        self.assertEqual(path_count(data, ["a.b", "a.c"]), 1)
        with self.assertRaises(ValueError):
            dig(data, "a..b")


if __name__ == "__main__":
    unittest.main()
