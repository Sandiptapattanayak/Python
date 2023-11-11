#tuple converting to list for sorting the elements

t=(10,20,30,60,80,70,50)
L=list(t)
print(L)

L.sort()
print(L)

t=tuple(L)
print(t)