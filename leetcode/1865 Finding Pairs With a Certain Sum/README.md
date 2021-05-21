### tl;dr
[Link to the problem.](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/)  
Given two integer arrays `A` and `B`, implement a class that supports two methods:

- `add(i, v)`: add `v` to `B[i]`
- `count(target)`: count the number of pairs `i, j` such that: `A[i] + B[j] == target`

### Idea

It screams out "please use hash" multiple times in the problem statement so we would indeed use hash. Steps:
- Construct a counter hash `counter = Counter(B)`.
- When adding: `counter[B[i]] -= 1`, `counter[B[i] + va] += 1`
- When counting, noticing that `len(A)` is much smaller than `len(B)`, we just need to sum up `counter[target - i]` for each `i` in `A`.

### Complexity

with `n = len(A)` and `m = len(B)`
- Time: much fast
  - Add: `O(1)`
  - Count: `O(n)`
- Space: `O(m)` such small
