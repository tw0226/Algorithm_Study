import sys
from collections import deque
input = sys.stdin.readline

nx = [-1, -1, -1, 0, 0, 1, 1, 1]
ny = [-1, 0, 1, -1, 1, -1 ,0, 1]

def bfs(x, y, w, h, tile):
    queue = deque()
    queue.append((x, y))
    tile[x][y] = -1
    while queue:
        cx, cy = queue.popleft()
        for i in range(8):
            dx = cx + nx[i]
            dy = cy + ny[i]
            if dx <0 or dx >= w or dy < 0 or dy >= h:
                continue
            if tile[dx][dy] == 1:
                tile[dx][dy] = -1
                queue.append((dx, dy))
    return tile

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    tile = [[0 for _ in range(w)] for _ in range(h)]
    count = 0
    for i in range(h):
        tile[i] = list(map(int, input().split()))
    for i in range(h):
        for j in range(w):
            if tile[i][j] != 1:
                continue
            tile = bfs(i, j, h, w, tile)
            count += 1
    print(count)