import heapq as pq

class Solution:
    def assignTasks(self, S, T):
        busy = []
        free = [[w, i, 0] for i, w in enumerate(S)]
        pq.heapify(free)
        now = 0
        ret = []
        for i, t in enumerate(T):
            while busy and busy[0][0] <= now:
                st, w, i = pq.heappop(busy)
                pq.heappush(free, [w, i, st])
            w, i, st = pq.heappop(free)
            ret.append(i)
            pq.heappush(busy, [now + t, w, i])
            now += 1
            if not free:
                now = busy[0][0]

        return ret
