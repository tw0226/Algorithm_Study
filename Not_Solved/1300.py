# 1차원으로 변환해서 풀려고 하니까 안 됐음
# 위에 대로 하면 N^2logN^2 가 되서 N: 1e5 면 1e10 으로 오버플로가 발생한다.
# 2차원 기준으로 행을 한번 검색 후, 열에서 찾는 방식으로 가야 시간이 이분탐색 2번이라 2*(NlogN) 으로 줄어든다.
n = int(input())
k = int(input())
# b = [i*j for j in range(1, n+1) for i in range(1, n+1)]

# b = sorted(b)
start, end = 1, k 
result = 0
while start <= end:
    mid = (start+end)//2
    value = 0
    print(start, mid, end, value)
    for i in range(1, n+1):
        value += min(mid//i, n)
    if value >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)