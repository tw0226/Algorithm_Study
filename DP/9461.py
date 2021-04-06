n = int(input())
dp = [0 for i in range(101)]
dp[0], dp[1], dp[2] = 1, 1, 1
for i in range(3, 101):
	dp[i] = dp[i-2] + dp[i-3]
for _ in range(n):
	a = int(input())
	print(dp[a-1])
