'''Task 22 Write a Program to Check Whether a Number is Prime or Not.'''
import math

n = int(input("Enter the number: "))
val= True
sq_num = math.sqrt(n)
for i in range(2, int(sq_num)):
    if (n % i == 0):
        val = False

if val:
    print("prime")
else:
    print("not Prime")
