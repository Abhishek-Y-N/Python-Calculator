balance=0

while True:
	print("1.Check balance\n2.Deposite\n3.Withdraw\n4.Exit")
	ch=int(input("Enter Your Choice:"))

	if ch==1:
		print("Balance:",balance)
	elif ch==2:
		amount=float(input("Enter Amount:"))
		balance+=amount
		print("Transaction Successful!")
	elif  ch==3:
		amount=float(input("Enter Amount:"))
		if amount>balance:
			print("Insufficient Balance")
		else:
			balance-=amount
			print("Amount Debited:",amount)
			print("Balance:",balance)
	elif ch==4:
		exit(0)