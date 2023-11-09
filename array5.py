#Array Predefined Function(insert())

import array as ar

A=ar.array('i',[34,24,54,44])
print(A)

A.insert(2,64)
A.insert(3,74)
A.insert(1,84)

print(A)