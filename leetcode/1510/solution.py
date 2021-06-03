class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        def sqr(n): return int(n ** 0.5)
        def square(n): return sqr(n) ** 2 == n
        def dp(n, player):
            if square(n):
                return True if player == 0 else False
            for i in range(sqr(n) + 1):
                if dp(n - i, 1 - player):
                    return True
            return False
        return dp(n, 0)
