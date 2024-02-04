import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[a] = b
    else:
        parents[b] = a


n, m = map(int, input().split())

parents = [i for i in range(n)]
answer = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())

    if find(a) == find(b):
        cycle = True
        answer = i
        break
    else:
        union(a, b)

if answer:
    print(answer)
else:
    print(0)