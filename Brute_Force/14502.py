import itertools
import copy
N, M = map(int, (input().split()))
arr = [0 for x in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))

def count_space(temp):
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j]==0:
                count+=1
    return count

def spread_virus(x, y, temp):
    if y+1 < M:
        if temp[x][y + 1] == 0:
            temp[x][y + 1] = 2
            spread_virus(x, y + 1, temp)
    if x+1 < N:
        if temp[x + 1][y] == 0:
            temp[x + 1][y] = 2
            spread_virus(x + 1, y, temp)
    if y-1 >= 0:
        if temp[x][y - 1] == 0:
            temp[x][y - 1] = 2
            spread_virus(x, y-1, temp)
    if x-1 >= 0:
        if temp[x-1][y] == 0:
            temp[x-1][y] = 2
            spread_virus(x-1, y, temp)
    return temp

def find_virus():
    virus = list()
    for i in range(N):
        for j in range(M):
            if arr[i][j]==2:
                virus.append((i, j))
    return virus

W = list()
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            W.append((i, j))

W = list(itertools.permutations(W, 3))
max_count = 0
for i, way in enumerate(W):
    temp = copy.deepcopy(arr)

    #make wall
    for x,y in way:
        temp[x][y] = 1

    #spread virus
    for x,y in find_virus():
        temp = spread_virus(x,y, temp)
    max_count = max(max_count, count_space(temp))

print(max_count)