# 예상풀이방법 1: 이분탐색에 맞춰서 풀기
# 포인트 : 딕셔너리 쓰기...
import sys
N = int(input())
cards = sorted(list(map(int, input().split())))

card_dict = {}
for card in cards:
    if card in card_dict:
        card_dict[card] += 1
    else: 
        card_dict[card] = 1
M = int(input())
to_finds = list(map(int, input().split()))

for find in to_finds:
    count = 0
    start, end = 0, len(cards) -1
    while start <= end:
        mid = (start+end)//2
        if cards[mid] == find:
            count = card_dict[find]
            break
        elif cards[mid] < find:
            start = mid+1
        elif cards[mid] > find:
            end = mid -1
    print(count)