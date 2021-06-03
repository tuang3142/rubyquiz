import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.winnerSquareGame = Solution().winnerSquareGame

    def test_general(self):
        self.assertTrue(self.winnerSquareGame(1))
        self.assertFalse(self.winnerSquareGame(2))
        self.assertFalse(self.winnerSquareGame(7))
        self.assertFalse(self.winnerSquareGame(17))

    def test_largest_n(self):
        self.assertTrue(self.winnerSquareGame(100000))


if __name__ == '__main__':
    unittest.main()
