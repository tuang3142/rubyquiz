### tl;dr

[Link to problem statement.](https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/)


### Idea

Think dynamically. The punch line is to arrange the sticks from right to left, so that when planting the highest stick available, it is surely visible from left. That leaves us two options for calculation:
- Planting the highest stick, then reduce `k` by 1.
- Not planting the highest, then don't reduce `k`. There are `n - 1` ways to do this.

```python
dp(n, k) = dp(n - 1, k - 1) + (n - 1) * dp(n - 1, k)
```

### Complexity

with `1 <= n <= 1000`
- time: `O(n^2)`
- space: `O(n^2)`
