import sys
import math

input = sys.stdin.readline
n, m = map(int, input().split())

datas = []
for i in range(m):
    datas.append(int(input().rstrip()))

start = 1
end = max(datas)
answer = 0
while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(len(datas)):
        count += math.ceil(datas[i] / mid)

    if count <= n:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)