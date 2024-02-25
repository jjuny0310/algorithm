import sys
sys.setrecursionlimit(10 ** 8)


def dp_solve(graph, now, visited, dp):
    visited[now] = True
    for node in graph[now]:
        if not visited[node]:
            dp_solve(graph, node, visited, dp)
            dp[now][0] += max(dp[node])
            dp[now][1] += dp[node][0]
    

def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)]
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n + 1)
    dp = [[0, 1] for _ in range(n + 1)]
    dp_solve(graph, 1, visited, dp)
    
    return n - max(dp[1])