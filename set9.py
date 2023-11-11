#Set(Symmetric_difference)

s1={3,5,8,9}
s2={5,4,9,10}
print(s1.symmetric_difference(s2))
print(s1^s2)

s1.symmetric_difference_update(s2)
print(s1)
print(s2)