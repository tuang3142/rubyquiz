DIR = { "U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1) }
BACK = { "U": "D", "L": "R", "D": "U", "R": "L" }
N = 500

class Solution(object):
    def __init__(self):
        self.grid = [[-1] * (N * 2) for _ in range(N * 2)]

    def findShortestPath(self, robot):
        if not self.dfs(robot, N, N): return -1
        return self.bfs()

    def dfs(self, robot, i, j):
        if self.grid[i][j] != -1: return
        self.grid[i][j] = 2 if robot.isTarget() else 0
        found = True if robot.isTarget() else False
        for d in DIR.keys():
            x, y = self.move_from(i, j, d)
            if not robot.canMove(d):
                self.grid[x][y] = 1
                continue
            robot.move(d)
            if self.dfs(robot, x, y): found = True
            robot.move(BACK[d])
        return found

    def bfs(self):
        qu = [(N, N, 0)]
        for i, j, dis in qu:
            if self.grid[i][j] == 2: return dis
            if self.grid[i][j] == 1: continue
            self.grid[i][j] = 1
            for d in DIR.keys():
                x, y = self.move_from(i, j, d)
                qu.append((x, y, dis + 1))

    def move_from(self, i, j, d):
        return i + DIR[d][0], j + DIR[d][1]
