N, M = map(int, input().split())
moneys = []
for i in range(N):
    moneys.append(int(input()))

start, end = min(moneys), sum(moneys)
K = min(moneys)
while start <= end:
    mid = (start + end) //2
    balance = mid
    count = 1
    for money in moneys:
        if balance - money < 0:
            balance = mid
            count += 1
        balance -= money
    if count > M or mid < max(moneys):
        start = mid + 1
    else:
        end = mid -1
        K = mid
print(K)