### tl;dr

[Link to the original problem](https://leetcode.com/problems/max-number-of-k-sum-pairs/)  
Given an integer array `A` and an integer `k`.  
Operation: Pick two numbers from `A` whose sum equals `k` and remove them from `A`.  
Return the maximum number of operations can be performed.


### Idea

Make a `counter = collections.Counter(A)`. For each key `n` of `counter`, check for `counter[k - n]`, then update their counter to the final result accordingly (you know what I'm talking about right? Right?). Mind when `n == k - n`.


### Complexity

- Time: `O(n)`
- Space: `O(n)`
