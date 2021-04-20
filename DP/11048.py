n, m = map(int, input().split())
dp = [[0]*(m+1) for i in range(n+1)]
maze = [0 for i in range(n)]
for i in range(n):
    maze[i] = list(map(int, input().split()))
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = maze[i-1][j-1]+max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
print(dp[n][m])