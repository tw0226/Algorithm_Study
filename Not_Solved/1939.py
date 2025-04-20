from collections import deque
n, m = map(int, input().split())
land = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    land[a].append((c, b))
    land[b].append((c, a))
start, end = map(int, input().split())

def bfs(w):
    queue = deque()
    visited = [0 for i in range(n+1)]
    visited[start] = True
    queue.append(start)
    while queue:
        curr_node = queue.popleft()
        for next_dist, next_node in land[curr_node]:
            if not visited[next_node] and next_dist >= w:
                visited[next_node] = True
                queue.append(next_node)
    return visited[end]

left, right = 1, int(1e9)
result = 0
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        left = mid +1
        result = mid
    else:
        right = mid -1
print(result)