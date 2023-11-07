#List Comprehnsion

L=[10,20,30,40]
L1=[]
 
#with List Comprehnsion
for i in L:
 	if i>20:
 		L1.append(i**2)
print(L)

#Using List Comprehnsion

L2=[5,15,20,30]
L3=[j**2 for j in L2 if j>20]
print(L3)