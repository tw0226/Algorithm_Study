# 문제 : 길이 N, 높이 H 인 동굴에 아래 석순, 위 종주석이 번갈아있는 동굴에 최소한만 부딪히면서 통과하기
# 구현방법 고민 : 이분 탐색은 확실한 거고, 알고리즘을 2개로 나눠서 풀어야하나? 아니면 리스트를 두개로 나눠야하나?
# H를 뺴서 하면 밑에서부터만 계산하면 되니까 편리할 것 같다
# 1-1) 1개 리스트에서 홀짝 나눠서 구현한다
# 1-2) 중간에서부터 시작해서 높이 천장까지 갯수 빼기하면 될거 같은데..
# 1-3) 중간에서 갯수 센다음에 빼면
# walls 가 최대 200000 x 500000 = 1e11 이라서 무조건 연산량 오버가 되는데 walls 를 scan 해야한다..
# 2-1) 2개 리스트에서 홀짝 나눠서 구현
# 2-2) H로 빼면 2개의 리스트인데 검색량은 O(N/2) 가 된다

# 포인트 : 이분탐색에 목 매지말고 제대로 풀자.
N, H = map(int, input().split())
bottom, top = [0 for i in range(H)], [0 for i in range(H)]
for i in range(N):
    h = int(input())
    if i%2==0:
        bottom[h] += 1
    else:
        top[h] += 1

for i in range(H-1, 0, -1):
    bottom[i-1] += bottom[i]
    top[H-i] += top[H-(i+1)]

# print(bottom)
# print(top)
# print(sorted(top, reverse=False))

count = 0
start, end = 0, H-1
min_value = 1e11
while start < end:
    current_value = bottom[start] + top[H-(1+start)]
    if current_value < min_value:
        min_value = current_value
        count = 1
    
    if min_value <= current_value:
        count += 1
        start +=1
    else:
        end +=1
    print(start, end, current_value, min_value, count)
print(min_value, count)