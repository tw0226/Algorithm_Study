n = int(input())
board = []
dp = [[-1] *(n+1) for _ in range(n+1)]
for i in range(n):
    board.append(list(map(int, input().split())))


def dfs(x,y):
    # print(x,y, route)
    if x==n-1 and y==n-1:
        return 1
    if dp[x][y]==-1:
        dp[x][y]=0
        x1, y1 = x + board[x][y], y
        x2, y2 = x, y + board[x][y]
        if 0<=x1<n and 0<=y1<n: dp[x][y] += dfs(x1, y1)
        if 0<=x2<n and 0 <= y2 < n: dp[x][y] += dfs(x2, y2)
    return dp[x][y]
route = dfs(0,0)
print(route)