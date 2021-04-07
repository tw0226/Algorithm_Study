n = int(input())
count = 0
for i in range(int(1e+10)):
    if '666' in str(i):
        # print(i)
        count +=1
    if count==n:
        print(i)
        break