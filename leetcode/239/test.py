import unittest
from solution import Solution

class Test(unittest.TestCase):
    def test_general_cases(self):
        A = [1,3,-1,-3,5,3,6,7]
        k = 3
        self.assertEqual(Solution().maxSlidingWindow(A, k), [3,3,5,5,6,7])

        A = [7,2,4]
        k = 2
        self.assertEqual(Solution().maxSlidingWindow(A, k), [7, 4])

    def test_k_equal_1(self):
        A = [-1, 2, 3]
        k = 1
        self.assertEqual(Solution().maxSlidingWindow(A, k), [-1, 2, 3])

    def test_k_equal_array_length(self):
        A = [-1, 2, 3]
        k = 3
        self.assertEqual(Solution().maxSlidingWindow(A, k), [3])

if __name__ == '__main__':
    unittest.main()
