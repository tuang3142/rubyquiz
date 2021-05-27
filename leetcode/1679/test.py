import unittest
from solution import Solution

class TestMaxOperations(unittest.TestCase):
    def test_regular_cases(self):
        result = Solution().max_operations([1, 2, 3, 4], 5)
        self.assertEqual(result, 2)

        result = Solution().max_operations([3,1,3,4,3], 6)
        self.assertEqual(result, 1)

    # tbd

if __name__ == '__main__':
    unittest.main()
