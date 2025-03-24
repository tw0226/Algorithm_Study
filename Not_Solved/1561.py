# 어떻게 풀까?
# 1) DP 같은 곳에다가 누적합으로 쌓게 만들고, 이분탐색으로 누적합이 N이 되는 지점 찾기 ?? => 문제 이해가 잘 안됌

import sys
n, m =  map(int, input().split())
p = list(map(int, sys.stdin.readline().split()))

if n<m:
    print(n)
else:
    start, end = 1, 2e9
    total = 0
    while start <= end:
        mid = (start+end)//2
        count = m
        for i in range(m):
            count += mid//p[i]
        if count >= n:
            total = mid
            end = mid -1
        else:
            start = mid +1
        
        count = m
        for i in range(m):
            count += (total-1)//p[i]
        
        for i in range(m):
            if total % p[i] == 0:
                count += 1
            if count == n:
                print(i+1)
                break