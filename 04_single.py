#Single inheritance using method (without parameter)

class A:							
	def show(self):
		print("A class method")
class B(A):
	def show(self):
		super().show()
		print("B class method")
ob=B()
ob.show()
obj=A()
obj.show()
