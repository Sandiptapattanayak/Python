#set(difference/difference_update)

s1={20,30,40,60,70}
s2={30,23,45,67}
print(s1-s2)
print(s1.difference(s2))

s1.difference_update(s2)
print(s1)
print(s2)