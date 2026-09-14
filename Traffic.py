color=input("Enter Color:")

match color.lower():
	case "red":
		print("Stop")
	case "yellow":
		print("Get Ready")
	case "green":
		print("go")
	case _:
		print("Invalid Color")