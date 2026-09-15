num=int(input("Enter A Number:"))
count=0
i=2

while i<=num:
	flag=True
	n=2
	while n<i:
		if i%n==0:
			flag=False
			break
		n+=1
	if flag:
		count+=1
	i+=1

print(count)