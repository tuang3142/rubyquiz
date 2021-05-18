*This solution is implemented in python because binary search tree (BST) is not (yet) supported for ruby*

### Idea

Sort the two arrays by the size of the room. With each query, we chose a handful of rooms that meet the size requirement and store their ids in the array `room_ids`.
Now we just need a way to meet the id requirement. This is where BST is used for. `room_ids` is essentially a balanced BST that has insertion operation in `O(log(n))` time while maintaining the order of the ids. This way we can quickly find the satisfied id with binary search in `O(log(n))` as well.

### Complexity

- Time: `O(n * log(n))`
- Space: `O(n)`

### Code

```python
from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms, q):
      def find(tree_map, condition):
        p = tree_map.bisect_right(condition)
        ret = []
        if p > 0:
          ret.append(tree_map[p - 1])
        if p < len(tree_map):
          ret.append(tree_map[p])
        if not ret: return -1
        return min(ret, key=lambda x: abs(condition - x))

      rooms.sort(key=lambda x: x[1])
      ans = [-1] * len(q)
      tree_map = SortedList()
      q = [[i, prefer_id, min_size] for i, (prefer_id, min_size) in enumerate(q)]
      q.sort(key=lambda x: x[2], reverse=True)
      for i, prefer_id, min_size in q:
        while rooms and rooms[-1][1] >= min_size:
          tree_map.add(rooms[-1][0]) # add the id
          rooms.pop()
        ans[i] = find(tree_map, prefer_id)
      return ans
```
