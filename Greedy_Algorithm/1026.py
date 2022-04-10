N = int(input())
A1 = sorted(list(map(int, input().split())), reverse=True)
A2 = sorted(list(map(int, input().split())))
s = 0
for a,b in zip(A1, A2):
    s += a*b
print(s)