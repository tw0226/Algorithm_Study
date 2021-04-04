N = int(input())
data_list = list(map(int, input().split()))[:N]
max_sum = 0
current_sum = 0
minus_max = -1001
for current in data_list:
    current_sum += current
    if current_sum >= max_sum:
        max_sum = current_sum

    if current_sum < 0:
        current_sum = 0

if max_sum != 0:
    print(max_sum)
else:
    print(max(data_list))