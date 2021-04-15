x = input()
y = input()
n = len(x)+1
dp = [0 for i in range(n)]

for i in range(len(x)):
	for j in range(i, len(y)):
		if x[i]==y[j]:
			dp[i]+=1
print(dp)
			
