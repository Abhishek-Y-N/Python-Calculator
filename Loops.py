correct_pass="some_pass"
not_found=True

while not_found:
	str=input("Enter A String:")
	if str==correct_pass:
		not_found=False
	else:
		print("Wrong Password Try Again!")
print("Password Matched!")