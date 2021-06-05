import unittest
from solution import Solution


class Test(unittest.TestCase):
    def test_general(self):
        self.assertEqual(Solution().maxOperations([1, 2, 3, 4], 5), 2)

        self.assertEqual(Solution().maxOperations([3,1,3,4,3], 6), 1)

    def test_no_solution(self):
        self.assertEqual(Solution().maxOperations([1], 1), 0)
        self.assertEqual(Solution().maxOperations([1, 1, 1, 1, 1], 3), 0)

    def test_all_number_are_equal(self):
        self.assertEqual(Solution().maxOperations([2, 2, 2, 2, 2], 4), 2)


if __name__ == '__main__':
    unittest.main()
