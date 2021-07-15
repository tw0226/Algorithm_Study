N, S, M = map(int, input().split())
V = list(map(int, input().split()))
dp = [[False for j in range(M+1)] for i in range(N+1)]

for i in range(N+1):
    dp[i] = [False] * (M+1)

dp[0][S] = True

for i in range(N):
    for j in range(M+1):
        check = dp[i][j]
        if check:
            if j + V[i] <= M:
                dp[i+1][j + V[i]] = True
            if j - V[i] >= 0:
                dp[i+1][j - V[i]] = True

result = -1
for i in range(M+1):
    if dp[N][i]:
        result = i
print(result)