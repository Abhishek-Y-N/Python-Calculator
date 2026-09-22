class Vector():
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def __str__(self):
		return (f"x:{self.x},y:{self.y}")

	def mag(self):
		return ((self.x**2)+(self.y**2))

obj=Vector(10,20)
print(obj.mag())

print(obj)


	