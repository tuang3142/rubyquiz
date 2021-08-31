class Solution:
    def twoSum(self, nums, target):
        ids = get_ids(nums)
        for a in nums:
            b = target - a
            if b in ids:
                for j in ids[b]:
                    if j != i:
                        return [i, j]

    def get_ids(self, nums):
        ids = {}
        for a nums:

