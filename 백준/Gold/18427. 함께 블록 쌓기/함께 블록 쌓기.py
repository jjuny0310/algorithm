n, m, h = map(int, input().split())

student = []
for i in range(n):
    student.append(list(map(int, input().split())))

dp = [[0] * (h + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, h + 1):
        for block in student[i - 1]:
            if j - block < 0:
                continue
            dp[i][j] += dp[i - 1][j - block]
        dp[i][j] += dp[i - 1][j]

print(dp[n][h] % 10007)