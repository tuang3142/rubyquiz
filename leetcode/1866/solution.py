class Solution:
    def rearrangeSticks(self, n, k):
        mem = [[0] * (k + 1) for _ in range(n + 1)]
        mod = int(1e9 + 7)

        def dp(n, k):
            if k == 0 or k > n:
                return 0
            if n == 1:
                return 1
            if mem[n][k]:
                return mem[n][k]
            mem[n][k] = dp(n - 1, k - 1) % mod
            mem[n][k] = (mem[n][k] + (n - 1) * dp(n - 1, k)) % mod
            return mem[n][k]

        return dp(n, k)

