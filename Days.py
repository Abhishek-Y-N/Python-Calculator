# n=int(input("Enter No:"))

# if n==1:
# 	print("Sunday")
# elif n==2:
# 	print("Monday")
# elif n==3:
# 	print("Tuesday")
# elif n==4:
# 	print("Wednesday")
# elif n==5:
# 	print("Tuesday")
# elif n==6:
# 	print("Friday")
# elif n==7:
# 	print("Saturday")
# else:
# 	print("Invalid Number")

day=int(input("Enter Number:"))

match day:
	case 1:
		print("Monday")
	case 2:
		print("Tuesday")
	case 3:
		print("Wednesday")
	case 4:
		print("Thursday")
	case 5:
		print("Friday")
	case 6:
		print("Saturday")
	case 7:
		print("Sunday")
	case _:
		print("Invalid Number")