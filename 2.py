#Perfect number upto range

print("enter a range ")
rg=int(input())
for no in range(1,rg+1):
  s=0
  d=1
  while d<=no//2:
    if no%d==0:
      s=s+d
    d=d+1
  if no==s:
    print(no," is perfect number ")
