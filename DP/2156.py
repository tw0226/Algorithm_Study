n = int(input())
p = []
dp = [0 for i in range(n+1)]
for i in range(n+1):
    dp[i] = [0 for x in range(3)]
for i in range(n):
    p.append(int(input()))
dp[0][0] = p[0]
dp[1][0] = p[1]+p[0]
dp[1][1] = p[1]
dp[1][2] = p[1]
dp[2][0] = p[0]+p[1]
dp[2][1] = p[1]+p[2]
dp[2][2] = p[2]+p[0]
for i in range(3, n):
    print(i)
    if i%3!=0:
        dp[i][0] = dp[i-2][0] + p[i-1]
    if i%3!=1:
        dp[i][1] = dp[i-1][1] + p[i]
    if i%3!=2:
        dp[i][2] = dp[i-2][2] + p[i]
    # dp[i] = max(dp[i])
    print(dp)