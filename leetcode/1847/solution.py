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
