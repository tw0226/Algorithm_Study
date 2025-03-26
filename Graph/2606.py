from collections import deque
n = int(input())
line = int(input())
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
for i in range(line):
    a, b =map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
visited[1] = True
queue.append(1)
while queue:
    curr = queue.popleft()
    for node in graph[curr]:
        if not visited[node]:
            queue.append(node)
            visited[node] = True


print(sum(visited)-1)