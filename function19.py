

def square_elements(nums):
    return [num ** 2 for num in nums]

def filter_even(nums):
    return [num for num in nums if num % 2 == 0]


numbers = [1, 2, 3, 4, 5]
squared_numbers = square_elements(numbers)
even_numbers = filter_even(numbers)

print("Original Numbers:", numbers)
print("Squared Numbers:", squared_numbers)
print("Even Numbers:", even_numbers)
