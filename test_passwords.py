import unittest

from passwords import is_valid_password_simple, is_valid_password_strict


class TestPasswords(unittest.TestCase):
    def test_simple_1(self):
        self.assertTrue(is_valid_password_simple("111111"))

    def test_simple_2(self):
        self.assertFalse(is_valid_password_simple("223450"))

    def test_simple_3(self):
        self.assertFalse(is_valid_password_simple("123789"))

    def test_simple_4(self):
        self.assertTrue(is_valid_password_simple("112233"))

    def test_simple_5(self):
        self.assertTrue(is_valid_password_simple("123444"))

    def test_simple_6(self):
        self.assertTrue(is_valid_password_simple("111122"))

    def test_strict_1(self):
        self.assertFalse(is_valid_password_strict("111111"))

    def test_strict_2(self):
        self.assertFalse(is_valid_password_strict("223450"))

    def test_strict_3(self):
        self.assertFalse(is_valid_password_strict("123789"))

    def test_strict_4(self):
        self.assertTrue(is_valid_password_strict("112233"))

    def test_strict_5(self):
        self.assertFalse(is_valid_password_strict("123444"))

    def test_strict_6(self):
        self.assertTrue(is_valid_password_strict("111122"))


if __name__ == '__main__':
    unittest.main()
