import bisect
n = int(input())
lines = list(map(int, input().split()))
lis = [lines[0]]
for i in range(n):
    curr = lines[i]
    local = lis[-1]
    if local < curr:
        lis.append(curr)
    else:
        left = bisect.bisect_left(lis, curr)
        lis[left] = curr
print(n-len(lis))