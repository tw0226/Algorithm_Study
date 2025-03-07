import sys
from decimal import Decimal
X, Y = map(int, input().split())
Z = int(Decimal(Y)/Decimal(X)*100)
start, end = 1, X
result = sys.maxsize
while start <= end:
    mid = (start +end )//2
    win_rate = int(Decimal(Y + mid)/Decimal(X + mid) * 100)    
    if win_rate > Z:
        end = mid - 1
        result = min(mid, result)
    else:
        start = mid +1
if result == sys.maxsize:
    print(-1)
else:
    print(result)