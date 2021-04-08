import math
n = int(input())
count = 1
k = int(math.sqrt(n))
while k*k!=n:
    count += 1
    print(n, k, count)
    n -= k * k
    k = int(math.sqrt(n))



print(count)