import sys
import heapq

t = int(input())
results = []
for _ in range(t):
    m = int(sys.stdin.readline().strip())
    k = (m//10)+1
    
    left_hq = []
    right_hq = []
    median = None

    result = []

    count = 1
    for _ in range(k):
        for num in list(map(int, sys.stdin.readline().split())):
            if median is None:
                median = num
            else:
                if num >= median:
                    # 왼쪽 최대힙에 넣기
                    heapq.heappush(right_hq, num)
                else:
                    heapq.heappush(left_hq, -num)
                    # 오른쪽 최소힙에 넣기
            if count % 2 == 1:
                if len(left_hq) > len(right_hq):
                    heapq.heappush(right_hq, median)
                    median = -heapq.heappop(left_hq)
                elif len(right_hq) > len(left_hq):
                    heapq.heappush(left_hq, -median)
                    median = heapq.heappop(right_hq)
                result.append(median)
            count += 1
    results.append(result)

for r in results:
    print(len(r), end='')
    for i in range(len(r)):
        if i % 10 == 0:
            print()
        print(r[i], end=' ')
    print()