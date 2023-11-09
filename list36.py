# keyboad input and display the addition of two matrix

print("Enter the L1 matrix: ")
L1=eval(input())
print(L1)

print("Enter the L2 matrix: ")
L2=eval(input())
print(L2)

L3=[]

for i in range(len(L1)):
	x=[]
	for j in range(len(L1[i])):
		x.append(L1[i][j]+L2[i][j])
	L3.append(x)
print(L3)		
