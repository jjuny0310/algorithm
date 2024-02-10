from collections import deque


def bfs(start):
    queue = deque()
    queue.append((start, 0, {start}))

    res = 1e9
    while queue:
        now, dist, visited = queue.popleft()
        if res <= dist:
            continue

        if len(visited) == n:
            res = min(res, dist)
            continue

        for _next in range(n):
            if now == _next:
                continue

            if _next not in visited:
                queue.append((_next, dist + graph[now][_next], visited.union({_next})))
    return res


n, k = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for l in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][l] + graph[l][b])

answer = bfs(k)
print(answer)