# How to set a thread's name 


from threading import *

def fun1():
	for i in range(5):
		print("Lira")

def fun2():
	
	for i in range(5):
		print("Ahhan")

t1=Thread(target=fun1)

t1.start()
t1.name='mythread1'
print(t1.name)
t2=Thread(target=fun2)		

t2.start()	
t1.name='mythread2'
print(t1.name)
	