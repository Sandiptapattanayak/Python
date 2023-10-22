L=[10,5,7,6]
try:
	print(L[2]/0)
except:
	print("exception handle")
finally:
	print("must exceute")
print("program end")

