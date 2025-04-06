import bisect
N = int(input())
A = list(map(int, input().split()))
curr = [A[0]]
for i in range(N):
    if A[i] > curr[-1]:
        curr.append(A[i])
    else:
        left = bisect.bisect_left(curr, A[i])
        curr[left] = A[i]
print(len(curr))