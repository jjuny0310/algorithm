import heapq

def dijkstra(graph, start, distance):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    
    while hq:
        dist, now = heapq.heappop(hq)
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))


def solution(n, roads, sources, destination):
    INF = int(1E9)
    
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    distance = [INF] * (n + 1)
    dijkstra(graph, destination, distance)
    
    answer = []
    for source in sources:
        if distance[source] >= INF:
            answer.append(-1)
        else:
            answer.append(distance[source])
    
    return answer