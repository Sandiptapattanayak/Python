#Multilevel inheritance by using constructor(without parameter) 

class A:
	def __init__(self):
		print("A Class")
class B(A):
	def __init__(self):
		super(). __init__()
		print("B Class")
class C(B):
	def __init__(self):
		super(). __init__()
		print("C Class")			
ob=C()