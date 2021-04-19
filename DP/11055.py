n = int(input())
a = list(map(int, input().split()))
dp = [x for x in a]
# dp[0] = [a[0]] * (n+1)
# print(dp[0])
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i] = max(dp[i], dp[j]+a[i])
        print(dp)

# 다시 풀어보기