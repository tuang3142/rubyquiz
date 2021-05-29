from collections import deque

class Solution:
    def constrainedSubsetSum(self, A, k):
        ret = A[0]
        dp = deque([0])

        for i, val in enumerate(A):
            if i == 0:
                continue
            while dp and i - dp[0] > k:
                dp.popleft()
            val = max(val, val + A[dp[0]])
            A[i] = val
            ret = max(val, ret)
            while dp and A[dp[-1]] < val:
                dp.pop()
            dp.append(i)

        return ret
