n = int(input())
dp = [[0]*(n+1) for i in range(n+1)]
# dp2 = [[0]*(n+1) for i in range(n+1)]
a = list(map(int, input().split()))
for i in range(1, n+1):
    for j in range(1, n+1):
        if a[j-1] > a[i-1]:
            dp[i][j] = dp[i-1][j]+1
        if a[j-1] < a[i-1]:
            dp[i][j] = dp[i-1][j]+1
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(i, dp[i])
