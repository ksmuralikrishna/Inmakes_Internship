'''Task 12 Unique Characters
Create a Python program that takes a string as input and 
checks if all the characters in the string are unique (i.e., no character repeats). 
Return True if all characters are unique, and False otherwise.'''


def uniqueChar(user_string):
    string = set(user_string)
    if len(string) == len(user_string):
        return True
    else:
        return False

user_string = input("Enter the string\n")
print("\n",uniqueChar(user_string))