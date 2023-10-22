L=[10,5,7,6]
try:
	print(L[2]/3)
except IndexError:
	print("index error")
except ZeroDivisionError:
	print("zero division error")
print("program end")
