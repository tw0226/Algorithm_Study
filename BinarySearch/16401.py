m, n  = map(int, input().split())
snacks = list(map(int, input().split()))

start, end = 1, max(snacks)
max_len = 0
while start <= end:
    count = 0
    mid = (start+end)//2
    for snack in snacks:
        count += snack//mid
        if count >= m:
            break
    if count < m:
        end = mid - 1
    else:
        start = mid + 1
        max_len = mid

print(max_len)