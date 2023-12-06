#Find the sum of the digits using function

def sdtest(no):
	r,s=0,0
	while(no!=0):
		r=no%10
		s=s+r
		no=no//10
	return s
print("enter a number ")
no=int(input())
res=sdtest(no)
print("sum of digit=",res)
