# 방법1) NxN 을 1차원으로 변환해서 풀려고 하니까 안 됐음
# 위에 대로 하면 이분탐색을 해도 N^2logN^2 가 되기도 하고, 배열 자체가 N: 1e5 면 1e10 으로 오버플로가 발생
# 방법2) 2차원 기준으로 행을 한번 검색 후, 열에서 찾는 방식으로 가야 시간이 이분탐색 2번이라 2*(NlogN) 으로 줄어들 것 같다 => 구현을 못했음..
# 몰랐던 점) b[K] 라는 값이 N x N 보다 작은 값의 갯수와 같다고 할 수 있으니, 행 기준으로 먼저 찾고, 그다음 열에 대해서 탐색하면 되더라..
# 궁금했던 점) end가 왜 K일까? N^2로 하면 안되나? => 된다
# 링크 참고 : https://claude-u.tistory.com/449
n = int(input())
k = int(input())
start, end = 1, n**2
result = 0 
while start <= end:
    mid = (start+end)//2
    count = 0
    for i in range(1, n+1):
        count += min(n, mid//i)
    if count < k:
        start = mid+1
    else:
        result = mid
        end = mid-1
print(result)