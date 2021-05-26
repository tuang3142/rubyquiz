class Solution:
    def __init__(self):
        self.ret = 0

    def dfs(self, flag, node, step):
        if not node: return 0
        self.ret = max(self.ret, step)

        if flag == "left":
            self.dfs("right", node.left, step + 1)
            self.dfs("left", node.left, 0)
        else:
            self.dfs("left", node.right, step + 1)
            self.dfs("right", node.right, 0)

    def longestZigZag(self, root):
        self.dfs("left", root, 0)
        self.dfs("right", root, 0)
        return self.ret

