from heapq import heappush as push
from heapq import heappop as pop
from heapq import heapify

class Solution:
    def kthSmallest(self, mat, k):
        M = [sorted(row) for row in mat]
        n, m = len(M), len(M[0])
        ret = sum([M[i][0] for i in range(n)])
        if m == 1: return ret

        qu = [(M[i][1] - M[i][0], i) for i in range(n)]
        heapify(qu)
        current_index = [1] * n
        for _ in range(1, k):
            # print(qu)
            diff, i = pop(qu)
            ret += diff
            print(i, current_index[i])
            current_index[i] += 1
            j = current_index[i]
            if j == m: continue
            diff = M[i][j] - M[i][j-1]
            push(qu, (diff, i))
        return ret
