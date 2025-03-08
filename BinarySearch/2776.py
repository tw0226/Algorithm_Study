T = int(input())
note_dict = {}

for t in range(T):
    D1 = int(input())
    note1 = list(map(int, input().split()))
    D2 = int(input())
    note2 = list(map(int, input().split()))
    note1 = sorted(note1)
    for num in note2:
        start, end = 0, len(note1)-1
        exist = 0
        while start <= end:
            mid = (start + end) // 2
            if note1[mid] == num:
                exist = 1
                break
            elif note1[mid] < num:
                start = mid +1
            else:
                end = mid -1
        print(exist)