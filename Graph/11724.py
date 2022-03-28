N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

def dfs(stack):
    while stack:
        a = stack.pop()
        # print(a)
        visited[a] = 1
        for i in range(1, N+1):
            if graph[a][i] != 0 and not visited[i]:
                graph[a][i] = 0
                dfs([i])

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs([i])
        count += 1
print(count)