#operator Overloading(With different methods)                #doubt
#Example-2

class Test:
	def __init__(self,m,a):
		self.m=m
		self.a=a
	def show(self):
		print(self.m,"+",self.a,"i")
	def __add__(self,c2):
		c3=Test(0,0)
		c3.m=self.m+c2.m			
		c3.a=self.a+c2.a
		return c3

c1=Test(4,5)
c2=Test(10,11)
c3=c1+c2
c1.show()
c2.show()
c3.show()
