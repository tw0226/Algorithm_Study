import sys
from collections import deque
input = sys.stdin.readline

nx = [-1, -1, -1, 0, 0, 1, 1, 1]
ny = [-1, 0, 1, -1, 1, -1 ,0, 1]

def bfs(x, y, w, h, tile):
    queue = deque()
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(8):
            dx = cx + nx[i]
            dy = cy + ny[i]
            if dx<0 or dx >= w or dy < 0 or dy > h:
                continue
            if tile[cx][cy] == 1 and tile[dx][dy] == 1:
                tile[cx][cy] = -1
                queue.append((dx, dy))

while True:
    w,h = input().split()
    if w == 0 and h == 0:
        break
    tile = [0 for i in range(h) for i in range(w)]
    count = 0
    for i in range(h):
        tile[i] = list(map(int, input().split()))
    for i in range(w):
        for j in range(h):
            if tile[i][j] != 1:
                continue
            bfs(i, j, w, h, tile)
            count += 1
    print(count)