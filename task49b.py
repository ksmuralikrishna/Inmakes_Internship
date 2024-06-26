'''
Task 49
Part 2 
Write a Python program that matches a string that has an a followed by zero or one 'b' '''

import re

def match_pattern(string):
    pattern = re.compile(r'^ab?$')

    match = pattern.search(string)

    return bool(match)

strings = ['ab', 'abb', 'ba', 'b', 'abc']

for string in strings:
    if match_pattern(string):
        print(f'String "{string}" matches the pattern.')
    else:
        print(f'String "{string}" does not match the pattern.')
