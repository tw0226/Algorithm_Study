# 다익스트라는 구현했는데 뭔가 잘못된 것 같다
# 이분탐색으로 구현할만한 공간이 있을까?


import heapq
n, p, k = map(int, input().split())
net = [[] for i in range(n+1)]
for i in range(p):
    a,b,c = map(int, input().split())
    net[a].append((c, b))
    net[b].append((c, a))

node_cost = [1e9 for i in range(n+1)]
visited = [0 for i in range(n+1)]
costs = []
node = []
heapq.heappush(node, (0, 1))

while node:
    curr_cost, curr_node = heapq.heappop(node)
    visited[curr_node] = True
    for next_cost, next_node in net[curr_node]:
        if visited[next_node]:
            continue
        min_cost = curr_cost + next_cost
        print("!", curr_node, next_node, min_cost)
        if not visited[next_node] and min_cost < node_cost[next_node]:
            node_cost[next_node] = min_cost
            heapq.heappush(node, (min_cost, next_node))
            costs.append(next_cost)


print(costs)
costs = sorted(costs, reverse=True)
print(visited)
print(node_cost)
print(costs)
if not visited[n]:
    print(-1)
else:
    print(costs[k])