import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.min_move = Solution().minMoves

    def test_general(self):
        A, lim = [1,2,4,3], 4
        self.assertEqual(self.min_move(A, lim), 1)

        A, lim = [1,2,2,1], 2
        self.assertEqual(self.min_move(A, lim), 2)

    def test_array_is_already_complement(self):
        A, lim = [1,2,3,4,5,6], 6
        self.assertEqual(self.min_move(A, lim), 0)


if __name__ == '__main__':
    unittest.main()
