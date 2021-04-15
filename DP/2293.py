n, k = map(int, input().split())
dp = [0 for i in range(k+1)]
coin = []
for i in range(n):
	coin.append(int(input()))
dp[0]=1

for j in coin:
	for i in range(1, k+1):
		if i-j>=0:
			dp[i] += dp[i-j]
print(dp[n])
