#Nested Function

def outer_function(a,b):
	print("a+b is=",a+b)
	print("a-b is=",a-b)
	print("a*b is=",a*b)

	def inner_function(c,d):
		print("c+d is",c+d)
		print("c-d is",c-d)
		print("c*d is",c*d)
	inner_function(100,20)

o=outer_function
o(600,30)
