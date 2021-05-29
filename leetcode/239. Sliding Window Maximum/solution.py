from collections import deque

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
