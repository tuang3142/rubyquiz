class Solution:
    def isSubPath(self, head, root):
        A, lps = self.convert_to_array(head) # lps = longest "prefix which is also suffix"
        def visit(node, i):
            if i >= len(A):
                return True
            if not node:
                return False
            if node.val == A[i]:
                return(visit(node.left, i + 1) or visit(node.right, i + 1))
            if i > 0:
                return visit(node, lps[i - 1])
            return visit(node.left, 0) or visit(node.right, 0)

        return visit(root, 0)

    def convert_to_array(self, node):
        A = []
        while node:
            A.append(node.val)
            node = node.next
        lps = [0] * len(A)
        i, j = 1, 0
        while i < len(A):
            if A[i] == A[j]:
                lps[i] = j + 1
                i, j = i + 1, j + 1
            else:
                if j > 0: j = lps[j - 1]
                else: i += 1
        return A, lps
