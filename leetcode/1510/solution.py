class Solution:
    def winnerSquareGame(self, n):
        def sqr(n): return int(n ** 0.5)
        def square(n): return sqr(n) ** 2 == n

        dp = [[True, False] if square(i) else [-1, -1] for i in range(n + 1)]
        for i in range(n + 1):
            for p in range(2):
                if dp[i][p] != -1: continue
                win = True if p == 0 else False
                for j in range(1, sqr(i) + 1):
                    if win == dp[i - j**2][1 - p]:
                        dp[i][p] = win
                        break
                if dp[i][p] == -1:
                    dp[i][p] = not win
        return dp[n][0]
