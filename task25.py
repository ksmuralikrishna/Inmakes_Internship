'''Task 25
Write a Python program that uses a "for" loop to iterate over a string and prints out each character along with its count.'''


string_1 = "HelloWorld"
seen_chars = set()
list_1 = [(char, string_1.count(char)) for char in string_1 if char not in seen_chars and not seen_chars.add(char)]
print(list_1)
