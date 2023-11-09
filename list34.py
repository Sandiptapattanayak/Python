#Matrix Addition

L1=[[10,20],[30,40],[50,60]]
L2=[[1,2],[3,4],[5,6]]
L3=[]

for i in range(len(L1)):
	x=[]
	for j in range(len(L1[i])):
		x.append(L1[i][j]+L2[i][j])
	L3.append(x)

print(L3)		

