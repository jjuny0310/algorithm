from itertools import permutations

n, k = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for l in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][l] + graph[l][b])

cases = permutations([i for i in range(n)], n)
answer = 1e9
for case in cases:
    if case[0] != k:
        continue

    cur = k
    dist = 0
    for i in case:
        if i == k:
            continue
        dist += graph[cur][i]
        if dist >= answer:
            break
        cur = i
    answer = min(answer, dist)
print(answer)