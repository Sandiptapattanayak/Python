#check the number is prime number using function.


def is_prime(number):
   
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # The number is divisible by i, so it's not prime
    
    return True  


number_to_check = 17
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")
