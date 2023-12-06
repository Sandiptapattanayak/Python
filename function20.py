def calculate_average(numbers):
    if not numbers:
        return "List is empty, cannot calculate average."
    return sum(numbers) / len(numbers)


num_list = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
average = calculate_average(num_list)
print(f"The average of the numbers is: {average:.2f}")
