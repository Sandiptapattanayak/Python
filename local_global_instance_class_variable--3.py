class Test:
	x=1
	def __init__(self):
		self.y=1
		Test.x=Test.x+1
		self.y=self.y+1
	def show(self):
		print(Test.x,self.y)
Test.x=6		
t=Test()
t1=Test()
t2=Test()
t.show()
t1.show()			
t2.show()	