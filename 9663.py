from copy import deepcopy
N = int(input())
board = [0 for x in range(N)]
for i in range(N):
    board[i] = [0 for x in range(N)]

def put_queen(x,y, temp):
    for i in range(N):
        temp[x][i] = 1
        temp[i][y] = 1
    for i in range(N):
        if 0< x+i < N:
            if 0 <= y - i < N:
                temp[x + i][y - i] = 1
            if 0 <= y + i < N:
                temp[x + i][y + i] = 1
        if 0 <= x - i < N:
            if 0 <= y - i < N:
                temp[x - i][y - i] = 1
            if 0 <= y + i < N:
                temp[x - i][y + i] = 1
        '''
        if x+y > 2*i:
            temp[x-i][y-i] = 1
        if x+y + 2*i < 2*(N-1):
            temp[x+i][y+i] = 1
        if x+y>=0 and x+y < N:
            print(x,y,i)
            temp[x+i][y-i] = 1
            temp[x-i][y+i] = 1
        '''
case = 0
case_list = list()

for i in range(N):
    for j in range(N):
        count = N-1
        temp = deepcopy(board)
        put_queen(i, j, temp)
        success = list()
        for x in range(N):
            for y in range(N):
                if temp[x][y] != 1:
                    put_queen(x,y, temp)
                    count -= 1

        if count == 0:
            print(i,j)
            case += 1
print(case)
