d, k = map(int, input().split())

a, b = 1, 1
for _ in range(4, d+1):
    a, b = b, a+b

ac, bc = 1, 0
while True:
    tmp = k - ac * a
    if tmp < 0:
        break
    if tmp % b == 0:
        bc = tmp//b
        break
    ac += 1

print(ac)
print(bc)
