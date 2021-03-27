from copy import deepcopy
N = int(input())
board = [0 for x in range(N)]
visited_row = [0 for x in range(N)]
visited_col = [0 for x in range(N)]
for i in range(N):
    board[i] = [0 for x in range(N)]


def put_queen(x,y):
    visited_row[x] = 1
    visited_col[y] = 1
    count = 0
    for i in range(x, N):
        check_rows = deepcopy(visited_row)
        for j in range(y+1, N):
            check_cols = deepcopy(visited_col)
            if find_route(x,y+1):
                put_queen(x, j)
        if find_route(i, y):
            put_queen(i, y)

def find_route(x,y):
    if visited_row[x]==0 and visited_col[y]==0:
        return True
    else:
        return False
case = 0
case_list = list()

for i in range(N):
    for j in range(N):
        put_queen(i,j)

print(case)
