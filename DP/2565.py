n = int(input())
A = []
for i in range(n):
    x,y = map(int, input().split())
    A.append([x,y])
A.sort()
dp = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if A[i][1] > A[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))