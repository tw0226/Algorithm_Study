import itertools

N = int(input())
A = sorted(list(map(int, input().split())))
result = 0
arrs = itertools.permutations(A)
for arr in arrs:
    _max = 0
    for i in range(1, N):
        _max += abs(arr[i] - arr[i-1])
    if _max >= result:
        result = _max
print(result)