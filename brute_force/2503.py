from itertools import permutations
N = int(input())
num = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(N):
	D, S, B = map(int, input().split())
	D = list(str(D))
	remove_cnt = 0

	for i in range(len(num)):
		s_cnt = b_cnt = 0
		i -= remove_cnt

		for j in range(3):
			D[j] = int(D[j])
			if D[j] in num[i]:
				if j== num[i].index(D[j]):
					s_cnt += 1
				else:
					b_cnt += 1
		if s_cnt != S or b_cnt != B:
			num.remove(num[i])
			remove_cnt += 1

print(len(num))