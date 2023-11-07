#Search and remove element

L=[10,20,30,'hi','python',12.34]
print("Enter the element: ")
s=int(input())

for i in L:
	if i==s:
		print("Element found")
		L.remove(i)
print(L)		