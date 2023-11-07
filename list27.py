#search element, append and remove

L=[10,20,30,40,50,60,70,'hi','python']

print("Enter the element")
s=int(input())

for i in L:
	if i==s:
		print("Search successfully")
		L.append(80)
		L.remove(i)
print(L)		

