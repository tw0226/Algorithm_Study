n = int(input())
dp = [0 for x in range(n+1)]
rect =[0 for x in range(n+1)]
dp[0],dp[1] = 1, 1
rect[0] = dp[0]*4
rect[1] = dp[0]*2 +2*(dp[1]+dp[0])
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    rect[i] = 2*(dp[i]+dp[i-1])+2*dp[i]

print(rect[n-1])