class Solution:
    def winnerSquareGame(self, n):
        def sqr(n): return int(n ** 0.5)
        dp = [False] * (n + 1)
        for i in range(n + 1):
            if dp[i]: continue
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = True
                j += 1

        return dp[n]
