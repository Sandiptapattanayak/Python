#Filter Function
#Find out the even numbers from the list

L=[10,20,23,11,24,25,26,27,31,32]
data=list(filter(lambda x:x%2==0,L))
print(data)