import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

def dfs(a):
    visited[a] = 1
    for i in range(1, N+1):
        if graph[a][i] != 0 and not visited[i]:
            dfs(i)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)