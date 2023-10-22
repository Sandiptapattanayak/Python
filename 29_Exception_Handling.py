# Handling Index Error

L=[12,16,20]
try:
	print(L[3])
except IndexError:
	print("index out of range")
print("program end")
