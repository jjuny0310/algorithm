import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))

hq = []
for i in range(n):
    heapq.heappush(hq, cards[i])

for i in range(m):
    v1 = heapq.heappop(hq)
    v2 = heapq.heappop(hq)
    heapq.heappush(hq, v1 + v2)
    heapq.heappush(hq, v1 + v2)

print(sum(hq))