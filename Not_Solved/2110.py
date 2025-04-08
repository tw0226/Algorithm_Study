# 공유기 간 최대 거리 만들기
import sys
input = sys.stdin.readline
n, c = map(int, (input().split()))
node = [0]
for i in range(n):
    node.append(int(input()))
node = sorted(node)

left, right = 1, n
count = c-2
max_dist = 0

while left<right and count != 0:
    mid = (left+right)//2
    left_dist = node[mid] - node[left]
    right_dist = node[right] - node[mid]
    curr_max_dist = min(left_dist, right_dist)
    if max_dist < curr_max_dist:
        max_dist = curr_max_dist
        count -= 1
        print(mid)
    
    print(left, right, mid, left_dist, right_dist, max_dist, curr_max_dist)
    if left_dist < right_dist:
        right = mid -1
    else:
        left = mid + 1
    
print(max_dist)