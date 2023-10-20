#Abstract Class

from abc import *

class MyDemo(ABC):
	@abstractmethod
	def show(self):
		print("MyDemo Class")

class MyDemo1(MyDemo):
	def show(self):
		print("MyDemo1 Class")

class MyDemo2(MyDemo):
	def show(self):
		print("MyDemo2 Class")

class MyDemo3(MyDemo):
	def show(self):
		print("MyDemo3 Class")


obj1=MyDemo1()
obj1.show()
obj2=MyDemo3()	
obj2.show()			