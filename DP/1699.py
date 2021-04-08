n = int(input())
count=0
while n>0:
    k = int(n**0.5)
    if n==k*k:
        count+=1
        break
    else:
        n-=k*k
        count+=1
print(count)

# 못풀어따