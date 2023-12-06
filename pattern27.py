for i in range(4,0,-1):
	for j in range(1,i+1,1):
		print(j,end="")
	if i==4:
		for j in range(i-1,0,-1):
			print(j,end="")
		print()
		continue
	for j in range(2*(4-i)-1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	print()
for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(j,end="")
	if i==4:
		for j in range(i-1,0,-1):
			print(j,end="")
		print()
		continue
	for j in range(2*(4-i)-1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	print()
