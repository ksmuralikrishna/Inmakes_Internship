'''Task 30
Count Vowels and Consonants
Create a Python function that takes a string as input and counts the number of vowels and consonants in the string.'''

def countVowels(str1):
    vowels = "aeiouAEIOU"
    vCount=0
    for i in str1:
        if i in vowels:
            vCount+=1
    consonants = len(str1.replace(" ","")) - vCount

    print("number of vowels is", vCount)
    print("number of consonants is", consonants)

def maIn():
    str1 = input("Enter the string\n")
    return countVowels(str1)

maIn()
