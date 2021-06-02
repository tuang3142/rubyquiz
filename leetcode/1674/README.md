### tl;dr

[Link to problem statement.]()


### Idea
- change are either 0, 1, or 2
- each pair lets assum x <= y
- for each target: count(target <= x) and count(y < target - lim).  
its proven that they are separate
- `bisect_left` make sense
- log(n) is ok


### Complexity

with `n = `:
- time: `O()`
- space: `O()`
