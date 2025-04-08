# 공유기 간 최대 거리 만들기
import sys
input = sys.stdin.readline
n, c = map(int, (input().split()))
x = [0 for i in range(n+1)]
node = []
for i in range(n):
    h = input()
    node.append(h)
    x[h] = 1
sorted(node)

start, end = 0, n
count = c-2
dist = max(node) - min(node)
while start<=end:
    mid = (start+end)//2
    if node[mid] == 0:
        continue
    elif node[mid] - node[start] < dist:
        dist = node[mid]-node[start]
        end = mid -1
    elif node[end] - node[mid] < dist:
        dist = node[end] - node[mid]
        start = mid +1