### tl;dr

[Link to problem statement.](https://leetcode.com/problems/minimum-moves-to-make-array-complementary)


### Idea

To make a pair `x, y`'s sum equal a target `t`:

- if `t == x + y`, no changes are made
- if `t <= x`, decrease both numbers
- if `y + lim < t`, increase both numbers
- otherwise, change one number  

so the cost to change all pairs to meet a target: `change_one + increase_both * 2 + decrease_both * 2`

Since `t <= n = 10^5`, we can check each `t` and do binary search for `O(n*log(n)`. Steps:
- create 2 arrays `maxs` and `mins` that are the sorted versions of `pairs` with key `x` and `y` respectively (`x <= y`, mind)
- for each target `t`: 
  - `count x >= t for x in mins` and `count y < t - lim for i in maxs`
  - `bisect_left` makes sense here
  - it can be proven that the two above set are separated, so we dont count a pair twice.
  - calculate the result


### Complexity

- time: `O(n*log(n))`
- space: `O(n)`
