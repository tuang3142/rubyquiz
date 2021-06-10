import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.minWastedSpace = Solution().minWastedSpace

    def test_general(self):
        packages = [2,3,5]; boxes = [[4,8],[2,8]]
        self.assertEqual(self.minWastedSpace(packages, boxes), 6)


if __name__ == '__main__':
    unittest.main()
