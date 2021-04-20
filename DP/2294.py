n, k = map(int, (input().split()))
coins = []
INT = 100001
dp = [INT for i in range(100001)]
for i in range(n):
    coins.append(int(input()))
    dp[coins[i]] = 1

for coin in coins:
    for i in range(1, k+1):
        if i-coin>=0:
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == INT:
    print(-1)
else:
    print(dp[k])