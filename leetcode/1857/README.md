[Link to the problem](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/submissions/)

### Idea

[Thanks lzl124631x for the original solution](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/discuss/1198658/C%2B%2B-Topological-Sort)

We do normal topo sort. The catch here is to use BFS and make sure that a node is visited only when all of its parents (node that directs to it) are visited. In the code below, we use the array `in_degree` for that purpose and only visit a node `u` if `in_degree[u] == 0`. This way, we can compare all the incoming result and update acordingly for the current node.

For each node `u`, we have `cnt[u][i]` which is the maximum count of color `i` in all paths that ends up at node `u`

If there is a cycle in the graph, we would not visit a node in that cycle at all since the `in_degree` of them woule never be 0. We use this inuiton to detect cycle.

### Complexity

- Time & Space: O(n)

### Code

```ruby
def largest_path_value(color, edges)
  color = color.split("").map { |c| c.ord - "a".ord }
  n = color.size
  graph = 0.upto(n - 1).map { [] }
  in_degree = [0] * n

  edges.each do |u, v|
    graph[u] << v
    in_degree[v] += 1
  end

  qu = []
  cnt = 0.upto(n - 1).map { [0] * 26 }
  0.upto(n - 1) do |u|
    next if in_degree[u] != 0

    qu.push(u)
    cnt[u][color[u]] = 1
  end

  ret, seen = 0, 0
  until qu.empty?
    u = qu.shift
    ret = [ret, cnt[u][color[u]]].max
    seen += 1

    graph[u].each do |v|
      0.upto 25 do |i|
        add = i == color[v] ? 1 : 0
        cnt[v][i] = [cnt[v][i], cnt[u][i] + add].max
      end
      qu << v if (in_degree[v] -= 1).zero?
    end
  end

  seen < n ? -1 : ret
end
```
