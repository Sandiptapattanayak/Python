
amount=10000

def deposit(amt):
	global amount
	amount=amount+amt 
	print(amt,"deposit")

def withdraw(amt):
	global amount 
	amount=amount-amt 
	print(amt,"withdraw")
	
print("balance=",amount)
deposit(3000)
withdraw(6000)
print("balance=",amount)