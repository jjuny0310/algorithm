import heapq

n, l = map(int, input().split())
arr = list(map(int, input().split()))

hq = []
answer = []
for i in range(n):
    heapq.heappush(hq, (arr[i], i))

    while hq:
        now, idx = heapq.heappop(hq)
        if i - l + 1 <= idx <= i:
            answer.append(now)
            heapq.heappush(hq, (now, idx))
            break

print(" ".join(map(str, answer)))