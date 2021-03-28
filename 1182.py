import itertools
N, S = map(int, input().split())
data_list = list(map(int, input().split()))
count = 0
for i in range(N):
    for data in itertools.combinations(data_list, i+1):
        if sum(data) == S:
            print(data)
            count += 1
print(count)
