import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        busy = []
        free = [[0, w, i] for servers]
        heapq.heapify(free)
        ret = []
        for now, process_time in enumerate(tasks):
            while busy and (busy[0][0] <= now or not free):
                st, w, i = heapq.heappop(busy)
                if st <= now: st = 0
                heapq.heappush(free, [st, w, i])
            st, w, i = heapq.heappop(free)
            ret.append(i)
            heapq.heappush(busy, [max(st, now) + process_time, w, i])
        return ret
