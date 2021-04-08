n = int(input())
up = [0 for i in range(n+1)]
down = [0 for i in range(n+1)]
s = [0] + list(map(int, input().split()))
dp = [0 for i in range(n+1)]

for i in range(1, n+1):
    if s[i] >= s[i-1]:
        up[i] += up[i-1]+1
    else:
        up[i]=1
    if s[i] <= s[i-1]:
        down[i] += down[i-1]+1
    else:
        down[i]=1
    dp[i] = max(down[i], up[i])

print(max(dp))