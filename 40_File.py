f=open("sita.txt","r")
print(f.tell())
f.seek(4)
print(f.read())
print(f.tell())
f.close()