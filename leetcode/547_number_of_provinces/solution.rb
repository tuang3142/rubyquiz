def find_circle_num(is_connected)
  def find(i):
    root[i] = find(root[i]) if i != root[i]

    root[i]
  end

  def union(i, j)
    root[find(i)] = find(j)
  end
  n = is_connected.length
  root = Array (0..n-1)
end


class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        root = [i for i in range(n)]
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]
        def union(i, j):
            root[find(i)] = find(j)
        
        for a in range(n):
            for b in range(n):
                c = isConnected[a][b]
                if c:
                    union(a, b)
        return sum([find(i) == i for i in range(n)])
