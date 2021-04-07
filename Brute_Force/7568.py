N = int(input())
user_list = list()
for x in range(N):
    kg, cm = map(int, input().split())
    user_list.append({'kg' : kg, 'cm' : cm})

for x in user_list:
    count=1
    for y in user_list:
        if x['cm'] < y['cm'] and x['kg'] < y['kg']:
            count+=1
    print(count)
