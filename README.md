# Why

This is my take on [leetcode](http://leetcode.com/) problems. Occasionally, I'll write algorithms and data structures from scratch. The purpose is to practice and showcase clean and test-driven code. I primarily use python (over ruby, which I use professionally) because of the wide range of supported python libraries for solving algorithmic problems.

Each problem comes with an explanation of what it is, how to solve it, and test suites. I keep it brief as it takes great effort to write an "easy-to-understand" solution and even greater effort to understand it. Again, the punch line is only "clean and test-driven" code.


# Examples
(to be added 3 examples)

## 239. Sliding Window Maximum

### tl;dr
[Link to the original problem.](https://leetcode.com/problems/sliding-window-maximum/)  
Given an array of integers `A` and a window of size `k`, return the largest number in the window when moving it from left to right one index at a time.
```
Input: A = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Window position                Max
----------------------------------
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

### Idea

Use [monotonic queue](http://www.algorithmsandme.com/monotonic-queue/). Basically, create a queue and make sure the order is decreasing so that the first number in q is the largest.

### Complexity

With `n = len(A)`:
- time: `O(n)`
- space: `O(n)`


### Code
```python
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

## two more
