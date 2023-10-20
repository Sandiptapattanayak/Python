#Abstract Method

from abc import *

class Polygon(ABC):
	@abstractmethod		
	def show(self):
		print("it has 6 sides")

class Triangle(Polygon):		
	def show(self):
		print("it has 3 sides")

class Pentagon(Polygon):	
	def show(self):
		print("it has 5 sides")

class Quadrilateral(Polygon):		
	def show(self):
		print("it has 4 sides")	

T=Triangle()
T.show()

Q=Quadrilateral()
Q.show()