# K 개로 나누는 기준을 어떻게 구현할까??
# 탐색범위는 시험점수 최대화이기 때문에 0~sum 이다.

n, k = map(int, input().split())
points = list(map(int, input().split()))
start, end = 0, sum(points)
max_score = 0
while start <= end:
    mid = (start + end) //2
    scores = []
    score, count = 0, 0
    for p in points:
        score += p
        if score > mid:
            count += 1
            scores.append(score)
            score = 0
    if count < k:
        end = mid -1
    else:
        start = mid + 1
        max_score = min(scores)
print(max_score)