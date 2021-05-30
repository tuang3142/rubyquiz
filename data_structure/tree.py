class Tree():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def convert_array(A):
        B = [Tree(i) if i else None for i in A]
        root = B[0]
        for i, node in enumerate(B):
            if not node:
                continue
            left, right = i * 2 + 1, i * 2 + 2
            if left < len(B): node.left = B[i * 2 + 1]
            if right < len(B): node.right = B[i * 2 + 2]
        return root
