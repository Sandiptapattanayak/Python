#How to know thread's name

from threading import *

def fun1():
	print(current_thread().name)
	for i in range(5):
		print("Lira")

def fun2():
	
	for i in range(5):
		print("Ahhan")

t1=Thread(target=fun1)
t1.start()
print(current_thread().name)

t2=Thread(target=fun2)		
t2.start()
print(current_thread().name)	

	