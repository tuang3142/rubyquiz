### tl;dr

[Link to problem statement.](https://leetcode.com/problems/constrained-subsequence-sum/)  
Given an integer array `A` and an integer `k`, return the maximum sum of a non-empty subsequence from `A` such that every two consecutive integers, `A[i]` and `A[j]`, in the subsequence satisfy `j - i <= k`.


### Idea

For each number, check for the largest sum previously calculated within the window size. The sum is saved for future comparation (dynamic programming here). To get the largest value quickly, several methods can be used. Then "k sized window" screams out [monotonic queue](https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6) which is the best solution, but acceptable others include priority queue and balanced binary search tree.


### Complexity

with `n = len(A)`:
- time: `O(n)` (`O(log(n))` for priority queue and bst)
- space: `O(k)`
