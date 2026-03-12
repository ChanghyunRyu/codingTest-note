import sys
import heapq

n = int(input())
h = []

for _ in range(n):
    for num in map(int, sys.stdin.readline().split()):
        heapq.heappush(h, num)
        if len(h) > n:
            heapq.heappop(h)

print(heapq.heappop(h))
