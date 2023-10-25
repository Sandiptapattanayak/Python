# By Extending Thread Class

from threading import *

class Thread1(Thread):

	def run(self):
		for i in range(5):
			print("I love cycling")

class Thread2(Thread):

	def run(self):
		for i in range(5):
			print("I love bike riding")

obj1=Thread1()
obj1.start()

obj2=Thread2()
obj2.start()						