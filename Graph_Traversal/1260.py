import sys
sys.setrecursionlimit(1000)

N, M, V = list(map(int, input().split()))
graph = [[0 for i in range(N+1)] for i in range(N+1)]
for k in range(M):
    v, n = map(int, input().split())
    graph[v][n] = 1
    graph[n][v] = 1


def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, N + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visited[v] = 1
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, N + 1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1

visited = [0 for i in range(N+1)]
dfs(V)
print()
visited = [0 for i in range(N+1)]
bfs(V)
