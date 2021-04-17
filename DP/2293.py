n, k = map(int, input().split())
dp = [0 for i in range(k+1)]
coin = []
for i in range(n):
    coin.append(int(input()))
    dp[coin[i]] = 1
print(dp)
for i in range(1, k+1):
    for j in range(n):
        if i-coin[j]>=0:
            dp[i]+=dp[i-j]

