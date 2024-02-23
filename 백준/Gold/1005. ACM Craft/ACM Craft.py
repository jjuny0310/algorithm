from collections import deque
import sys

input = sys.stdin.readline


def topology_sort(graph, in_degree, build_time):
    queue = deque()

    for i in range(1, len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)

    res = build_time.copy()
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            res[i] = max(res[i], res[now] + build_time[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

    return res


t = int(input().rstrip())

for _ in range(t):
    n, k = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for i in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    w = int(input())
    answer = topology_sort(graph, in_degree, build_time)
    print(answer[w])