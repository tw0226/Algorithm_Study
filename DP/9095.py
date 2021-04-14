T = int(input())
dp = [0 for i in range(11)]
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in range(T):
    n = int(input())
    print(dp[n-1])