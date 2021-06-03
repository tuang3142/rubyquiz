DIR = { "U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1) }
BACK = { "U": "D", "L": "R", "D": "U", "R": "L" }
N = 500

# maybe apply struct like python
class Solution(object):
    def __init__(self):
        self.found = False
        self.grid = [[-1] * (N * 2) for _ in range(N * 2)] # -1: unexplored, 0: empty, 1: blocked, 2: target

    def findShortestPath(self, gm):
        self.dfs(gm, N, N)
        if not self.found: return -1
        return self.bfs()

    def dfs(self, gm, i, j):
        if self.grid[i][j] != -1: return # visited
        if gm.isTarget():
            self.grid[i][j] = 2
            self.found = True
        else:
            self.grid[i][j] = 0
        for d in DIR.keys():
            x, y = i + DIR[d][0], j + DIR[d][1]
            if not gm.canMove(d):
                self.grid[x][y] = 1
                continue
            gm.move(d)
            self.dfs(gm, x, y)
            gm.move(BACK[d])

    def bfs(self):
        qu = [(N, N, 0)]
        for i, j, dis in qu:
            if self.grid[i][j] == 2: return dis
            if self.grid[i][j] != 0: continue
            self.grid[i][j] = 1 # block it to not go back
            for d in DIR.keys():
                x, y = i + DIR[d][0], j + DIR[d][1]
                qu.append((x, y, dis + 1))
