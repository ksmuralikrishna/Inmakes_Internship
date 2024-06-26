'''Write a Python program to remove duplicates from a list while preserving the order of elements.'''

list_1 = ['a', 'b', 'c', 'a']
chars = set()
list_2 = [x for x in list_1 if x not in chars and not chars.add(x)]

print(list_2)