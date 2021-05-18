[Link to original problem](https://leetcode.com/problems/maximum-building-height/)

**Idea**

[Thanks votrubac for the original idea](https://leetcode.com/problems/maximum-building-height/discuss/1175269/C%2B%2B-with-picture-2-passes)

Going from left to right, let's find the maximum height `h` between two limits: `h1` and `h2` which are indexed `i` and `j`.
To get the highest result from `h1`, we keep increasing the height by 1 from `i` to `j`. At best, `h = h1 + (j - i)`.
If `h <= h2`: decrease h2 to meet h (`h2 = h`) since it's no help keeping it higher.
If `h > h2`: find a mutual "top" so we can ascend to that point and descend to h2: `h = (h + h2) / 2`.
Repeat from right to left and update the answer.

 **Complexity**

- Time & Space: `O(n)`

**Code**

```ruby
def get_max_height(cap, i, j)
  i1, h1 = cap[i]
  i2, h2 = cap[j]

  h = h1 + (i2 - i1).abs

  h <= h2 ? cap[j][1] = h : (h + h2) / 2
end

def max_building(n, cap)
  cap.concat [[1, 0], [n, n - 1]]
  cap.sort!
  size = cap.size

  0.upto(size - 2).map { |i| get_max_height(cap, i, i + 1) }
  (size - 1).downto(1).map { |i| get_max_height(cap, i, i - 1) }.max
end
```
