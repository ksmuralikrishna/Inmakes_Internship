#Write a program that counts the number of vowels and consonants in a string.

def countVowels(str1):
    vowels = "aeiouAEIOU"
    vCount=0
    for i in str1:
        if i in vowels:
            vCount+=1
    consonants = len(str1.replace(" ","")) - vCount

    print("number of vowels is", vCount)
    print("number of consonants is", consonants)

str1 = input("Enter the string\n")
countVowels(str1)
