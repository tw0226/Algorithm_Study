n = int(input())
m = int(input())
dp = [0 for i in range(n+1)]
dp[0]=dp[1]=1
for i in range(2, n+1):
    dp[i] = dp[i-1]+dp[i-2]

tmp = 0
case = 1
for i in range(m):
    a = int(input())
    case *= dp[a-tmp-1]
    tmp = a
case *= dp[n-tmp]
print(case)