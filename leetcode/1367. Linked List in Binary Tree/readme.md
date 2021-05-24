[Link to the problem statement](https://leetcode.com/problems/linked-list-in-binary-tree/)

### Idea

This solution is similar to finding a pattern in a string.
Naturally, the brute force solution comes up and it is acceptable.
However, just like finding a string pattern, we can use the KMP algorithm to produce a faster solution.

### Code

```python
class Solution:
    def isSubPath(self, head, root):
        arr, lps = self.convert_to_array(head)
        def visit(node, i):
            if i >= len(arr): return True
            if not node: return False
            if node.val == arr[i]:
                return(visit(node.left, i + 1) or visit(node.right, i + 1))
            if i > 0:
                return visit(node, lps[i - 1])
            return visit(node.left, 0) or visit(node.right, 0)

        return visit(root, 0)

    def convert_to_array(self, node):
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        lps = [0] * len(arr)
        i, j = 1, 0
        while i < len(arr):
            if arr[i] == arr[j]:
                lps[i] = j + 1
                i, j = i + 1, j + 1
            else:
                if j > 0: j = lps[j - 1]
                else: i += 1
        return arr, lps
```
