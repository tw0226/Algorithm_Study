n = int(input())
a = list(map(int, input().split()))
dp = [1 for i in range(n+1)]
for i in range(n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j]+1)
        print(i,j,dp)
print(max(dp))
# 다시 풀기