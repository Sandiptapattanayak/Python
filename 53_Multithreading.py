#List of active thread(By using enumerate())

from threading import *

def fun1():
	for i in range(5):
		print("Lira")

def fun2():
	
	for i in range(5):
		print("Ahhan")

t1=Thread(target=fun1)
t1.start()

t2=Thread(target=fun2)		
t2.start()
print(enumerate())	

	