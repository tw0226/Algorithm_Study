# 문제 : N 개 중에서 작은 것과, 큰 것을 합쳤을 때 0에 가까운 숫자 2개 선정
# 어떻게 풀까?
# 1) sort 후 -X ~ +X 일테니 중간 기준으로 0 에 가까워지도록 0보다 크면 left 쪽으로, 0보다 작으면 right 쪽으로 쭉 탐색하면서 마지막까지 가기
# 1-1) min + right < min_value 라면 max1 = right
# 1-2) max + left < min_value 라면 min1 = left


# 놓친점 : 너무 어렵게 돌아간 느낌이다
# RESOLVE 필요..

N = int(input())
x = sorted(list(map(int, input().split())))
left, right = 0, N-1
min1, max1 = x[left], x[right]
min_value = abs(x[left] + x[right])
while left < right:
    left_value = x[left]
    right_value = x[right]
    total = left_value + right_value
    if abs(total) < min_value:
        min_value = abs(total)
        min1, max1 = x[left], x[right]
        if min_value== 0:
            break
    if total < 0:
        left +=1
    else:
        right -= 1
print(min1, max1)