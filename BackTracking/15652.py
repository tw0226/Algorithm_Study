import itertools
n, m = map(int, input().split())
n = [i+1 for i in range(n)]

for s in itertools.combinations_with_replacement(n, m):
    t = ""
    for i in s:
        t+=str(i)+" "
    print(t)