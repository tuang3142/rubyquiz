class Solution:
    def minFlips(self, s):
        def srange(a, i, j):
            if i == 0: return a[j]
            return a[j] - a[i - 1]

        n = len(s)
        a = ["1" if i % 2 else "0" for i in range(n)] # start with 0
        b = ["0" if i % 2 else "1" for i in range(n)] # start with 1
        accumulate_cost = lambda a, b: list(accumulate([0 if i == j else 1 for i, j in zip(a, b)]))
        prefix0 = accumulate_cost(s, a)
        prefix1 = accumulate_cost(s, b)
        if a[-1] == "0":
            suffix0, suffix1 = prefix0, prefix1
        else:
            suffix0, suffix1 = prefix1, prefix0

        ret = min(prefix0[-1], prefix1[-1])
        for i in range(1, n):
            ret = min(ret, srange(suffix0, i, n - 1) + srange(prefix1, 0, i - 1))
            ret = min(ret, srange(suffix1, i, n - 1) + srange(prefix0, 0, i - 1))
        return ret
