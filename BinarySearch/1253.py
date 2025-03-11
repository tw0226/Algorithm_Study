# 문제 : N개의 수가 주어졌을 때, 그 중에 두 수의 합으로 표현될수 있는 숫자 M개 구하기
# 구현 방법 고민 : 어떻게 좋은 수를 판별할까?
# 어떻게 풀까?
# 1) 그리드 알고리즘 쓰기엔 최악의 경우 1999x 1998 => 1백만 넘어가면서 타임아웃 뜰 거 같음
# 2) 인덱스 기준으로 하나씩 줄여나가면서 검색하기

# 놓친 점 : N 개중 본인 인덱스를 제외하기

N = int(input())
arr = sorted(list(map(int, input().split())))
count = 0
for i in range(N):
    temp = arr[:i] + arr[i+1:]
    start, end = 0, len(temp)-1
    while start < end:
        total = temp[start] + temp[end]
        if total == arr[i]:
            count +=1
            break
        elif total < arr[i]:
            start += 1
        else:
            end -= 1
print(count)