N = int(input())
A = list(map(int, input().split()))
dp = [0 for i in range(N+1)]
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
order = max(dp)
print(order)
sequences = []
for i in range(N-1, -1, -1):
    if dp[i] == order:
        sequences.append(A[i])
        order -=1

sequences.reverse()
print(*sequences)