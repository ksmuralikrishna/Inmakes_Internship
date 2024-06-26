'''Task 43
 Write a Python program to create Fibonacci series up to n using Lambda'''



fibonacci = lambda n: [0, 1, 1] if n <= 2 else fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-2)[-1]]
n = 10

print("Fibonacci series up to", n, ":", fibonacci(n))

