n = int(input())
for i in range(n):
    j = int(input())
    a = sorted(list(map(int, input().split())))
    dp = [0 for x in range(j+1)]
    dp[0] = a[0]
    print(a)
    for k in range(1, j+1):
        dp[k] += min(dp[k-1]+a[k], sum(a[k:k+2]))
        print(dp)
    # print(sum(dp))