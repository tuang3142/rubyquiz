import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.min_move = Solution().minMoves

    def test_general(self):
        nums = [1,2,4,3]
        limit = 4
        self.assertEqual(self.min_move(nums, limit), 1)

        nums = [1,2,2,1]
        limit = 2
        self.assertEqual(self.min_move(nums, limit), 2)

    # really small/large cases, usually 0 or n
    def test_array_is_already_complement(self):
        nums = [1,2,3,4,5,6]
        limit = 6
        self.assertEqual(self.min_move(nums, limit), 0)


    # def test_no_solution(self):

    # not edge case, but could fail if not handle properly
    # def test_tricky(self):


if __name__ == '__main__':
    unittest.main()
