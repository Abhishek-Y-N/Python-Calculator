num=int(input("Enter A Number:"))
count=0

while (num!=0):
	num=num//10
	count+=1

print("Number Of Digits:",count)