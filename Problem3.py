
def AddZero(li):
	count=0
	for i in range(0,len(li)):
		if(li[i]==0):
			count+=1

	for i in range(0,count):
		li.remove(0)
	
	for i in range(0,count):
		li.append(0)

	return li

li=[1,0,0,0,5]
print(AddZero(li))