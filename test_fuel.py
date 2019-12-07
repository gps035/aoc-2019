import unittest

from fuel import get_fuel_requirement, get_total_fuel_requirement


class TestFuelCalculation(unittest.TestCase):
    def test_no_rounding(self):
        self.assertEqual(get_fuel_requirement(12), 2)

    def test_rounding(self):
        self.assertEqual(get_fuel_requirement(14), 2)

    def test_big(self):
        self.assertEqual(get_fuel_requirement(1969), 654)

    def test_huge(self):
        self.assertEqual(get_fuel_requirement(100756), 33583)

    def test_recursive_no_extra(self):
        self.assertEqual(get_total_fuel_requirement(14), 2)

    def test_recursive_big(self):
        self.assertEqual(get_total_fuel_requirement(1969), 966)

    def test_recursive_huge(self):
        self.assertEqual(get_total_fuel_requirement(100756), 50346)


if __name__ == '__main__':
    unittest.main()
