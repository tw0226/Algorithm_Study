from collections import deque
n = int(input())
graph = [[] for i in range(n)]
graph2= [[] for i in range(n)]
RGB = {'R': 0, 'G':1, 'B':2}
RGB2 = {'R': 0, 'G':0, 'B':1}
for i in range(n):
    line = list(input())
    graph[i]= [RGB[x] for x in line]
    graph2[i]= [RGB2[x] for x in line]

visited = [[0 for i in range(n)] for i in range(n)]
visited2 = [[0 for i in range(n)] for i in range(n)]

queue = deque()

dx = [0, 0, +1, -1]
dy = [-1, +1, 0, 0]
value, value2 = 0, 0

def bfs(x, y, graph, visited, value):
    queue = deque()
    queue.append((x, y))
    while queue:
        x,y = queue.popleft()
        for nx, ny in zip(dx, dy):
            cx, cy = nx+x, ny+y
            if not 0<=cx<n:
                continue
            if not 0<=cy<n:
                continue
            if not visited[cx][cy] and graph[x][y] == graph[cx][cy]:
                visited[cx][cy] = value
                queue.append((cx,cy))

for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            value += 1
            bfs(x,y, graph, visited, value)
        if not visited2[x][y]:
            value2 +=1 
            bfs(x,y, graph2, visited2, value2)

print(value, value2)