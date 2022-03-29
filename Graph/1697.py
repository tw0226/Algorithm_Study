from collections import deque
N, K = map(int, input().split())
MAX = 100000
graph = [0] * (MAX+1)


def bfs():
    que = deque()
    que.append(N)
    while que:
        x = que.popleft()
        # graph[x] = v
        if x==K:
            print(graph[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=MAX and not graph[nx]:
                graph[nx]= graph[x]+1
                que.append(nx)
        
bfs()