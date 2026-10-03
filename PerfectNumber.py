
def perfect(num):
	sum=0
	for i in range(1,num):
		if num%i==0:
			sum+=i

	if num==sum:
		return True
	return False


num=int(input("Enter A Number:"))
print("Is Perfect:",perfect(num))
