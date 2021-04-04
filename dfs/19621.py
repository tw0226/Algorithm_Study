N = int(input())
meetings = []
for _ in range(N):
    meetings.append(tuple(map(int, input().split())))

meetings.sort()

def dfs(x, current):
    current += meetings[x][2]
    if meetings[x][1] > last_start:
        peoples.append(current)
    for i in range(x+1, N):
        if meetings[x][1] > meetings[i][0]:
            continue
        dfs(i, current)

peoples = []
last_start = max([s for s,e,p in meetings])
for i in range(N):
    dfs(i, 0)
print(max(peoples))
