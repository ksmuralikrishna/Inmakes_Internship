#Task 4 Find the Sum and Average 
# Write a Python program that takes a list of numbers 
# as input and calculates and prints the sum and average of those numbers.
l = []

def sum_and_average(l):
    sum = 0
    for i in l:
        sum = sum + i

        avg = sum/len(l)

    print("sum of the number : ", sum, "\nAverage of the numbers :", avg)

for i in range(3):
    l.append(int(input("enter the number: ")))

sum_and_average(l)

