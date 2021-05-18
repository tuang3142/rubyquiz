from pdb import set_trace

class Solution:
    def countSquares(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        res = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    continue
                if i == 0 or j == 0:
                    res += matrix[i][j]
                else:
                    cell_val = matrix[i][j] + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
                    res += cell_val
                    matrix[i][j] = cell_val
        return res

n, m = 100, 100
matrix = [[1] * m for _ in range(n)]
# matrix = [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
print(Solution().countSquares(matrix))
