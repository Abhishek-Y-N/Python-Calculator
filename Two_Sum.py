arr=[8,3,5,9]
target=8

def check(arr,targer):
	for i in range(0,len(arr)):
		for j in range (i+1,len(arr)):
			if arr[i]+arr[j]==target:
				return i,j

	return "No Solution"

print(check(arr,target))