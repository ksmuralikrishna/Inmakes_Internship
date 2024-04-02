'''Task 11 Find Common Elements
Create a Python program that takes two sets and returns a new set containing elements that are common in both input sets.'''


s1 = {1, 2, 3}
s2 = {'a', 'b', 'c', 1,2}
s3 = s1.intersection(s2)
print(s3)  
print(type(s1))
print(type(s2))
print(type(s3))