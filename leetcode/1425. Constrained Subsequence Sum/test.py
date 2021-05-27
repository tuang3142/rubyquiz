import heapq
import random

n = 100
h = []

for _ in range(n):
    heapq.heappush(h, random.randrange(n))

for _ in range(n):
    heapq.heappush(h, random.randrange(n))
    if h[0] != heapq.heappop(h):
        print("break")

print(h)
print("true")
