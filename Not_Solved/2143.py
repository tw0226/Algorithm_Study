
#문제 : T와 숫자들의 집합 A,B 가 주어졌을때 A,B 의 부분집합의 합으로 T가 되는 갯수
#어떻게 풀까? 
# 1) A+B 의 합을 set에 저장해놓고, 각 원소마다 하나씩 더해보면서 T가 되는지 확인...? => 부분집합 5개 이상의 경우는 확인이 어렵다
# 2) A의 누적합이랑 B의 누적합 만들어놓고, A-T=B 랑 B-T=A 해볼까? 하기엔 음수도 들어가 있어서 안될듯한데 이게 된다네..?

import bisect
T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

a_sum = []
for i in range(N):
    temp = A[i]
    a_sum.append(A[i])
    for j in range(i+1, N):
        temp += A[j]
        a_sum.append(temp)

b_sum = []
for i in range(M):
    temp = B[i]
    b_sum.append(B[i])
    for j in range(i+1, M):
        temp += B[j]
        b_sum.append(temp)

a_sum.sort()
b_sum.sort()
count = 0
for i in range(len(a_sum)):
    temp = T - a_sum[i]
    l = bisect.bisect_left(b_sum, T-a_sum[i])
    r = bisect.bisect_right(b_sum, T-a_sum[i])
    count += (r - l)
print(count)