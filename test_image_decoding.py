import unittest

from image_decoding import flatten_layers


class TestImageDecoding(unittest.TestCase):
    def test_flatten_layers(self):
        self.assertEqual(flatten_layers("0222112222120000", 2, 2), "0110")


if __name__ == '__main__':
    unittest.main()
