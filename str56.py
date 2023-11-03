#wap take string from keyboad a swapcase(other symbols and digits etc if included in the string)

print("Enter the string")
s=input()
x=""

for i in s:
	x1=ord(i)
	if (x1>=65 and x1<=90) or (x1>=97 and x1<=122):
		if(x1>=65 and x1<=90):
			x=x+chr(x1+32)
		else:
			x=x+chr(x1-32)
	else:
		x=x+chr(x1)		
	
print(x)			







