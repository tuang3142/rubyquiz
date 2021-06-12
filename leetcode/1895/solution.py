class Solution:
    def largestMagicSquare(self, grid):
        n, m = len(grid), len(grid[0])
        ret = 1
        for i in range(n):
            for j in range(m):
                size = ret
                while i + size <= n and j + size <= m:
                    if self.magic(grid, i, j, size):
                        ret = size
                    size += 1
        return ret

    def magic(self, grid, i, j, size):
        r_range = range(i, i + size)
        c_range = range(j, j + size)
        ref = 0

        for r in r_range:
            s = 0
            for c in c_range:
                s += grid[r][c]
            if ref == 0: ref = s
            if ref != s: return False

        for c in c_range:
            s = 0
            for r in r_range:
                s += grid[r][c]
            if ref != s: return False

        a, b = 0, 0
        for s in range(size):
            a += grid[i + s][j + s]
            b += grid[i + size - s - 1][j + size - s - 1]
        return a == ref and b == ref
        return True


grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# print(Solution().magic(grid, 1, 1, 3))
print(Solution().largestMagicSquare(grid))
