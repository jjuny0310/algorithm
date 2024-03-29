import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dp_solve(now):
    for node in graph[now]:
        if not visited[node]:
            visited[node] = True
            dp_solve(node)
            dp[now][0] += max(dp[node][0], dp[node][1])
            dp[now][1] += dp[node][0]


n = int(input().rstrip())
citizen = [-1] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, citizen[i]] * 2 for i in range(n + 1)]
visited = [False] * (n + 1)
visited[1] = True
dp_solve(1)
print(max(dp[1]))