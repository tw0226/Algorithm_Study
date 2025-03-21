from collections import deque
import sys
N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def bfs(mid):
    visited = [False for i in range(N+1)]
    queue = deque()
    queue.append(init)
    visited[init] = True

    while queue:
        idx = queue.popleft()
        for i,w in graph[idx]:
            if not visited[i] and mid <= w:
                queue.append(i)
                visited[i] = True
    if visited[dest]:
        return True
    else:
        return False

init, dest = map(int, input().split())
start, end = 1, 1e9
result = 0
while start <= end:
    mid = (start+end)//2
    if bfs(mid):
        result = mid
        start = mid +1
    else: 
        end = mid -1
print(int(result))
