'''Task 48
Write a function in Python to count and display the 
total number of words in a text file.'''

def countWords():
    file = open("task47.txt","r")
    count = 0
    data = file.read()
    print("The text in file is :- ", data)
    words = data.split()
    print("Number of words in the file is ;-", len(words))
    file.close()

countWords()