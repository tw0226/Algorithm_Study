n = int(input())
dp = [0 for i in range(n+1)]
t, p = [], []
for i in range(n):
	a ,b = list(map(int, input().split()))
	t.append(a)
	p.append(b)
for i in range(n):
print(max(dp))
