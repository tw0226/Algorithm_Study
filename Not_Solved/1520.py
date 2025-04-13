import sys
sys.setrecursionlimit(int(1e9))
m,n = map(int, input().split())
maze = [[] for i in range(m)]
dp = [[-1 for i in range(n)] for i in range(m)]
for i in range(m):
    maze[i] = list(map(int, input().split()))
xx = [0, 0, -1, +1]
yy = [+1, -1, 0, 0]


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        dx, dy = x+xx[i], y+yy[i]
        if dx<0 or dx>m-1 or dy<0 or dy>n-1:
            continue
        if maze[dx][dy] < maze[x][y]:
            dp[x][y] += dfs(dx, dy)
    return dp[x][y]
print(dfs(0, 0))