#Single inheritance with constructor (with parameter)

class A:
	def __init__(self,n,r):
		self.name=n
		self.roll=r
		print(self.name,self.roll)
class B(A):
	def __init__(self,n,r,m):
		super(). __init__(n,r)
		self.mark=m
		print(self.name,self.roll,self.mark)
				
obj=B("Radhya",101,90)