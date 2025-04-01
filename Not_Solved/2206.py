# 벽을 부쉈는지 안 부쉈는지에 대한 고려를 visited N x M x 2 형태로 반영..

from collections import deque
n, m = map(int, input().split())
maze = [[] for i in range(n)]
for i in range(n):
    maze[i] = list(map(int, list(input().strip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[[0]*2 for i in range(m)] for i in range(n)]
visited[0][0][0] = 1

def bfs(x,y,z):
    queue = deque()
    queue.append((x, y, z))
    while queue:
        x, y, c = queue.popleft()
        if x== n-1 and y == m-1:
            return visited[x][y][c]
        for xx,yy in zip(dx, dy):
            nx, ny = x+xx, y+yy

            if not 0<=nx<n:
                continue
            if not 0<=ny<m:
                continue
            if maze[nx][ny] == 1 and c==0:
                visited[nx][ny][1] = visited[x][y][0] +1
                queue.append((nx, ny, 1))
            elif maze[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c] +1
                queue.append((nx, ny, c))
    return -1
print(bfs(0, 0, 0))