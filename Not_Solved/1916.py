import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[] for i in range(n+1)]
dp = [INF for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
start, dest = map(int, input().split())
queue = []
dp[start] = 0

def bfs(start):
    heapq.heappush(queue, (0, start))
    while queue:
        now_d, node = heapq.heappop(queue)
        if dp[node] < now_d:
            continue
        for next_d, next in graph[node]:
            min_dist = next_d + now_d
            if min_dist >= dp[next]:
                continue
            queue.append((min_dist, next))
            dp[next] = min_dist

bfs(start)
print(dp[dest])