#filter Function

d={1:"Riya",2:"Rehan",3:"Lira",4:"Ahhan",5:"samisha",6:"sandy"}
data=dict(filter(lambda x:x[0]%2==0,d.items()))
print(data)