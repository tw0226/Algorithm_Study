n=int(input())
dp = [0 for i in range(31)]
dp[1] = 0
dp[2] = 3
dp[3] = 0
for i in range(4, n+1):
    if i*3%2==1:
        dp[i]=0
    else:
        dp[i] = dp[i - 2] * 3 +2
        for j in range(i-4, -1, -2):
             dp[i] += dp[j]*2
print(dp[n])