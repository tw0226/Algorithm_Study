n = int(input())
b = [0] + list(map(int, input().split()))
dp = [0 for i in range(n+1)]

for i in range(1, n+1):
    for j in range(i):
        if b[i] > b[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))