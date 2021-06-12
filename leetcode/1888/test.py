import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.minFlips = Solution().minFlips

    def test_general(self):
        self.assertEqual(self.minFlips("111000"), 2)
        self.assertEqual(self.minFlips("010"), 0)
        self.assertEqual(self.minFlips("1110"), 1)

    def test_size1_string(self):
        self.assertEqual(self.minFlips("1"), 0)
        self.assertEqual(self.minFlips("0"), 0)


if __name__ == '__main__':
    unittest.main()
