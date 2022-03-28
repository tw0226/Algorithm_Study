T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(point):
    while len(point) != 0:
        x, y = point.pop(0)
        X[x][y] = 0
        for idx in range(4):
            _x = x + dx[idx]
            _y = y + dy[idx]
            if 0<=_x<N and 0<=_y<M and X[_x][_y] !=0:
                point.append((_x, _y))

for i in range(T):
    M, N, K = map(int, input().split())
    X = [[0 for i in range(M+1)] for i in range(N+1)]
    count = 0
    for j in range(K):
        y, x = map(int, input().split())
        X[x][y] = 1
        
    for x in range(N):
        for y in range(M):
            if X[x][y] != 0:
                bfs([(x,y)])
                count += 1
    print(count)    
    