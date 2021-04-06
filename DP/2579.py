n = int(input())
s = []
dp = [0 for x in range(n+1)]
for i in range(n):
	s.append(int(input()))


dp[0] = s[0]
if n>1:
	dp[1] = s[0]+s[1]
elif n>2:
	dp[2] = max(s[1]+s[2], s[0]+s[2])
for i in range(3, n):
	dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])
print(dp[n-1])
