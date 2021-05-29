### tl;dr

[Link to problem statement.](https://leetcode.com/problems/constrained-subsequence-sum/)  
Given an integer array `A` and an integer `k`, return the maximum sum of a non-empty subsequence from `A` such that every two consecutive integers, `A[i]` and `A[j]`, in the subsequence satisfy `j - i <= k`.


### Idea

For each number, check for the largest sum previously calculated (using dynamic programming) within the window size. To get the largest previous sum, several methods can be used. Then "k sized window" screams out [monotonic queue](https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6) which is the best solution, but acceptable others include priority queue and balanced binary search tree.


### Complexity

with `n = len(A)`:
- time: `O(n)`
- space: `O(k)`
