import itertools
from copy import deepcopy
N, M = map(int, input().split())
x = [0 for i in range(N+1)]
chicken =[]
house = []
for i in range(1, N+1):
    x[i] = [0] + list(map(int, input().split()))
    for j in range(1, N+1):
        if x[i][j] == 2:
            chicken.append((i,j))
        elif x[i][j]==1:
            house.append((i,j))

result = 10000
for chi in itertools.combinations(chicken, M):
    _sum = 0
    for r1,c1 in house:
        dist = 999
        for point in chi:
            r2, c2 = point
            dist = min(dist, abs(r1-r2) + abs(c1-c2))
            # print(r1, c1, point[0], point[1])
            # for r2,c2 in point:
            # dist = min(abs(r1-r2) + abs(c1-c2), dist)
        _sum += dist

    result = min(result, _sum)
print(result)