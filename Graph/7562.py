from collections import deque
T = int(input())
xx =[-2,-2,-1,-1, 1, 1, 2, 2]
yy= [-1, 1,-2, 2,-2, 2,-1, 1]

for t in range(T):
    l = int(input())
    start_x, start_y = map(int, (input().split()))
    dest_x, dest_y = map(int, (input().split()))
    graph = [[0 for i in range(l)] for i in range(l)]
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        curr_x, curr_y = queue.popleft()
        if curr_x == dest_x and curr_y == dest_y:
            print(graph[dest_x][dest_y])
            break
        for dx,dy in zip(xx, yy):
            next_x, next_y = curr_x +dx, curr_y+dy
            if not 0<=next_x<l:
                continue
            if not 0<=next_y<l:
                continue
            if not graph[next_x][next_y]:
                graph[next_x][next_y] = graph[curr_x][curr_y] +1
                queue.append((next_x, next_y))