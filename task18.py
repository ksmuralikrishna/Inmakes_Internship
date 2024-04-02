'''Task 18 Print the Fibonacci series for first 12 numbers'''

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        nextNumber = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(nextNumber)
    return fib_sequence

print("Fibonacci series for the first 12 numbers:", fibonacci(12))
