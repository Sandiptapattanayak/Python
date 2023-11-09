#Nested List(Displaying all the elements using index)

 L=[[10,20,30],[40,50,60],[70,80,90]]

 for i in range(len(L)):
 	for j in range(L[i]):
 		print(L[i][j],end="\t")
 	print()	

