import unittest
from solution import Solution


class Test(unittest.TestCase):
    def test_general(self):
        A, k = [10,2,-10,5,20], 2
        self.assertEqual(Solution().constrainedSubsetSum(A, k), 37)

        A, k = [10,-2,-10,-5,20], 2
        self.assertEqual(Solution().constrainedSubsetSum(A, k), 23)

        A, k = [1, 2, 3], 1
        self.assertEqual(Solution().constrainedSubsetSum(A, k), 6)

    def test_too_bad_but_have_to_choose(self):
        A, k = [-1, -2, -3], 2
        self.assertEqual(Solution().constrainedSubsetSum(A, k), -1)

    def test_k_equal_len_A(self):
        A, k = [10,-2,-10,-5,20], 5
        self.assertEqual(Solution().constrainedSubsetSum(A, k), 30)


if __name__ == '__main__':
    unittest.main()
