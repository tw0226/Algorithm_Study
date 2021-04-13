n = int(input())
count=0
for i in range(int(10**n)):
	x =[x for x in str(i)]
	for j in range(1, len(x)):
		if abs(int(x[j]) - int(x[j-1]))>1 or x[j]==x[j-1]:
			continue
		count+=1
if n==1:
	print(9)
else:
	print(count%10**9)
