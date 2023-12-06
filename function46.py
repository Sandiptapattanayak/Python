#Filter Function
#Filter all the negative digits from the tuple

T=(-90,45,67,-89,43,-97,56,-74)
data=tuple(filter(lambda x:x<0,T))
print(data)

