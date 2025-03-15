# 문제 : 집합 U에서 3개를 골랐을 때, 그 세수의 합 d가 U에 있다면 그 중 가장 큰 d 를 찾기
# 고려사항1 : U의 최악의 경우 1e3 **3 = 1e9 로 시간초과 에러가 날 것 같다 이를 줄여야 한다
# 예상구현방법 : 누적합이나 슬라이딩 윈도우로 연산량을 줄여야 될 것 같다
# 어떻게 풀까? 
# 1) grid search로 모든 경우의 수로 푼다. => 시간초과 100%..
# 2) sliding window = x: u[0] + y: u[1] + z: u[2] 로 해놓고, 
# for 1<y<N 
#   for 2<z<N로 +해보면서 가는데 이럼 느리니까 Z 축부터 이분탐색 해보자 그러면 log(N) ** 3
# 푸는 방법
# # x+y+z = k 라면 x+y = z-k 도 가능하다
# # x+y 를 집합에 저장시켜놓고, z,k 를 루프 돌아보면서 탐색하기
N = int(input())
U = []
for i in range(N):
    U.append(int(input()))
U.sort()
pool = set()

for x in U:
    for y in U:
        pool.add(x+y)

def solve():
    for i in range(len(U)-1, -1, -1):
        for j in range(i+1):
            if U[i]-U[j] in pool:
                return U[i]
print(solve())