import unittest
from misaligned import get_index, get_color_map_length, print_color_map


class TestMisaligned(unittest.TestCase):
    def test_get_index(self):
        self.assertEqual(get_index(1, 2), "8")
        self.assertNotEqual(get_index(1, 2), 8)

    def test_get_color_map_length(self):
        self.assertEqual(get_color_map_length(5, 5), 25)

    def test_print_color_map(self):
        self.assertTrue(print_color_map())


if __name__ == "__main__":
    unittest.main()
