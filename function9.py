#return value with no argument

def show():
	a=10
	return a,a+3,12.34,"hi"
p,q,r,s=show()
print(p,q,r,s)
res=show()
print(res)