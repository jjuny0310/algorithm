import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def make_tree(now, parent):
    for child in graph[now]:
        if child != parent:
            tree[now].append(child)
            parents[child] = now
            make_tree(child, now)


def dp_solve(now):
    for child in tree[now]:
        dp[now] += dp_solve(child)

    return dp[now]


n, r, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

INF = int(1E9)
parents = [INF] * (n + 1)
tree = [[] for _ in range(n + 1)]

make_tree(r, -1)

dp = [1] * (n + 1)
dp_solve(r)

for i in range(q):
    u = int(input().rstrip())
    print(dp[u])