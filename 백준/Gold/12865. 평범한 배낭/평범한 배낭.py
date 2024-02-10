n, k = map(int, input().split())

w_list = [0]
v_list = [0]
for i in range(n):
    w, v = map(int, input().split())
    w_list.append(w)
    v_list.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j - w_list[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w_list[i]] + v_list[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])