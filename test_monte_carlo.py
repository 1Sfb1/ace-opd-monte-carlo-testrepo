"""Controleer dat het voorbeeldbestand beide functies beschikbaar maakt."""

import unittest

from monte_carlo import estimate_pi, is_in_unit_circle


class VoorbeeldbestandenTest(unittest.TestCase):
    def test_cirkelfunctie_kan_worden_geimporteerd(self):
        self.assertTrue(callable(is_in_unit_circle))

    def test_schattingsfunctie_kan_worden_geimporteerd(self):
        self.assertTrue(callable(estimate_pi))


if __name__ == "__main__":
    unittest.main()
