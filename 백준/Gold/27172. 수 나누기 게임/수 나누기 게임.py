n = int(input())
players = list(map(int, input().split()))

points = set(players)
max_point = max(players)
res = [0 for _ in range(max_point + 1)]
for i in range(n):
    j = 2
    while players[i] * j <= max_point:
        if players[i] * j in points:
            res[players[i] * j] -= 1
            res[players[i]] += 1
        j += 1

answer = []
for i in range(n):
    answer.append(res[players[i]])
print(" ".join(map(str, answer)))