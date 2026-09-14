num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Number:"))

op=input("Enter operation(+, -, /, *): ")

match op:
	case "+":
		print("Addition:",num1+num2)
	case "-":
		print("Subtraction:",num1-num2)
	case "*":
		print("Multiplication:",num1*num2)
	case "/":
		if(num2==0):            			
			print("Cannot Divide By Zero")
		else:
			print("Division:",num1/num2)
	case _:
		print("Invaid Choice")