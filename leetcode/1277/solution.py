class Solution:
    def countSquares(self, grid):
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                res += grid[i][j]
                if i != 0 and j != 0:
                    cell_val = min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1])
                    res += cell_val
                    grid[i][j] += cell_val
        return res
