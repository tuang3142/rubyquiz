from collections import deque
from pdb import set_trace

class Solution:
    def maxSlidingWindow(self, A, k):
        qu = deque()
        ret = []
        for i in range(len(A)):
            while qu and A[i] >= A[qu[-1]]: # keep the qu in decreasing order
                qu.pop()                    # make sure the first number in qu is the largest
            qu.append(i)
            if i < k - 1:                   # appending the first k numbers to qu
                continue
            while qu and i - qu[0] + 1 > k: # pop the first in qu if it is out of window range
                qu.popleft()
            ret.append(A[qu[0]])
        return ret

A = [7, 2, 4]
k = 2

print(Solution().maxSlidingWindow(A, k))
