# 푸는 방법 1: while문 재귀
'''
result = 0
while start <= end:
    mid = (start+ end)//2
    _sum = 0
    for budget in budgets:
        if budget <= mid:
            _sum += budget
        else:
            _sum += mid
    if _sum <= maximum:
        start = mid + 1
        result = mid
    else:
        end = mid -1
print(result)
'''
# method 2 : 재귀
def binary(budgets, start, end, M):
    global result
    if start > end: 
        return
    else:
        mid = (start+end)//2
        _sum = 0
        for budget in budgets:
            if budget <= mid:
                _sum += budget
            else:
                _sum += mid
        if _sum <= M:
            result = mid
            return binary(budgets, mid+1, end, M)
        else:
            return binary(budgets, start, mid-1, M)
N = int(input())
budgets = sorted(list(map(int, input().split())))
maximum = int(input())
start, end = 1, max(budgets)
binary(budgets, start, end, maximum)
print(result)