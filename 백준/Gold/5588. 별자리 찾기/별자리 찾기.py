m = int(input())

left_graph = []
for i in range(m):
    x, y = map(int, input().split())
    left_graph.append((x, y))

n = int(input())

right_graph = set()
for i in range(n):
    x, y = map(int, input().split())
    right_graph.add((x, y))

now_x, now_y = left_graph[0]
answer = [0, 0]
for r_x, r_y in right_graph:
    dx = r_x - now_x
    dy = r_y - now_y

    for l_x, l_y in left_graph:
        nx = l_x + dx
        ny = l_y + dy
        if (nx, ny) not in right_graph:
            break
    else:
        answer = [dx, dy]
        break

print(answer[0], answer[1])