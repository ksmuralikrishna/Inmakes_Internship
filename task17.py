'''Task 17 Write a program to print sum of digits.'''


num = int(input("Enter the Input: "))
snum = 0
s = num
f = 0
for i in range(len(str(num))):
    f = s % 10
    snum = snum + s % 10
    s = s //10
print("Sum of the Number is ",snum)
