#wap count no of char alp up lw vw co dg space sy word.


print('Enter a string')
s=input()
ch,alp,up,lw,vw,cons,dig,space,sy,word=0,0,0,0,0,0,0,0,0,0
for i in s:
	if i.isalpha():
		if s.isupper():
			up=up+1
		else:
			lw=lw+1	
		if i in "aeiouAEIOU":
			vw=vw+1
		else:
			cons=cons+1
	elif i.isdigit():
		dig=dig+1
	elif i.isspace():
		space=space+1
	else:
		sy=sy+1
	ch=ch+1
word=word+1
print("No of character=",ch)
print("No of alphabet=",alp)
print("No of uppercase=",up)
print("No of lowercase=",lw)
print("No of vowel=",vw)
print("No of consonant=",cons)
print("No of digit=",dig)
print("No of space=",space)
print("No of symbol=",sy)
print("No of word=",word)




