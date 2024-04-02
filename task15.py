'''Task 15 Write a program to check Armstrong number.'''
number = int(input("Enter the number : "))
dup_number = number
sum_of_number = 0
for i in range(len(str(dup_number))):
    remainder = dup_number % 10
    sum_of_number = sum_of_number + remainder ** 3 
    dup_number = dup_number // 10

if sum_of_number == number:
    print(f"the number {number} is armstrong")
else:
    print(f"the number {number} is not armstrong")
