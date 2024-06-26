'''Task 44 
Write a Python program to find numbers divisible by 
nineteen or thirteen from a list of numbers using Lambda.'''

numbers = [19, 26, 39, 52, 65, 70, 78, 91, 104, 120, 117, 130, 200]

div = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

print("Original list ", numbers)
print("Numbers divisible by nineteen or thirteen:", div)
