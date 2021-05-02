n, m = map(int, input().split())
a = [0 for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

dp = [[0 for i in range(n + 1)] for i in range(n + 1)]


m_list = []
for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + a[i][j]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))
