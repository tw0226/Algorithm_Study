N = int(input())
A = list(map(int, input().split()))
start, end = 0, len(A)
curr = min(A)
count = 1
for i in range(len(A)):
    if curr < A[i]:
        curr = A[i]
        count += 1
print(count)
def binary_search(A, start, end, curr, count):
    mid = (start + end) //2
    if start > end:
        return count
    elif A[mid] < curr:
        binary_search(A, start, mid -1, A[mid], count+1)
    else:
        binary_search(A, mid+1, end, A[mid])