import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


v, e = map(int, input().split())
start = int(input())
INF = 1e9
graph = [[] for i in range(v+1)]
dp = [INF for i in range(v+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, start))
dp[start] = 0
while q:
    curr_w, curr = heapq.heappop(q)
    if dp[curr] < curr_w:
        continue
    for dest, dest_w in graph[curr]:
        dist = curr_w + dest_w
        if dist < dp[dest]:
            dp[dest] = dist
            heapq.heappush(q, (dist, dest))

[print('INF') if x==INF else print(x) for x in dp[1:]]