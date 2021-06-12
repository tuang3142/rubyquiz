### tl;dr

[Link to problem statement.](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)

### Idea

Let `id = []` to store the index of the targeted array.  
Initially, `id = [0, 0, ..., 0]`, representing the smallest summed array.  
The next `id` to be inspected should be among `[1, 0, ..., 0], [0, 1, ..., 0], [0, 0, ..., 1]`.  
Does it seem bfs-y to you? Cus we gonna perform bfs with a min heap, prioritized by the array sum, to get the next `id`.

### Complexity

This solution is not the best performance-wise, but on the plus side requires the least brain power to digest and hopefully we can use our floppy English to make interviewer understand it.  

Let `N = k * n`:
- time: `O(N * log(N)`
- space: `O(N)`'
