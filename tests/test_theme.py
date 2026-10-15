import unittest
from app.theme import PALETTES
from app.utils.scaling import compact_layout, columns_for_width

class ThemeTests(unittest.TestCase):
    def test_both_palettes_have_same_tokens(self):
        self.assertEqual(set(PALETTES["light"]), set(PALETTES["dark"]))

    def test_accent_tokens_are_present(self):
        self.assertTrue(PALETTES["light"]["accent"])
        self.assertTrue(PALETTES["dark"]["accent"])

    def test_responsive_breakpoint(self):
        self.assertTrue(compact_layout(800))
        self.assertFalse(compact_layout(1000))

    def test_grid_column_estimate(self):
        self.assertEqual(columns_for_width(100), 1)
        self.assertGreaterEqual(columns_for_width(1200), 1)

if __name__ == "__main__":
    unittest.main()
