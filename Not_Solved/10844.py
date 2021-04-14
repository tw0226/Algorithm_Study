n = int(input())
dp = [0 for i in range(n+2)]
for i in range(n+2):
    dp[i] = [0 for i in range(10)]
dp[1] = [0] + [1 for i in range(9)]
# dp[2] =  10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 89 98
# dp[3] = 987 989   # 876 878 890 898
# dp[4] = 9876 9878 9898
# dp[5] = 98765 98767 98787 98789 98987 98989
for i in range(1, n+1):
    for j in range(9, 0, -1):
        if i+j>=10 or i>j:
            dp[i+1][j] = dp[i][j]+1
        else:
            dp[i+1][j] = dp[i][j]*2
    print(dp[i], sum(dp[i]))