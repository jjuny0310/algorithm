from collections import deque


def solve(start, target):
    queue = deque()
    queue.append((start, 0))

    while queue:
        now, dist = queue.popleft()

        if now > MAX_VALUE:
            continue

        if now == target:
            return dist

        for i in range(2):
            _next = 0
            if i == 0:
                _next = now * 2
            else:
                _next = now * 10 + 1

            queue.append((_next, dist + 1))

    return -1


a, b = map(int, input().split())

MAX_VALUE = int(1E9)
answer = solve(a, b)

if answer == -1:
    print(answer)
else:
    print(answer + 1)