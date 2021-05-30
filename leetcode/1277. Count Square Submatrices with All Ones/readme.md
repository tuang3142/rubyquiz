### tl;dr

[Link to problem statement.](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)  
Given a `m * n` grid of 1s and 0s, return how many squares have all 1s.

### Idea

[You should read this execlent visual explanation.](https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space))  
It's dynamic programming, but with an unusual punch line. Imagine 2x2 squares:
```
1 1     1 0
1 1     1 1
```
and notice the bottom right one. When counting squares of different sizes containing it, we take the minimum out of its neighbors. The formular is:
```
grid[i][j] += min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1])
```
Think about "you can only form squares if your neighbors also are square".


### Complexity

- time: `O(m * n)`
- space: `O(1)` (we reuse `grid` for memorizing so no extra space needed)
