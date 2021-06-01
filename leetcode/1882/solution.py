import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        busy = []
        free = [[0, w, i] for servers] # server_time, weight, index
        heapq.heapify(free)
        ret = []
        for now, process_time in enumerate(tasks):
            while busy and (busy[0][0] <= now or not free): # check for servers that finish their tasks
                st, w, i = heapq.heappop(busy)              # or pop anyway if there are no free servers
                if st <= now: st = 0 # equalize all free servers' times to prioritize by their weights later
                heapq.heappush(free, [st, w, i])
            st, w, i = heapq.heappop(free)
            ret.append(i)
            heapq.heappush(busy, [max(st, now) + process_time, w, i])
        return ret
