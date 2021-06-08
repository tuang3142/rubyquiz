class Solution:
    def minFlips(self, s):
        def srange(a, i, j):
            if i == 0: return a[j]
            return a[j] - a[i - 1]

        s = list(s)
        n = len(s)
        a = ["1" if i % 2 else "0" for i in range(n)] # start with 0
        b = ["0" if i % 2 else "1" for i in range(n)] # start with 1
        start0 = list(accumulate([0 if i == j else 1 for i, j in zip(s, a)]))
        start1 = list(accumulate([0 if i == j else 1 for i, j in zip(s, b)]))
        if a[-1] == "0":
            end0, end1 = start0, start1
        else:
            end0, end1 = start1, start0
        ret = min(start0[-1], start1[-1])
        for i in range(1, n):
            ret = min(ret, srange(end0, i, n - 1) + srange(start1, 0, i - 1))
            ret = min(ret, srange(end1, i, n - 1) + srange(start0, 0, i - 1))
        return ret
