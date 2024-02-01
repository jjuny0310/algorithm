def solve(w, h):
    if cache[w][h] != -1:
        return cache[w][h]

    if w == 0 and h == 0:
        return 1

    if w > 0 and h > 0:
        cache[w][h] = solve(w - 1, h + 1) + solve(w, h - 1)
        return cache[w][h]

    elif w > 0 and h == 0:
        cache[w][h] = solve(w - 1, h + 1)
        return cache[w][h]

    elif w == 0 and h > 0:
        cache[w][h] = solve(w, h - 1)
        return cache[w][h]


cache = [[-1 for _ in range(31)] for _ in range(31)]
solve(30, 0)

while True:
    n = int(input())
    if n == 0:
        break
    print(cache[n][0])