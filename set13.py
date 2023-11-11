#set (clear()/pop()/issubset()/superset()/copy()/isdisjoint())

s1={12,22,32,43}
s1.clear()
print(s1)

s1.pop()
print(s1)

s2=s1.copy()
print(s2)

print(s1.issubset({12,22,32,43,52}))
print(s1.issuperset({12,22,32,43,52}))
print({12,22,32,43}.issuperset(s1))

s3={23,45}
print(s1.isdisjoint(s3))
