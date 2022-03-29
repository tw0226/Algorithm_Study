from collections import deque
from re import T
M, N = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1 ,-1, 0, 0]

def bfs(queue):
    # count = 1
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            _x = x + dx[idx]
            _y = y + dy[idx]
            if 0<=_x<N and 0<=_y<M and graph[_x][_y]==0:
                graph[_x][_y] = graph[x][y] + 1
                queue.append((_x,_y))

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            queue.append((i,j))
bfs(queue)

is_all_mature = True
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            is_all_mature = False

if not is_all_mature:
    print(-1)
else:
    print(max(0, max(map(max, graph))-1))