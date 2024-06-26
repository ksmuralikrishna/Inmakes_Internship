'''Task 20 Write a Program to print the multiplication table'''

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 11):
            print(i, "x", j, "=", i * j)
        print()


n = int(input("Enter the range: "))
print("Multiplication table up to", n, ":")
multiplication_table(n)
