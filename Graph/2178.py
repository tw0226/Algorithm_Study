from collections import deque
x,y = map(int, input().split())
maze = [[0 for i in range(y+2)] for i in range(x+2)]
visited = [[0 for i in range(y+2)] for i in range(x+2)]
for i in range(1, x+1):
    maze[i][1:] = list(map(int, list(input())))+[0]
queue = deque()
queue.append((1,1))

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]
visited[1][1] = 1
while queue:
    c_x,c_y = queue.popleft()
    for _dx, _dy in zip(dx, dy):
        xx, yy = c_x+_dx, c_y+_dy
        if maze[xx][yy] == 1 and not visited[xx][yy]:
            visited[xx][yy] = visited[c_x][c_y] +1
            queue.append((xx, yy))
print(visited[x][y])