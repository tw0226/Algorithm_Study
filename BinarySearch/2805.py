# 떠오르는 방법 1 : BruteForce로 최댓값부터 하나씩 줄여가면서 진행하기 => 시간초과로 에러뜸
# 떠오르는 방법 2 : 입력된 나무들의 중간값으로부터 이진탐색하면서 M보다 작으면 return, M보다 크면 재귀 진행
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 방법 1
'''
max_height = max(trees)
availables = 0
for h in range(max_height, 0, -1):
    sum_mod = 0
    for tree in trees:
        if tree >= h:
            sum_mod += tree - h
    if sum_mod >= M:
        if h > availables:
            availables = h
print(availables)
'''
# 방법 2
start, end = 1, max(trees)

while start <= end:
    mid = (start+end) //2
    _sum = 0
    for tree in trees:
        if tree >= mid:
            _sum += tree - mid
    if _sum >= M:
        start = mid +1
    else:
        end = mid -1
print(end)