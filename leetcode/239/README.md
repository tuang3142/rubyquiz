### tl;dr

[Link to the problems statement.](https://leetcode.com/problems/sliding-window-maximum/)  
Given an array of integers `A` and a window of size `k`, return the largest number in the window when moving it from left to right one index at a time.


### Idea

Use [monotonic queue](http://www.algorithmsandme.com/monotonic-queue/). Basically, create a queue and make sure the order is decreasing so that the first number in q is the largest.


### Complexity

With `n = len(A)`:
- time: `O(n)`
- space: `O(n)`



