# 슬라이딩 윈도우 개념을 이용하면 연산량을 줄일 수 있다
N, K = map(int, input().split())
arr = list(map(int, input().split()))
total = sum(arr[:K])
part_total =total
idx = N//2
for i in range(N-K):
    part_total += arr[i+K] - arr[i]
    if total < part_total:
        total = part_total
print(total)