import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.min_move = Solution().minMoves

    def test_general(self):
        A = [1,2,4,3]
        limit = 4
        self.assertEqual(self.min_move(A, limit), 1)

        A = [1,2,2,1]
        limit = 2
        self.assertEqual(self.min_move(A, limit), 2)

    def test_increase_both_or_decrease_both(self):
        # tbd
        pass

    def test_array_is_already_complement(self):
        A = [1,2,3,4,5,6]
        limit = 6
        self.assertEqual(self.min_move(A, limit), 0)


if __name__ == '__main__':
    unittest.main()
