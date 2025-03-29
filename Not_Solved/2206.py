

from collections import deque
n, m = map(int, input().split())
maze = [[] for i in range(n)]
for i in range(n):
    maze[i] = list(map(int, list(input())))

dx = [0, 0, +1, -1]
dy = [-1, +1, 0, 0]

visited = [[0 for i in range(m)] for i in range(n)]
visited[0][0] = 1
queue = deque()
queue.append((0, 0))
queue2 = deque()
while queue:
    x, y = queue.pop()
    for xx,yy in zip(dx, dy):
        nx, ny = x+xx, y+yy
        if not 0<=nx<n:
            continue
        if not 0<=ny<m:
            continue
        if maze[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] +1
            queue.append((nx, ny))
        elif maze[x][y] == 0 and maze[nx][ny] ==1 and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] +1
            # queue.append((nx, ny))
            queue2.append((nx, ny))

while queue2:
    x, y = queue2.pop()
    for xx,yy in zip(dx, dy):
        nx, ny = x+xx, y+yy
        if not 0<=nx<n:
            continue
        if not 0<=ny<m:
            continue
        if maze[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] +1
            queue2.append((nx, ny))

if visited[n-1][m-1] == 0:
    print(-1)
else:
    print(visited[n-1][m-1])