#wap count no of upper case in a string

print("Enter the string")
s=input()
c=0
for i in s:
	if ord(i)>=65 and ord(i)<=90:
		c=c+1
print("Number of uppercase",c)		
