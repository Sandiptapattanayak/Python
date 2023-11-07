#List Comprehnsion 

L=[5,8,20,7,34,45]

#without List Comprehnsion
L1=[]
for i in L:
 	L1.append(i)
print(L1)

# Using List Comprehnsion
L2=[i for i in L]
print(L2)

