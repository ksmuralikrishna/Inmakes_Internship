'''Task 16 Write a program to check palindrome number.'''

num = int(input("Enter the INPUT: "))
num = str(num)
rnum = ""
for i in range(len(num)):
    rnum = num[::-1]
if rnum == num:
    print("The number is palindrome")

else: 
    print("The number is not a palindrome")

