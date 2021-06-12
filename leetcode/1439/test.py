import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.kthSmallest = Solution().kthSmallest

    # example cases, can be solved by hand, given in statement
    def test_general(self):
        mat = [[1,3,11],[2,4,6]]; k = 5
        self.assertEqual(self.kthSmallest(mat, k), 7)

    # really small/large cases, usually 0 or n
    # def test_edge(self):

    # def test_no_solution(self):

    # not edge case, but could fail if not handle properly
    # def test_tricky(self):


if __name__ == '__main__':
    unittest.main()
