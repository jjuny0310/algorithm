import sys
input = sys.stdin.readline


n = int(input().rstrip())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

answer = 0
stack = []
for x, y in points:
    while stack and stack[-1] > y:
        stack.pop()
        answer += 1

    if stack and stack[-1] == y:
        continue

    if y != 0:
        stack.append(y)

print(len(stack) + answer)