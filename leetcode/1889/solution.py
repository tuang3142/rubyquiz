from bisect import bisect_right
from itertools import accumulate

class Solution:
    def minWastedSpace(self, packs, boxes):
        packs.sort()
        ret = float('inf')
        for box in boxes:
            box.sort()
            if box[-1] < packs[-1]: continue
            i = 0
            total_box = 0
            for b in box:
                j = bisect_right(packs, b)
                total_box += (j - i) * b
                i = j
            ret = min(ret, total_box)

        if ret == float('inf'): return -1
        return (ret - sum(packs)) % int(1e9 + 7)
