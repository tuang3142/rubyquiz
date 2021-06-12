### tl;dr

[Link to problem statement.](https://leetcode.com/problems/minimum-space-wasted-from-packaging)


### Idea

Assume all the packages and factoies' boxes are sorted increasingly size-wise.  
For each box `box[i]`, in each factory, use binary search to find the number of packages it can covers.  
Let `k` is that number, box size used should be `box[i] * k`. Add it to `total_box_size`.  
Note that we can skip the packages that are covered by the previous, smaller box `box[i-1]`.  
In the end, the total waste for each factory should be: `total_waste = total_box_size - total_package_size`

### Complexity

let `m = total boxes, n = total packages`:
- time: `O(m * log(n))`
- space: `O(1)`
