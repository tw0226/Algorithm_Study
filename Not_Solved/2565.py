n = int(input())
lines = []
for i in range(n):
    x, y = map(int, input().split())
    lines.append([x, y])
lines.sort()
dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] +1)
print(n-max(dp))