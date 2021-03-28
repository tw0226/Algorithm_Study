N = int(input())

hap = list()
for i in range(N):
    D = str(i)
    sum = 0
    for x in D:
        sum += int(x)
    if sum + i == N:
        hap.append(i)

if hap != []:
    print(min(hap))
else:
    print(0)