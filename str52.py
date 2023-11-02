#wap count no of lower case

print("Enter the input")
s=input()
c=0

for i in s:
	if ord(i)>=97 and ord(i)<=122:
		c=c+1
print("No of lowercase",c)		
