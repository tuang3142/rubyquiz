import sys, os
sys.path.append(os.path.abspath("./data_structure"))
import unittest
from linked_list import LinkedList
from tree import Tree
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.isSubPath = Solution().isSubPath

    def test_general(self):
        head = LinkedList.convert_array([4,2,8])
        root = Tree.convert_array([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
        self.assertEqual(self.isSubPath(head, root), True)

        head = LinkedList.convert_array([1,4,2,6])
        root = Tree.convert_array([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
        self.assertEqual(self.isSubPath(head, root), True)

        head = LinkedList.convert_array([1,4,2,6,8])
        root = Tree.convert_array([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
        self.assertEqual(self.isSubPath(head, root), False)

    def test_len_head_is_1(self):
        head = LinkedList(7)
        root = Tree.convert_array([1, 7])
        self.assertEqual(self.isSubPath(head, root), True)

    def test_head_is_longer_than_tree_depth(self):
        head = LinkedList([1, 2, 3, 4, 5])
        root = Tree.convert_array([1, 2, 3, 4])
        self.assertEqual(self.isSubPath(head, root), False)

        head = LinkedList([1, 2, 3, 4, 5])
        root = Tree.convert_array([1, 2])
        self.assertEqual(self.isSubPath(head, root), False)


if __name__ == '__main__':
    unittest.main()
