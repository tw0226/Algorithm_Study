import heapq
n, m = map(int, input().split())
land = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    land[a].append((c, b))
    land[b].append((c, a))

dist = [1e9 for i in range(n+1)]
visited = [0 for i in range(n+1)]
start, end = map(int, input().split())
node = []
heapq.heappush(node, (0, start))

while node:
    curr_dist, curr_node = heapq.heappop(node)
    visited[curr_node] = True
    for next_dist, next_node in land[curr_node]:
        if visited[next_node]:
            continue
        min_dist = next_dist + curr_dist
        if not visited[next_dist] and min_dist< dist[next_node]:
            dist[next_node] = min_dist
            heapq.heappush(node, (min_dist, next_node))
print(dist[end])