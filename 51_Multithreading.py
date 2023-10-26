#Program by using is_alive()

from threading import *
import time

def fun1():
	time.sleep(5)
	print("Riya")

def fun2():
	print("Lira")	

t1=Thread(target=fun1)
t2=Thread(target=fun2)
print(t1.is_alive())
print(t2.is_alive())
t1.start()
t2.start()
print(t1.is_alive())
print(t2.is_alive())
