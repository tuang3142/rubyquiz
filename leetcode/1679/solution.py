from collections import Counter


class Solution:
    def maxOperations(self, nums, s):
        counter = Counter(nums)
        ret = 0
        for k in counter.keys():
            if s - k not in counter:
                continue
            if s - k == k:
                ret += counter[k] // 2
                counter[k] %= 2
                continue
            to_add = min(counter[k], counter[s - k])
            counter[k] -= to_add
            counter[s - k] -= to_add
            ret += to_add

        return ret

