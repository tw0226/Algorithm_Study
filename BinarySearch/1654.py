K, N = map(int, input().split())
line = []
for _ in range(K):
    line.append(int(input()))

start, end = 1, max(line)
while start <= end:
    mid = (start +end)//2
    count = 0
    for i in line:
        count += i//mid

    if count >= N:
        start = mid +1
    else:
        end = mid -1
        
print(end)