# LIS + 이분탐색 문제
# 0번을 일단 넣고, 0번 값보다 크면 append, 작으면 값을 인덱스 찾아 바꿔치기
import bisect
n = int(input())
p = list(map(int, input().split()))

lis = [p[0]]

for i in range(n):
    idx = lis[-1]
    if p[i] > idx:
        lis.append(p[i])
    else:
        left = bisect.bisect_left(lis, p[i])
        lis[left] = p[i]

print(len(lis))