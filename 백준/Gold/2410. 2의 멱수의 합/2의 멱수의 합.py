n = int(input())

coins = []
idx = 0
while True:
    if 1 << idx > n:
        break
    coins.append(1 << idx)
    idx += 1

mod = 1_000_000_000
dp = [0] * (n + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, n + 1):
        dp[i] = (dp[i] + dp[i - coin]) % mod

print(dp[n])