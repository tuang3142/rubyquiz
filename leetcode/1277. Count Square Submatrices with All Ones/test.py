import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.countSquares = Solution().countSquares

    def test_general(self):
        grid = [
          [0,1,1,1],
          [1,1,1,1],
          [0,1,1,1]
        ]
        self.assertEqual(self.countSquares(grid), 15)

        grid = [
          [1,0,1],
          [1,1,0],
          [1,1,0]
        ]
        self.assertEqual(self.countSquares(grid), 7)


if __name__ == '__main__':
    unittest.main()
