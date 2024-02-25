import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dp_solve(now):
    visited[now] = True
    for node in graph[now]:
        if not visited[node]:
            dp_solve(node)
            dp[now][0] += max(dp[node][0], dp[node][1])
            dp[now][1] += dp[node][0]


n = int(input().rstrip())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
dp = [[0, 1] for _ in range(n + 1)]

dp_solve(1)
print(n - max(dp[1]))