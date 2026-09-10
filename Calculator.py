num1=float(input("Enter Frst Number:"))
num2=float(input("Enter Second Number:"))

op=input("Enter operation(+, -, /, *): ")

if(op =="+"):
	print("Addition:",num1+num2)
elif(op=="-"):
	print("Subtraction:",num1-num2)
elif(op=="*"):
	print("Multiplication:",num1*num2)
elif(op=="/"):
	if(num2==0):
		print("Cannot Divide by 0")
	print("Divion:",num1/num2)	
else:
	print("Invalid Choice")