class Solution:
    def ways(self, pizza, k):
        self.grid = [[0 if c == '.' else 1 for c in row] for row in pizza]
        self.row, self.col = len(pizza), len(pizza[0])
        self.dp = {}
        self.sum_grid = None

        return self.dfs(0, 0, k)

    def dfs(self, a, b, k):
        if (a, b, k) in self.dp: return self.dp[(a, b, k)]
        if k == 1 and self.count(a, b, self.row, self.col) >= 1: return 1
        if k == 0 or self.count(a, b, self.row, self.col) < k: return 0

        mod = int(1e9) + 7
        ret = 0
        for i in range(a + 1, self.row):
            if self.count(a, b, i, self.col) > 0:
                ret = (ret + self.dfs(i, b, k - 1)) % mod
        for i in range(b + 1, self.col):
            if self.count(a, b, self.row, i) > 0:
                ret = (ret + self.dfs(a, i, k - 1)) % mod

        self.dp[(a, b, k)] = ret
        return ret

    def count(self, a, b, c, d):
        if a == c or b == d: return 0
        a, b = a + 1, b + 1
        if not self.sum_grid:
            self.sum_grid = self.init_sum_grid(self.grid)
        return self.sum_grid[c][d] - self.sum_grid[c][b-1] \
             - self.sum_grid[a-1][d] + self.sum_grid[a-1][b-1]

    def init_sum_grid(self, grid):
        n, m = len(grid) + 1, len(grid[0]) + 1
        sum_grid = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                sum_grid[i][j] = grid[i-1][j-1]
                sum_grid[i][j] += sum_grid[i-1][j] + sum_grid[i][j-1] - sum_grid[i-1][j-1]

        return sum_grid
