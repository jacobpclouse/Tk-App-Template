import unittest
from app.utils.icons import symbol

class ComponentHelperTests(unittest.TestCase):
    def test_known_symbols(self):
        self.assertEqual(symbol("home"), "⌂")
        self.assertEqual(symbol("plus"), "+")

    def test_unknown_symbol_falls_back(self):
        self.assertEqual(symbol("not-a-real-icon"), "•")

if __name__ == "__main__":
    unittest.main()
