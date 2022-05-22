N = int(input())
S = [0 for i in range(N)]
is_sinked = [0 for i in range(N)]
max_value = 0
for i in range(N):
    S[i] = list(map(int, input().split()))
    is_sinked[i] = [0 for i in range(N)]
    max_value = max(max_value, max(S[i]))
max_count = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(que, v):
    while que:
        x, y = que.pop(-1)
        for ax, ay in zip(dx, dy):
            _x = x+ax
            _y = y+ay
            if 0<=_x<N and 0<=_y<N:
                if S[_x][_y] > v and not is_sinked[_x][_y]:
                    que.append((_x,_y))
                    is_sinked[_x][_y] = 1


for i in range(max_value):
    non_sink = []
    for x in range(N):
        is_sinked[x] = [0 for k in range(N)]
        for y in range(N):
            if S[x][y] > i:
                non_sink.append((x,y))
            else:
                is_sinked[x][y] = 1
    count = 0
    for point in non_sink:
        x,y = point
        if not is_sinked[x][y]:
            dfs([point], i)
            count+=1
    max_count = max(count, max_count)
print(max_count)