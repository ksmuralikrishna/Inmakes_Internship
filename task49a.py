'''Task 49
Part 1
Write a Python program to check that a string contains 
only a certain set of characters (in this case a-z, A-Z and 0-9).'''


import re
def check_characters(string):
    
    pattern = re.compile(r'^[a-zA-Z0-9]+$')

 
    match = pattern.search(string)

    return bool(match)
strings = ['Helloworld123', 'hi@#$%' ]

for string in strings:
    if check_characters(string):
        print(f'String "{string}" contains only allowed characters.')
    else:
        print(f'String "{string}" contains characters other than a-z, A-Z, and 0-9.')
