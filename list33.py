#Nested List(Displaying all the elements using index)

L=[[10,20,30],[40,50,60],[70,80,90],[100,110]]
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
		print(L[i][j],end="\t")
	print()

