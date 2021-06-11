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


    # really small/large cases, usually 0 or n
    # def test_edge(self):

    # def test_no_solution(self):

    # not edge case, but could fail if not handle properly
    # def test_tricky(self):


if __name__ == '__main__':
    unittest.main()
