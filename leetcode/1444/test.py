import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.ways = Solution().ways

    def test_general(self):
        pizza, k = ["A..","AAA","..."], 3
        self.assertEqual(self.ways(pizza, k), 3)

        pizza, k = ["A..","AA.","..."], 3
        self.assertEqual(self.ways(pizza, k), 1)

        pizza, k = ["A..","A..","..."], 1
        self.assertEqual(self.ways(pizza, k), 1)


    def test_k_equal_pizza_size(self):
        pizza, k = ["A..","AAA","..."], 3
        self.assertEqual(self.ways(pizza, k), 3)

        pizza, k = ["AAA","AAA","AAA"], 3
        self.assertEqual(self.ways(pizza, k), 10)


if __name__ == '__main__':
    unittest.main()
