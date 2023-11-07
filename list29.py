#List Comprehnsion

L=[10,20,30,40,50,60]
L1=[]

#Without List Comprehnsion
for i in L:
	L1.append(i**2)
print(L1)	

#Using List Comprehnsion
L2=[2,3,4]
L3=[j**2 for j in L2]
print(L3)