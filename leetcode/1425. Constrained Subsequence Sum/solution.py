from collections import deque


class Solution:
    def constrainedSubsetSum(self, A, k):
        ret = A[0]
        dp = deque([0])

        for i, val in enumerate(A):
            if i == 0:
                continue
            while dp and i - dp[0] > k:    # pop all out-of-k-range index
                dp.popleft()
            val = max(val, val + A[dp[0]]) # add to the previous largest sum, or dont if it worsens the result
            A[i] = val                     # do this for future "reference"
            ret = max(val, ret)
            while dp and A[dp[-1]] < val:  # make sure the order is always decreasing
                dp.pop()
            dp.append(i)

        return ret
