import heapq

class Solution:
    def constrainedSubsetSum(self, nums, k):
        nums = [-i for i in nums]
        h = []
        heapq.heappush(h, [nums[0], 0])
        ret = nums[0]

        for i, val in enumerate(nums):
            if i == 0: continue
            while i - h[0][1] > k:          # pop out of range number from i
                heapq.heappop(h)
            val = min(h[0][0] + val, val)   # 2 choices: pick the best prior sum or "no, thanks"
            ret = min(ret, val)
            heapq.heappush(h, [val, i])

        return -ret
