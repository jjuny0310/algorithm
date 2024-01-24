n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    if i % 2 == 0:
        # 짝수일 때
        dp[i] = dp[i - 1] + dp[i//2]
    else:
        # 홀수일 때
        dp[i] = dp[i - 1]

print(dp[n] % 1_000_000_000)