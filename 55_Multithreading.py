#Number of active thread(By using active_count())

from threading import *
import time

def fun1():
	time.sleep(5)
	print("Raha")

def fun2():
	time.sleep(5)
	print("Riya")

t1=Thread(target=fun1)
t1.start()

t2=Thread(target=fun2)		
t2.start()

time.sleep(3)
print("number of active thread are:",active_count())	

	