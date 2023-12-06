#check no is pd no using function return value with arguemnt


def revno(no):
	r,s=0,0
	while(no!=0):
		r=no%10
		s=s*10+r
		no=no//10
	return s
print("enter a number ")
no=int(input())
if(no==revno(no)):
	print(no,"is pd number")
else:
	print(no,"is not pd number")

