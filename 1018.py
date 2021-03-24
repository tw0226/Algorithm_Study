H, W = map(int,input().split())
arr = [[0] for i in range(W)]
for i in range(H):
    arr[i] = map(str, input())

print(arr)

