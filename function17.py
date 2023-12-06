#Fibinacci sequence using function

def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


terms = int(input("Enter the number of Fibonacci sequence terms to generate: "))
result = fibonacci(terms)
print("Fibonacci Sequence:", result)
