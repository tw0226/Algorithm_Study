n, k = map(int , input().split())
dp = [0 for i in range(n)]
for i in range(n):
    dp[i] = [0 for x in range(i+1)]
    dp[i][0] = 1
    dp[i][len(dp[i])-1]=1
dp[0][0] =1

for i in range(1, n):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j]

print(dp[n-1][k-1])