from collections import Counter
from bisect import bisect_left


class Solution:
    def minMoves(self, A, lim):
        n = len(A) // 2
        pairs = zip(A, A[::-1])[:n]
        maxs = sorted(map(max, pairs))
        mins = sorted(map(min, pairs))
        counter = Counter([x + y for x, y in pairs])

        ret = float('inf')
        for target in range(2, 2 * lim + 1):
            increase_both = bisect_left(maxs, target - lim)
            decrease_both = n - bisect_left(mins, target)
            equal = counter[target]
            ret = min(ret, n - equal + increase_both + decrease_both)

        return ret
