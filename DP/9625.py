n = int(input())
dp = [x for x in range(n+1)]
dp[0]=0
dp[1]=1
for i in range(2, n+1):
    dp[i] = dp[i-2]+dp[i-1]
print(dp[n-1], dp[n])