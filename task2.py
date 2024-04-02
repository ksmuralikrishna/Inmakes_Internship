#Write Program to given string is a palindrome (reads the same forwards and backwards).

def is_Palindrome(str1):
    str1 = str1.lower()
    str2 = str1[::-1]
    if str1 == str2:
         print("The string is palindrome")
    else:
         print("The string is not palindrome")

str1 = input("Enter the string: ")
is_Palindrome(str1)