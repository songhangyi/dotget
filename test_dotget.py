import unittest

from dotget import all_paths, any_path, dig, dig_all, first_path, has_path, missing_count, missing_paths, path_count, present_paths


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
        self.assertEqual(missing_paths(data, ["a.b", "a.c"]), ["a.c"])
        self.assertEqual(present_paths(data, ["a.b", "a.c"]), ["a.b"])
        self.assertTrue(any_path(data, ["a.c", "a.b"]))
        self.assertFalse(any_path(data, ["a.c"]))
        self.assertTrue(all_paths(data, ["a.b"]))
        self.assertFalse(all_paths(data, ["a.b", "a.c"]))
        self.assertEqual(missing_count(data, ["a.b", "a.c"]), 1)
        with self.assertRaises(ValueError):
            dig(data, "a..b")


if __name__ == "__main__":
    unittest.main()
