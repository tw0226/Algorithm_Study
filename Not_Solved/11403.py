from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [0 for i in range(n)]
visited = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

def bfs(queue, graph):
    rows = [0 for i in range(n)]
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(n):
            if graph[cx][i] and not rows[i]:
                rows[i] = 1
                queue.append((i, cx))
    return rows

queue = deque()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        queue.append((i, j))
    visited[i] = bfs(queue,graph)
    print(*visited[i])