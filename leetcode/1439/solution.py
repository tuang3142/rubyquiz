from heapq import heappush as push
from heapq import heappop as pop
from heapq import heapify

class Solution:
    def kthSmallest(self, M, k):
        n, m = len(M), len(M[0])
        init_j = [0] * n
        init_sum = sum([i[0] for i in M])
        qu = [[init_sum, init_j]]
        seen = [self.make_key(init_j)]

        for _ in range(1, k):
            now_sum, now_id = pop(qu)
            for i in range(n):
                next_id = [v for v in now_id]
                next_id[i] += 1
                key = self.make_key(next_id)
                if next_id[i] >= m or key in seen:
                    continue
                seen.append(key)
                j = next_id[i]
                next_sum = now_sum + M[i][j] - M[i][j-1]
                push(qu, [next_sum, next_id])

        ret, _ = pop(qu)
        return ret

    def make_key(self, arr):
        return ",".join([str(v) for v in arr])
