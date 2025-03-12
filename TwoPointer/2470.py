# 문제 : N 개 중에서 작은 것과, 큰 것을 합쳤을 때 0에 가까운 숫자 2개 선정
# 어떻게 풀까?
# 1) sort 후 -X ~ +X 일테니 중간 기준으로 0 에 가까워지도록 0보다 크면 left 쪽으로, 0보다 작으면 right 쪽으로 쭉 탐색하면서 마지막까지 가기
N = int(input())
x = sorted(list(map(int, input().split())))
left, right = 0, N-1
mid = (left + right) // 2
min1, max1 = x[left], x[right]
min_value = 1e9
print(x, mid)
while left != right:
    expect = x[left] + x[right]
    print(left, right, x[left], x[right], expect)
    if expect == 0:
        min1, max1 = x[left], x[right]
        break 
    if min1 + max1 < min1 + x[right]:
        max1 = min(max1, x[right])
        right -=1
    else:
        min1 = max(min1, x[left])
        left +=1
    
print(min1, max1)