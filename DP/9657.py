n = int(input())
dp = [0 for i in range(1001)]
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1

for i in range(5, 1001):
    dp[i] = 0 if dp[i-1] == 1 and dp[i-3] == 1 and dp[i-4] ==1 else 1
print("SK") if dp[n]==1 else print("CY")