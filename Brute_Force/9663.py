import itertools
N= int(input())
board = [str(x) for x in range(N)]
chess_board = list(itertools.product(board, repeat=2))
print(chess_board)


for i in range(N):
    for j in range(N):
        chess_board = list(itertools.product(board, repeat=2))
        for x,y in chess_board:
            if i==x or j==y:
                chess_board.remove(i)
            elif