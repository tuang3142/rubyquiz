import unittest
from solution import FindSumPairs
from collections import Counter


class Test(unittest.TestCase):
    def setUp(self):
        self.A = [1, 1, 2, 2, 2, 3]
        self.B = [1, 4, 5, 2, 5, 4]

    def test_init(self):
        fsp = FindSumPairs(self.A, self.B)
        self.assertEqual(fsp.counter, Counter({4: 2, 5: 2, 1: 1, 2: 1}))

    def test_add_then_count(self):
        A = [1, 1, 2, 2, 2, 3]
        B = [1, 4, 5, 2, 5, 4]
        fsp = FindSumPairs(A, B)
        self.assertEqual(fsp.count(7), 8)
        fsp.add(3, 2)
        self.assertEqual(fsp.count(8), 2)
        self.assertEqual(fsp.count(4), 1)
        fsp.add(0, 1)
        fsp.add(1, 1)
        self.assertEqual(fsp.count(7), 11)


if __name__ == '__main__':
    unittest.main()
