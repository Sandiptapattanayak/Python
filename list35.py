#Matrix Addition

L1=[[11,12],[13,14]]
L2=[[21,22],[23,24]]
L3=[[0,0],[0,0]]

for i in range(len(L1)):
	for j in range(len(L1[i])):
		L3[i][j]=(L1[i][j]+L2[i][j])

print(L3)