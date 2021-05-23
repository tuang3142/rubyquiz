class Solution:
    def kmp(self, word, pattern):
        i, j = 0, 0
        n, m = len(word), len(pattern)
        while i < n:
            if word[i] == pattern[j]:    # match
                i, j = i + 1, j + 1
                if j == m:               # found pattern
                    return i - m
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

    def build_lps(self, pattern):
        n = len(pattern)
        lps = [0] * n
        i, j = 1, 0 # skip first position since its always 0
        while i < n:
            if pattern[j] == pattern[i]: # if prefix match suffix
                j += 1                   # increase prefix length
                lps[i] = j
                i += 1                   # and move on
            else:                        # else
                if j > 0:
                    j = lps[j - 1]   # try shorter prefix
                else:
                    i += 1               # move on cus no prefix match
        return lps

sol = Solution()
word = "cababcabab"
pattern = "aba"
print(sol.kmp(word, pattern))
