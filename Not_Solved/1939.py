from collections import deque
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

_from, _to = map(int, input().split())
start, end = 1, int(1e9)

def bfs(val):
    visited = [0 for i in range(n+1)]
    queue = deque()
    queue.append(_from)
    visited[_from] = True
    while queue:
        curr = queue.popleft()
        for dest, weight in graph[curr]:
            if not visited[dest] and weight >= val:
                visited[dest] = True
                queue.append(dest)
    if visited[_to]:
        return True
    else:
        return False

result = 0
while start<=end:
    mid = (start+end)//2
    if bfs(mid):
        start = mid+1
        result = mid
    else:
        end = mid-1
print(result)