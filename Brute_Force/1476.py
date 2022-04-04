import itertools
E, S, M = 15, 28, 19
e, s, m = map(int, input().split())
count = 1
i, j, k = 1, 1, 1
while not (i == e and j ==s and m == k):
    i = (i % E)+1
    j = (j % S)+1
    k = (k % M)+1
    count += 1

print(count)