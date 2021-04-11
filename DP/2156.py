n = int(input())
dp = [0]
p = [0]
for i in range(n):
    p.append(int(input()))
dp.append(p[1])
if n>1:
    dp.append(p[1]+p[2])
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3] + p[i-1] + p[i], dp[i-2] + p[i]))
print(dp[n])