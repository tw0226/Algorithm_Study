N, M, x, y, K = map(int, input().split())


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

board = [0 for i in range(N)]
dice = [0] * 6
for i in range(N):
    board[i] = list(map(int, input().split()))

def roll(dir):
    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]


    
directions = list(map(int, input().split()))

for d in directions:
    dir = d -1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not (0<=nx < N and 0<=ny<M):
        continue
    roll(dir)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    x, y = nx, ny
    print(dice[0])