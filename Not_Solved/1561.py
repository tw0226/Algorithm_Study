# 어떻게 풀까?
# 1) DP 같은 곳에다가 누적합으로 쌓게 만들고, 이분탐색으로 누적합이 N이 되는 지점 찾기

import sys
n, m =  map(int, input().split())
p = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(m+1)]

for i in p:
    for j in range(1, 10000, i):
        dp[j] += dp[j-i] + 1

start, end = 1, 2e9
while start < end:
    mid = (start+end)//2
    