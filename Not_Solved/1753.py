import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
INF = 1e9
dp = [INF for i in range(v+1)]
dp[start]=0
graph = [[] for i in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

queue = []
def dijkstra(queue):
    while queue:
        curr_w, curr = heapq.heappop(queue)
        if dp[curr] < curr_w:
            continue
        for next_w, next in graph[curr]:
            dist = curr_w + next_w
            if dp[next] > dist: 
                dp[next] = dist
                heapq.heappush(queue, (dist, next))
heapq.heappush(queue, (0, start))
dijkstra(queue)

for i in range(1, v+1):
    if dp[i] != INF:
        print(dp[i])
    else:
        print("INF")