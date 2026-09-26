
def Convert(s):
	str=""
	for i in range(0,len(s)):
		if(i%2==0):
			str=str+(s[i].lower())
		else:
			str=str+(s[i].upper())

	return str

print(Convert("ABCDE"))
print(Convert("abcde"))