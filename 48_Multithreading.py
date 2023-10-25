#By extending thread class with constructor

from threading import *

class Thread1(Thread):

	def __init__(self,vehicle):
		#Overriding parent class constructor
		Thread. __init__(self)
		self.vehicle=vehicle

	def run(self):
		for i in range(5):
			print(self.vehicle)

class Thread2(Thread):
	
	def __init__(self,vehicle):
		#Overriding parent class constructor
		Thread. __init__(self)
		self.vehicle=vehicle


	def run(self):
		for i in range(5):
			print(self.vehicle)
			
obj1=Thread1("Bike")
obj1.start()	

obj2=Thread2("Car")
obj2.start()		
	