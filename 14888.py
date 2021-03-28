import itertools
N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
opt_list = []
for opt, number in zip(['+', '-', '*', '/'], operators):
    opt_list += opt*number

operator_combination = set(list(itertools.permutations(opt_list)))
max_value = -10**9
min_value = 10**9

for operators in operator_combination:
    result = numbers[0]
    for i in range(N-1):
        result = int(eval(str(result)+operators[i]+str(numbers[i+1])))
    max_value = max(max_value, result)
    min_value = min(min_value, result)
print(max_value)
print(min_value)
