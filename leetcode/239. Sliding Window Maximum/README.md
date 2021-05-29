#### tl;dr
[Link to the original problem](https://leetcode.com/problems/sliding-window-maximum/)  
Given an array of integers `A` and a window of size `k`,  
return the largest number in the window when moving it from left to right one index at a time.
```
Input: A = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
----------------------------------
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

#### Idea

Use [monotonic queue](http://www.algorithmsandme.com/monotonic-queue/). Basically, create a queue and make sure the order is decreasing so that the first number in q is the largest.


#### Code
```python
# complexity with n = len(A):
# time: O(n) 
# space: O(n)

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
```
