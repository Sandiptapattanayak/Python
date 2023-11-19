#Set (issubset()/superset()/isdisjoint())
s1=s1={12,22,32,43}
print(s1.issubset({12,22,32,43,52}))
print(s1.issuperset({12,22,32,43,52}))
print({12,22,32,43}.issuperset(s1))

s3={23,45}
print(s1.isdisjoint(s3))
