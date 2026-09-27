li1=[1,3]
li2=[2]

def Median(li1,li2):
	arr=li1+li2
	arr.sort()
	if len(arr)%2==1:        
		i=len(arr)//2        
		return arr[i]        

	i=len(arr)//2
	return (arr[i]+arr[i-1])/2



print(Median(li1,li2))

