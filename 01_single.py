#Single inheritance with constructor without parameter

class A:
	def __init__(self):
		print("A class constuructor")
class B(A):
	def __init__(self):
		super(). __init__()
		print("B class constructor")		
obj=B()