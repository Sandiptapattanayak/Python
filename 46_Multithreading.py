#By Using Object Oriented Approach(Without extendingthread class)

from threading import *

class Test:
	
	def stay1(self):
		for i in range(5):
			print("I stay in BBSR")

	def stay2(self):
		for i in range(5):
			print("I would like to go to Mumbai")		

obj=Test()

t1=Thread(target=obj.stay1)
t1.start()

t2=Thread(target=obj.stay2)			
t2.start()