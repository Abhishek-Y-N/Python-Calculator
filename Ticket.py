age=int(input("Enter Age:"))
price=500

if(age<12):
	print("Ticket Price:",price-(price/100)*10)
else:
	print("Ticket Price:",price)