#Number of active thread(By using active_count())

from threading import *
import time

def fun1():
	print("Lira")

def fun2():
		print("Ahhan")

t1=Thread(target=fun1)
t1.start()

t2=Thread(target=fun2)		
t2.start()

print("number of active thread are:",active_count())	

	