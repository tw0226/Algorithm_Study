N, M = map(int, input().split())
lectures = list(map(int, input().split(' ')))
start, end = max(lectures), sum(lectures)
while start <= end:
    mid = (start + end) // 2
    total_mins = 0
    count = 1
    for lec in lectures:
        if total_mins + lec > mid:
            count += 1
            total_mins = 0
        total_mins += lec
    if count <= M:
        end = mid - 1
    else:
        start = mid + 1
print(start)