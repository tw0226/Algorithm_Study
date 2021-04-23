n = int(input())
dp = [0 for _ in range(n+1)]
items = []
b = []
for _ in range(n):
    items.append(list(map(int, input().split())))
items = sorted(items, key=lambda x: x[0])

for i in items:
    b.append(i[1])
print(b)
for i in range(n):
    for j in range(i):
        if b[i] > b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] +=1
print(dp)
print(n - max(dp))