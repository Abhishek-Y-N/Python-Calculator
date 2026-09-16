while True:
	print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Factorial\nType 'exit' To Terminate")
	ch=input("Enter Your Choice:")

	match ch:
		case "1":
			num1=float(input("Enter 1st Number:"))
			num2=float(input("Enter 2nd Number:"))
			print("Addition:",num1+num2)
		case "2":
			num1=float(input("Enter 1st Number:"))
			num2=float(input("Enter 2nd Number:"))
			print("Subtraction:",num1-num2)
		case "3":
			num1=float(input("Enter 1st Number:"))
			num2=float(input("Enter 2nd Number:"))
			print("Multiplication:",num1*num2)
		case "4":
			num1=float(input("Enter 1st Number:"))
			num2=float(input("Enter 2nd Number:"))
			if(num2==0):
				print("Cannot Divide By Zero!")
			else:
				print("Division:",num1/num2)
		case "5":
			num=float(input("Enter A Number:"))
			i=1
			fact=1
			while i<=num:
				fact=fact*i      
				i+=1
			print("Factorial:",fact)
		case "exit":
			print("Terminated")
			break
		case _:
			print("Invalid Choice")
	 