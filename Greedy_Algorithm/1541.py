arr = input().split('-')
_min = 0
for a in arr[0].split('+'):
    _min += int(a)
for a in arr[1:]:
    for a2 in a.split('+'):
        _min -= int(a2)
print(_min)