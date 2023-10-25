# By using functional approach

from threading import *

def fun1():
	for i in range(5):
		print("Ahhan")

def fun2():
	for i in range(5):
		print("Lira")

t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
t2.start()				