n = int(input())
dp = [0 for i in range(n+1)]
t, p = [], []
for i in range(n):
	a ,b = list(map(int, input().split()))
	t.append(a)
	p.append(b)
for i in range(n-1, -1, -1):
	if t[i]+i > n:
		dp[i] = dp[i+1]
	else:
		dp[i] = max(dp[i+1], dp[i+t[i]]+ p[i])
	# print(dp)
print(max(dp))
