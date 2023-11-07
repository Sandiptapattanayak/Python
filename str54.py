#Converting lower case into upper case

print("Enter the string")
s=input()
x=""

for i in s:
	x1=ord(i)
	if x1>=97 and x1<=122:
		x=x+chr(x1-32)
	else:
		x=x+chr(x1)
print(x)			