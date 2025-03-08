T = int(input())
D1 = int(input())
num_d1 = list(map(int, input().split()))
D2 = int(input())
note_dict = {}
num_d2 = list(map(int, input().split()))
for num in num_d2:
    note_dict[num] = 1

for dict in note_dict:
    if dict in num_d1:
        print(1)
    else:
        print(0)