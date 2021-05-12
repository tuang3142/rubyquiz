[Link to original problem](https://leetcode.com/problems/distinct-numbers-in-each-subarray/)

Given an integer array nums and an integer k, contrusct array ans of size n-k+1 where ans[i] is the number of distinct numbers in the subarray nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]].

```
*Input*: nums = [1,2,3,2,2,1,3], k = 3
*Output*: [3,2,2,2,3]
*Explanation*: The number of distinct elements in each subarray goes as follows:
- nums[0:2] = [1,2,3] so ans[0] = 3
- nums[1:3] = [2,3,2] so ans[1] = 2
- nums[2:4] = [3,2,2] so ans[2] = 2
- nums[3:5] = [2,2,1] so ans[3] = 2
- nums[4:6] = [2,1,3] so ans[4] = 3
```

**Idea**

This is the classic "sliding window" problem. Take the example: `[1,2,3,2,2,1,3]`.

- First, we construct a hash to count numbers of the first k numbers: `counter = { 1: 1, 2: 1, 3: 1 }`.
- Also, do note that `ans[0] = 3` since we have 3 distinct numbers in the first array.
- Loop thru the array, for each number from k to n, we maintain an array of size k: (initially, it equals to the first k numbers of the array: `[1, 2, 3]`)
  - add the new number to the array: `[1, 2, 3, 2]`
  - increase the counter of the new number: `counter[2] += 1`. if the number is not previously in the array, update `ans`
  - we want the array size to always equal k, then remove the first number: `[2, 3, 2]`
  - decrease the counter: `counter[1] -= 1`. if the number is no longer in the array, update `ans`

This is where the term "window" comes from. At this example below, we treat the array as a window and "slide" it from left to right:

```
[1, 2, 3], 2, 2, 1, 3
1, [2, 3, 2], 2, 1, 3
1, 2, [3, 2, 2], 1, 3
```

**Complexity**

- Time & Space: `O(n)`

**Code**
```ruby
def distinct_numbers(nums, k)
  n = nums.size
  dist = [0]
  counter = nums[0, k].each_with_object({}) do |v, counter|
    counter[v] = counter[v].to_i + 1
    dist[0] += 1 if counter[v] == 1
  end

  k.upto(n-1) do |i|
    first = nums[i - k]
    last = nums[i]
    dist << dist[-1]
    dist[-1] += 1 if (counter[last] = counter[last].to_i + 1) == 1
    dist[-1] -= 1 if (counter[first] -= 1) == 0
  end

  dist
end
```
