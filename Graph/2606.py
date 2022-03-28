n = int(input())
k = int(input())
node = [[0 for x in range(n+1)] for i in range(n+1)]
visited = [False for x in range(n+1)]

for i in range(k):
    a, b = map(int, input().split(' '))
    node[a][b] = node[b][a] = 1

def dfs(data):
    while len(data) != 0:
        x = data.pop(0)
        for i in range(n+1):
            # print(x, i)
            if node[x][i] != 0 and visited[i] is False:
                data.append(i)
                visited[i] = True
                print(i)

dfs([1])
print(visited[2:].count(True))