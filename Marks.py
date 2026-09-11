marks=int(input("Enter Marks:"))

if(marks>=90 and marks<=100):
	print("O Grade")
elif(marks>=80 and marks<90):
	print("A Grade")
elif(marks>=65 and marks<80):
	print("B Grade")
elif(marks>=35 and marks<65):
	print("C Grade")
elif(marks<35):
	print("Fail")
else:
	print("Invalid Input")
