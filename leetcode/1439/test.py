import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.kthSmallest = Solution().kthSmallest

    def test_general(self):
        mat = [[1,3,11],[2,4,6]]; k = 5
        self.assertEqual(self.kthSmallest(mat, k), 7)

        mat = [[1,10,10],[1,4,5],[2,3,6]]; k = 7
        self.assertEqual(self.kthSmallest(mat, k), 9)

        mat = [[1,1,10],[2,2,9]]; k = 7
        self.assertEqual(self.kthSmallest(mat, k), 12)

    def test_small_k(self):
        mat = [[1,3,11],[2,4,6]]; k = 1
        self.assertEqual(self.kthSmallest(mat, k), 3)

    def test_small_array(self):
        mat = [[1],[1]]; k = 1
        self.assertEqual(self.kthSmallest(mat, k), 2)


if __name__ == '__main__':
    unittest.main()
