#Programs using sleep()

from threading import *
import time

def fun1():
	time.sleep(5)
	print("Ahhan")

def fun2():
	time.sleep(3)
	print("Lira")

t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
t2.start()		

