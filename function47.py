#Filter Function

L1=[32,34,36,37,39,41,43,45,46]
L2=[45,47,35,34,44,42,43,48,49]

data=list(filter(lambda x:x in L1,L2))
print(data)