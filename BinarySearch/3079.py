# 문제 : N 줄 별로 심사시간이 주어졌을 때, M명의 최소 시간 계산하기
# 구현 방법 고민 : 조금 더 기다렸을 때 빠르다는 건 어떻게 구현할까?
# 어떻게 풀까? : 1) DP로 구현하기 2) 이분탐색이 되나?

# 1-1) DP로 푼다면 : line 간격마다 1을 추가해서 sum(True)==M인 최솟값 진행하기 => [M * max(line)] 크기의 배열 선언이 필요한데 메모리 초과 나려나?
# 1-2) 이렇게 만든 뒤에 이분탐색하면 빠를듯?
# => 역시나 메모리 초과 : DP 불가능
N, M = map(int, input().split())
lines = []
for _ in range(N):
    lines.append(int(input()))

'''
dp = [0 for i in range(max(lines))]
for i in range(1, max(lines)):
    count = 0
    for line in lines:
        if i%line == 0:
            count += 1
    dp[i] = dp[i-1] + count
'''
N, M = map(int, input().split())
lines = []
for _ in range(N):
    lines.append(int(input()))
def get_count(mid, lines):
    count = 0
    for line in lines:
        count += (mid //line)
    return count

start, end = 1, 10**18
while start <= end:
    mid = (start +end) // 2
    count = get_count(mid, lines)
    if count < M:
        start = mid + 1
    else:
        end = mid -1
print(start)