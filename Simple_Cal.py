def add(num1,num2):
	print("Addition:",num1+num2)

def sub(num1,num2):
	print("Subtraction:",num1-num2)

def mul(num1,num2):
	print("Multiplication:",num1*num2)

def div(num1,num2):
	print("Division:",num1/num2)

num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Function:"))
ch=input("ENter Choice(+,-,*,/):")
if(ch=="+"):
	add(num1,num2)
elif(ch=="-"):
	sub(num1,num2)
elif(ch=="*"):
	mul(num1,num2)
elif(ch=="/"):
	div(num1,num2)
else:
	print("Invalid Choice")