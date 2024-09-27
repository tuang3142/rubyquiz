class Solution:
    def countSubstrings(self, s):
        def dp(i, j):
            if i == j - 1: return 1
            return dp(i, j - 1) + dp(i + 1,  j) + palin(s[i:j])

        def palin(s):
            return 1 if s == s[::-1]
