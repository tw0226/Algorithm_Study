t = int(input())
def factorial(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    return sum
for i in range(t):
    n, m = list(map(int, input().split()))
    s = factorial(m) // (factorial(n) * factorial(m - n ))
    print(int(s))