'''Task 26
Write a Python program that uses a list comprehension to create a new list that contains only the uppercase letters in an existing list of strings.'''

list_1 = ["a", "b", "c"]
list_2 = [item.upper() for item in list_1 ]

print(list_2)