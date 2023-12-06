#check the number is armstrong number using function.


def is_armstrong_number(number):

    num_str = str(number)
    num_digits = len(num_str)
    
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    

    return armstrong_sum == number


number_to_check = 153
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")
