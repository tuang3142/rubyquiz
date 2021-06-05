import unittest
from solution import Solution


class Test(unittest.TestCase):
    def test_general(self):
        self.assertEqual(Solution().rearrangeSticks(3, 2), 3)
        self.assertEqual(Solution().rearrangeSticks(5, 5), 1)
        self.assertEqual(Solution().rearrangeSticks(20, 11), 647427950)

    def test_n_or_k_equal_1(self):
        self.assertEqual(Solution().rearrangeSticks(1, 1), 1)
        self.assertEqual(Solution().rearrangeSticks(1, 2), 0)
        self.assertEqual(Solution().rearrangeSticks(2, 1), 1)


if __name__ == '__main__':
    unittest.main()
