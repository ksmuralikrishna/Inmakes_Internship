#Write a program to remove duplicate values in the given string.

def string_duplicate(string1):
    string1 = string1.lower()
    count = ''
    for i in string1:
        if i in count:
            pass
        else:
            count=count+i
        
    print("the string after removing duplicates : ", count)

string1 = input("Enter the string : ")
string_duplicate(string1)
